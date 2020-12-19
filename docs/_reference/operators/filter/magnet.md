---
layout: page
title: magnet
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/magnet
redirect_from:
  - /reference/opType/raytk.operators.filter.magnet/
---

# magnet

Category: filter



Pulls or twists space within an area.

If the magnet definition input is connected, that operator is used to determine how much transformation to apply at each point in space.
If there is no magnet definition connected, the magnet is based around a center point with a radius, and a blending region.

## Parameters

* `Enable` *Enable*
* `Amount` *Amount*: How much effect to apply overall.
* `Center` *Center*: The center position of the magnet (used if the magnet definition is not connected).
* `Radius` *Radius*: The radius of the magnet area.
* `Fade` *Fade*: The width of the blending region between the magnet and the rest of space.
* `Scale` *Scale*: Scaling to be applied within the magnet area.
* `Rotate` *Rotate*: Rotation to be applied within the magnet area.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`
* `magnet_definition_in` *Magnet*: Magnet definition used to determine how much transformation to apply at each point. If this is an operator that produces an SDF or float value, that value is used to decide how far each point is from the magnet. If it returns a vec4, it is used to determine where the magnet center position is relative to each point.
* `easing_definition_in` *Easing*: Easing function used to control how the blending region is smoothed.