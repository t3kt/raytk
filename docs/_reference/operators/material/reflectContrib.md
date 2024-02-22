---
layout: operator
title: reflectContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/reflectContrib
redirect_from:
  - /reference/opType/raytk.operators.material.reflectContrib/
op:
  category: material
  detail: In order for this to work, reflection support needs to be enabled in the
    renderer.
  keywords:
  - lighting
  - material
  - modularmat
  - reflection
  - shading
  name: reflectContrib
  opType: raytk.operators.material.reflectContrib
  parameters:
  - label: Level
    name: Level
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The general intensity of the color.
  - label: Ks
    name: Ks
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Fresnel
    name: Fresnel
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to apply the shadow to the color/level produced by this element.
  status: beta
  summary: A material element that produces color based on light reflected from other
    surfaces.

---


A material element that produces color based on light reflected from other surfaces.

In order for this to work, reflection support needs to be enabled in the renderer.