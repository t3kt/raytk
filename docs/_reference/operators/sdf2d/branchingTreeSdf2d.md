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
    supportedVariableInputs:
    - radiusField
    supportedVariables:
    - normdist
    - forkindex
    - normforkindex
  name: branchingTreeSdf2d
  opType: raytk.operators.sdf2d.branchingTreeSdf2d
  parameters:
  - label: Branches
    name: Branches
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Forks
    name: Forks
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Exponent
    name: Exponent
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Thickness Inner
    name: Thicknessinner
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Thickness Outer
    name: Thicknessouter
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Limit Outside
    name: Limitoutside
    readOnlyHandling: constant
    regularHandling: runtime
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
