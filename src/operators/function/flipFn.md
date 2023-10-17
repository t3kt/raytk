Function that flips its input in one of several different modes.

## Parameters

* `Enable`
* `Fliptype`: The type of flipping to apply.
  * `flipdomain`: Negates the coordinate passed to the input function, flipping the x axis of a function graph across the y axis.
  * `fliprange`: Negates the input function's return value, flipping the y axis of a function graph across the x axis.
  * `mirrorposdomain`: Mirrors the coordinate so only the positive half is used, reflecting the positive side of a function graph across the y axis replacing the negative side.
  * `flipnegdomain`: Mirrors the coordinate so only the positive half is used, but also flips the return value when on the negative side, reflecting the positive side of a function graph across the y axis but then also flipping that side upside down.
  * `flipdomain01`: Flips the x axis in the 0..1 range so that what used to be x=0 is now x=1 and what used to be x=1 is now x=0.
  * `fliprange01`: Flips the y (value) axis in the 0..1 range so that what used to be y=0 is now y=1 and what used to be y=1 is now y=0.
* `Returntype`
  * `Sdf`
  * `float`
  * `vec4`
  * `Ray`
  * `Light`

## Inputs

* `definition_in`: 