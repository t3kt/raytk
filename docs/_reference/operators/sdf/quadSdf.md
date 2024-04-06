---
layout: operator
title: quadSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/quadSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.quadSdf/
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  keywords:
  - plane
  - quad
  - rectangle
  - square
  name: quadSdf
  opType: raytk.operators.sdf.quadSdf
  parameters:
  - label: Plane
    menuOptions:
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    - label: Custom
      name: custom
    name: Plane
    readOnlyHandling: baked
    regularHandling: baked
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 3
    name: Point3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 4
    name: Point4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/quadSdf_thumb.png

---
