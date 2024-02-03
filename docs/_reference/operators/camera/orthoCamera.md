---
layout: operator
title: orthoCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/orthoCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.orthoCamera/
op:
  category: camera
  name: orthoCamera
  opType: raytk.operators.camera.orthoCamera
  parameters:
  - label: Direction
    menuOptions:
    - label: Left (X+)
      name: xpos
    - label: Right (X-)
      name: xneg
    - label: Bottom (Y+)
      name: ypos
    - label: Top (Y-)
      name: yneg
    - label: Back (Z+)
      name: zpos
    - label: Front (Z-)
      name: zneg
    name: Direction
    summary: Direction that the camera faces.
  - label: Position
    name: Campos
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Position of the camera.
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Rotation of the camera view on the axis facing the camera.
  status: beta
  summary: An orthographic (non-perspective) camera, which can be used for flattened
    front/side/etc views.

---


An orthographic (non-perspective) camera, which can be used for flattened front/side/etc views.