Produces colors using rainbow spectrum patterns.

There are several spectrum types to choose from which balance the colors in different ways.

The field will produce a color based on either the Wavelength parameter, or values from the wavelength input field.

## Parameters

* `Wavelength`: Constant value to use as the wavelength to map to a color. This is only used when there is no wavelength input field.
* `Wavelengthunit`: How wavelength values should be interpreted.
  * `norm`: Normalized to a 0..1 range.
  * `nm`: Nanometers.
* `Spectrumtype`
  * `zucconi`
  * `zucconi6`
  * `jet`
  * `gems`
  * `bruton`
  * `spektre`

## Inputs

* `wavelengthField`: Field that provides the wavelengths that the colors are based on.