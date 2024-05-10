Ambient light source that doesn't come from a particular location.

As far as a material is concerned, an ambient light is always right in front of any point on a surface.

Use cases for this are relatively rare.

## Parameters

* `Intensity`: Brightness that is applied to the `Color`.
* `Color`: Color of the light.
* `Enableshadow`: Whether the light should produce shadows.

## Inputs

* `colorField`: Field controls the color of the light based on the position of surface hits where it is being applied. The resulting color is multiplied by the `Color` parameter and `Intensity`.

## Variables

* `lightdir`: Direction that the light is from the current position on a surface that's being shaded. This will always be directly in front of whatever point is being shaded based on the surface normal at that point.