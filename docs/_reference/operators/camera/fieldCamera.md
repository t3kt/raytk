---
layout: operator
title: fieldCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/fieldCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.fieldCamera/
op:
  category: camera
  inputs:
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Direction Field
    name: directionField
    required: true
    returnTypes:
    - vec4
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Position Field
    name: positionField
    returnTypes:
    - vec4
  name: fieldCamera
  opType: raytk.operators.camera.fieldCamera
  parameters:
  - label: Position
    name: Campos
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Position of the camera.
  status: beta

---
