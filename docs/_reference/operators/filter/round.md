---
layout: operator
title: round
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/round
redirect_from:
  - /reference/opType/raytk.operators.filter.round/
op:
  category: filter
  detail: 'Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm)
    from Inigo Quilez.

    See [example](https://www.shadertoy.com/view/Mt3BDj).'
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
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
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
    label: Amount Field
    name: amountField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
    supportedVariables:
    - sdf
  name: round
  opType: raytk.operators.filter.round
  parameters:
  - label: Amount
    name: Amount
    readOnlyHandling: macro
    regularHandling: runtime
    summary: positive numbers increase and round out the shape, negative numbers shrink
      it.
  - name: Usefield
    summary: whether to use the second input to determine the amount of rounding using
      a value field so various positions can use different amounts of rounding.
  - label: Enable
    name: Enable
  summary: Adds to (or subtracts from) the size of an SDF, which has the effect of
    rounding it out or shrinking it.
  thumb: assets/images/reference/operators/filter/round_thumb.png
  variables:
  - label: sdf
    name: sdf

---


Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.

Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Mt3BDj).