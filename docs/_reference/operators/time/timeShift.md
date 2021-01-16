---
layout: operator
title: timeShift
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/timeShift
redirect_from:
  - /reference/opType/raytk.operators.time.timeShift/
op:
  name: timeShift
  opType: raytk.operators.time.timeShift
  category: time
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
    - name: shift_definition_in
      label: shift_definition_in
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float]
  parameters:
    - name: Enable
      label: Enable
    - name: Shift
      label: Shift
    - name: Intervaltype
      label: Interval Type
      menuOptions:
        - name: seconds
          label: Seconds (Timeline)
        - name: frames
          label: Frames (Timeline)
        - name: absseconds
          label: Seconds (Absolute)
        - name: absframes
          label: Frames (Absolute)
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# timeShift

Category: time

