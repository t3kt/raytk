---
layout: operator
title: customFilter
parent: Misc Operators
grand_parent: Operators
permalink: /reference/operators/misc/customFilter
redirect_from:
  - /reference/opType/raytk.operators.misc.customFilter/
op:
  category: misc
  inputs:
  - contextTypes:
    - none
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in1
    name: definition_in1
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in2
    name: definition_in2
    returnTypes:
    - float
    - vec4
    - Sdf
  - contextTypes:
    - none
    - Context
    coordTypes:
    - vec2
    - vec3
    label: definition_in3
    name: definition_in3
    returnTypes:
    - float
    - vec4
    - Sdf
  name: customFilter
  opType: raytk.operators.misc.customFilter
  parameters:
  - label: Enable
    name: Enable
  - label: Vec Param 1
    name: Vecparam1
  - label: Vec Param 2
    name: Vecparam2
  - label: Vec Param 3
    name: Vecparam3
  - label: Vec Param 4
    name: Vecparam4
  - label: Float Param 1
    name: Floatparam1
  - label: Float Param 2
    name: Floatparam2
  - label: Float Param 3
    name: Floatparam3
  - label: Float Param 4
    name: Floatparam4
  - label: Coord Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: 3D
      name: vec3
    - label: 2D
      name: vec2
    name: Coordtype
  - label: Return Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: SDF Result
      name: Sdf
    - label: Float
      name: float
    - label: Vector4
      name: vec4
    - label: Ray
      name: Ray
    name: Returntype
  - label: Context Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    name: Contexttype
  - label: Function
    name: Function
  - label: Create Function
    name: Createfunction
  - label: Op Globals
    name: Opglobals
  - label: Init Code
    name: Initcode
  - label: Macro Table
    name: Macrotable
  - label: Library Names
    menuOptions:
    - label: hg_sdf
      name: hg_sdf
    - label: raytkCommon
      name: raytkCommon
    - label: raytkSdf
      name: raytkSdf
    - label: raytkMaterial
      name: raytkMaterial
    name: Librarynames
  status: deprecated

---
