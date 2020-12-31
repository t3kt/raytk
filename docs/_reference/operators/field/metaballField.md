---
layout: operator
title: metaballField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/metaballField
redirect_from:
  - /reference/opType/raytk.operators.field.metaballField/
op:
  name: metaballField
  summary: Metaball value field.
  opType: raytk.operators.field.metaballField
  category: field
  parameters:
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: float
          label: 1D
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Center
      label: Center
      summary: |
        Center position of the ball.
    - name: Radius
      label: Radius
      summary: |
        Radius of the ball on each axis. In 2D mode, only x and y are used. In 1D only x is used.
    - name: Radiusscale
      label: Radius Scale
      summary: |
        Scales the radius on all axes.
    - name: Weight
      label: Weight
      summary: |
        The returned values are multiplied by this.
    - name: Exponent
      label: Exponent
      summary: |
        Controls the shape of the ball by applying exponential scaling to coordinates.
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
        - name: RayContext
          label: Ray Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# metaballField

Category: field



Metaball value field.