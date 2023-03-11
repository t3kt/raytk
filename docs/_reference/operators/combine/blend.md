---
layout: operator
title: blend
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/blend
redirect_from:
  - /reference/opType/raytk.operators.combine.blend/
op:
  category: combine
  detail: The blend index only considers inputs that are connected, so if you connect
    the second and fourth inputs, it will treat the second as 0 and the fourth as
    1.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in_1
    name: definition_in_1
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
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in_2
    name: definition_in_2
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
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in_3
    name: definition_in_3
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
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in_4
    name: definition_in_4
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
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: blendField
    name: blendField
    returnTypes:
    - float
  name: blend
  opType: raytk.operators.combine.blend
  parameters:
  - label: Enable
    name: Enable
  - label: Blend
    name: Blend
    summary: Which input or combination of inputs to use. If this value is 0, the
      first connected input is used. 0.5 is half way between the first and second
      connected inputs, etc.
  - label: Use Last Input As Switch
    name: Usefield
    summary: Whether to use the 4th input as a field to determine the blending, instead
      of using it as just another input.
  - label: Blend Source
    name: Blendsource
  status: deprecated
  summary: Smoothly blends/morphs between up to 4 SDFs.
  thumb: assets/images/reference/operators/combine/blend_thumb.png

---


Smoothly blends/morphs between up to 4 SDFs.

The blend index only considers inputs that are connected, so if you connect the second and fourth inputs, it will treat the second as 0 and the fourth as 1.