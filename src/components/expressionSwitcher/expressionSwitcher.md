# expressionSwitcher

Supports switching between different available expressions based around a menu parameter.

For example, an operator could use this to allow choosing different blending modes.
The switcher is based around a table of expressions which have names, labels, a code snippet,
and other properties.

The switcher will update the parameter menu (when in development mode), using a `parMenuUpdater`.

The expressions can include references to parameters such as `doStuff(p, THIS_Value)`. The switcher
can selectively enable and disable parameters needed for the selected expression.

It generates a macro table that can be used by the ROP to control behavior based on the selected
expression. It also generates a list of the used parameter names.
