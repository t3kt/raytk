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
    summary: Value field used to add to the `Shift` value.
  name: timeShift
  opType: raytk.operators.time.timeShift
  parameters:
  - label: Enable
    name: Enable
  - label: Shift
    name: Shift
    summary: Fixed offset to apply to contextual time of upstream operators.
  - label: Interval Type
    menuOptions:
    - description: Shifts timeline time by seconds (also updates timeline frame).
      label: Seconds (Timeline)
      name: seconds
    - description: Shifts timeline time by frames (also updates timeline seconds).
      label: Frames (Timeline)
      name: frames
    - description: Shifts absolute time by seconds (also updates absolute seconds).
      label: Seconds (Absolute)
      name: absseconds
    - description: Shifts absolute time by frames (also updates absolute frame).
      label: Frames (Absolute)
      name: absframes
    name: Intervaltype
    summary: The unit and part of time to shift.
  summary: Shifts contextual time for upstream operators, either by a fixed amount
    or using a value field.

---


Shifts contextual time for upstream operators, either by a fixed amount or using a value field.