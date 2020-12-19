---
layout: page
title: blend
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/blend
redirect_from:
  - /reference/opType/raytk.operators.combine.blend/
---

# blend

Category: combine



Smoothly blends/morphs between up to 4 SDFs.

The blend index only considers inputs that are connected, so if you connect the second and fourth inputs, it will treat the second as 0 and the fourth as 1.

## Parameters

* `Enable` *Enable*
* `Blend` *Blend*: Which input or combination of inputs to use. If this value is 0, the first connected input is used. 0.5 is half way between the first and second connected inputs, etc.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`
* `definition_in_2`
* `definition_in_3`
* `definition_in_4`