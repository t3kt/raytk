---
layout: operator
title: ellipsoidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/ellipsoidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.ellipsoidSdf/
op:
  category: sdf
  detail: Based on [Ellipsoid bound](https://www.shadertoy.com/view/tdS3DG) by iq.
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
    - vec4
  keywords:
  - circle
  - ellipse
  - ellipsoid
  - oval
  - sphere
  name: ellipsoidSdf
  opType: raytk.operators.sdf.ellipsoidSdf
  parameters:
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Size of the ellipsoid on each axis.
  summary: Ellipsoid (sphere with different sizes on each axis).
  thumb: assets/images/reference/operators/sdf/ellipsoidSdf_thumb.png

---


Ellipsoid (sphere with different sizes on each axis).

Based on [Ellipsoid bound](https://www.shadertoy.com/view/tdS3DG) by iq.