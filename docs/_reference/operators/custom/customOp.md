---
layout: operator
title: customOp
parent: Custom Operators
grand_parent: Operators
permalink: /reference/operators/custom/customOp
redirect_from:
  - /reference/opType/raytk.operators.custom.customOp/
op:
  category: custom
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
  name: customOp
  opType: raytk.operators.custom.customOp
  parameters:
  - label: Enable
    name: Enable
  - label: Code
    name: Codeheader
  - label: Op Globals
    name: Opglobals
  - label: Init Code
    name: Initcode
  - label: Function
    name: Function
  - label: Material Code
    name: Materialcode
  - label: Settings
    name: Settingsheader
  - label: Macro Table
    name: Macrotable
  - label: Buffer Table
    name: Buffertable
  - label: Texture Table
    name: Texturetable
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
  - label: Types
    name: Typesheader
  - label: Coord Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: 1D
      name: float
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
    - label: Light
      name: Light
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
    - label: Light Context
      name: LightContext
    name: Contexttype
  - label: Create Op Globals
    name: Createopglobals
  - label: Create Init
    name: Createinit
  - label: Create Function
    name: Createfunction
  - label: Create Material
    name: Creatematerial
  - label: Create Missing Params
    name: Createmissingparams
  - label: Remove Unused Params
    name: Removeunusedparams
  - label: Auto Create Missing Params
    name: Autocreatemissingparams
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  status: beta

---

# customOp

Category: custom

