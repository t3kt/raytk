---
layout: operator
title: crossSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/crossSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.crossSdf/
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
    name: sizeField
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
    label: Smooth Radius Field
    name: smoothRadiusField
    returnTypes:
    - float
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
    label: Length Field
    name: lengthField
    returnTypes:
    - float
    - vec4
  name: crossSdf
  opType: raytk.operators.sdf.crossSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the cross.
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The width of the arms of the cross.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Smoothing applied to the intersections of the arms.
  - label: Axes
    menuOptions:
    - label: All Axes
      name: xyz
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    name: Axes
  - label: Shape
    menuOptions:
    - label: Infinite
      name: infinite
    - label: Limited XYZ
      name: limitxyz
    name: Shape
  - label: Length
    name: Length
    readOnlyHandling: macro
    regularHandling: runtime
  summary: An SDF for a 3D cross of infinite length along each axis.
  thumb: assets/images/reference/operators/sdf/crossSdf_thumb.png

---


An SDF for a 3D cross of infinite length along each axis.