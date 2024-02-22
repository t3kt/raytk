---
layout: operator
title: timeField
parent: Time Operators
grand_parent: Operators
permalink: /reference/operators/time/timeField
redirect_from:
  - /reference/opType/raytk.operators.time.timeField/
op:
  category: time
  detail: 'This field ignores the provided coordinates and instead returns one of
    several different types of time-based values.


    For timeline based values, output operators have a parameter that can specify
    the time reference operator. Otherwise it uses the timeline scoped to the COMP
    containing the scene.'
  name: timeField
  opType: raytk.operators.time.timeField
  parameters:
  - label: Part
    menuOptions:
    - description: Timeline seconds.
      label: Seconds
      name: seconds
    - description: Timeline frame index.
      label: Frame
      name: frame
    - description: The start frame of the timeline.
      label: Start Frame
      name: start
    - description: The end index of the timeline.
      label: End Frame
      name: end
    - description: The fraction of the current frame within the timeline range.
      label: Fraction
      name: fraction
    - description: The timeline frame rate (which isn't necessarily the actual frame
        rate).
      label: Frame Rate
      name: rate
    - description: The timeline BPM.
      label: BPM
      name: bpm
    - description: Absolute frame counting from when TouchDesigner started.
      label: Absolute Frame
      name: absFrame
    - description: Absolute seconds counting from when TouchDesigner started.
      label: Absolute Seconds
      name: absSeconds
    - description: The number of absolute frames elapsed between the previous and
        current frame.
      label: Absolute Step Frames
      name: absStepFrames
    - description: The number of absolute seconds elapsed between the previous and
        current frame.
      label: Absolute Step Seconds
      name: absStepSeconds
    name: Part
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Which type of time value to produce.
  - label: Time Source
    menuOptions:
    - description: Global time is always the same throughout the whole shader scene
        graph.
      label: Global
      name: global
    - description: Context time can be modified by downstream operators.
      label: Context
      name: context
    name: Timesource
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Where to pull the time values from.
  summary: Field that produces time-based values, equivalent to a `timeline CHOP`.

---


Field that produces time-based values, equivalent to a `timeline CHOP`.

This field ignores the provided coordinates and instead returns one of several different types of time-based values.

For timeline based values, output operators have a parameter that can specify the time reference operator. Otherwise it uses the timeline scoped to the COMP containing the scene.