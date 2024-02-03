---
layout: operator
title: circleSdf
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/circleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.circleSdf/
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
  name: circleSdf
  opType: raytk.operators.sdf2d.circleSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the circle.
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Radius of the circle.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Cartesian
      name: cartesian
    - label: Polar
      name: polar
    - label: External Parameterization
      name: extparam
    - label: Normalized Extern Parameterization
      name: normextparam
    name: Uvmode
    readOnlyHandling: constant
    regularHandling: constant
  - label: External Band Size
    name: Externalbandsize
    readOnlyHandling: macro
    regularHandling: runtime
  summary: 2D circle SDF.
  thumb: assets/images/reference/operators/sdf2d/circleSdf_thumb.png

---


2D circle SDF.