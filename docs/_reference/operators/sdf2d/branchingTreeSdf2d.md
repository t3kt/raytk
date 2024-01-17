---
layout: operator
title: branchingTreeSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/branchingTreeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.branchingTreeSdf2d/
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  name: branchingTreeSdf2d
  opType: raytk.operators.sdf2d.branchingTreeSdf2d
  parameters:
  - label: Branches
    name: Branches
  - label: Radius
    name: Radius
  - label: Forks
    name: Forks
  - label: Exponent
    name: Exponent
  - label: Thickness Inner
    name: Thicknessinner
  - label: Thickness Outer
    name: Thicknessouter
  - label: Limit Outside
    name: Limitoutside
  status: beta
  thumb: assets/images/reference/operators/sdf2d/branchingTreeSdf2d_thumb.png
  variables:
  - label: normdist
    name: normdist
  - label: forkindex
    name: forkindex
  - label: normforkindex
    name: normforkindex

---
