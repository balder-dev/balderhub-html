from typing import Any

from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

import balderhub.html.lib.utils.components as html


from .base_html_elem_field_collector_callback import BaseHtmlElemFieldCollectorCallback


class TextCollectorFieldCallback(BaseHtmlElemFieldCollectorCallback):
    """
    A callback class for collecting specific field values from HTML elements.

    This class is designed to extract and collect text values from certain types
    of HTML elements as part of a data collection or transformation pipeline.
    It ensures compatibility with HTML elements defined in its allowed types.

    :ivar ALLOWED_HTML_ELEMENT_TYPES: Specifies the types of HTML elements that
        this callback supports.
    :type ALLOWED_HTML_ELEMENT_TYPES: tuple
    """
    #: supports HTML elements
    ALLOWED_HTML_ELEMENT_TYPES = (html.HtmlElement, )

    def _collect_field_value(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_collected_data: dict[str, Any],
            **kwargs
    ) -> Any:
        html_element: html.HtmlSelectElement = self.get_html_element(element_object)

        return html_element.text
