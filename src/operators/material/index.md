# Material operators

Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work with a particular type
of output renderer. So a `sampledPointMat` can only be used with
a `pointMapRender`, and a `phongMat` can only be used with a
`raymarchRender3d`.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.