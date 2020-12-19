---
layout: page
title: geodesicSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/geodesicSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.geodesicSdf/
---

# geodesicSdf

Category: sdf



A geodesic polyhedron, optionally with a spike on each face.

Based on [Geodesic domain manipulation](https://www.shadertoy.com/view/4tG3zW) by tdhooper.

## Parameters

* `Enable` *Enable*
* `Shape` *Shape*: The type of polyhedron.
  * `icosahedron` *Icosahedron*
  * `dodecahedron` *Dodecahedron*
* `Divisions` *Divisions*: Number of divisions of the faces. Increasing this will result in more sides on the shape.
* `Enablefaces` *Enable Faces*: Whether to include the flat surfaces on each face.
* `Faceoffset` *Face Offset*: Distance of the faces from the center point.
* `Enablespikes` *Enable Spikes*: Whether to include a spike on each face.
* `Spikelength` *Spike Length*: The length of the spikes.
* `Spikeoffset` *Spike Offset*: The distance from the center point of the base of each spike.
* `Spikeradius` *Spike Radius*: The base radius of each spike.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1` *Spike Tip Shape*: Optional SDF that is placed at the tip of each spike.