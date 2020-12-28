---
layout: page
title: coneSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/coneSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.coneSdf/
---

# coneSdf

Category: sdf



Defines a cone or capped cone shape.

## Parameters

* `Enable` *Enable*
* `Shape` *Shape*: Choose between a regular cone and a capped cone without a tip.
  * `cone` *Cone*
  * `cappedcone` *Capped Cone*
* `Translate` *Translate*: Move the center of the shape.
* `Height` *Height*: The height of the cone.
* `Radius` *Radius*: The radius of the base of the cone.
* `Radius2` *Radius 2*: The radius of the top of the cone, if using a capped cone.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `height_field_definition_in` *Height Field*:  Value field that can be used to vary the height of the cone.
* `radius_field_definition_in` *Radius Field*:  Value field that can be used to vary the radius (both base and top) of the cone.