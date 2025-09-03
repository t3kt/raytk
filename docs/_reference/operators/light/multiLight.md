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
    sourceParamLabel: Bounds 1
    sourceParamName: Bounds1
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
    sourceParamLabel: Bounds 2
    sourceParamName: Bounds2
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
    sourceParamLabel: Bounds 3
    sourceParamName: Bounds3
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
    sourceParamLabel: Bounds 4
    sourceParamName: Bounds4
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
    sourceParamLabel: Bounds 5
    sourceParamName: Bounds5
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
    sourceParamLabel: Bounds 6
    sourceParamName: Bounds6
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
    sourceParamLabel: Bounds 7
    sourceParamName: Bounds7
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
    sourceParamLabel: Bounds 8
    sourceParamName: Bounds8
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
  - label: Color 1
    name: Color1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 1
    name: Translate1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 2
    name: Color2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 2
    name: Translate2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 3
    name: Color3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 3
    name: Translate3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 4
    name: Color4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 4
    name: Translate4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 5
    name: Color5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 5
    name: Translate5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 6
    name: Color6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 6
    name: Translate6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 7
    name: Color7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 7
    name: Translate7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 8
    name: Color8
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate 8
    name: Translate8
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Combines multiple light sources.

---


Combines multiple light sources.

This causes the renderer to repeat the surface shading process for each light and then combine the results.

If shadows are enabled, this can have a significant impact on performance.

Each light source can optionally specify an SDF that defines the bounds of the area where that light is used. This can help to optimize rendering if one light is only needed in certain areas.