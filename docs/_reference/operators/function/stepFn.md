---
layout: operator
title: stepFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/stepFn
redirect_from:
  - /reference/opType/raytk.operators.function.stepFn/
op:
  category: function
  name: stepFn
  opType: raytk.operators.function.stepFn
  parameters:
  - label: Function
    menuOptions:
    - label: Step
      name: step
    - label: Smoothstep
      name: smoothstep
    - label: Smoothstep Integral
      name: smoothstepIntegral
    name: Function
    readOnlyHandling: macro
    regularHandling: macro
  - label: Edge
    name: Edge
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Below this the result will be 0 and above it will produce 1. When using
      blending, the bottom edge will be `Blend/2` lower than this and the upper edge
      will be `Blend/2` higher.
  - label: Blend
    name: Blend
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The amount of smoothing to apply on the edge.
  - label: Invert
    name: Invert
    readOnlyHandling: macro
    regularHandling: macro
  summary: A function that changes from zero to one at a cutoff point.
  thumb: assets/images/reference/operators/function/stepFn_thumb.png

---


A function that changes from zero to one at a cutoff point.