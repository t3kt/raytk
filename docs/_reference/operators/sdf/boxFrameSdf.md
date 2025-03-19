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
    - VertexContext
    - PixelContext
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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - scaleField
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
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Move the center of the shape.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the box.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The thickness of the bars of the box.
  - label: Thickness Mode
    menuOptions:
    - label: Inset
      name: inset
    - label: Centered
      name: centered
    - label: Outset
      name: outset
    name: Thicknessmode
  - label: Bar Shape
    menuOptions:
    - label: Square
      name: square
    - label: Round
      name: round
    name: Barshape
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds XYZ
      name: bounds
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  shortcuts:
  - bfs
  summary: SDF for the squared frame of the edges of a box.
  thumb: assets/images/reference/operators/sdf/boxFrameSdf_thumb.png

---


SDF for the squared frame of the edges of a box.