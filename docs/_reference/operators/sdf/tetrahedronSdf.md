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
    - VertexContext
    - PixelContext
    - PopContext
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
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the shape.
  summary: Tetrahedron shape.
  thumb: assets/images/reference/operators/sdf/tetrahedronSdf_thumb.png

---


Tetrahedron shape.