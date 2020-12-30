---
layout: operator
title: generalizedPolyhedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/generalizedPolyhedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.generalizedPolyhedronSdf/
op:
  name: generalizedPolyhedronSdf
  summary: |
    Generates one of several different types of polyhedra.
  detail: |
    Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf) by Akleman and Chen.
  opType: raytk.operators.sdf.generalizedPolyhedronSdf
  category: sdf
  parameters:
    - name: Shape
      label: Shape
      summary: |
        Chooses between several different predefined types of polyhedra, or `Custom`, which uses the `Begin` and `End` parameters to generate different shapes.
      menuOptions:
        - name: custom
          label: Custom
        - name: octahedron
          label: Octahedron
        - name: dodecahedron
          label: Dodecahedron
        - name: icosahedron
          label: Icosahedron
        - name: truncatedoctahedron
          label: Truncated Octahedron
        - name: truncatedicosahedron
          label: Truncated Icosahedron
    - name: Begin
      label: Begin
      summary: |
        Only used when the `Custom` shape. It's a bit hard to describe, so it's best to just experiment with it and see how it behaves.
    - name: End
      label: End
      summary: |
        Used along with `Begin`.
    - name: Translate
      label: Translate
      summary: |
        Shifts the center of the shape.
    - name: Radius
      label: Radius
      summary: |
        The size of the shape.
    - name: Useexponent
      label: Use Exponent
      summary: |
        Enables the use of the `Exponent`, which controls the sharpness of the edges. When this is switched off, the shape will have sharp edges.
    - name: Exponent
      label: Exponent
      summary: |
        Controls the sharpness or smoothness of the edges.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# generalizedPolyhedronSdf

Category: sdf



Generates one of several different types of polyhedra.

Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf) by Akleman and Chen.