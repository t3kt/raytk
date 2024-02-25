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
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Direction Rotate
    name: Dirrotate
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta

---
