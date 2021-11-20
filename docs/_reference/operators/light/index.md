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
  - name: axisLight
    status: beta
  - name: directionalLight
    summary: A directional light.
  - name: hardShadow
    summary: A simple hard-edged shadow.
  - name: lightVolume
    status: beta
  - name: linkedLight
    status: beta
    summary: Light that is based on a standard Light COMP.
  - name: pointLight
    summary: Light eminating from a single point in space, with optional distance
      attentuation.
  - name: softShadow
    summary: A soft-edged shadow.
  - name: spotLight
    status: beta
    summary: Cone-shaped spotlight.
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
