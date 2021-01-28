---
layout: operator
title: generalizedPolyhedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/generalizedPolyhedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.generalizedPolyhedronSdf/
op:
  category: sdf
  detail: Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf)
    by Akleman and Chen.
  name: generalizedPolyhedronSdf
  opType: raytk.operators.sdf.generalizedPolyhedronSdf
  parameters:
  - label: Shape
    menuOptions:
    - label: Custom
      name: custom
    - label: Octahedron
      name: octahedron
    - label: Dodecahedron
      name: dodecahedron
    - label: Icosahedron
      name: icosahedron
    - label: Truncated Octahedron
      name: truncatedoctahedron
    - label: Truncated Icosahedron
      name: truncatedicosahedron
    name: Shape
    summary: Chooses between several different predefined types of polyhedra, or `Custom`,
      which uses the `Begin` and `End` parameters to generate different shapes.
  - label: Begin
    name: Begin
    summary: Only used when the `Custom` shape. It's a bit hard to describe, so it's
      best to just experiment with it and see how it behaves.
  - label: End
    name: End
    summary: Used along with `Begin`.
  - label: Translate
    name: Translate
    summary: Shifts the center of the shape.
  - label: Radius
    name: Radius
    summary: The size of the shape.
  - label: Use Exponent
    name: Useexponent
    summary: Enables the use of the `Exponent`, which controls the sharpness of the
      edges. When this is switched off, the shape will have sharp edges.
  - label: Exponent
    name: Exponent
    summary: Controls the sharpness or smoothness of the edges.
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Generates one of several different types of polyhedra.

---

# generalizedPolyhedronSdf

Category: sdf



Generates one of several different types of polyhedra.

Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf) by Akleman and Chen.