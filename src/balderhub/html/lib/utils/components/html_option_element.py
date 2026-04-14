from typing import Any

from .html_element import HtmlElement


class HtmlOptionElement(HtmlElement):
    """
    The element is implemented like described here: https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionElement
    """

    def is_selected(self) -> bool:
        """
        This method checks if the select option is selected
        :return: True if the option is selected otherwise False
        """
        return self.bridge.is_selected()

    def get_value(self) -> Any:
        """
        This method returns the value of the option.
        :return: the value of the option
        """
        return self.bridge.get_attribute('value')
