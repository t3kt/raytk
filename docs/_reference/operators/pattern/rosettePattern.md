---
layout: operator
title: rosettePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/rosettePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.rosettePattern/
op:
  category: pattern
  detail: 'This pattern produces just float values not colors. To apply color to it,
    pass it into a `colorRampField`.


    The edges of the circles produce values of 1 and the background produces values
    of 0.'
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
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Glow Field
    name: glowField
    returnTypes:
    - float
    summary: Field that controls the amount of glow or blending.
    supportedVariableInputs:
    - coordField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    summary: Field that controls the radii of the circles.
    supportedVariableInputs:
    - coordField
    - glowField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Spread Field
    name: spreadField
    returnTypes:
    - vec4
    summary: Field that controls how much the circles are spread apart.
    supportedVariableInputs:
    - coordField
    - glowField
    - radiusField
  name: rosettePattern
  opType: raytk.operators.pattern.rosettePattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the pattern.
  - label: Glow
    name: Glow
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of glow, or blending between the circle edges and the background.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the circles. A value of 1 makes the circles overlap perfectly
      at the center of their neighbors, 0.5 causes them to touch the edges of the
      neighbors, and 0 makes the circles dots. Values larger than 1 will cut off parts
      of the circles.
  - label: Spread
    name: Spread
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How much the arrangement of circles should be spread out along each axis.
  summary: Pattern with overlapping circles in a hexagonal arrangement.
  thumb: assets/images/reference/operators/pattern/rosettePattern_thumb.png

---


Pattern with overlapping circles in a hexagonal arrangement.

This pattern produces just float values not colors. To apply color to it, pass it into a `colorRampField`.

The edges of the circles produce values of 1 and the background produces values of 0.