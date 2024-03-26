Access the world position values from a raymarchRender3D, scaled to a normalized range.

In order for this to work, the associated raymarchRender3D has to have its World Position output enabled.

## Parameters

* `Rangex`
* `Rangey`
* `Rangez`
* `Snapshotrange`: Looks at the world position data and finds the minimum / maximum for each axis and updates `Rangex`, `Rangey`, `Rangez` so the data is scaled from that range to 0..1.
* `Outputop`

## Inputs

* `worldPos_in`: World position data from a raymarchRender3D's world position output.
