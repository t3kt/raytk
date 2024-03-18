---
layout: operatorCategory
title: Combine Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/combine/
cat:
  detail: 'This includes operations that merge SDFs (union, diff, intersect), as

    well as more generic things like switches and cross-fade blending.'
  name: combine
  operators:
  - name: addFields
    status: deprecated
  - name: arrange
  - name: boundLimit
    status: beta
  - keywords:
    - combine
    - diff
    - intersect
    - union
    name: combine
    shortcuts:
    - cmb
  - name: combineFields
  - name: composeSdf
    status: beta
  - name: compositeFields
  - name: edgeCombine
  - name: iterationSwitch
  - name: layoutGrid
  - name: mergeFields
  - name: shapedCombine
  - name: simpleDiff
  - name: simpleIntersect
  - name: simpleUnion
    shortcuts:
    - su
  - keywords:
    - blend
    name: switch
  - name: triPlanarCombine
    status: beta
  summary: 'Operators that take two or more inputs and combine them into a single

    output.'

---

# Combine Operators

Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.
