---
layout: operator
title: matCapContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/matCapContrib
redirect_from:
  - /reference/opType/raytk.operators.material.matCapContrib/
op:
  category: material
  detail: 'MatCap images are available on [github](https://github.com/nidorx/matcaps).


    Note that this shading does not use actual lights or reflections, it''s a shortcut
    that fakes those things which are pre-computed and baked into the images that
    the shading is based on.


    This approach is commonly used in sculpting tools like zBrush.'
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Rotate Field
    name: rotateField
    returnTypes:
    - float
  name: matCapContrib
  opType: raytk.operators.material.matCapContrib
  parameters:
  - label: Enable
    name: Enable
  - label: Level
    name: Level
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Mat Cap Texture TOP
    name: Texturetop
  - label: Map Cap Texture File
    name: Texturefile
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
  status: beta
  summary: Shading using a MatCap (Material Capture) image to fake lighting and reflections.

---


Shading using a MatCap (Material Capture) image to fake lighting and reflections.

MatCap images are available on [github](https://github.com/nidorx/matcaps).

Note that this shading does not use actual lights or reflections, it's a shortcut that fakes those things which are pre-computed and baked into the images that the shading is based on.

This approach is commonly used in sculpting tools like zBrush.