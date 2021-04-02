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
  - label: Return Type
    menuOptions:
    - label: Level Only
      name: float
    - label: Color
      name: vec4
    name: Returntype
    summary: Whether the lighting should have coloration or just a brightness level.
  - label: Color
    name: Color
  - label: Level
    name: Level
  - label: Direction
    name: Dir
    summary: The direction from which the "light" comes from.
  status: beta
  summary: A material element that acts as a basic pseudo directional light.

---


A material element that acts as a basic pseudo directional light.

It applies lighting based on the direction that surfaces are facing.
Unlike the main lighting system, it does not support shadows or other lighting behavior.
It is a cheap way to add some secondary coloration to surfaces.

It is equivalent to the sky lighting feature in `basicMat`.