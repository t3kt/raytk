---
layout: operator
title: timeShift
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/timeShift
redirect_from:
  - /reference/opType/raytk.operators.time.timeShift/
op:
  category: time
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: shift_definition_in
    name: shift_definition_in
    returnTypes:
    - float
  name: timeShift
  opType: raytk.operators.time.timeShift
  parameters:
  - label: Enable
    name: Enable
  - label: Shift
    name: Shift
  - label: Interval Type
    menuOptions:
    - label: Seconds (Timeline)
      name: seconds
    - label: Frames (Timeline)
      name: frames
    - label: Seconds (Absolute)
      name: absseconds
    - label: Frames (Absolute)
      name: absframes
    name: Intervaltype

---

# timeShift

Category: time

