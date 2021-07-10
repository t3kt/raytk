Multi-segment line SDF.

The line is defined my a list of points, which are either defined by parameters or by CHOP channels.

## Parameters

* `Source`: Where to get the point positions.
  * `params`: Points are based on the `Point 1, etc parameters.
  * `chop`: The points are based on the `Points CHOP`.
* `Radius`: The thickness of the line segments.
* `Segments`: The number of line segments. This controls how many parameters or CHOP samples are used.
* `Closepath`: Whether to add a line segment connecting the first and last points.
* `Points`: CHOP used for point positions, using the `tx`, `ty`, and `tz` channels
* `Point1`
* `Point2`
* `Point3`
* `Point4`
* `Point5`
* `Point6`
* `Point7`
* `Point8`