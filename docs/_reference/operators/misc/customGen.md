---
layout: operator
title: customGen
parent: Misc Operators
grand_parent: Operators
permalink: /reference/operators/misc/customGen
redirect_from:
  - /reference/opType/raytk.operators.misc.customGen/
op:
  category: misc
  name: customGen
  opType: raytk.operators.misc.customGen
  parameters:
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
    - label: 3D
      name: vec3
    - label: 2D
      name: vec2
    name: Coordtype
  - label: Return Type
    menuOptions:
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
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  status: deprecated

---

# customGen

Category: misc

