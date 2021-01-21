---
layout: operatorCategory
title: Light Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/light/
cat:
  name: light
  summary: |
    Operators that are used in raymarching to define the behavior of light, including
    light sources and shadow behaviors.
  detail: |
    These operators are generally specialized for use in the raymarching `LightContext`
    and may not support being fed through other OPs like filters.
  operators:
    - op:
      name: directionalLight
      status: beta
    - op:
      name: hardShadow
      summary: A simple hard-edged shadow.
    - op:
      name: pointLight
      summary: Light eminating from a single point in space, with optional distance attentuation.
    - op:
      name: softShadow
      summary: A soft-edged shadow.

---

# Light Operators

Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.

These operators are generally specialized for use in the raymarching `LightContext`
and may not support being fed through other OPs like filters.
