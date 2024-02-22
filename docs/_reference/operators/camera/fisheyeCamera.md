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
  keywords:
  - '360'
  - cubemap
  - dome
  - equiangular
  - equirectangular
  - pinhole
  - stereographic
  name: fisheyeCamera
  opType: raytk.operators.camera.fisheyeCamera
  parameters:
  - label: Fisheye Mode
    menuOptions:
    - label: Pinhole
      name: pinhole
    - label: Stereographic
      name: stereographic
    - label: Equi-Angular
      name: equiangular
    - label: Equi-Solid Angle
      name: equisolidangle
    - label: Orthographic Fisheye
      name: orthographicfisheye
    name: Fisheyemode
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Aperture
    name: Aperture
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Position
    name: Campos
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Position of the camera.
  - label: Rotate
    name: Camrot
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotates the camera in XYZ.
  - label: Look At Position
    name: Lookatpos
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Coordinates that the camera should face.
  - label: Up Vector
    name: Camup
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Look At
    name: Enablelookat
    readOnlyHandling: semibaked
    regularHandling: runtime
  summary: A 360 fisheye camera, that shows all directions from a specific point in
    space.
  thumb: assets/images/reference/operators/camera/fisheyeCamera_thumb.png

---


A 360 fisheye camera, that shows all directions from a specific point in space.