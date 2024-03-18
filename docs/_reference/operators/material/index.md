---
layout: operatorCategory
title: Material Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/material/
cat:
  detail: 'These operators are specialized to work in the `MaterialContext`

    and may not support being fed through other OPs like filters.'
  name: material
  operators:
  - name: backgroundFieldContrib
  - name: basicMat
  - name: colorizeSdf2d
  - keywords:
    - diffuse
    - lambert
    - lighting
    - material
    - modularmat
    - oren-nayar
    - shading
    name: diffuseContrib
    shortcuts:
    - dc
  - name: goochShadingContrib
  - name: hologramContrib
    status: beta
  - name: iridescenceContrib
    status: beta
  - name: matCapContrib
    status: beta
  - name: modularMat
    shortcuts:
    - mm
  - name: pbrMat
    status: beta
  - name: phongMat
    status: deprecated
  - keywords:
    - lighting
    - material
    - modularmat
    - reflection
    - shading
    name: reflectContrib
    status: beta
  - name: reflectMat
    status: beta
  - name: rimContrib
  - name: sampledPointMat
  - name: shadingProperty
    status: beta
  - keywords:
    - lighting
    - material
    - modularmat
    - shading
    - shadow
    name: shadowContrib
    status: beta
  - name: skyLightContrib
  - keywords:
    - ggx
    - lighting
    - material
    - modularmat
    - phong
    - shading
    - specular
    name: specularContrib
    shortcuts:
    - sc
  - name: subsurfaceContrib
    status: beta
  - keywords:
    - color
    - material
    - modularmat
    - surface
    name: surfaceColorContrib
  - name: toonShadingContrib
    status: beta
  summary: 'Material operators that are used by renderers to determine the

    color of points on the surface of geometry.'

---

# Material Operators

Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.
