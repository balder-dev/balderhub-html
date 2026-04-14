from typing import Any

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

import balderhub.html.lib.utils.components as html

from .base_html_elem_field_filler_callback import BaseHtmlElemFieldFillerCallback


class InputFillerFieldCallback(BaseHtmlElemFieldFillerCallback):
    """
    This class is responsible for handling the process of filling and unsetting
    input fields for supported HTML element types. It provides functionality to
    interact with various kinds of HTML input elements.
    """
    #: supports HTML elements
    ALLOWED_HTML_ELEMENT_TYPES = (html.inputs.HtmlEmailInput, html.inputs.HtmlMonthInput, html.inputs.HtmlNumberInput,
                                  html.inputs.HtmlSearchInput, html.inputs.HtmlTextInput, html.inputs.HtmlTelInput,
                                  html.inputs.HtmlPasswordInput, html.inputs.HtmlUrlInput,
                                  # TODO html.inputs.HtmlDateInput,
                                  # TODO html.inputs.HtmlDatetimelocalInput,
                                  # TODO html.inputs.HtmlHiddenInput,
                                  # TODO html.inputs.HtmlTimeInput,
                                  # TODO html.inputs.HtmlWeekInput
                                  )

    def _fill_in(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            field_value_to_fill: Any,
            already_filled_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element = self.get_html_element(element_object)
        html_element.type_text(field_value_to_fill, clean_before=True)

    def _unset_field(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_filled_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element = self.get_html_element(element_object)
        html_element.bridge.clear()  # TODO use native method
