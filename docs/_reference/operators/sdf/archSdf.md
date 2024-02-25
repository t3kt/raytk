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
    supportedVariableInputs:
    - heightField
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
    supportedVariableInputs:
    - heightField
    - widthField
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
    supportedVariableInputs:
    - heightField
    - widthField
    - roundingField
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
    supportedVariableInputs:
    - heightField
    - widthField
    - roundingField
    - frameThicknessField
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
    supportedVariableInputs:
    - heightField
    - widthField
    - roundingField
    - frameThicknessField
    - frameDepthField
  name: archSdf
  opType: raytk.operators.sdf.archSdf
  parameters:
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Width
    name: Width
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rounding
    name: Rounding
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Panel
    name: Enablepanel
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Panel Depth
    name: Paneldepth
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Frame
    name: Enableframe
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Frame Thickness
    name: Framethickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Frame Depth
    name: Framedepth
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Hide Frame Bottom
    name: Hideframebottom
    readOnlyHandling: semibaked
    regularHandling: semibaked
  status: beta
  thumb: assets/images/reference/operators/sdf/archSdf_thumb.png

---
