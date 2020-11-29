---
layout: page
title: Light Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/light/
---

Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.

These operators are generally specialized for use in the raymarching `LightContext`
and may not support being fed through other OPs like filters.

* [`hardShadow`](hardShadow/) - A simple hard-edged shadow.
* [`pointLight`](pointLight/) - Light eminating from a single point in space, with optional distance attentuation.
* [`softShadow`](softShadow/) - A soft-edged shadow.
