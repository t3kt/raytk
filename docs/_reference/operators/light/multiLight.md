---
layout: operator
title: multiLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/multiLight
redirect_from:
  - /reference/opType/raytk.operators.light.multiLight/
op:
  category: light
  detail: 'This causes the renderer to repeat the surface shading process for each
    light and then combine the results.


    If shadows are enabled, this can have a significant impact on performance.


    Each light source can optionally specify an SDF that defines the bounds of the
    area where that light is used. This can help to optimize rendering if one light
    is only needed in certain areas.'
  inputs:
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 1
    name: definition_in_1
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 2
    name: definition_in_2
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 3
    name: definition_in_3
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 4
    name: definition_in_4
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 5
    name: definition_in_5
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 6
    name: definition_in_6
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 7
    name: definition_in_7
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light 8
    name: definition_in_8
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 1
    name: bounds1
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 2
    name: bounds2
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 3
    name: bounds3
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 4
    name: bounds4
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 5
    name: bounds5
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 6
    name: bounds6
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 7
    name: bounds7
    returnTypes:
    - Sdf
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds 8
    name: bounds8
    returnTypes:
    - Sdf
  name: multiLight
  opType: raytk.operators.light.multiLight
  parameters:
  - label: Enable 1
    name: Enable1
  - label: Level 1
    name: Level1
  - label: Bounds 1
    name: Bounds1
  - label: Enable 2
    name: Enable2
  - label: Level 2
    name: Level2
  - label: Bounds 2
    name: Bounds2
  - label: Enable 3
    name: Enable3
  - label: Level 3
    name: Level3
  - label: Bounds 3
    name: Bounds3
  - label: Enable 4
    name: Enable4
  - label: Level 4
    name: Level4
  - label: Bounds 4
    name: Bounds4
  - label: Enable 5
    name: Enable5
  - label: Level 5
    name: Level5
  - label: Bounds 5
    name: Bounds5
  - label: Enable 6
    name: Enable6
  - label: Level 6
    name: Level6
  - label: Bounds 6
    name: Bounds6
  - label: Enable 7
    name: Enable7
  - label: Level 7
    name: Level7
  - label: Bounds 7
    name: Bounds7
  - label: Enable 8
    name: Enable8
  - label: Level 8
    name: Level8
  - label: Bounds 8
    name: Bounds8
  status: beta
  summary: Combines multiple light sources.

---


Combines multiple light sources.

This causes the renderer to repeat the surface shading process for each light and then combine the results.

If shadows are enabled, this can have a significant impact on performance.

Each light source can optionally specify an SDF that defines the bounds of the area where that light is used. This can help to optimize rendering if one light is only needed in certain areas.