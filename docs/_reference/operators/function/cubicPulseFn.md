---
layout: operator
title: cubicPulseFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/cubicPulseFn
redirect_from:
  - /reference/opType/raytk.operators.function.cubicPulseFn/
op:
  category: function
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
    - float
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
    - float
    label: Phase Field
    name: phaseField
    returnTypes:
    - float
  name: cubicPulseFn
  opType: raytk.operators.function.cubicPulseFn
  parameters:
  - label: Width
    name: Width
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Phase
    name: Phase
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/function/cubicPulseFn_thumb.png

---
