2D line segment SDF.

The line segment is defined by two points.
By default those come from the "Point A" and "Point B" parameters.
But if the "Points Field" input is connected, it will use that to get the points instead.

## Parameters

* `Pointa`
* `Pointb`

## Inputs

* `points_definition_in`: If connected, this field will be used to pick both points. The first point comes from the X and Y components of the vector that comes out of the field, and the second point will use the Z and W components.