from ..abstract_html_input_element import AbstractHtmlInputElement


class HtmlTimeInput(AbstractHtmlInputElement):
    """
    The element is implemented like described here:
    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/time
    """

    def clear(self):
        """
        Clears html input element.
        """
        return self.bridge.clear()
