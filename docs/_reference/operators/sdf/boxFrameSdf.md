---
layout: operator
title: boxFrameSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/boxFrameSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.boxFrameSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  keywords:
  - box
  - cube
  - frame
  - rectangle
  - square
  name: boxFrameSdf
  opType: raytk.operators.sdf.boxFrameSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Move the center of the shape.
  - label: Scale
    name: Scale
    summary: The size of the box.
  - label: Thickness
    name: Thickness
    summary: The thickness of the bars of the box.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds XYZ
      name: bounds
    name: Uvmode
  summary: SDF for the squared frame of the edges of a box.
  thumb: assets/images/reference/operators/sdf/boxFrameSdf_thumb.png

---


SDF for the squared frame of the edges of a box.