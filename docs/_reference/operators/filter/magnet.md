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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - magnet_definition_in
    - easing_definition_in
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Magnet
    name: magnet
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Easing
    name: radiusField
    returnTypes:
    - float
    summary: Easing function used to control how the blending region is smoothed.
    supportedVariableInputs:
    - magnet
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Fade Field
    name: fadeField
    returnTypes:
    - float
    supportedVariableInputs:
    - magnet
    - radiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    label: Easing Function
    name: easing
    returnTypes:
    - float
    supportedVariableInputs:
    - magnet
    - radiusField
    - fadeField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Amount Field
    name: amountField
    returnTypes:
    - float
    supportedVariableInputs:
    - magnet
    - radiusField
    - easing
    - amountField
  name: magnet
  opType: raytk.operators.filter.magnet
  parameters:
  - label: Enable
    name: Enable
  - label: Amount
    name: Amount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How much effect to apply overall.
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The center position of the magnet (used if the magnet definition is not
      connected).
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the magnet area.
  - label: Fade
    name: Fade
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The width of the blending region between the magnet and the rest of space.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scaling to be applied within the magnet area.
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotation to be applied within the magnet area.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of translation along each axis. For 2D, only X and Y are used.
  - label: Scale Type
    menuOptions:
    - label: Separate XYZ
      name: separate
    - label: Uniform
      name: uniform
    name: Scaletype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Uniform Scale
    name: Uniformscale
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Pulls or twists space within an area.
  thumb: assets/images/reference/operators/filter/magnet_thumb.png

---


Pulls or twists space within an area.

If the magnet definition input is connected, that operator is used to determine how much transformation to apply at each point in space.
If there is no magnet definition connected, the magnet is based around a center point with a radius, and a blending region.