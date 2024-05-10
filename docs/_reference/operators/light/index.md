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
    summary: Ambient light source that doesn't come from a particular location.
  - name: axisLight
    summary: Light that emits from along an axis, similar to an infinitely long tube
      light.
    thumb: assets/images/reference/operators/light/axisLight_thumb.png
  - name: directionalLight
    summary: Directional or distant light which always comes from one direction.
    thumb: assets/images/reference/operators/light/directionalLight_thumb.png
  - name: hardShadow
    summary: A simple hard-edged shadow.
    thumb: assets/images/reference/operators/light/hardShadow_thumb.png
  - name: instanceLight
  - name: lightVolume
    status: beta
    thumb: assets/images/reference/operators/light/lightVolume_thumb.png
  - name: linkedLight
    status: beta
    summary: Light that is based on a standard Light COMP.
  - name: multiLight
    summary: Combines multiple light sources.
  - name: pointLight
    shortcuts:
    - pl
    summary: Light that emits from a single point in space.
  - name: ringLight
    summary: Light that emits from a torus or ring shape.
  - name: softShadow
    summary: A soft-edged shadow.
    thumb: assets/images/reference/operators/light/softShadow_thumb.png
  - name: spotLight
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
