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
    summary: Adds the values of multiple fields.
  - name: arrange
    summary: Combines multiple SDFs, with a different position for each.
  - name: blend
    status: deprecated
    summary: Smoothly blends/morphs between up to 4 SDFs.
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
    summary: Combines SDFs in various ways.
  - name: combineFields
    summary: Combines float or vector fields using one of several mathematical operations.
  - name: composeSdf
    status: beta
    summary: Combine multiple SDFs using different combination modes into a single
      SDF.
  - name: compositeFields
    summary: Combines two vector fields using color compositing.
  - name: edgeCombine
    summary: Combines two SDFs in ways that use the intersection areas.
  - name: iterationSwitch
    summary: Switches between inputs based on the iteration value provided by a downstream
      operator.
  - name: layoutGrid
    summary: Slices space into a grid, and places each input in a separate cell.
  - name: mergeFields
    summary: Merges multiple vector fields, using different fields for each vector
      part.
  - name: shapedCombine
    status: beta
    summary: Combine two SDFs, using a 2D SDF to shape the blending region.
  - name: simpleDiff
    summary: Combines two SDFs using the difference operator.
  - name: simpleIntersect
    summary: Combines SDFs using the intersect operator.
  - name: simpleUnion
    shortcuts:
    - su
    summary: Combines several SDFs using the union operator.
  - keywords:
    - blend
    name: switch
    summary: Switches between several inputs, without the need to rebuild the shader,
      allowing for fast switching.
  summary: 'Operators that take two or more inputs and combine them into a single

    output.'

---

# Combine Operators

Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.
