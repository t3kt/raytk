---
layout: operator
title: linkedLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/linkedLight
redirect_from:
  - /reference/opType/raytk.operators.light.linkedLight/
op:
  category: light
  detail: 'This can be used to synchronize lighting between a `raymarchRender3d` and
    a traditional Render TOP.


    Not all light types are supported.'
  name: linkedLight
  opType: raytk.operators.light.linkedLight
  parameters:
  - label: Light
    name: Light
    summary: The Light COMP to match.
  - label: Create Light
    name: Createlight
    summary: Creates and attaches a new Light COMP.
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Light that is based on a standard Light COMP.

---


Light that is based on a standard Light COMP.

This can be used to synchronize lighting between a `raymarchRender3d` and a traditional Render TOP.

Not all light types are supported.