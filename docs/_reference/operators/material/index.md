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
    summary: Accesses color from the background field of the renderer, which is based
      on the surface normal, for use in a modularMat.
  - name: basicMat
    summary: Material with a basic lighting model.
    thumb: assets/images/reference/operators/material/basicMat_thumb.png
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
    thumb: assets/images/reference/operators/material/diffuseContrib_thumb.png
  - name: goochShadingContrib
    summary: A material element that uses the Gooch shading model.
  - name: hologramContrib
    status: beta
  - name: iridescenceContrib
    summary: Shading element that produces a rainbow pattern around the edges of shapes,
      depending on which direction the surface is facing (the surface normal).
    thumb: assets/images/reference/operators/material/iridescenceContrib_thumb.png
  - name: matCapContrib
    summary: Shading using a MatCap (Material Capture) image to fake lighting and
      reflections.
  - name: modularMat
    shortcuts:
    - mm
    summary: A material that is composed of one or more shading elements.
  - name: pbrMat
    status: beta
    thumb: assets/images/reference/operators/material/pbrMat_thumb.png
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
    thumb: assets/images/reference/operators/material/reflectMat_thumb.png
  - name: rimContrib
    summary: Shading that is applied to the edges of a surface relative to where it's
      viewed from.
    thumb: assets/images/reference/operators/material/rimContrib_thumb.png
  - name: sampledPointMat
    summary: A material that produces color for volumetric points relative to the
      input shape.
  - name: shadingProperty
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
    thumb: assets/images/reference/operators/material/skyLightContrib_thumb.png
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
    thumb: assets/images/reference/operators/material/specularContrib_thumb.png
  - name: subsurfaceContrib
    status: beta
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
    thumb: assets/images/reference/operators/material/toonShadingContrib_thumb.png
  summary: 'Material operators that are used by renderers to determine the

    color of points on the surface of geometry.'

---

# Material Operators

Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.
