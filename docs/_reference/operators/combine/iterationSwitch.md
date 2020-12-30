---
layout: operator
title: iterationSwitch
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/iterationSwitch
redirect_from:
  - /reference/opType/raytk.operators.combine.iterationSwitch/
op:
  name: iterationSwitch
  opType: raytk.operators.combine.iterationSwitch
  category: combine
  inputs:
    - name: definition_in_1
      label: definition_in_1
      required: true
    - name: definition_in_2
      label: definition_in_2
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Scaling
      label: Scaling
      menuOptions:
        - name: raw
          label: Raw
        - name: scaled
          label: Scaled to Total Iterations
    - name: Extend
      label: Extend
      menuOptions:
        - name: clamp
          label: Clamp
        - name: loop
          label: Loop
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# iterationSwitch

Category: combine

