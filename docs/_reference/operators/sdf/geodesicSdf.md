---
layout: operator
title: geodesicSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/geodesicSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.geodesicSdf/
op:
  category: sdf
  detail: Based on [Geodesic domain manipulation](https://www.shadertoy.com/view/4tG3zW)
    by tdhooper.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Face Offset Field
    name: faceOffset
    returnTypes:
    - float
    summary: Optional SDF that is placed at the tip of each spike.
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: Spike Tip Shape
    name: spikeSdf
    returnTypes:
    - Sdf
  keywords:
  - geodesic
  - polyhedron
  - spikes
  name: geodesicSdf
  opType: raytk.operators.sdf.geodesicSdf
  parameters:
  - label: Enable
    name: Enable
  - label: Shape
    menuOptions:
    - label: Icosahedron
      name: icosahedron
    - label: Dodecahedron
      name: dodecahedron
    name: Shape
    summary: The type of polyhedron.
  - label: Divisions
    name: Divisions
    summary: Number of divisions of the faces. Increasing this will result in more
      sides on the shape.
  - label: Enable Faces
    name: Enablefaces
    summary: Whether to include the flat surfaces on each face.
  - label: Face Offset
    name: Faceoffset
    summary: Distance of the faces from the center point.
  - label: Enable Spikes
    name: Enablespikes
    summary: Whether to include a spike on each face.
  - label: Spike Length
    name: Spikelength
    summary: The length of the spikes.
  - label: Spike Offset
    name: Spikeoffset
    summary: The distance from the center point of the base of each spike.
  - label: Spike Radius
    name: Spikeradius
    summary: The base radius of each spike.
  - label: Face Offset Field Coord Mode
    menuOptions:
    - label: Original Position
      name: origpos
    - label: Geodesic Position
      name: geopos
    name: Faceoffsetfieldcoordmode
  summary: A geodesic polyhedron, optionally with a spike on each face.
  thumb: assets/images/reference/operators/sdf/geodesicSdf_thumb.png

---


A geodesic polyhedron, optionally with a spike on each face.

Based on [Geodesic domain manipulation](https://www.shadertoy.com/view/4tG3zW) by tdhooper.