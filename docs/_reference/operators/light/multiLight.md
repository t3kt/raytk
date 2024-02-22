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
    supportedVariableInputs:
    - bounds1
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
    supportedVariableInputs:
    - bounds[1-2]
    - inputOp1
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
    supportedVariableInputs:
    - bounds[1-3]
    - inputOp[1-2]
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
    supportedVariableInputs:
    - bounds[1-4]
    - inputOp[1-3]
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
    supportedVariableInputs:
    - bounds[1-5]
    - inputOp[1-4]
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
    supportedVariableInputs:
    - bounds[1-6]
    - inputOp[1-5]
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
    supportedVariableInputs:
    - bounds[1-7]
    - inputOp[1-6]
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
    supportedVariableInputs:
    - bounds[1-8]
    - inputOp[1-7]
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
    supportedVariableInputs:
    - bounds1
    - inputOp1
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
    supportedVariableInputs:
    - bounds[1-2]
    - inputOp[1-2]
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
    supportedVariableInputs:
    - bounds[1-3]
    - inputOp[1-3]
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
    supportedVariableInputs:
    - bounds[1-4]
    - inputOp[1-4]
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
    supportedVariableInputs:
    - bounds[1-5]
    - inputOp[1-5]
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
    supportedVariableInputs:
    - bounds[1-6]
    - inputOp[1-6]
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
    supportedVariableInputs:
    - bounds[1-7]
    - inputOp[1-7]
  name: multiLight
  opType: raytk.operators.light.multiLight
  parameters:
  - label: Enable 1
    name: Enable1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 1
    name: Level1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 1
    name: Bounds1
  - label: Enable 2
    name: Enable2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 2
    name: Level2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 2
    name: Bounds2
  - label: Enable 3
    name: Enable3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 3
    name: Level3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 3
    name: Bounds3
  - label: Enable 4
    name: Enable4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 4
    name: Level4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 4
    name: Bounds4
  - label: Enable 5
    name: Enable5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 5
    name: Level5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 5
    name: Bounds5
  - label: Enable 6
    name: Enable6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 6
    name: Level6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 6
    name: Bounds6
  - label: Enable 7
    name: Enable7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 7
    name: Level7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 7
    name: Bounds7
  - label: Enable 8
    name: Enable8
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 8
    name: Level8
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds 8
    name: Bounds8
  status: beta
  summary: Combines multiple light sources.

---


Combines multiple light sources.

This causes the renderer to repeat the surface shading process for each light and then combine the results.

If shadows are enabled, this can have a significant impact on performance.

Each light source can optionally specify an SDF that defines the bounds of the area where that light is used. This can help to optimize rendering if one light is only needed in certain areas.