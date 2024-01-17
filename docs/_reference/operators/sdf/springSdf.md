---
layout: operator
title: springSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/springSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.springSdf/
op:
  category: sdf
  detail: This is similar to `helixSdf`, but with the fixed height rather than infinite.
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
    - float
    - vec3
    label: Height Field
    name: heightField
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
    - float
    - vec3
    label: Radius Field
    name: radiusField
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
    - float
    - vec3
    label: Coils Field
    name: coilsField
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
    - float
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
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
    label: Cross Section Shape
    name: crossSection
    returnTypes:
    - Sdf
    summary: Optional 2D SDF used as the cross-section for the shape.
  name: springSdf
  opType: raytk.operators.sdf.springSdf
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
  - label: Reverse
    name: Reverse
  - label: Radius
    name: Radius
    summary: The radius of the spring, i.e. the distance of the spring from the center
      axis.
  - label: Height
    name: Height
    summary: Height or length of the spring.
  - label: Coils
    name: Coils
    summary: The number of rotations in the spring. Larger values mean a tighter coil.
  - label: Thickness
    name: Thickness
    summary: Thickness of the spring, used when no cross-section SDF is attached.
  status: beta
  summary: A coiled spring shape.
  thumb: assets/images/reference/operators/sdf/springSdf_thumb.png
  variables:
  - label: axisoffset
    name: axisoffset
  - label: normoffset
    name: normoffset
  - label: angle
    name: angle
  - label: normangle
    name: normangle

---


A coiled spring shape.

This is similar to `helixSdf`, but with the fixed height rather than infinite.