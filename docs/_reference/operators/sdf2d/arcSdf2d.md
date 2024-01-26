---
layout: operator
title: arcSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/arcSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.arcSdf2d/
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
    label: Orientation Field
    name: orientationField
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
    label: Aperture Field
    name: apertureField
    returnTypes:
    - float
    supportedVariableInputs:
    - orientationField
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - orientationField
    supportedVariables:
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
    - vec2
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - orientationField
    - radiusField
    supportedVariables:
    - normangle
  name: arcSdf2d
  opType: raytk.operators.sdf2d.arcSdf2d
  parameters:
  - label: Orientation
    name: Orientation
  - label: Aperture
    name: Aperture
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  thumb: assets/images/reference/operators/sdf2d/arcSdf2d_thumb.png
  variables:
  - label: normangle
    name: normangle

---
