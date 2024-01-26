---
layout: operator
title: pieSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/pieSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.pieSdf2d/
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
    label: Angle Field
    name: angleField
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    - vec4
    summary: Radius field, either a float, or a vector with outer and inner radius
    supportedVariableInputs:
    - angleField
    supportedVariables:
    - normangle
  keywords:
  - arc
  - ring
  - slice
  name: pieSdf2d
  opType: raytk.operators.sdf2d.pieSdf2d
  parameters:
  - label: Radius
    name: Radius
    summary: The distance from the center to the outer edge.
  - label: Angle
    name: Angle
    summary: The width of the slice in degrees.
  - label: Rotate
    name: Rotate
    summary: Rotation for the slice in degrees.
  - label: Shape
    menuOptions:
    - label: Slice
      name: slice
    - label: Ring
      name: ring
    - label: Infinite
      name: infinite
    name: Shape
  - label: Inner Radius
    name: Innerradius
  summary: SDF for a 2D pie-slice shape.
  thumb: assets/images/reference/operators/sdf2d/pieSdf2d_thumb.png
  variables:
  - label: normangle
    name: normangle

---


SDF for a 2D pie-slice shape.