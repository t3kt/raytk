---
layout: operator
title: orthoCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/orthoCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.orthoCamera/
op:
  name: orthoCamera
  summary: |
    An orthographic (non-perspective) camera, which can be used for flattened front/side/etc views.
  opType: raytk.operators.camera.orthoCamera
  category: camera
  parameters:
    - name: Direction
      label: Direction
      summary: |
        Direction that the camera faces.
      menuOptions:
        - name: xpos
          label: Left (X+)
        - name: xneg
          label: Right (X-)
        - name: ypos
          label: Bottom (Y+)
        - name: yneg
          label: Top (Y-)
        - name: zpos
          label: Back (Z+)
        - name: zneg
          label: Front (Z-)
    - name: Campos
      label: Position
      summary: |
        Position of the camera.
    - name: Rotate
      label: Rotate
      summary: |
        Rotation of the camera view on the axis facing the camera.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# orthoCamera

Category: camera



An orthographic (non-perspective) camera, which can be used for flattened front/side/etc views.