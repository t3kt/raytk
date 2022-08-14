Convert from cartesian space to various types of polar spaces.

## Parameters

* `Enable`
* `Conversion`
  * `spherical`: X becomes distance from the origin, Y becomes secondary angle, Z becomes angle around the Z axis.
  * `cylindricalx`: X stays as X, Y becomes distance from the X axis, Z becomes angle around the X axis. 
  * `cylindricaly`: X becomes angle around the Y axis, Y stays as Y, Z becomes distance from the Y axis.
  * `cylindricalz`: X becomes distance from the Z axis, Y becomes angle around the Z axis, Z stays as Z.
  * `logcylindricalx`: Same as Cylindrical X but the distance is treated as logarithmic.
  * `logcylindricaly`: Same as Cylindrical Y but the distance is treated as logarithmic.
  * `logcylindricalz`: Same as Cylindrical Z but the distance is treated as logarithmic.
* `Angleunit`
  * `ratio`
  * `degrees`
  * `radians`

## Inputs

* `definition_in`: 