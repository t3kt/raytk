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
    - none
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
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
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
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    - Sdf
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
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Smoothly blends/morphs between up to 4 SDFs.

---

# blend

Category: combine



Smoothly blends/morphs between up to 4 SDFs.

The blend index only considers inputs that are connected, so if you connect the second and fourth inputs, it will treat the second as 0 and the fourth as 1.