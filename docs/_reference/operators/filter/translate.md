---
layout: operator
title: translate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/translate
redirect_from:
  - /reference/opType/raytk.operators.filter.translate/
op:
  category: filter
  detail: 'Translate can be used in 2D or 3D.

    It can optionally use a vector field to apply variable amounts of translation
    based on coordinates.

    If a field is used, the field values are added to the Translate XYZ parameter.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: Translate Field
    name: translateField
    returnTypes:
    - vec4
    summary: If provided, this field is used to control the amount of translation
      at each point in space. If the field returns a float (or SDF), the `Translate`
      parameter is *multiplied* by that value. If it returns a vec4, the parts are
      *added* to the `Translate` parameter parts.
  keywords:
  - move
  - position
  - transform
  - translate
  name: translate
  opType: raytk.operators.filter.translate
  parameters:
  - label: Enable
    name: Enable
  - label: Translate
    name: Translate
    summary: Amount of translation along each axis. For 2D, only X and Y are used.
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
  shortcuts:
  - tr
  summary: Translates coordinates of the input ROP.

---


Translates coordinates of the input ROP.

Translate can be used in 2D or 3D.
It can optionally use a vector field to apply variable amounts of translation based on coordinates.
If a field is used, the field values are added to the Translate XYZ parameter.