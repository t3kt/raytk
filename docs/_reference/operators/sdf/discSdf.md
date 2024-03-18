---
layout: operator
title: discSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/discSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.discSdf/
op:
  category: sdf
  detail: Because the disc is infinitely thin, it will only appear as a line when
    viewed from the side.
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
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
    - radiusField
    supportedVariables:
    - angle
    - normangle
    - normaxisdist
  name: discSdf
  opType: raytk.operators.sdf.discSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the center of the disc.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the disc.
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
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  summary: A flat disc facing the Y axis.
  thumb: assets/images/reference/operators/sdf/discSdf_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf_discSdf_angle
    name: RTK_raytk_operators_sdf_discSdf_angle
  - label: RTK_raytk_operators_sdf_discSdf_normangle
    name: RTK_raytk_operators_sdf_discSdf_normangle
  - label: RTK_raytk_operators_sdf_discSdf_normaxisdist
    name: RTK_raytk_operators_sdf_discSdf_normaxisdist

---


A flat disc facing the Y axis.

Because the disc is infinitely thin, it will only appear as a line when viewed from the side.