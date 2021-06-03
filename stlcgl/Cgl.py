# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Cgl(Component):
    """A Cgl component.


Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- label (string; optional)
- value_rows (string; optional)
- value_cols (string; optional)
- network (string; required): added by Phillip
stringified clustergrammer-gl network object
- divId (string; required): added by Phillip"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.UNDEFINED, value_rows=Component.UNDEFINED, value_cols=Component.UNDEFINED, network=Component.REQUIRED, divId=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'label', 'value_rows', 'value_cols', 'network', 'divId']
        self._type = 'Cgl'
        self._namespace = 'stlcgl'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'label', 'value_rows', 'value_cols', 'network', 'divId']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['network', 'divId']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Cgl, self).__init__(**args)
