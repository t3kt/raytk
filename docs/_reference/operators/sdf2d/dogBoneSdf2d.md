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
    label: Point 1 Field
    name: point1
    returnTypes:
    - vec4
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
    label: Point 2 Field
    name: point2
    returnTypes:
    - vec4
    supportedVariableInputs:
    - point1Field
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
    supportedVariableInputs:
    - point1Field
    - point2Field
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
    - vec2
    label: Bulge Field
    name: bulgeField
    returnTypes:
    - float
    supportedVariableInputs:
    - point1Field
    - point2Field
    - lengthField
    - radiusField
  name: dogBoneSdf2d
  opType: raytk.operators.sdf2d.dogBoneSdf2d
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Radius Multiplier
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Radius of the circles.
  - label: Length
    name: Length
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Spacing between the two circles.
  - label: Bulge
    name: Bulge
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Negative values pull the connection tighter, positive values bulge out
      perpendicular to the main axis.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Custom
      name: custom
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Point 1
    name: Pointa
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Pointb
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius
    name: Rad
    readOnlyHandling: baked
    regularHandling: runtime
  summary: 2D SDF for two connected circles.
  thumb: assets/images/reference/operators/sdf2d/dogBoneSdf2d_thumb.png

---


2D SDF for two connected circles.