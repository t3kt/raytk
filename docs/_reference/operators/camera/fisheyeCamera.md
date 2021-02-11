---
layout: operator
title: fisheyeCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/fisheyeCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.fisheyeCamera/
op:
  category: camera
  name: fisheyeCamera
  opType: raytk.operators.camera.fisheyeCamera
  parameters:
  - label: Fisheye Mode
    menuOptions:
    - label: pinhole
      name: pinhole
    - label: stereographic
      name: stereographic
    - label: equirectangular
      name: equiangular
    - label: equisolidangle
      name: equisolidangle
    - label: orthographicfisheye
      name: orthographicfisheye
    name: Fisheyemode
  - label: Aperture
    name: Aperture
  - label: Position
    name: Campos
    summary: Position of the camera.
  - label: Rotate
    name: Camrot
    summary: Rotates the camera in XYZ.
  - label: Look At Position
    name: Lookatpos
    summary: Coordinates that the camera should face.
  - label: Up Vector
    name: Camup
  summary: A 360 fisheye camera, that shows all directions from a specific point in
    space.

---

# fisheyeCamera

Category: camera



A 360 fisheye camera, that shows all directions from a specific point in space.