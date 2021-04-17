---
layout: operator
title: compositeFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/compositeFields
redirect_from:
  - /reference/opType/raytk.operators.combine.compositeFields/
op:
  category: combine
  detail: 'Based on Photoshop blending modes, using [glsl-blend](https://github.com/jamieowen/glsl-blend).


    The alpha channel is linearly blended between the two inputs using the `Blend`
    parameter.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
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
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: compositeFields
  opType: raytk.operators.combine.compositeFields
  parameters:
  - label: Enable
    name: Enable
  - label: Blend Mode
    menuOptions:
    - label: Add
      name: add
    - label: Average
      name: average
    - label: Color Burn
      name: colorburn
    - label: Color Dodge
      name: colordodge
    - label: Darken
      name: darken
    - label: Difference
      name: difference
    - label: Exclusion
      name: exclusion
    - label: Glow
      name: glow
    - label: Hard Light
      name: hardlight
    - label: Hard Mix
      name: hardmix
    - label: Lighten
      name: lighten
    - label: Linear Burn
      name: linearburn
    - label: Linear Dodge
      name: lineardodge
    - label: Linear Light
      name: linearlight
    - label: Multiply
      name: multiply
    - label: Negation
      name: negation
    - label: Normal
      name: normal
    - label: Overlay
      name: overlay
    - label: Phoenix
      name: phoenix
    - label: PinLight
      name: pinlight
    - label: Reflect
      name: reflect
    - label: Screen
      name: screen
    - label: SoftLight
      name: softlight
    - label: Subtract
      name: subtract
    - label: VividLight
      name: vividlight
    name: Blendmode
  - label: Blend
    name: Blend
  - label: Swap Inputs
    name: Swapinputs
  summary: Combines two vector fields using color compositing.

---


Combines two vector fields using color compositing.

Based on Photoshop blending modes, using [glsl-blend](https://github.com/jamieowen/glsl-blend).

The alpha channel is linearly blended between the two inputs using the `Blend` parameter.