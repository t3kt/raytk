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
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Caps
    name: Enablecaps
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Angle Width
    name: Anglewidth
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Angle Offset
    name: Angleoffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Torus
      name: torus
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  summary: SDF for a torus.
  thumb: assets/images/reference/operators/sdf/torusSdf_thumb.png
  variables:
  - label: angle
    name: angle
  - label: normangle
    name: normangle

---


SDF for a torus.