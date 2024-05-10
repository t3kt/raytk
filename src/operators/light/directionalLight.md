Directional or distant light which always comes from one direction.

The light always comes from the specified direction, rather than from a point.

## Parameters

* `Direction`: Vector pointing which direction the light shines. This vector is automatically normalized.
* `Intensity`: Brightness that is applied to the `Color`.
* `Color`: Color of the light.
* `Rotate`: Rotates the direction of the light on all 3 axes.
* `Enableshadow`: Whether the light should produce shadows.

## Inputs

* `colorField`: Field controls the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.

## Variables

* `lightdir`: Direction that the light is from the current position on a surface that's being shaded. This will always be the Direction with rotation applied.