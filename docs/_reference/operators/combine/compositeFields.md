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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - vec4
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
    label: Field 2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp1
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
    label: Blend Field
    name: blendField
    required: true
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp[1-2]
  name: compositeFields
  opType: raytk.operators.combine.compositeFields
  parameters:
  - label: Enable
    name: Enable
  - label: Blend Mode
    menuOptions:
    - label: Add
      name: add
    - label: Atop
      name: atop
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
    - label: Over
      name: over
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
    - label: Under
      name: under
    - label: VividLight
      name: vividlight
    - label: Xor
      name: xor
    name: Blendmode
  - label: Blend
    name: Blend
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Swap Inputs
    name: Swapinputs
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Blend Field
    name: Blendfield
  summary: Combines two vector fields using color compositing.
  thumb: assets/images/reference/operators/combine/compositeFields_thumb.png

---


Combines two vector fields using color compositing.

Based on Photoshop blending modes, using [glsl-blend](https://github.com/jamieowen/glsl-blend).

The alpha channel is linearly blended between the two inputs using the `Blend` parameter.