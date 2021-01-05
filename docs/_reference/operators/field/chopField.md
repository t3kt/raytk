---
layout: operator
title: chopField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/chopField
redirect_from:
  - /reference/opType/raytk.operators.field.chopField/
op:
  name: chopField
  opType: raytk.operators.field.chopField
  category: field
  status: beta
  parameters:
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Returntype
      label: Return Type
      menuOptions:
        - name: float
          label: Float
        - name: vec4
          label: Vector
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
        - name: LightContext
          label: Light Context
    - name: Axis
      label: Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Translate
      label: Translate
    - name: Scale
      label: Scale
    - name: Chop
      label: CHOP
    - name: Extendmode
      label: Extend Mode
      menuOptions:
        - name: hold
          label: Hold
        - name: zero
          label: Zero
        - name: repeat
          label: Repeat
        - name: mirror
          label: Mirror
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# chopField

Category: field

