---
layout: operator
title: limitLight
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/limitLight
redirect_from:
  - /reference/opType/raytk.operators.filter.limitLight/
op:
  category: filter
  detail: 'Attenuation makes the light full brightness at the position of the light
    and after a distance it tapers off to darkness.


    Bounding SDFs do something similar but instead of using distance from the light
    source, they use an SDF that defines an area within which the light is at full
    brightness.


    The optimization feature tells the renderer that in places where attentuation
    / bounding says the light should be totally off, the renderer can skip attempting
    to use that light at all for any materials there.'
  inputs:
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Light
    name: light
    required: true
    returnTypes:
    - Light
    summary: Light whose brightness is to be limited.
  - contextTypes:
    - LightContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bounds SDF
    name: bounds
    returnTypes:
    - Sdf
    summary: SDF that defines an area for the light to be at full brightness.
  name: limitLight
  opType: raytk.operators.filter.limitLight
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Attenuation
    name: Enableattenuation
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to use distance from the light source to dim the light.
  - label: Attenuation Distance
    name: Attenuationdistance
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Range within which the light is at full brightness.
  - label: Attenuation Fade
    name: Attenuationfade
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width of the transition from light to dark for distance attenuation.
      This fading is centered on the range from the distance parameter, so half the
      fade will be inside that range and half will be extending beyond that range.
  - label: Enable Bounds
    name: Enablebounds
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to use an SDF to dim the light outside an area.
  - label: Bounds Offset
    name: Boundsoffset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Expands or shrinks the bounding area from the SDF, equivalent to inserting
      a `round` operator between the SDF and the `limitLight`.
  - label: Bounds Blending
    name: Boundsblending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width of the transition from light to dark from the bounding SDF.
  - label: Optimize Outside
    name: Optimizeoutside
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to tell the renderer it can skip material calculations for the
      light in areas outside the attenuation / bounding SDF.
  status: beta
  summary: Limits the brightness of a light using distance attenuation or a bounding
    SDF (or both).

---


Limits the brightness of a light using distance attenuation or a bounding SDF (or both).

Attenuation makes the light full brightness at the position of the light and after a distance it tapers off to darkness.

Bounding SDFs do something similar but instead of using distance from the light source, they use an SDF that defines an area within which the light is at full brightness.

The optimization feature tells the renderer that in places where attentuation / bounding says the light should be totally off, the renderer can skip attempting to use that light at all for any materials there.