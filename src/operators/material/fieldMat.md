A material that uses a vector field input to determine
the color.

Essentially this is a conversion from a field to a material, with no other features.

## Parameters

* `Enable`
* `Uselocalpos`: Whether to use the "local" position relative to the input shape when looking up colors using the `Color Field` input. If enabled, the coordinates used for the color field will be "before" any downstream transformations are applied. When disabled, the final global position where a point ends up in the render is used instead.

## Inputs

* `definition_in`: 
* `color_definition_in`: Vector field used to provide the color for each surface point.