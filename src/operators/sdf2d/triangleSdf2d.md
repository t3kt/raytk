SDF for a 2D triangle.

## Parameters

* `Shape`: Which type of triangle to produce. The types are defined by different sets of parameters.
  * `equilateral`: An equilateral triangle (all sides are the same). This is defined based on `Radius`. The triangle is centered around the origin.
  * `isosceles`: An iscosceles triangle (2 sides are the same). This is defined based on `Width` and `Height`. The tip of the triangle is placed at the origin.
  * `arbitrary`: An arbitrary triangle based on 3 points.
* `Radius`: The distance from the center to each corner of the triangle. Used for equilateral triangles.
* `Height`: The distance from the base of an iscosceles triangle to the opposite tip.
* `Width`: The width of the base of an isosceles triangle.
* `Point1`: The first corner position, for an arbitrary triangle.
* `Point2`: The second corner position, for an arbitrary triangle.
* `Point3`: The third corner position, for an arbitrary triangle.