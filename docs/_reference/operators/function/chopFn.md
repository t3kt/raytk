---
layout: operator
title: chopFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/chopFn
redirect_from:
  - /reference/opType/raytk.operators.function.chopFn/
op:
  category: function
  name: chopFn
  opType: raytk.operators.function.chopFn
  parameters:
  - name: Contexttype
  - label: Chop
    name: Chop
    summary: The CHOP that values are pulled from.
  - label: Extend Mode
    menuOptions:
    - description: Extends the first/last value on each end.
      label: Hold
      name: hold
    - description: Produces a value of zero outside the range.
      label: Zero
      name: zero
    - description: Repeats the range.
      label: Repeat
      name: repeat
    - description: Repeats the range but flips every other part.
      label: Mirror
      name: mirror
    name: Extendmode
    readOnlyHandling: baked
    regularHandling: baked
    summary: How to handle coordinates outside the range.
  - label: Range
    name: Range
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The range of indices to map to the full range of the CHOP.
  summary: Function that looks up values in a CHOP.

---


Function that looks up values in a CHOP.