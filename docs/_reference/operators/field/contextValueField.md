---
layout: operator
title: contextValueField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/contextValueField
redirect_from:
  - /reference/opType/raytk.operators.field.contextValueField/
op:
  name: contextValueField
  summary: Field that returns various fields from the context, from a downstream OP.
  opType: raytk.operators.field.contextValueField
  category: field
  parameters:
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Contextfield
      label: Context Field
      menuOptions:
        - name: iteration
          label: Iteration
        - name: matorbit
          label: Orbit Trap (Material)
        - name: matsteps
          label: Step Count (Material)
        - name: matnearhits
          label: Near Hits (Material)
        - name: matiteration
          label: Iteration (Material)
        - name: matobjectid
          label: Object ID (Material)
        - name: lightorbit
          label: Orbit Trap (Light)
        - name: lightsteps
          label: Step Count (Light)
        - name: lightnearhits
          label: Near Hits (Light)
        - name: lightiteration
          label: Iteration (Light)
        - name: lightobjectid
          label: Object ID (Light)
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# contextValueField

Category: field



Field that returns various fields from the context, from a downstream OP.