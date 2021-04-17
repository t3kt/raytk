---
layout: operator
title: magnet
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/magnet
redirect_from:
  - /reference/opType/raytk.operators.filter.magnet/
op:
  category: filter
  detail: 'If the magnet definition input is connected, that operator is used to determine
    how much transformation to apply at each point in space.

    If there is no magnet definition connected, the magnet is based around a center
    point with a radius, and a blending region.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Magnet
    name: magnet_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    summary: Magnet definition used to determine how much transformation to apply
      at each point. If this is an operator that produces an SDF or float value, that
      value is used to decide how far each point is from the magnet. If it returns
      a vec4, it is used to determine where the magnet center position is relative
      to each point.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    label: Easing
    name: easing_definition_in
    returnTypes:
    - float
    summary: Easing function used to control how the blending region is smoothed.
  name: magnet
  opType: raytk.operators.filter.magnet
  parameters:
  - label: Enable
    name: Enable
  - label: Amount
    name: Amount
    summary: How much effect to apply overall.
  - label: Center
    name: Center
    summary: The center position of the magnet (used if the magnet definition is not
      connected).
  - label: Radius
    name: Radius
    summary: The radius of the magnet area.
  - label: Fade
    name: Fade
    summary: The width of the blending region between the magnet and the rest of space.
  - label: Scale
    name: Scale
    summary: Scaling to be applied within the magnet area.
  - label: Rotate
    name: Rotate
    summary: Rotation to be applied within the magnet area.
  summary: Pulls or twists space within an area.

---


Pulls or twists space within an area.

If the magnet definition input is connected, that operator is used to determine how much transformation to apply at each point in space.
If there is no magnet definition connected, the magnet is based around a center point with a radius, and a blending region.