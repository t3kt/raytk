---
layout: operator
title: lookAtCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/lookAtCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.lookAtCamera/
op:
  category: camera
  name: lookAtCamera
  opType: raytk.operators.camera.lookAtCamera
  parameters:
  - label: FOV Angle
    name: Camfov
    readOnlyHandling: macro
    regularHandling: runtime
    summary: FOV angle.
  - label: Position
    name: Campos
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Position of the camera.
  - label: Rotate
    name: Camrot
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Rotation of the camera in XYZ.
  - label: Look At Position
    name: Lookatpos
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Position that the camera faces.
  - label: Up Vector
    name: Camup
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Up vector (used to interpret the `Lookatpos`).
  shortcuts:
  - lac
  summary: A camera that focuses on a specific point in space.

---


A camera that focuses on a specific point in space.