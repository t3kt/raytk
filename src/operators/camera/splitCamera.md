A camera that splits the viewport into several zones, each using a separate camera.

Important note that when the horizontal and vertical layouts currently only use the first two inputs.

## Parameters

* `Enable`
* `Layout`: How to arrange the zones.
  * `horz`: Output is split into two horizontal slices. When using this layout, only the first two inputs are used.
  * `vert`: Output is split into two vertical slices. When using this layout, only the first two inputs are used.
  * `grid`: Output is arranged in a 2x2 grid.
* `Rescale`: Whether to rescale each camera to fit each zone. When switched off, if using a grid, you will only see the top right corner of the first camera, the top left of the second, etc. When switched on, you see the full view that each camera would normally get.
* `Cameramap`: Texture that switches between cameras on a per-pixel basis. Values are scaled from 0..1 to 0..(N-1), where N is the number of connected inputs. So if there are 4 connected inputs, 0..0.249999.. is input 1, 0.25..0.49999.. is input 2, etc.

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `definition_in_3`:  This is only used by the grid layout.
* `definition_in_4`:  This is only used by the grid layout.