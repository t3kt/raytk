---
layout: operator
title: instanceLight
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/instanceLight
redirect_from:
  - /reference/opType/raytk.operators.light.instanceLight/
op:
  category: light
  inputs:
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light
    required: true
    returnTypes:
    - Light
  name: instanceLight
  opType: raytk.operators.light.instanceLight
  parameters:
  - label: Enable
    name: Enable
  - label: Instance Count
    name: Instancecount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The number of copies to produce and merge.
  - label: Enable Transform CHOP
    name: Enabletransformchop
  - label: Transform CHOP
    name: Transformchop
    summary: A CHOP containing channels `tx ty tz` and/or `rx ry rz` that specifies
      the translate and/or rotate for each instance.
  - label: Enable Translate
    name: Enabletranslate
  - label: Enable Rotate
    name: Enablerotate
  - label: Enable Active CHOP
    name: Enableactivechop
  - label: Active CHOP
    name: Activechop
    summary: A CHOP containing a channel named `active`, which is used to selectively
      turn instances off. Any instance with an active value of 0 or less will be excluded
      from the combined result.
  variables:
  - label: Index
    name: index
  - label: Normalized Index (0..1)
    name: normindex

---
