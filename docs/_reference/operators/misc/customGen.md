---
layout: operator
title: customGen
parent: Misc Operators
grand_parent: Operators
permalink: /reference/operators/misc/customGen
redirect_from:
  - /reference/opType/raytk.operators.misc.customGen/
op:
  name: customGen
  opType: raytk.operators.misc.customGen
  category: misc
  status: deprecated
  parameters:
    - name: Vecparam1
      label: Vec Param 1
    - name: Vecparam2
      label: Vec Param 2
    - name: Vecparam3
      label: Vec Param 3
    - name: Vecparam4
      label: Vec Param 4
    - name: Floatparam1
      label: Float Param 1
    - name: Floatparam2
      label: Float Param 2
    - name: Floatparam3
      label: Float Param 3
    - name: Floatparam4
      label: Float Param 4
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: vec3
          label: 3D
        - name: vec2
          label: 2D
    - name: Returntype
      label: Return Type
      menuOptions:
        - name: Sdf
          label: SDF Result
        - name: float
          label: Float
        - name: vec4
          label: Vector4
        - name: Ray
          label: Ray
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
    - name: Function
      label: Function
    - name: Createfunction
      label: Create Function
    - name: Opglobals
      label: Op Globals
    - name: Initcode
      label: Init Code
    - name: Macrotable
      label: Macro Table
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
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# customGen

Category: misc

