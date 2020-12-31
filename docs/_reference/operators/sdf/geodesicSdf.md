---
layout: operator
title: geodesicSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/geodesicSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.geodesicSdf/
op:
  name: geodesicSdf
  summary: A geodesic polyhedron, optionally with a spike on each face.
  detail: |
    Based on [Geodesic domain manipulation](https://www.shadertoy.com/view/4tG3zW) by tdhooper.
  opType: raytk.operators.sdf.geodesicSdf
  category: sdf
  inputs:
    - name: definition_in_1
      label: Spike Tip Shape
      required: false
      summary: |
        Optional SDF that is placed at the tip of each spike.
  parameters:
    - name: Enable
      label: Enable
    - name: Shape
      label: Shape
      summary: |
        The type of polyhedron.
      menuOptions:
        - name: icosahedron
          label: Icosahedron
        - name: dodecahedron
          label: Dodecahedron
    - name: Divisions
      label: Divisions
      summary: |
        Number of divisions of the faces. Increasing this will result in more sides on the shape.
    - name: Enablefaces
      label: Enable Faces
      summary: |
        Whether to include the flat surfaces on each face.
    - name: Faceoffset
      label: Face Offset
      summary: |
        Distance of the faces from the center point.
    - name: Enablespikes
      label: Enable Spikes
      summary: |
        Whether to include a spike on each face.
    - name: Spikelength
      label: Spike Length
      summary: |
        The length of the spikes.
    - name: Spikeoffset
      label: Spike Offset
      summary: |
        The distance from the center point of the base of each spike.
    - name: Spikeradius
      label: Spike Radius
      summary: |
        The base radius of each spike.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# geodesicSdf

Category: sdf



A geodesic polyhedron, optionally with a spike on each face.

Based on [Geodesic domain manipulation](https://www.shadertoy.com/view/4tG3zW) by tdhooper.