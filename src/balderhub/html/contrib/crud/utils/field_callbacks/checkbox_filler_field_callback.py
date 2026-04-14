from typing import Any

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

import balderhub.html.lib.utils.components as html

from .base_html_elem_field_filler_callback import BaseHtmlElemFieldFillerCallback


class CheckboxFillerFieldCallback(BaseHtmlElemFieldFillerCallback):
    """
    Handles operations related to setting and unsetting HTML checkbox input fields.

    This callback class is designed to interact with HTML checkbox elements, specifically
    for filling in and unsetting checkbox values in a field. It ensures that the checkbox
    fields are filled or unset based on provided boolean values.
    """
    #: supports HTML elements
    ALLOWED_HTML_ELEMENT_TYPES = (html.inputs.HtmlCheckboxInput, )

    def _fill_in(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            field_value_to_fill: Any,
            already_filled_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element: html.inputs.HtmlCheckboxInput = self.get_html_element(element_object)

        if not isinstance(field_value_to_fill, bool):
            raise ValueError(f'can not apply this callback on value type {type(field_value_to_fill)} '
                             f'- needs to be a boolean value')

        if field_value_to_fill and not html_element.is_checked():
            html_element.click()
        if not field_value_to_fill and html_element.is_checked():
            html_element.click()

    def _unset_field(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_filled_data: dict[str, Any],
            **kwargs
    ) -> Any:
        # todo does this make sense for a checkbox field?
        html_element: html.inputs.HtmlCheckboxInput = self.get_html_element(element_object)

        if html_element.is_checked():
            html_element.click()
