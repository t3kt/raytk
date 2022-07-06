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
    status: beta
  - name: basicMat
    summary: Material with a basic lighting model.
  - name: colorizeSdf2d
    summary: Converts a 2D SDF to a striped distance pattern.
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
    summary: A material element that provides diffuse light contribution.
  - name: fieldMat
    status: deprecated
    summary: 'A material that uses a vector field input to determine

      the color.'
  - name: goochShadingContrib
    status: beta
    summary: A material element that uses the Gooch shading model.
  - name: matCapContrib
    status: beta
  - name: modularMat
    shortcuts:
    - mm
    summary: A material that is composed of one or more shading elements.
  - name: pbrMat
    status: beta
  - name: phongMat
    status: deprecated
    summary: Material that uses phong shading.
  - keywords:
    - lighting
    - material
    - modularmat
    - reflection
    - shading
    name: reflectContrib
    status: beta
    summary: A material element that produces color based on light reflected from
      other surfaces.
  - name: reflectMat
    status: beta
  - name: sampledPointMat
    status: beta
    summary: A material that produces color for volumetric points relative to the
      input shape.
  - keywords:
    - lighting
    - material
    - modularmat
    - shading
    - shadow
    name: shadowContrib
    status: beta
    summary: A material element that produces the shading level for the surface.
  - name: skyLightContrib
    summary: A material element that acts as a basic pseudo directional light.
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
    summary: A material element that provides specular light contribution.
  - keywords:
    - color
    - material
    - modularmat
    - surface
    name: surfaceColorContrib
    summary: A material element that produces the assigned color attribute for the
      surface.
  - name: toonShadingContrib
    status: beta
    summary: Modular shading element which uses a cell/toon shading technique with
      a color ramp.
  summary: 'Material operators that are used by renderers to determine the

    color of points on the surface of geometry.'

---

# Material Operators

Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.
