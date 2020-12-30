---
layout: operator
title: lookAtCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/lookAtCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.lookAtCamera/
op:
  name: lookAtCamera
  summary: |
    A camera that focuses on a specific point in space.
  opType: raytk.operators.camera.lookAtCamera
  category: camera
  parameters:
    - name: Camfov
      label: FOV Angle
      summary: |
        FOV angle.
    - name: Campos
      label: Position
      summary: |
        Position of the camera.
    - name: Camrot
      label: Rotate
      summary: |
        Rotation of the camera in XYZ.
    - name: Lookatpos
      label: Look At Position
      summary: |
        Position that the camera faces.
    - name: Camup
      label: Up Vector
      summary: |
        Up vector (used to interpret the `Lookatpos`).
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# lookAtCamera

Category: camera



A camera that focuses on a specific point in space.