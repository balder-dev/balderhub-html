from __future__ import annotations
from typing import TYPE_CHECKING

import balderhub.html.lib.utils.components as html

from .base_html_elem_field_collector_callback import BaseHtmlElemFieldCollectorCallback
from .base_html_elem_field_filler_callback import BaseHtmlElemFieldFillerCallback
from .checkbox_collector_field_callback import CheckboxCollectorFieldCallback
from .checkbox_filler_field_callback import CheckboxFillerFieldCallback
from .input_collector_field_callback import InputCollectorFieldCallback
from .input_filler_field_callback import InputFillerFieldCallback
from .select_collector_field_callback import SelectCollectorFieldCallback
from .select_filler_field_callback import SelectFillerFieldCallback
from .text_collector_field_callback import TextCollectorFieldCallback
from .value_from_url_collector_field_callback import ValueFromUrlCollectorFieldCallback

if TYPE_CHECKING:
    from balderhub.crud.lib.utils.field_callbacks import FieldCollectorCallback, FieldFillerCallback


def get_field_collector_callback_type_for(
        widget_type: type[html.HtmlElement]
) -> type[FieldCollectorCallback]:
    """
    Determine and return the appropriate field collector callback type for a given widget type. The function uses the
    widget type to identify its corresponding field collector callback. If the widget type is not recognized,
    it raises an ValueError.

    :param widget_type: The class type of a widget, either an HTML element or a change form fieldset field. It must be
        a subclass of HtmlElement.
    :return: The corresponding field collector callback type for the given widget type.
    """
    if issubclass(widget_type, CheckboxCollectorFieldCallback.ALLOWED_HTML_ELEMENT_TYPES):
        return CheckboxCollectorFieldCallback
    if issubclass(widget_type, InputCollectorFieldCallback.ALLOWED_HTML_ELEMENT_TYPES):
        return InputCollectorFieldCallback
    if issubclass(widget_type, SelectCollectorFieldCallback.ALLOWED_HTML_ELEMENT_TYPES):
        return SelectCollectorFieldCallback
    if issubclass(widget_type, (html.HtmlElement,)):
        # otherwise determine value over `text` attribute
        return TextCollectorFieldCallback

    raise ValueError(f'unable to resolve callback for element from type {widget_type}')


def get_field_filler_callback_type_for(
        widget_type: type[html.HtmlElement]
) -> type[FieldFillerCallback]:
    """
    Determines the appropriate callback type for filling fields, based on the provided html element type. The function
    maps specific widget types to their respective field filler callback classes. If the widget type is not recognized,
    it raises an ValueError.

    :param widget_type: The type of widget for which the field filler callback type is to be determined. It must be
        a subclass of HtmlElement.
    :return: The class type of the appropriate `FieldFillerCallback` for the given widget type.
    """
    if issubclass(widget_type, CheckboxFillerFieldCallback.ALLOWED_HTML_ELEMENT_TYPES):
        return CheckboxFillerFieldCallback
    if issubclass(widget_type, InputFillerFieldCallback.ALLOWED_HTML_ELEMENT_TYPES):
        return InputFillerFieldCallback
    if issubclass(widget_type, SelectFillerFieldCallback.ALLOWED_HTML_ELEMENT_TYPES):
        return SelectFillerFieldCallback

    # TODO add support for `html.inputs.HtmlColorInput`, `html.inputs.HtmlFileInput`, `html.inputs.HtmlImageInput`,
    #  `html.inputs.HtmlRadioInput`, `html.inputs.HtmlRangeInput`, `html.inputs.HtmlResetInput`,
    #  `html.inputs.HtmlSubmitInput`

    raise ValueError(f'unable to resolve callback for element from type {widget_type}')


__all__ = [
    'BaseHtmlElemFieldCollectorCallback',
    'BaseHtmlElemFieldFillerCallback',
    'CheckboxCollectorFieldCallback',
    'CheckboxFillerFieldCallback',
    'InputCollectorFieldCallback',
    'InputFillerFieldCallback',
    'SelectCollectorFieldCallback',
    'SelectFillerFieldCallback',
    'TextCollectorFieldCallback',
    'ValueFromUrlCollectorFieldCallback',
    'get_field_collector_callback_type_for',
    'get_field_filler_callback_type_for',
]
