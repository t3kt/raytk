---
layout: operator
title: magnet
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/magnet
redirect_from:
  - /reference/opType/raytk.operators.filter.magnet/
op:
  name: magnet
  summary: Pulls or twists space within an area.
  detail: |
    If the magnet definition input is connected, that operator is used to determine how much transformation to apply at each point in space.
    If there is no magnet definition connected, the magnet is based around a center point with a radius, and a blending region.
  opType: raytk.operators.filter.magnet
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
    - name: magnet_definition_in
      label: Magnet
      required: false
      summary: |
        Magnet definition used to determine how much transformation to apply at each point. If this is an operator that produces an SDF or float value, that value is used to decide how far each point is from the magnet. If it returns a vec4, it is used to determine where the magnet center position is relative to each point.
    - name: easing_definition_in
      label: Easing
      required: false
      summary: |
        Easing function used to control how the blending region is smoothed.
  parameters:
    - name: Enable
      label: Enable
    - name: Amount
      label: Amount
      summary: |
        How much effect to apply overall.
    - name: Center
      label: Center
      summary: |
        The center position of the magnet (used if the magnet definition is not connected).
    - name: Radius
      label: Radius
      summary: |
        The radius of the magnet area.
    - name: Fade
      label: Fade
      summary: |
        The width of the blending region between the magnet and the rest of space.
    - name: Scale
      label: Scale
      summary: |
        Scaling to be applied within the magnet area.
    - name: Rotate
      label: Rotate
      summary: |
        Rotation to be applied within the magnet area.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# magnet

Category: filter



Pulls or twists space within an area.

If the magnet definition input is connected, that operator is used to determine how much transformation to apply at each point in space.
If there is no magnet definition connected, the magnet is based around a center point with a radius, and a blending region.