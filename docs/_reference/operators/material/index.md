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
  - name: fieldMat
    summary: 'A material that uses a vector field input to determine

      the color.'
  - name: phongMat
    summary: Material that uses phong shading.
  - name: reflectMat
    status: beta
  summary: 'Material operators that are used by renderers to determine the

    color of points on the surface of geometry.'

---

# Material Operators

Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.
