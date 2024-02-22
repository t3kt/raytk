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
    supportedVariables:
    - axisoffset
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
    - float
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    supportedVariables:
    - axisoffset
    - normoffset
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
    - float
    - vec3
    label: Coils Field
    name: coilsField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - radiusField
    supportedVariables:
    - axisoffset
    - normoffset
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
    - float
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - radiusField
    - coilsField
    supportedVariables:
    - axisoffset
    - normoffset
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
    - vec2
    label: Cross Section Shape
    name: crossSection
    returnTypes:
    - Sdf
    summary: Optional 2D SDF used as the cross-section for the shape.
    supportedVariableInputs:
    - heightField
    - radiusField
    - coilsField
    supportedVariables:
    - axisoffset
    - normoffset
    - angle
    - normangle
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
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Reverse
    name: Reverse
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the spring, i.e. the distance of the spring from the center
      axis.
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Height or length of the spring.
  - label: Coils
    name: Coils
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of rotations in the spring. Larger values mean a tighter coil.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
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