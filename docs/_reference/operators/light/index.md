---
layout: operatorCategory
title: Light Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/light/
cat:
  detail: 'These operators are generally specialized for use in the raymarching `LightContext`

    and may not support being fed through other OPs like filters.'
  name: light
  operators:
  - name: ambientLight
    status: beta
  - name: axisLight
  - name: directionalLight
  - name: hardShadow
  - name: lightVolume
    status: beta
  - name: linkedLight
    status: beta
  - name: multiLight
  - name: pointLight
    shortcuts:
    - pl
  - name: ringLight
  - name: softShadow
  - name: spotLight
  - name: volumetricRayCast
    status: beta
  summary: 'Operators that are used in raymarching to define the behavior of light,
    including

    light sources and shadow behaviors.'

---

# Light Operators

Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.

These operators are generally specialized for use in the raymarching `LightContext`
and may not support being fed through other OPs like filters.
