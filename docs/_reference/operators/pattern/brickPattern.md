---
layout: operator
title: brickPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/brickPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.brickPattern/
op:
  category: pattern
  detail: 'This pattern produces just float values not colors. To apply color to it,
    pass it into a `colorRampField`.


    The bricks themselves produce values of 0 (or black) and the spaces between them
    produce values of 1 (or white).'
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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    summary: Field that controls the thickness of the spacing between bricks.
    supportedVariableInputs:
    - coordField
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
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    summary: Field that controls the amount of blending between bricks and spacing.
    supportedVariableInputs:
    - coordField
    - thicknessField
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
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    summary: Field that controls how much alternating rows are shifted.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - shiftField
  name: brickPattern
  opType: raytk.operators.pattern.brickPattern
  parameters:
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offsets every other row of bricks. A value of 0 means a regular grid,
      and 0.5 is a standard staggered brick layout.
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
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the spacing between the bricks.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of blending between bricks and spacing.
  summary: Pattern of stacked rectangular bricks.
  thumb: assets/images/reference/operators/pattern/brickPattern_thumb.png

---


Pattern of stacked rectangular bricks.

This pattern produces just float values not colors. To apply color to it, pass it into a `colorRampField`.

The bricks themselves produce values of 0 (or black) and the spaces between them produce values of 1 (or white).