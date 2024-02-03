---
layout: operator
title: archSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/archSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.archSdf/
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
    label: Width Field
    name: widthField
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
    label: Rounding Field
    name: roundingField
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
    label: Frame Thickness Field
    name: frameThicknessField
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
    label: Frame Depth Field
    name: frameDepthField
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
    label: Panel Depth Field
    name: panelDepthField
    returnTypes:
    - float
  name: archSdf
  opType: raytk.operators.sdf.archSdf
  parameters:
  - label: Height
    name: Height
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Width
    name: Width
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Rounding
    name: Rounding
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Panel
    name: Enablepanel
    readOnlyHandling: constant
    regularHandling: constant
  - label: Panel Depth
    name: Paneldepth
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Frame
    name: Enableframe
    readOnlyHandling: constant
    regularHandling: constant
  - label: Frame Thickness
    name: Framethickness
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Frame Depth
    name: Framedepth
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Hide Frame Bottom
    name: Hideframebottom
    readOnlyHandling: constant
    regularHandling: constant
  status: beta
  thumb: assets/images/reference/operators/sdf/archSdf_thumb.png

---
