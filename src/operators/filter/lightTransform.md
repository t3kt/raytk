Specialized transform that can be applied to lights, taking into account things like look at direction.

Similar to `cameraTransform`, this operator is specificaly designed to work on lights.

## Parameters

* `Enable`
* `Postranslate`: Translation offset applied to the position of the light source.
* `Dirrotate`: Rotation applied to the direction which the light source is facing.
* `Lookatmode`: Whether the look at position (if used) should be adjusted with the main position or remain stationary.
  * `includepos`: The look at position should be moved by the same amount that the main position is moved.
  * `separate`: The look at position should remain in place regardless of how the main position moves.
* `Lookattranslate`: Translation offset applied to only the look at position.

## Inputs

* `light`: 
* `posTranslateField`: 
* `dirRotateField`: 
* `lookAtTranslateField`: 