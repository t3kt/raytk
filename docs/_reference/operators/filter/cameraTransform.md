---
layout: operator
title: cameraTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/cameraTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.cameraTransform/
op:
  category: filter
  detail: Similar to `lightTransform`, this operator is designed to work specifically
    with cameras, including changes to direction and look at position.
  inputs:
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera
    name: camera
    required: true
    returnTypes:
    - Ray
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec3
    label: Translate Field
    name: translateField
    required: true
    returnTypes:
    - vec4
    supportedVariableInputs:
    - camera
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec3
    label: Direction Rotate Field
    name: dirRotateField
    required: true
    returnTypes:
    - vec4
    supportedVariableInputs:
    - camera
    - translateField
  name: cameraTransform
  opType: raytk.operators.filter.cameraTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Position Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offset applied to the camera's origin position.
  - label: Direction Rotate
    name: Dirrotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotation applied to the direction that the camera is facing. Note that
      this does not impact the position of the camera.
  - label: Look At Mode
    menuOptions:
    - description: The look at position should be moved by the same amount that the
        main position is moved.
      label: Include Position Translate
      name: includepos
    - description: The look at position should remain in place regardless of how the
        main position moves.
      label: Separate Translate Only
      name: separate
    name: Lookatmode
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the look at position (if used) should be adjusted with the position
      or remain stationary.
  - label: Look At Translate
    name: Lookattranslate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Translation offset applied to only the look at position.
  status: beta
  summary: Specialized transform that can be applied to cameras.

---


Specialized transform that can be applied to cameras.

Similar to `lightTransform`, this operator is designed to work specifically with cameras, including changes to direction and look at position.