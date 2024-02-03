---
layout: operator
title: sphericalMobiusTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/sphericalMobiusTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.sphericalMobiusTransform/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: sphericalMobiusTransform
  opType: raytk.operators.filter.sphericalMobiusTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Rotation Amount
    name: Rotationamount
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/filter/sphericalMobiusTransform_thumb.png

---
