from typing import Any, Callable

from balderhub.crud.lib.utils.field_callbacks import FieldCollectorCallback
from balderhub.crud.lib.utils.field_callbacks.base_field_callback import CallbackElementObjectT
from balderhub.data.lib.scenario_features import AbstractDataItemRelatedFeature
from balderhub.data.lib.utils import LookupFieldString

from balderhub.html.lib.scenario_features import HtmlPage
from balderhub.url.lib.utils import Url


class ValueFromUrlCollectorFieldCallback(FieldCollectorCallback):
    """
    This field callback expects a html page as the container object. Over this object, the callback reads the url and
    resolves the provided url parameter
    """

    def __init__(self, url_schema: Url, parameter_name: str, type_convert_cb: Callable[[Any], Any] = None, **kwargs):
        super().__init__(type_convert_cb=type_convert_cb, **kwargs)

        if not url_schema.is_schema():
            raise ValueError('given url schema is not a schema')
        if parameter_name not in url_schema.get_unfilled_parameters().keys():
            raise ValueError(f'given url parameter {parameter_name} is not mentioned in '
                             f'schema: {url_schema}')

        self._url_schema = url_schema
        self._parameter_name = parameter_name

    def _collect_field_value(
            self,
            feature: AbstractDataItemRelatedFeature,
            abs_field_name: LookupFieldString,
            element_object: CallbackElementObjectT,
            already_collected_data: dict[str, Any],
            **kwargs
    ) -> Any:
        if not isinstance(element_object, HtmlPage):
            raise TypeError(f'can not determine the current url because the given element-object is not a '
                            f'{HtmlPage.__name__} - is {element_object.__class__.__name__}')

        expected_type = feature.data_item_type.get_field_data_type(abs_field_name)
        if issubclass(expected_type, list):
            raise NotImplementedError('can not get value from simple HtmlElement as a list')

        url = element_object.driver.current_url
        result_raw = Url(url).extract_parameters(self._url_schema)[self._parameter_name]
        try:
            return expected_type(result_raw)
        except ValueError as exc:
            raise ValueError(f'unable to get correct type {expected_type} for text value of `{result_raw}`') from exc
