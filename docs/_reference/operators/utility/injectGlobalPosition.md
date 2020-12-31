---
layout: operator
title: injectGlobalPosition
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/injectGlobalPosition
redirect_from:
  - /reference/opType/raytk.operators.utility.injectGlobalPosition/
op:
  name: injectGlobalPosition
  summary: Calls its input using the untransformed global position.
  detail: |
    This can be used for fields that are passed to other ops that are using downstream transforms to have the field use the raw global position while being used on an op that is transformed.
  opType: raytk.operators.utility.injectGlobalPosition
  category: utility
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# injectGlobalPosition

Category: utility



Calls its input using the untransformed global position.

This can be used for fields that are passed to other ops that are using downstream transforms to have the field use the raw global position while being used on an op that is transformed.