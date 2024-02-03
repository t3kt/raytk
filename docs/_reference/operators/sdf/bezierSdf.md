---
layout: operator
title: bezierSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/bezierSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.bezierSdf/
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
    label: Point 1 Field
    name: point1Field
    returnTypes:
    - vec4
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
    label: Point 2 Field
    name: point2Field
    returnTypes:
    - vec4
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
    label: Point 3 Field
    name: point3Field
    returnTypes:
    - vec4
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
    - float
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  keywords:
  - bezier
  - curve
  - line
  name: bezierSdf
  opType: raytk.operators.sdf.bezierSdf
  parameters:
  - label: Point 1
    name: Point1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 3
    name: Point3
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Radius Start
    name: Radiusstart
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Radius End
    name: Radiusend
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/bezierSdf_thumb.png
  variables:
  - label: normoffset
    name: normoffset

---
