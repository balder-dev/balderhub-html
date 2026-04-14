from typing import Any, Union, Callable

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

import balderhub.html.lib.utils.components as html

from .base_html_elem_field_filler_callback import BaseHtmlElemFieldFillerCallback


class SelectFillerFieldCallback(BaseHtmlElemFieldFillerCallback):
    """
    Handles the behavior and interaction for filling and unsetting HTML select
    elements.

    This class is designed to manage the functionality for interacting with
    HTML `<select>` elements. It fills these elements with specific values or
    reverts them to an unset state based on defined rules and inputs.
    """
    #: supports HTML elements
    ALLOWED_HTML_ELEMENT_TYPES = (html.HtmlSelectElement, )

    def __init__(
            self,
            html_element: Union[html.HtmlElement, Callable[[CallbackElementObjectT], html.HtmlElement]],
            unset_value: Union[str, None] = '',
            **kwargs
    ):
        super().__init__(html_element, **kwargs)
        self._unset_value = unset_value

    def _fill_in(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            field_value_to_fill: Any,
            already_filled_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element: html.HtmlSelectElement = self.get_html_element(element_object)

        html_element.select_by_value(str(field_value_to_fill))
        return field_value_to_fill

    def _unset_field(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_filled_data: dict[str, Any],
            **kwargs
    ) -> Any:
        if self._unset_value is None:
            raise ValueError('can not unset the select')
        html_element: html.HtmlSelectElement = self.get_html_element(element_object)
        html_element.select_by_value(self._unset_value)

        return self._unset_value
