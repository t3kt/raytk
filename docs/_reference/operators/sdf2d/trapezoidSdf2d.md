---
layout: operator
title: trapezoidSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/trapezoidSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.trapezoidSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Width Field
    name: widthField
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
    - vec2
    label: Point 1+2 Coords Field
    name: pointsField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - widthField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Height Field
    name: heightField
    returnTypes:
    - float
    supportedVariableInputs:
    - widthField
  name: trapezoidSdf2d
  opType: raytk.operators.sdf2d.trapezoidSdf2d
  parameters:
  - label: Mode
    menuOptions:
    - label: Centered
      name: centered
    - label: End Points
      name: endpoints
    name: Mode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Width
    name: Width
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/trapezoidSdf2d_thumb.png

---
