---
layout: operator
title: pbrMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/pbrMat
redirect_from:
  - /reference/opType/raytk.operators.material.pbrMat/
op:
  category: material
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Irradiance Field
    name: irradianceField
    returnTypes:
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Reflectance Field
    name: reflectanceField
    returnTypes:
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Base Color Field
    name: baseColorField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Roughness Field
    name: roughnessField
    returnTypes:
    - float
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Metallic Field
    name: metallicField
    returnTypes:
    - float
  name: pbrMat
  opType: raytk.operators.material.pbrMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Use Surface Color
    name: Usesurfacecolor
  - label: Roughness
    name: Roughness
  - label: Albedo
    name: Albedo
  - label: Metallic
    name: Metallic
  - label: Enable Shadow
    name: Enableshadow
  - label: Use Local Position
    name: Uselocalpos
  - label: Apply When
    menuOptions:
    - label: Always
      name: always
    - label: Only If Unassigned
      name: missing
    name: Condition
  status: beta
  thumb: assets/images/reference/operators/material/pbrMat_thumb.png
  variables:
  - label: lightcolor
    name: lightcolor
  - label: lightpos
    name: lightpos
  - label: surfacecolor
    name: surfacecolor
  - label: surfaceuv
    name: surfaceuv
  - label: shadedlevel
    name: shadedlevel
  - label: normal
    name: normal

---
