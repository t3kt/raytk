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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Irradiance Field
    name: irradiance_definition_in
    returnTypes:
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Reflectance Field
    name: reflectance_definition_in
    returnTypes:
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Base Color Field
    name: baseColor_definition_in
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Roughness Field
    name: roughness_definition_in
    returnTypes:
    - float
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Metallic Field
    name: metallic_definition_in
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
  status: beta

---
