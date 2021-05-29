Value field based on an SDF shape.

This can be used to apply effects only within certain shaped areas of space.


## Parameters

* `Fieldtype`
  * `dist`: The raw distance from the surface. This will be negative inside the shape (hence "Signed" in SDF).
  * `inside`: Field with value 1 for points inside the shape and 0 outside the shape. If used, `Blending` starts at the surface and goes inward, so there will never be values > 0 outside the surface.
  * `outside`: Field with value 1 for points outside the shape and 0 inside the shape. If used, `Blending` starts at the surface and goes outward, so there will never be values > 0 inside the surface.
  * `surface`: Field with value 1 at the surface itself (with the specified `Thickness`) and 0 inside and outside the shape. If used, `Blending` starts at the surface (with `Thickness` applied) and goes inward/outward from there.
  * `surfaceinside`: Similar to `Surface` but `Thickness` and `Blending` are applied only inside the bounds of the shape. This is sort of like the "Inner Glow" feature in common graphics editors (e.g. Illustrator/Photoshop).
  * `surfaceoutside` Similar to `Surface` but `Thickness` and `Blending` are applied only outside the bounds of the shape. This is sort of like the "Inner Glow" feature in common graphics editors (e.g. Illustrator/Photoshop).
* `Offset`: Offsets the surface of the shape. Positive values expand the shape and negative values contract it. This is equivalent to the `round` operator.
* `Thickness`: For surface-based fields, this is the thickness of the area where the value is 1.
* `Blending`: The distance over which the 1 area transitions to the 0 area.

## Inputs

* `definition_in`: 