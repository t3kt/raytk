Pattern with two layers with gaps in a hexagonal layout.

This pattern always produces colors (vectors), but the Format parameter controls how those colors are produced.

## Parameters

* `Pattern`
  * `twolayer`
* `Translate`: Moves the entire pattern.
* `Size`: Scales the pattern.
* `Thickness`: Thickness of each layer, where larger values produce smaller gaps.
* `Blending`: Amount of blending between layers and edges.
* `Randomize`: Whether to weave the two layers together in a random arrangement, or always put one layer in front of the other.
* `Seed`: Seed number used to control randomization.
* `Format`: What type of values are produced.
  * `color`: Uses the color parameters to color layer 1, layer 2, and background.
  * `customcolor`: Uses the Color 1 field input for everything, relying on that field to use variables to differentiate between the different parts of the pattern.
* `Color1`: The color to use for layer 1.
* `Color2`: The color to use for layer 2.
* `Bgcolor`: The color to use for the background behind both layers.

## Inputs

* `coordField`: Field that produces vectors that the pattern uses as coordinates instead of regular spatial position. Only the X and Y parts are used.
* `thicknessField`: Field that controls the thickness of the edges between layers.
* `blendingField`: Field that controls the amount of blending between layers and edges.
* `color1Field`: Field providing either the color for layer 1 or the custom color for everywhere, depending on the selected Format.
* `color2Field`: Field providing the color for layer 2.
* `bgColorField`: Field providing the color for the background.

## Variables

* `axialdist`: 
* `mask`: 