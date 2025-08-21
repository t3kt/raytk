---
layout: operator
title: mixColorFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/mixColorFields
redirect_from:
  - /reference/opType/raytk.operators.combine.mixColorFields/
op:
  category: combine
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 2
    name: definition_in_2
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-2]
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-3]
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 5
    name: definition_in_5
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-4]
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 6
    name: definition_in_6
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-5]
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 7
    name: definition_in_7
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-6]
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 8
    name: definition_in_8
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-7]
  name: mixColorFields
  opType: raytk.operators.combine.mixColorFields
  parameters:
  - label: Combine Mode
    menuOptions:
    - label: Additive
      name: add
    - label: Weighted Average
      name: weighted
    name: Combinemode
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Base Color
    name: Basecolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Base Level
    name: Baselevel
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable1
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 1
    name: Level1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 1
    name: Color1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable2
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 2
    name: Level2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 2
    name: Color2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable3
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 3
    name: Level3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 3
    name: Color3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable4
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 4
    name: Level4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 4
    name: Color4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable5
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 5
    name: Level5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 5
    name: Color5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable6
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 6
    name: Level6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 6
    name: Color6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable7
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 7
    name: Level7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 7
    name: Color7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable8
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Level 8
    name: Level8
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 8
    name: Color8
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta

---
