from ..abstract_html_input_element import AbstractHtmlInputElement


class HtmlWeekInput(AbstractHtmlInputElement):
    """
    The element is implemented like described here:
    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/week
    """

    def clear(self):
        """
        Clears html input element.
        """
        return self.bridge.clear()
