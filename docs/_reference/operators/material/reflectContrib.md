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
    summary: The general intensity of the color.
  - label: Ks
    name: Ks
  - label: Fresnel
    name: Fresnel
  status: beta
  summary: A material element that produces color based on light reflected from other
    surfaces.

---


A material element that produces color based on light reflected from other surfaces.

In order for this to work, reflection support needs to be enabled in the renderer.