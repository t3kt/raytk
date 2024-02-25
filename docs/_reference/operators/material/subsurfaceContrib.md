---
layout: operator
title: subsurfaceContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/subsurfaceContrib
redirect_from:
  - /reference/opType/raytk.operators.material.subsurfaceContrib/
op:
  category: material
  name: subsurfaceContrib
  opType: raytk.operators.material.subsurfaceContrib
  parameters:
  - label: Enable
    name: Enable
  - label: Level
    name: Level
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Density
    name: Density
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Exponent
    name: Exponent
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scatter
    name: Scatter
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Use Color
    name: Usecolor
    summary: Whether to produce color or just a brightness value.
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Samples
    name: Samples
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Max Steps
    name: Maxsteps
    readOnlyHandling: semibaked
    regularHandling: semibaked
  status: beta

---
