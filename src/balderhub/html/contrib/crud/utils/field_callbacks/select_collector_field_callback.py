from typing import Any

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

import balderhub.html.lib.utils.components as html

from .base_html_elem_field_collector_callback import BaseHtmlElemFieldCollectorCallback


class SelectCollectorFieldCallback(BaseHtmlElemFieldCollectorCallback):
    """
    Callback to collect and process values from HTML select elements.

    This class is used to retrieve and process values from HTML select elements in
    a given context.
    """
    #: supports HTML elements
    ALLOWED_HTML_ELEMENT_TYPES = (html.HtmlSelectElement, )

    def _collect_field_value(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_collected_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element: html.HtmlSelectElement = self.get_html_element(element_object)
        expected_type = feature.data_item_type.get_field_data_type(abs_field_name)

        # TODO use native method!!
        options = [option.get_value() for option in html_element.options if option.bridge.get_attribute('selected')]
        if len(options) > 1:
            if not issubclass(expected_type, list):
                raise ValueError(f'can not resolve multiple options when field type is {expected_type}')
            # do type cast
            result = []
            inner_type = feature.data_item_type.get_element_type_for_list(abs_field_name)
            for cur_idx, cur_option in enumerate(options):
                try:
                    result.append(inner_type(cur_option))
                except ValueError as exc:
                    raise ValueError(f'can not convert option at index {cur_idx} with value '
                                     f'`{cur_option}` into expected list item type {inner_type}') from exc
            return result
        if len(options) == 1:
            try:
                return expected_type(options[0])
            except ValueError as exc:
                raise ValueError(
                    f'unable to get correct {expected_type} type for text value of `{options[0]}`'
                ) from exc

        # otherwise return None / empty list
        if issubclass(expected_type, list):
            return []

        return None
