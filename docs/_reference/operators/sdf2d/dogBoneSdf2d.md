---
layout: operator
title: dogBoneSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/dogBoneSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.dogBoneSdf2d/
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
    - vec2
    label: Length Field
    name: lengthField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
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
    label: Bulge Field
    name: bulgeField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - lengthField
  name: dogBoneSdf2d
  opType: raytk.operators.sdf2d.dogBoneSdf2d
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the shape.
  - label: Radius
    name: Radius
    summary: Radius of the circles.
  - label: Length
    name: Length
    summary: Spacing between the two circles.
  - label: Bulge
    name: Bulge
    summary: Negative values pull the connection tighter, positive values bulge out
      perpendicular to the main axis.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    name: Axis
  summary: 2D SDF for two connected circles.
  thumb: assets/images/reference/operators/sdf2d/dogBoneSdf2d_thumb.png

---


2D SDF for two connected circles.