---
layout: operator
title: linkSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/linkSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.linkSdf/
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
    label: Height field
    name: lengthField
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
    label: Radius field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - lengthField
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
    label: Thickness field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - lengthField
    - radiusField
  keywords:
  - chain
  - link
  name: linkSdf
  opType: raytk.operators.sdf.linkSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the shape.
  - label: Length
    name: Length
    summary: The length of the chain link.
  - label: Radius
    name: Radius
    summary: The radius or width of the chain shape as a whole.
  - label: Thickness
    name: Thickness
    summary: The thickness of the link.
  summary: SDF for a chain link shape (an elongated loop).
  thumb: assets/images/reference/operators/sdf/linkSdf_thumb.png

---


SDF for a chain link shape (an elongated loop).