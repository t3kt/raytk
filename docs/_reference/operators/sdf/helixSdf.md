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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec3
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
    coordTypes:
    - vec2
    label: Cross Section Shape
    name: crossSection
    returnTypes:
    - float
    - Sdf
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
  - label: Translate
    name: Translate
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  - label: Spread
    name: Spread
  - label: Dual Spread
    name: Dualspread
  - label: Reverse
    name: Reverse
  summary: SDF for a helix (an elongated spiral).
  thumb: assets/images/reference/operators/sdf/helixSdf_thumb.png
  variables:
  - label: axisoffset
    name: axisoffset
  - label: angle
    name: angle
  - label: normangle
    name: normangle

---


SDF for a helix (an elongated spiral).