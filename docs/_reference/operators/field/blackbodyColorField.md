---
layout: operator
title: blackbodyColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/blackbodyColorField
redirect_from:
  - /reference/opType/raytk.operators.field.blackbodyColorField/
op:
  category: field
  detail: 'The operator uses a temperature value, either from a parameter of an input
    field, and determines the glow color that temperature would produce.


    Based on [Tunnel Beauty](https://www.shadertoy.com/view/Mt3GW2) by aiekick.


    Details on [wikipedia](https://en.wikipedia.org/wiki/Black_body).'
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
    - vec4
    label: Temperature Field
    name: tempField
    required: true
    returnTypes:
    - float
  name: blackbodyColorField
  opType: raytk.operators.field.blackbodyColorField
  parameters:
  - label: Temperature
    name: Temp
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Constant value to use for the temperature, everywhere in space. This
      is only used if there is no input temperature field.
  - label: Temperature Unit
    menuOptions:
    - description: Normalized to a 0..1 range.
      label: Normalized (0..1)
      name: norm
    - description: Degrees kelvin.
      label: Degrees Kelvin
      name: deg
    name: Tempunit
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How to interpret temperature values.
  - label: Exponent
    name: Exp
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Tighness of the transition curve from dark to light.
  summary: Field that produces colors using a model of blackbody radiation from physics.
  thumb: assets/images/reference/operators/field/blackbodyColorField_thumb.png

---


Field that produces colors using a model of blackbody radiation from physics.

The operator uses a temperature value, either from a parameter of an input field, and determines the glow color that temperature would produce.

Based on [Tunnel Beauty](https://www.shadertoy.com/view/Mt3GW2) by aiekick.

Details on [wikipedia](https://en.wikipedia.org/wiki/Black_body).