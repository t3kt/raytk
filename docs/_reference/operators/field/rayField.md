---
layout: operator
title: rayField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/rayField
redirect_from:
  - /reference/opType/raytk.operators.field.rayField/
op:
  category: field
  detail: 'When used in a material context, the ray is the one that went from the
    camera to the surface.

    When used in a background field, the ray is the one that went from the camera
    and missed all surfaces.'
  name: rayField
  opType: raytk.operators.field.rayField
  parameters:
  - label: Ray Part
    menuOptions:
    - label: Direction
      name: dir
    - label: Position
      name: pos
    name: Raypart
    readOnlyHandling: constant
    regularHandling: constant
  - name: Contexttype
  summary: Field that provides the ray direction or origin.
  thumb: assets/images/reference/operators/field/rayField_thumb.png

---


Field that provides the ray direction or origin.

When used in a material context, the ray is the one that went from the camera to the surface.
When used in a background field, the ray is the one that went from the camera and missed all surfaces.