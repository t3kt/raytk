Specialized transform that can be applied to cameras.

Similar to `lightTransform`, this operator is designed to work specifically with cameras, including changes to direction and look at position.

## Parameters

* `Enable`
* `Translate`: Offset applied to the camera's origin position.
* `Dirrotate`: Rotation applied to the direction that the camera is facing. Note that this does not impact the position of the camera.
* `Lookatmode`: Whether the look at position (if used) should be adjusted with the position or remain stationary.
  * `includepos`: The look at position should be moved by the same amount that the main position is moved.
  * `separate`: The look at position should remain in place regardless of how the main position moves.
* `Lookattranslate`: Translation offset applied to only the look at position.

## Inputs

* `camera`: 
* `translateField`: 
* `dirRotateField`: 