---
layout: operator
title: mixFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/mixFields
redirect_from:
  - /reference/opType/raytk.operators.combine.mixFields/
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 1
    name: definition_in_1
    returnTypes:
    - float
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
    label: Field 2
    name: definition_in_2
    returnTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 3
    name: definition_in_3
    returnTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 4
    name: definition_in_4
    returnTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 5
    name: definition_in_5
    returnTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 6
    name: definition_in_6
    returnTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 7
    name: definition_in_7
    returnTypes:
    - float
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 8
    name: definition_in_8
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp[1-7]
  name: mixFields
  opType: raytk.operators.combine.mixFields
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
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Default Value
    name: Defaultvalue
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Default Level
    name: Defaultlevel
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 1
    name: Enable1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 1
    name: Level1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 2
    name: Enable2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 2
    name: Level2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 3
    name: Enable3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 3
    name: Level3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 4
    name: Enable4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 4
    name: Level4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 5
    name: Enable5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 5
    name: Level5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 6
    name: Enable6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 6
    name: Level6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 7
    name: Enable7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 7
    name: Level7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable 8
    name: Enable8
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Level 8
    name: Level8
    readOnlyHandling: baked
    regularHandling: runtime

---
