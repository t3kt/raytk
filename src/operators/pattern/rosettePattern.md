Pattern with overlapping circles in a hexagonal arrangement.

This pattern produces just float values not colors. To apply color to it, pass it into a `colorRampField`.

The edges of the circles produce values of 1 and the background produces values of 0.

## Parameters

* `Translate`: Moves the entire pattern.
* `Size`: Scales the pattern.
* `Glow`: The amount of glow, or blending between the circle edges and the background.
* `Radius`: The radius of the circles. A value of 1 makes the circles overlap perfectly at the center of their neighbors, 0.5 causes them to touch the edges of the neighbors, and 0 makes the circles dots. Values larger than 1 will cut off parts of the circles.
* `Spread`: How much the arrangement of circles should be spread out along each axis.

## Inputs

* `coordField`: Field that produces vectors that the pattern uses as coordinates instead of regular spatial position. Only the X and Y parts are used.
* `glowField`: Field that controls the amount of glow or blending.
* `radiusField`: Field that controls the radii of the circles.
* `spreadField`: Field that controls how much the circles are spread apart.