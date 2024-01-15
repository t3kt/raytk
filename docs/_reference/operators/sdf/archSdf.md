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
  - label: Width
    name: Width
  - label: Rounding
    name: Rounding
  - label: Enable Panel
    name: Enablepanel
  - label: Panel Depth
    name: Paneldepth
  - label: Enable Frame
    name: Enableframe
  - label: Frame Thickness
    name: Framethickness
  - label: Frame Depth
    name: Framedepth
  - label: Hide Frame Bottom
    name: Hideframebottom
  status: beta
  thumb: assets/images/reference/operators/sdf/archSdf_thumb.png

---
