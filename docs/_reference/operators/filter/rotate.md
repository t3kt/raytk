---
layout: operator
title: rotate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/rotate
redirect_from:
  - /reference/opType/raytk.operators.filter.rotate/
op:
  category: filter
  detail: 'The operator has 2 main modes: a single rotation around an axis, or 3 separate
    rotations around each axis.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
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
    coordTypes:
    - vec2
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
    - vec4
    - Sdf
    summary: Optional field that can be used to control the amount of rotation. If
      in single axis mode, this must produce a single float value, which is added
      to the `Rotate` parameter. If in 3 axis mode, it can either produce a single
      value, which is multiplied with each of the axis rotations. Or it can produce
      vectors which are added to the axis rotations.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: Pivot Field
    name: pivotField
    returnTypes:
    - vec4
    summary: Optional field that can be used to control the pivot point.
  keywords:
  - rotate
  - spin
  - transform
  - twist
  name: rotate
  opType: raytk.operators.filter.rotate
  parameters:
  - label: Enable
    name: Enable
  - label: Rotate Mode
    menuOptions:
    - label: Axis
      name: axis
    - label: Euler
      name: euler
    name: Rotatemode
  - label: Axis
    name: Axis
    summary: The direction of the axis around which to rotate. This is a vector pointing
      along the axis.
  - label: Rotate
    name: Rotate
    summary: The amount of rotation to use when in single-axis mode. This is specified
      in degrees (0..360).
  - label: Rotate Order
    menuOptions:
    - label: Rx Ry Rz
      name: xyz
    - label: Rx Rz Ry
      name: xzy
    - label: Ry Rx Rz
      name: yxz
    - label: Ry Rz Rx
      name: yzx
    - label: Rz Rx Ry
      name: zxy
    - label: Rz Ry Rx
      name: zyx
    name: Rord
    summary: The order of the 3 axis rotations.
  - label: Rotate XYZ
    name: Rot
    summary: The amount of rotation along each axis, in degrees (0..360).
  - label: Use Pivot
    name: Usepivot
    summary: Optionally pivot the rotation around a specific point instead of around
      the origin (0, 0, 0).
  - label: Pivot
    name: Pivot
    summary: The point around which to apply the rotation. For 2D coordinates, only
      the X and Y parts are used.
  shortcuts:
  - rot
  summary: Transforms space with rotation.

---


Transforms space with rotation.

The operator has 2 main modes: a single rotation around an axis, or 3 separate rotations around each axis.