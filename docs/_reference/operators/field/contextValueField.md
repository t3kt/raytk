---
layout: operator
title: contextValueField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/contextValueField
redirect_from:
  - /reference/opType/raytk.operators.field.contextValueField/
op:
  category: field
  name: contextValueField
  opType: raytk.operators.field.contextValueField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Field
    menuOptions:
    - label: Iteration
      name: iteration
    - label: Orbit Trap (Material)
      name: matorbit
    - label: Step Count (Material)
      name: matsteps
    - label: Near Hits (Material)
      name: matnearhits
    - label: Iteration (Material)
      name: matiteration
    - label: Object ID (Material)
      name: matobjectid
    - label: Orbit Trap (Light)
      name: lightorbit
    - label: Step Count (Light)
      name: lightsteps
    - label: Near Hits (Light)
      name: lightnearhits
    - label: Iteration (Light)
      name: lightiteration
    - label: Object ID (Light)
      name: lightobjectid
    name: Contextfield
    summary: Which context property to access.
  summary: Field that returns various fields from the context, from a downstream OP.

---


Field that returns various fields from the context, from a downstream OP.