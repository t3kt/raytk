---
layout: operator
title: fisheyeCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/fisheyeCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.fisheyeCamera/
op:
  name: fisheyeCamera
  summary: |
    A 360 fisheye camera, that shows all directions from a specific point in space.
  opType: raytk.operators.camera.fisheyeCamera
  category: camera
  parameters:
    - name: Fisheyemode
      label: Fisheye Mode
      menuOptions:
        - name: pinhole
          label: pinhole
        - name: stereographic
          label: stereographic
        - name: equiangular
          label: equirectangular
        - name: equisolidangle
          label: equisolidangle
        - name: orthographicfisheye
          label: orthographicfisheye
    - name: Aperture
      label: Aperture
    - name: Campos
      label: Position
      summary: |
        Position of the camera.
    - name: Camrot
      label: Rotate
      summary: |
        Rotates the camera in XYZ.
    - name: Lookatpos
      label: Look At Position
      summary: |
        Coordinates that the camera should face.
    - name: Camup
      label: Up Vector
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# fisheyeCamera

Category: camera



A 360 fisheye camera, that shows all directions from a specific point in space.