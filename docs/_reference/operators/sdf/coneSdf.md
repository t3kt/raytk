---
layout: operator
title: coneSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/coneSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.coneSdf/
op:
  name: coneSdf
  summary: Defines a cone or capped cone shape.
  opType: raytk.operators.sdf.coneSdf
  category: sdf
  inputs:
    - name: height_field_definition_in
      label: Height Field
      required: false
      coordTypes: [vec3]
      contextTypes: [Context]
      returnTypes: [float]
      summary: |
        Value field that can be used to vary the height of the cone.
    - name: radius_field_definition_in
      label: Radius Field
      required: false
      coordTypes: [vec3]
      contextTypes: [Context]
      returnTypes: [float]
      summary: |
        Value field that can be used to vary the radius (both base and top) of the cone.
  parameters:
    - name: Enable
      label: Enable
    - name: Shape
      label: Shape
      summary: |
        Choose between a regular cone and a capped cone without a tip.
      menuOptions:
        - name: cone
          label: Cone
        - name: cappedcone
          label: Capped Cone
    - name: Translate
      label: Translate
      summary: |
        Move the center of the shape.
    - name: Height
      label: Height
      summary: |
        The height of the cone.
    - name: Radius
      label: Radius
      summary: |
        The radius of the base of the cone.
    - name: Radius2
      label: Radius 2
      summary: |
        The radius of the top of the cone, if using a capped cone.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# coneSdf

Category: sdf



Defines a cone or capped cone shape.