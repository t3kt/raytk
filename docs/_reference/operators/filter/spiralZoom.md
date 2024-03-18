---
layout: operator
title: spiralZoom
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/spiralZoom
redirect_from:
  - /reference/opType/raytk.operators.filter.spiralZoom/
op:
  category: filter
  detail: 'See this article for a good description of the concept:

    https://isohedral.ca/escher-like-spiral-tilings/


    In a sense, this has some similar properties to `modulo2D` in that it

    takes a slice of space and repeats it. But instead of repeating it linearly

    along the x and y axes, it does so with polar coordinates (angle and distance).


    Important note: if the input pattern / shape does not tile correctly for the

    slice that''s used, you will get a discontinuity (break in space). This is similar

    to how you shapes can get cut off when using `modulo1D` / etc.


    When using 2D coordinates, the `Axis` is ignored, and the first axis is always
    X and the second is always Y.'
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
    supportedVariableInputs:
    - twistField
    - phaseField
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
    - vec3
    label: Twist Field
    name: twistField
    returnTypes:
    - vec4
    supportedVariables:
    - logdist
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
    - vec3
    label: Phase Field
    name: phaseField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - twistField
    supportedVariables:
    - logdist
  keywords:
  - log
  - polar
  - spiral
  name: spiralZoom
  opType: raytk.operators.filter.spiralZoom
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - description: 'Spiral the Y and Z axes around the X axis. First axis: Y, second:
        Z, around: X.'
      label: X
      name: x
    - description: 'Spiral the Z and X axes around the Y axis. First axis: Z, second:
        X, around: Y.'
      label: Y
      name: y
    - description: 'Spiral the X and Y axes around the Z axis. First axis: X, second:
        Y, around: Z.'
      label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: The axis around which to spiral. The position on this axis will stay
      the same. The position on the other two axes will be wrapped around this axis.
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The center position along the two spiralled axes. Note that the parts
      of this will control different axes on the selected `Axis`.
  - label: Twist 1
    name: Twist1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of twisting to apply to the first axis.
  - label: Twist 2
    name: Twist2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of twisting to apply to the second axis.
  - label: Phase
    name: Phase
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts coordinates along the first and second axes, which has the effect
      of "spinning" different parts of the pattern.
  - label: Branches
    name: Branches
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How many "arms" or "branches" of the spiral there should be. This is
      controls how many times the first axis repeats as it goes around the axis. Note
      that if this is not a whole integer, there will be a break in the spiral.
  summary: Transforms space using a logarithmic spiral.
  thumb: assets/images/reference/operators/filter/spiralZoom_thumb.png
  variables:
  - label: RTK_raytk_operators_filter_spiralZoom_logdist
    name: RTK_raytk_operators_filter_spiralZoom_logdist
  - label: RTK_raytk_operators_filter_spiralZoom_dist
    name: RTK_raytk_operators_filter_spiralZoom_dist

---


Transforms space using a logarithmic spiral.

See this article for a good description of the concept:
https://isohedral.ca/escher-like-spiral-tilings/

In a sense, this has some similar properties to `modulo2D` in that it
takes a slice of space and repeats it. But instead of repeating it linearly
along the x and y axes, it does so with polar coordinates (angle and distance).

Important note: if the input pattern / shape does not tile correctly for the
slice that's used, you will get a discontinuity (break in space). This is similar
to how you shapes can get cut off when using `modulo1D` / etc.

When using 2D coordinates, the `Axis` is ignored, and the first axis is always X and the second is always Y.