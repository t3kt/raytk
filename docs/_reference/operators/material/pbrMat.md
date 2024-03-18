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
    supportedVariableInputs:
    - metallicField
    - roughnessField
    - baseColorField
    supportedVariables:
    - RTK_raytk_operators_material_pbrMat_lightcolor
    - RTK_raytk_operators_material_pbrMat_lightpos
    - RTK_raytk_operators_material_pbrMat_surfacecolor
    - RTK_raytk_operators_material_pbrMat_surfaceuv
    - RTK_raytk_operators_material_pbrMat_shadedlevel
    - RTK_raytk_operators_material_pbrMat_normal
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Reflectance Field
    name: reflectanceField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - metallicField
    - roughnessField
    - baseColorField
    - irradianceField
    supportedVariables:
    - RTK_raytk_operators_material_pbrMat_lightcolor
    - RTK_raytk_operators_material_pbrMat_lightpos
    - RTK_raytk_operators_material_pbrMat_surfacecolor
    - RTK_raytk_operators_material_pbrMat_surfaceuv
    - RTK_raytk_operators_material_pbrMat_shadedlevel
    - RTK_raytk_operators_material_pbrMat_normal
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Base Color Field
    name: baseColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - metallicField
    - roughnessField
    supportedVariables:
    - RTK_raytk_operators_material_pbrMat_lightcolor
    - RTK_raytk_operators_material_pbrMat_lightpos
    - RTK_raytk_operators_material_pbrMat_surfacecolor
    - RTK_raytk_operators_material_pbrMat_surfaceuv
    - RTK_raytk_operators_material_pbrMat_shadedlevel
    - RTK_raytk_operators_material_pbrMat_normal
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Roughness Field
    name: roughnessField
    returnTypes:
    - float
    supportedVariables:
    - RTK_raytk_operators_material_pbrMat_lightcolor
    - RTK_raytk_operators_material_pbrMat_lightpos
    - RTK_raytk_operators_material_pbrMat_surfacecolor
    - RTK_raytk_operators_material_pbrMat_surfaceuv
    - RTK_raytk_operators_material_pbrMat_shadedlevel
    - RTK_raytk_operators_material_pbrMat_normal
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Metallic Field
    name: metallicField
    returnTypes:
    - float
    supportedVariableInputs:
    - roughnessField
    supportedVariables:
    - RTK_raytk_operators_material_pbrMat_lightcolor
    - RTK_raytk_operators_material_pbrMat_lightpos
    - RTK_raytk_operators_material_pbrMat_surfacecolor
    - RTK_raytk_operators_material_pbrMat_surfaceuv
    - RTK_raytk_operators_material_pbrMat_shadedlevel
    - RTK_raytk_operators_material_pbrMat_normal
  name: pbrMat
  opType: raytk.operators.material.pbrMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Use Surface Color
    name: Usesurfacecolor
    readOnlyHandling: baked
    regularHandling: baked
  - label: Roughness
    name: Roughness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Albedo
    name: Albedo
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Metallic
    name: Metallic
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
  - label: Use Local Position
    name: Uselocalpos
    readOnlyHandling: baked
    regularHandling: baked
  - label: Apply When
    menuOptions:
    - label: Always
      name: always
    - label: Only If Unassigned
      name: missing
    name: Condition
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/material/pbrMat_thumb.png
  variables:
  - label: RTK_raytk_operators_material_pbrMat_lightcolor
    name: RTK_raytk_operators_material_pbrMat_lightcolor
  - label: RTK_raytk_operators_material_pbrMat_lightpos
    name: RTK_raytk_operators_material_pbrMat_lightpos
  - label: RTK_raytk_operators_material_pbrMat_surfacecolor
    name: RTK_raytk_operators_material_pbrMat_surfacecolor
  - label: RTK_raytk_operators_material_pbrMat_surfaceuv
    name: RTK_raytk_operators_material_pbrMat_surfaceuv
  - label: RTK_raytk_operators_material_pbrMat_shadedlevel
    name: RTK_raytk_operators_material_pbrMat_shadedlevel
  - label: RTK_raytk_operators_material_pbrMat_normal
    name: RTK_raytk_operators_material_pbrMat_normal

---
