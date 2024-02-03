---
layout: operator
title: cylinderSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/cylinderSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.cylinderSdf/
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
    label: Height Field
    name: heightField
    returnTypes:
    - float
    summary: Optional field used to control the radius of the cylinder. If it uses
      1D coordinates, it is given the position along the axis. For 3D coordinates,
      it is given the raw position.
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
    label: Radius Field
    name: radiusField
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  keywords:
  - column
  - cylinder
  - pipe
  name: cylinderSdf
  opType: raytk.operators.sdf.cylinderSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Shifts the center of the cylinder.
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The radius of the cylinder.
  - label: Height
    name: Height
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The height of the cylinder, along the selected axis.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Infinite Height
    name: Infiniteheight
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Hollow
    name: Hollow
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
  summary: SDF for a cylinder.
  thumb: assets/images/reference/operators/sdf/cylinderSdf_thumb.png
  variables:
  - label: axispos
    name: axispos
  - label: normoffset
    name: normoffset
  - label: normangle
    name: normangle

---


SDF for a cylinder.