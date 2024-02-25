---
layout: operator
title: restrictStage
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/restrictStage
redirect_from:
  - /reference/opType/raytk.operators.filter.restrictStage/
op:
  category: filter
  detail: '

    This can be used for optimization, by switching off expensive ROPs for shadows.

    It can also be used to have shapes that are invisible but still cast shadows.


    In cases where the main operator is not being included, this will produce either
    the alternative operator input (if connected), or a default value otherwise.

    The default value is "non-hit" for SDFs, and `0` / `vec4(0)` etc for other types.'
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
    - vec4
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
    - vec4
    label: Alternate Definition
    name: alternate_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: restrictStage
  opType: raytk.operators.filter.restrictStage
  parameters:
  - label: Enable
    name: Enable
  - label: Include Primary
    name: Includeprimary
    readOnlyHandling: baked
    regularHandling: baked
    summary: 'Whether the operator should '
  - label: Include Shadow
    name: Includeshadow
    readOnlyHandling: baked
    regularHandling: baked
  - label: Include Reflect
    name: Includereflect
    readOnlyHandling: baked
    regularHandling: baked
  - label: Include Material
    name: Includematerial
    readOnlyHandling: baked
    regularHandling: baked
  - label: Include Occlusion
    name: Includeocclusion
    readOnlyHandling: baked
    regularHandling: baked
  - label: Include Volumetric
    name: Includevolumetric
    readOnlyHandling: baked
    regularHandling: baked
  - label: Include Volumetric Shadow
    name: Includevolumetricshadow
    readOnlyHandling: baked
    regularHandling: baked
  - label: Include Normal
    name: Includenormal
    readOnlyHandling: baked
    regularHandling: baked
  summary: Restricts which render stages an operator is used in.

---


Restricts which render stages an operator is used in.


This can be used for optimization, by switching off expensive ROPs for shadows.
It can also be used to have shapes that are invisible but still cast shadows.

In cases where the main operator is not being included, this will produce either the alternative operator input (if connected), or a default value otherwise.
The default value is "non-hit" for SDFs, and `0` / `vec4(0)` etc for other types.