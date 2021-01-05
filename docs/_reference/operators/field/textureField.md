---
layout: operator
title: textureField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/textureField
redirect_from:
  - /reference/opType/raytk.operators.field.textureField/
op:
  name: textureField
  summary: A float or vector field that looks up values from a texture.
  opType: raytk.operators.field.textureField
  category: field
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
      label: Plane
      menuOptions:
        - name: x
          label: YZ
        - name: y
          label: ZX
        - name: z
          label: XY
    - name: Translate
      label: Translate
    - name: Scale
      label: Scale
    - name: Texture
      label: Texture
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

# textureField

Category: field



A float or vector field that looks up values from a texture.