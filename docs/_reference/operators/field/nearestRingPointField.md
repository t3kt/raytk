---
layout: operator
title: nearestRingPointField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/nearestRingPointField
redirect_from:
  - /reference/opType/raytk.operators.field.nearestRingPointField/
op:
  category: field
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
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  name: nearestRingPointField
  opType: raytk.operators.field.nearestRingPointField
  parameters:
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
    regularHandling: semibaked
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Points
    name: Points
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Format
    menuOptions:
    - label: Distance
      name: dist
    - label: Absolute Position
      name: abspos
    - label: Vector
      name: vec
    name: Format
    readOnlyHandling: baked
    regularHandling: baked
  thumb: assets/images/reference/operators/field/nearestRingPointField_thumb.png
  variables:
  - label: RTK_raytk_operators_field_nearestRingPointField_pos
    name: RTK_raytk_operators_field_nearestRingPointField_pos
  - label: RTK_raytk_operators_field_nearestRingPointField_angle
    name: RTK_raytk_operators_field_nearestRingPointField_angle
  - label: RTK_raytk_operators_field_nearestRingPointField_dist
    name: RTK_raytk_operators_field_nearestRingPointField_dist
  - label: RTK_raytk_operators_field_nearestRingPointField_vector
    name: RTK_raytk_operators_field_nearestRingPointField_vector
  - label: RTK_raytk_operators_field_nearestRingPointField_step
    name: RTK_raytk_operators_field_nearestRingPointField_step
  - label: RTK_raytk_operators_field_nearestRingPointField_normstep
    name: RTK_raytk_operators_field_nearestRingPointField_normstep

---
