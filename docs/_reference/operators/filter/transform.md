---
layout: page
title: transform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/transform
---

# transform

Category: filter



Transform the coordinates of the input, with rotation, scaling, and translation.

Various parts of the transform can be switched off to improve performance, and the sequence of transform steps can be reordered.
It either uses the origin (0,0,0) as the pivot point, or can use another pivot point.

## Parameters

* `Enable` *Enable*
* `Enabletranslate` *Enable Translate*
* `Enablerotate` *Enable Rotate*
* `Enablescale` *Enable Scale*
* `Enablepivot` *Enable Pivot*
* `Translate` *Translate*
* `Rotate` *Rotate*
* `Scale` *Scale*
* `Pivot` *Pivot*
* `Transformorder` *Transform Order*
  * `srt` *Scale Rotate Translate*
  * `str` *Scale Translate Rotate*
  * `rst` *Rotate Scale Translate*
  * `rts` *Rotate Translate Scale*
  * `tsr` *Translate Scale Rotate*
  * `trs` *Translate Rotate Scale*
* `Rotateorder` *Rotate Order*
  * `xyz` *Rx Ry Rz*
  * `xzy` *Rx Rz Ry*
  * `yxz` *Ry Rx Rz*
  * `yzx` *Ry Rz Rx*
  * `zxy` *Rz Rx Ry*
  * `zyx` *Rz Ry Rx*
* `Inspect` *Inspect*

## Inputs

* `definition_in`