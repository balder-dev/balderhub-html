from typing import Any

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString
import balderhub.html.lib.utils.components as html

from .base_html_elem_field_collector_callback import BaseHtmlElemFieldCollectorCallback


class CheckboxCollectorFieldCallback(BaseHtmlElemFieldCollectorCallback):
    """
    Manages the collection of field values specifically for HTML checkbox input elements.

    This class is designed to handle the process of collecting field values for HTML checkbox inputs by
    checking their state (checked or unchecked).
    """
    #: supports HTML elements
    ALLOWED_HTML_ELEMENT_TYPES = (html.inputs.HtmlCheckboxInput, )

    def _collect_field_value(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT, already_collected_data: dict[str, Any],
            **kwargs
    ) -> bool:
        html_element = self.get_html_element(element_object)
        return html_element.is_checked()
