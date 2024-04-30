Shading that is applied to the edges of a surface relative to where it's viewed from.

This is similar to the Rim Light feature in a standard Phong MAT.

Using rim shading can result in aliasing issues, since it's essentially highlighting the areas that are most likely to have aliasing.

## Parameters

* `Enable`: When off, this shading will produce values of 0, meaning no contribution to shading.
* `Level`: Brightness of the shading, which is used as a multiplier for the Color.
* `Usecolor`: Whether to produce color or just a brightness value.
* `Color`: Color of the shading.
* `Usesurfacecolor`: Whether this shading should take into account the surface color attribute on the SDF (if present).
* `Enableshadow`: Whether to apply the shadow to the color/level produced by this element.
* `Thickness`: Width of the highlight area on the sides.
* `Blending`: Amount of fading between highlighted and not highlighted areas.

## Inputs

* `thicknessField`: 
* `blendingField`: 
* `colorField`: 

## Variables

* `normangle`: 