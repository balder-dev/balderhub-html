from ..abstract_html_input_element import AbstractHtmlInputElement


class HtmlColorInput(AbstractHtmlInputElement):
    """
    The element is implemented like described here:
    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/color
    """

    def clear(self):
        """
        Clears html input element.
        """
        return self.bridge.clear()
