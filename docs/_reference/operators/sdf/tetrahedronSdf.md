---
layout: operator
title: tetrahedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/tetrahedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.tetrahedronSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
  name: tetrahedronSdf
  opType: raytk.operators.sdf.tetrahedronSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Scale
    name: Scale
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The size of the shape.
  summary: Tetrahedron shape.
  thumb: assets/images/reference/operators/sdf/tetrahedronSdf_thumb.png

---


Tetrahedron shape.