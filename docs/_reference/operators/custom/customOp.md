---
layout: operator
title: customOp
parent: Custom Operators
grand_parent: Operators
permalink: /reference/operators/custom/customOp
redirect_from:
  - /reference/opType/raytk.operators.custom.customOp/
op:
  name: customOp
  opType: raytk.operators.custom.customOp
  category: custom
  inputs:
    - name: definition_in
      label: definition_in
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context]
      returnTypes: [float,vec4,Sdf]
    - name: definition_in1
      label: definition_in1
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context]
      returnTypes: [float,vec4,Sdf]
    - name: definition_in2
      label: definition_in2
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context]
      returnTypes: [float,vec4,Sdf]
    - name: definition_in3
      label: definition_in3
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context]
      returnTypes: [float,vec4,Sdf]
  parameters:
    - name: Enable
      label: Enable
    - name: Codeheader
      label: Code
    - name: Opglobals
      label: Op Globals
    - name: Initcode
      label: Init Code
    - name: Function
      label: Function
    - name: Materialcode
      label: Material Code
    - name: Settingsheader
      label: Settings
    - name: Macrotable
      label: Macro Table
    - name: Buffertable
      label: Buffer Table
    - name: Texturetable
      label: Texture Table
    - name: Librarynames
      label: Library Names
      menuOptions:
        - name: hg_sdf
          label: hg_sdf
        - name: raytkCommon
          label: raytkCommon
        - name: raytkSdf
          label: raytkSdf
        - name: raytkMaterial
          label: raytkMaterial
    - name: Typesheader
      label: Types
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: float
          label: 1D
        - name: vec3
          label: 3D
        - name: vec2
          label: 2D
    - name: Returntype
      label: Return Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: Sdf
          label: SDF Result
        - name: float
          label: Float
        - name: vec4
          label: Vector4
        - name: Ray
          label: Ray
        - name: Light
          label: Light
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Createopglobals
      label: Create Op Globals
    - name: Createinit
      label: Create Init
    - name: Createfunction
      label: Create Function
    - name: Creatematerial
      label: Create Material
    - name: Createmissingparams
      label: Create Missing Params
    - name: Removeunusedparams
      label: Remove Unused Params
    - name: Autocreatemissingparams
      label: Auto Create Missing Params
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# customOp

Category: custom

