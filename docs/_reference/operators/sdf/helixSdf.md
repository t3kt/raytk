---
layout: operator
title: helixSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/helixSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.helixSdf/
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
    - float
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    summary: Field used to multiply the `Radius` parameter. If it uses 1D coordinates,
      it is provided the position along the axis. If it uses 3D coordinates, it uses
      the absolute position.
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
    summary: Field used to multiply the `Thickness` parameter. If it uses 1D coordinates,
      it is provided the position along the axis. If it uses 3D coordinates, it uses
      the absolute position.
    supportedVariableInputs:
    - thicknessField
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
    label: Spread Field
    name: spreadField
    returnTypes:
    - float
    supportedVariableInputs:
    - thicknessField
    - radiusField
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
    - vec2
    label: Cross Section Shape
    name: crossSection
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - thicknessField
    - radiusField
    - spreadField
    supportedVariables:
    - axisoffset
    - angle
    - normangle
  keywords:
  - coil
  - helix
  - spiral
  name: helixSdf
  opType: raytk.operators.sdf.helixSdf
  parameters:
  - name: Enable
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
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Spread
    name: Spread
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Dual Spread
    name: Dualspread
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Reverse
    name: Reverse
    readOnlyHandling: semibaked
    regularHandling: runtime
  summary: SDF for a helix (an elongated spiral).
  thumb: assets/images/reference/operators/sdf/helixSdf_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf_helixSdf_axisoffset
    name: RTK_raytk_operators_sdf_helixSdf_axisoffset
  - label: RTK_raytk_operators_sdf_helixSdf_angle
    name: RTK_raytk_operators_sdf_helixSdf_angle
  - label: RTK_raytk_operators_sdf_helixSdf_normangle
    name: RTK_raytk_operators_sdf_helixSdf_normangle

---


SDF for a helix (an elongated spiral).