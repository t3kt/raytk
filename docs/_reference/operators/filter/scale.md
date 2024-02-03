---
layout: operator
title: scale
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/scale
redirect_from:
  - /reference/opType/raytk.operators.filter.scale/
op:
  category: filter
  detail: Scaling works for either 3D or 2D inputs.
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
    label: definition_in
    name: definition_in
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - Sdf
    summary: If provided, this field is used to modify the scaling at different points
      in space. If the field returns float values, the value of all the `Scale` parameters
      are multiplied by that value. If it returns vec4 values, each part of the `Scale`
      parameter is multiplied by the corresponding value in the vec4.
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
    label: Pivot Field
    name: pivotField
    returnTypes:
    - vec4
  keywords:
  - scale
  - transform
  name: scale
  opType: raytk.operators.filter.scale
  parameters:
  - label: Enable
    name: Enable
  - label: Scale
    name: Scale
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Scale to apply to each axis. If input is 2D only X and Y are used.
  - label: Scale Type
    menuOptions:
    - label: Separate XYZ
      name: separate
    - label: Uniform
      name: uniform
    name: Scaletype
    readOnlyHandling: constant
    regularHandling: constant
  - label: Uniform Scale
    name: Uniformscale
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Use Pivot
    name: Usepivot
    readOnlyHandling: constant
    regularHandling: runtime
    summary: Optionally pivot the rotation around a specific point instead of around
      the origin (0, 0, 0).
  - label: Pivot
    name: Pivot
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The point around which to apply the rotation. For 2D coordinates, only
      the X and Y parts are used.
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
  summary: Scales space.

---


Scales space.

Scaling works for either 3D or 2D inputs.