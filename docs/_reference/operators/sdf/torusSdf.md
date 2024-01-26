---
layout: operator
title: torusSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/torusSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.torusSdf/
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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Angle Width Field
    name: angleWidthField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Angle Offset Field
    name: angleOffsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - angleWidthField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - angleWidthField
    - angleOffsetField
    supportedVariables:
    - angle
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - angleWidthField
    - angleOffsetField
    - radiusField
    supportedVariables:
    - angle
    - normangle
  keywords:
  - donut
  - ring
  - torus
  name: torusSdf
  opType: raytk.operators.sdf.torusSdf
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  - label: Translate
    name: Translate
  - label: Enable Caps
    name: Enablecaps
  - label: Angle Width
    name: Anglewidth
  - label: Angle Offset
    name: Angleoffset
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Torus
      name: torus
    name: Uvmode
  summary: SDF for a torus.
  thumb: assets/images/reference/operators/sdf/torusSdf_thumb.png
  variables:
  - label: angle
    name: angle
  - label: normangle
    name: normangle

---


SDF for a torus.