# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Notification(Component):
    """A Notification component.
w dynamic notifications and alerts to user, part of notifications system

Keyword arguments:

- id (string; required):
    The ID of this component, used to identify dash components in
    callbacks.

- action (a value equal to: 'show', 'update', 'hide'; required):
    Action.

- autoClose (number; optional):
    Auto close timeout in milliseconds, False to disable auto close.

- bg (boolean | number | string | dict | list; optional)

- bga (boolean | number | string | dict | list; optional)

- bgp (string | number; optional)

- bgr (boolean | number | string | dict | list; optional)

- bgsz (string | number; optional)

- bottom (string | number; optional)

- c (boolean | number | string | dict | list; optional)

- className (string; optional):
    Often used with CSS to style elements with common properties.

- classNames (dict; optional):
    add class names to Mantine components.

- closeButtonProps (dict with strings as keys and values of type boolean | number | string | dict | list; optional):
    Props spread to close button.

- color (string; optional):
    Notification line or icon color.

- display (boolean | number | string | dict | list; optional)

- ff (boolean | number | string | dict | list; optional)

- fs (boolean | number | string | dict | list; optional)

- fw (boolean | number | string | dict | list; optional)

- fz (number; optional)

- h (string | number; optional)

- icon (a list of or a singular dash component, string or number; optional):
    Notification icon, replaces color line.

- inset (string | number; optional)

- left (string | number; optional)

- lh (string | number; optional)

- loading (boolean; optional):
    Replaces colored line or icon with Loader component.

- lts (string | number; optional)

- m (number; optional)

- mah (string | number; optional)

- maw (string | number; optional)

- mb (number; optional)

- message (a list of or a singular dash component, string or number; required):
    Notification body, place main text here.

- mih (string | number; optional)

- miw (string | number; optional)

- ml (number; optional)

- mr (number; optional)

- mt (number; optional)

- mx (number; optional)

- my (number; optional)

- opacity (boolean | number | string | dict | list; optional)

- p (number; optional)

- pb (number; optional)

- pl (number; optional)

- pos (boolean | number | string | dict | list; optional)

- pr (number; optional)

- pt (number; optional)

- px (number; optional)

- py (number; optional)

- radius (string; optional):
    Radius from theme.radius, or number to set border-radius in px.

- right (string | number; optional)

- style (boolean | number | string | dict | list; optional):
    Inline style.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- sx (boolean | number | string | dict | list; optional):
    With sx you can add styles to component root element. If you need
    to customize styles of other elements within component use styles
    prop.

- ta (boolean | number | string | dict | list; optional)

- td (string | number; optional)

- title (a list of or a singular dash component, string or number; optional):
    Notification title, displayed before body.

- top (string | number; optional)

- tt (boolean | number | string | dict | list; optional)

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- w (string | number; optional)

- withBorder (boolean; optional):
    Adds border styles.

- withCloseButton (boolean; optional):
    Determines whether close button should be visible, True by
    default."""
    _children_props = ['icon', 'title', 'message']
    _base_nodes = ['icon', 'title', 'message', 'children']
    _namespace = 'dash_mantine_components'
    _type = 'Notification'
    @_explicitize_args
    def __init__(self, color=Component.UNDEFINED, radius=Component.UNDEFINED, icon=Component.UNDEFINED, title=Component.UNDEFINED, message=Component.REQUIRED, loading=Component.UNDEFINED, withBorder=Component.UNDEFINED, withCloseButton=Component.UNDEFINED, closeButtonProps=Component.UNDEFINED, id=Component.REQUIRED, autoClose=Component.UNDEFINED, action=Component.REQUIRED, className=Component.UNDEFINED, style=Component.UNDEFINED, m=Component.UNDEFINED, my=Component.UNDEFINED, mx=Component.UNDEFINED, mt=Component.UNDEFINED, mb=Component.UNDEFINED, ml=Component.UNDEFINED, mr=Component.UNDEFINED, p=Component.UNDEFINED, py=Component.UNDEFINED, px=Component.UNDEFINED, pt=Component.UNDEFINED, pb=Component.UNDEFINED, pl=Component.UNDEFINED, pr=Component.UNDEFINED, bg=Component.UNDEFINED, c=Component.UNDEFINED, opacity=Component.UNDEFINED, ff=Component.UNDEFINED, fz=Component.UNDEFINED, fw=Component.UNDEFINED, lts=Component.UNDEFINED, ta=Component.UNDEFINED, lh=Component.UNDEFINED, fs=Component.UNDEFINED, tt=Component.UNDEFINED, td=Component.UNDEFINED, w=Component.UNDEFINED, miw=Component.UNDEFINED, maw=Component.UNDEFINED, h=Component.UNDEFINED, mih=Component.UNDEFINED, mah=Component.UNDEFINED, bgsz=Component.UNDEFINED, bgp=Component.UNDEFINED, bgr=Component.UNDEFINED, bga=Component.UNDEFINED, pos=Component.UNDEFINED, top=Component.UNDEFINED, left=Component.UNDEFINED, bottom=Component.UNDEFINED, right=Component.UNDEFINED, inset=Component.UNDEFINED, display=Component.UNDEFINED, classNames=Component.UNDEFINED, styles=Component.UNDEFINED, unstyled=Component.UNDEFINED, sx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'action', 'autoClose', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'closeButtonProps', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'inset', 'left', 'lh', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'message', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'w', 'withBorder', 'withCloseButton']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'action', 'autoClose', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'closeButtonProps', 'color', 'display', 'ff', 'fs', 'fw', 'fz', 'h', 'icon', 'inset', 'left', 'lh', 'loading', 'lts', 'm', 'mah', 'maw', 'mb', 'message', 'mih', 'miw', 'ml', 'mr', 'mt', 'mx', 'my', 'opacity', 'p', 'pb', 'pl', 'pos', 'pr', 'pt', 'px', 'py', 'radius', 'right', 'style', 'styles', 'sx', 'ta', 'td', 'title', 'top', 'tt', 'unstyled', 'w', 'withBorder', 'withCloseButton']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'action', 'message']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Notification, self).__init__(**args)
