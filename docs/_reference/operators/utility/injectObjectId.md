---
layout: operator
title: injectObjectId
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/injectObjectId
redirect_from:
  - /reference/opType/raytk.operators.utility.injectObjectId/
op:
  name: injectObjectId
  summary: Assigns an arbitrary value to the objectId field of an SDF, which can later be extracted from rendered output.
  detail: |
    This can be used to identify which object is shown at any given pixel in
    the output.
  opType: raytk.operators.utility.injectObjectId
  category: utility
  status: beta
  inputs:
    - name: definition_in
      label: definition_in
      required: true
  parameters:
    - name: Enable
      label: Enable
    - name: Objectid
      label: Object Id
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# injectObjectId

Category: utility



Assigns an arbitrary value to the objectId field of an SDF, which can later
be extracted from rendered output.

This can be used to identify which object is shown at any given pixel in
the output.