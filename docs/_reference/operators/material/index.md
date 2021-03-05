---
layout: operatorCategory
title: Material Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/material/
cat:
  detail: 'These operators are specialized to work with a particular type

    of output renderer. So a `sampledPointMat` can only be used with

    a `pointMapRender`, and a `phongMat` can only be used with a

    `raymarchRender3d`.


    These operators are specialized to work in the `MaterialContext`

    and may not support being fed through other OPs like filters.'
  name: material
  operators:
  - name: basicMat
    summary: Material with a basic lighting model.
  - name: colorizeSdf2d
  - name: fieldMat
    summary: 'A material that uses a vector field input to determine

      the color. Essentially this is a conversion from a

      field to a material, with no other features.'
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

These operators are specialized to work with a particular type
of output renderer. So a `sampledPointMat` can only be used with
a `pointMapRender`, and a `phongMat` can only be used with a
`raymarchRender3d`.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.
