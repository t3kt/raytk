SDF for a 2D star shape.

## Parameters

* `Radius`: The distance from the center to each outer point on the star.
* `Points`: The number of points for the star. When this is a non-integer value there will be one point that is partially cut off at the bottom.
* `Tightness`: How much the inner points of the start are pulled towards the center. At zero this will produce a polygon with two sides for each point. At one it will produce thin lines radiating from the center.