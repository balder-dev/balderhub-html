Contrib for ``balderhub-crud``
******************************

For activating this module, you need to install the package like shown below

.. code-block:: none

    >>> pip install balderhub-html[crud]

Once installed you can use it.

Field Callbacks
===============

This BalderHub project provides field callbacks for almost every normal HTML element, that is provided by this package.
You can use it right away.


.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.BaseHtmlElemFieldCollectorCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.BaseHtmlElemFieldFillerCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.CheckboxCollectorFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.CheckboxFillerFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.InputCollectorFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.InputFillerFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.SelectCollectorFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.SelectFillerFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.TextCollectorFieldCallback
    :members:

.. autoclass:: balderhub.html.contrib.crud.utils.field_callbacks.ValueFromUrlCollectorFieldCallback
    :members:


Field Callbacks Auto-Select Functions
=====================================

This package does also provide functions to auto select the correct callback based on the given html element.

.. autofunction:: balderhub.html.contrib.crud.utils.field_callbacks.get_field_collector_callback_type_for

.. autofunction:: balderhub.html.contrib.crud.utils.field_callbacks.get_field_filler_callback_type_for
