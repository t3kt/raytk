A material that produces color for volumetric points relative to the input shape.

This is intended for use with `pointMapRender`. It isn't useful for `raymarchRender3d` since that renderer only evaluates materials at points on the surface of the shape, and not inside/outside the shape.

## Parameters

* `Enable`
* `Enablefill`: Whether to apply a color to points within the shape.
* `Fillcolor`: The color used within the shape.
* `Enableedge`: Whether to apply a color to points that are at/near the surface of the shape.
* `Edgecolor`: The color applied to points at/near the surface.
* `Edgethickness`: The thickness of the area inside/outside the surface where the `Edge Color` is applied.
* `Blending`: The distance over which to blend between the inside color and the edge color.
* `Uselocalpos`: Whether to use the "local" position relative to the input shape when looking up colors using the `Color Field` input. If enabled, the coordinates used for the color field will be "before" any downstream transformations are applied. When disabled, the final global position where a point ends up in the render is used instead.

## Inputs

* `definition_in`: 
* `fill_color_field_definition_in`: Optional field used to control the color within the shape.
* `edge_color_field_definition_in`: Optional field used to control the color at the surface.