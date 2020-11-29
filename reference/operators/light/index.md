---
layout: page
title: Light Operators
---

Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.

These operators are generally specialized for use in the raymarching `LightContext`
and may not support being fed through other OPs like filters.

* [`hardShadow`](hardShadow.md) - A simple hard-edged shadow.
* [`pointLight`](pointLight.md) - Light eminating from a single point in space, with optional distance attentuation.
* [`softShadow`](softShadow.md) - A soft-edged shadow.
