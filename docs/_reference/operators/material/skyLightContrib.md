---
layout: operator
title: skyLightContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/skyLightContrib
redirect_from:
  - /reference/opType/raytk.operators.material.skyLightContrib/
op:
  category: material
  detail: 'It applies lighting based on the direction that surfaces are facing.

    Unlike the main lighting system, it does not support shadows or other lighting
    behavior.

    It is a cheap way to add some secondary coloration to surfaces.


    It is equivalent to the sky lighting feature in `basicMat`.'
  name: skyLightContrib
  opType: raytk.operators.material.skyLightContrib
  parameters:
  - label: Color
    name: Color
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Level
    name: Level
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Direction
    name: Dir
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The direction from which the "light" comes from.
  - label: Use Color
    name: Usecolor
    summary: Whether to produce color or just a brightness value.
  summary: A material element that acts as a basic pseudo directional light.
  thumb: assets/images/reference/operators/material/skyLightContrib_thumb.png

---


A material element that acts as a basic pseudo directional light.

It applies lighting based on the direction that surfaces are facing.
Unlike the main lighting system, it does not support shadows or other lighting behavior.
It is a cheap way to add some secondary coloration to surfaces.

It is equivalent to the sky lighting feature in `basicMat`.