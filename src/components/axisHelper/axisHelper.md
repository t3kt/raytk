# axisHelper

Generates macros and an info table based on a selected axis (x/y/z).

Typically this is bound to a parameter on the containing ROP which uses the generated macros
in its shader code.

Macros include `THIS_AXIS`, `THIS_PLANE_P1`, `THIS_PLANE_P2`, 'THIS_AXIS_VEC', etc.
