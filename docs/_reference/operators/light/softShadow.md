---
layout: operator
title: softShadow
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/softShadow
redirect_from:
  - /reference/opType/raytk.operators.light.softShadow/
op:
  category: light
  detail: This should be connected to the "Shadow" input of the `raymarchRender3d`
    operator.
  name: softShadow
  opType: raytk.operators.light.softShadow
  parameters:
  - label: Hardness
    name: Hardness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Override Minimum Distance
    name: Overridemindist
  - label: Minimum Dist
    name: Mindist
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Override Maximum Distance
    name: Overridemaxdist
  - label: Maximum Distance
    name: Maxdist
    readOnlyHandling: baked
    regularHandling: runtime
  summary: A soft-edged shadow.
  thumb: assets/images/reference/operators/light/softShadow_thumb.png

---


A soft-edged shadow.

This should be connected to the "Shadow" input of the `raymarchRender3d` operator.