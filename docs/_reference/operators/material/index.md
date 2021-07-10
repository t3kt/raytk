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
  - name: basicMat
    summary: Material with a basic lighting model.
  - name: colorizeSdf2d
    summary: Converts a 2D SDF to a striped distance pattern.
  - name: diffuseContrib
    status: beta
    summary: A material element that provides diffuse light contribution.
  - name: fieldMat
    summary: 'A material that uses a vector field input to determine

      the color.'
  - name: goochMat
    status: beta
    summary: A material that uses the Gooch shading model.
  - name: goochShadingContrib
    status: beta
    summary: A material element that uses the Gooch shading model.
  - name: modularMat
    status: beta
    summary: A material that is composed of one or more shading elements.
  - name: orenNayarMat
    status: beta
  - name: phongMat
    summary: Material that uses phong shading.
  - name: reflectContrib
    status: beta
    summary: A material element that produces color based on light reflected from
      other surfaces.
  - name: reflectMat
    status: beta
  - name: sampledPointMat
    status: beta
    summary: A material that produces color for volumetric points relative to the
      input shape.
  - name: shadowContrib
    status: beta
    summary: A material element that produces the shading level for the surface.
  - name: skyLightContrib
    status: beta
    summary: A material element that acts as a basic pseudo directional light.
  - name: specularContrib
    status: beta
    summary: A material element that provides specular light contribution.
  - name: surfaceColorContrib
    status: beta
    summary: A material element that produces the assigned color attribute for the
      surface.
  summary: 'Material operators that are used by renderers to determine the

    color of points on the surface of geometry.'

---

# Material Operators

Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.
