---
layout: operator
title: spiralSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/spiralSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.spiralSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Spread Field
    name: spreadField
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
    - vec2
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
    supportedVariableInputs:
    - spreadField
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
    - vec2
    label: Radius Limit Field
    name: radiusLimitField
    returnTypes:
    - float
    supportedVariableInputs:
    - spreadField
    - rotateField
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
    - vec2
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - spreadField
    - rotateField
    - radiusLimitField
  name: spiralSdf2d
  opType: raytk.operators.sdf2d.spiralSdf2d
  parameters:
  - label: Spread
    name: Spread
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Use Radius Limit
    name: Useradiuslimit
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Radius Limit
    name: Radiuslimit
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/sdf2d/spiralSdf2d_thumb.png

---
