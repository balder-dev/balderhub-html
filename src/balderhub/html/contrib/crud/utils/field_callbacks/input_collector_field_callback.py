from typing import Any

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

import balderhub.html.lib.utils.components as html

from .base_html_elem_field_collector_callback import BaseHtmlElemFieldCollectorCallback


class InputCollectorFieldCallback(BaseHtmlElemFieldCollectorCallback):
    """
    Class responsible for collecting field values from specified HTML input elements.

    This class provides a mechanism to collect data from various specified HTML input element types. It focuses
    on collecting the text content of the elements.
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

    def _collect_field_value(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_collected_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element = self.get_html_element(element_object)

        return html_element.text
