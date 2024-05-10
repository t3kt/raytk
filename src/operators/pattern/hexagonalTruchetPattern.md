Pattern using truchet tiling in a hexagonal arrangement.

This operator produces different types of values from the grid depending on the selected Pattern.

Truchet patterns involve a curving path through a grid (in this case hexagonal), where the path is always uninterrupted, but may sometimes form closed loops.

Based on [hexagonal truchet by FabriceNeyret2](https://www.shadertoy.com/view/Xdt3D8).

See details about [Truchet tiles](https://en.wikipedia.org/wiki/Truchet_tiles).

## Parameters

* `Pattern`: What type of values to produce from the grid.
  * `default`: Produces float values with 1 for the path and 0 for the space around the path.
  * `variant1`: Produces float values with multiple stripes going through the path.
  * `variant2`: Produces vectors with colors using stripes along the path. Currently these colors are fixed and unchangeable.
* `Seed`: Seed number used to control the randomization of the path.
* `Translate`: Moves the entire pattern.
* `Size`: Scales the pattern.

## Inputs

* `coordField`: Field that produces vectors that the pattern uses as coordinates instead of regular spatial position. Only the X and Y parts are used.
