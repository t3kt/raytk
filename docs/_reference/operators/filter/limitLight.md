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
  name: limitLight
  opType: raytk.operators.filter.limitLight
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Attenuation
    name: Enableattenuation
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Attenuation Distance
    name: Attenuationdistance
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Attenuation Fade
    name: Attenuationfade
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Bounds
    name: Enablebounds
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds Offset
    name: Boundsoffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bounds Blending
    name: Boundsblending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Optimize Outside
    name: Optimizeoutside
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta

---
