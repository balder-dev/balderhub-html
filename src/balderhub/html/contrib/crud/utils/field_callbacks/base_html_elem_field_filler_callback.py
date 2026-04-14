from abc import ABC
from typing import Callable, Union
from balderhub.crud.lib.utils.field_callbacks import FieldFillerCallback
from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
import balderhub.html.lib.utils.components as html


class BaseHtmlElemFieldFillerCallback(FieldFillerCallback, ABC):
    """
    Base class for creating callbacks for filling fields with HTML elements.

    This class defines a standardized way to create callbacks that manage
    HTML elements used for field-filling purposes. Subclasses are expected
    to specify the allowed HTML element types through the
    `ALLOWED_HTML_ELEMENT_TYPES` attribute and implement additional
    custom behavior as needed.

    """
    ALLOWED_HTML_ELEMENT_TYPES = ()

    def __init__(
            self,
            html_element: Union[html.HtmlElement, Callable[[CallbackElementObjectT], html.HtmlElement]],
            **kwargs
    ):
        super().__init__(**kwargs)
        if not callable(html_element) and not isinstance(html_element, self.ALLOWED_HTML_ELEMENT_TYPES):
            raise TypeError(f'html element needs to be from one of the type {self.ALLOWED_HTML_ELEMENT_TYPES}, '
                            f'but is from type {type(html_element)}')
        self._html_element_cb = html_element

    def get_html_element(self, for_container: CallbackElementObjectT):
        """
        Retrieves an HTML element based on the provided callback object. If the stored
        callback is already an instance of HtmlElement, it is returned directly. Otherwise,
        a callback function is invoked to generate the element out of the provided element
        callback.

        :param for_container: A callback object used to generate the HTML element if the
                              stored callback is not directly an HtmlElement.
        :return: The resulting HTML element from the callback or the pre-existing HtmlElement

        :raises TypeError: If the resulting element from the callback is not of a permitted type
        """
        if isinstance(self._html_element_cb, html.HtmlElement):
            return self._html_element_cb
        elem = self._html_element_cb(for_container)
        if not isinstance(elem, self.ALLOWED_HTML_ELEMENT_TYPES):
            raise TypeError(f'html element needs to be from one of the type {self.ALLOWED_HTML_ELEMENT_TYPES}, '
                            f'but is from type {type(elem)}')
        return elem
