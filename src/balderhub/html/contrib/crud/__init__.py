

try:
    import balderhub.crud
except ImportError as exc:
    raise RuntimeError(
        'you need to install this package with `crud` support '
        '(`pip install balderhub-html[crud]` or `pip  install balderhub-html[all]`)'
    ) from exc
