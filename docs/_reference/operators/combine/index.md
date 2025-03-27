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
  - name: arrange
    summary: Combines multiple SDFs, with a different position for each.
    thumb: assets/images/reference/operators/combine/arrange_thumb.png
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
    thumb: assets/images/reference/operators/combine/combine_thumb.png
  - name: combineFields
    summary: Combines float or vector fields using one of several mathematical operations.
  - name: composeSdf
    status: beta
    summary: Combine multiple SDFs using different combination modes into a single
      SDF.
  - name: compositeFields
    summary: Combines two vector fields using color compositing.
    thumb: assets/images/reference/operators/combine/compositeFields_thumb.png
  - name: edgeCombine
    summary: Combines two SDFs in ways that use the intersection areas.
    thumb: assets/images/reference/operators/combine/edgeCombine_thumb.png
  - name: iterationSwitch
    summary: Switches between inputs based on the iteration value provided by a downstream
      operator.
    thumb: assets/images/reference/operators/combine/iterationSwitch_thumb.png
  - name: layoutGrid
    summary: Slices space into a grid, and places each input in a separate cell.
    thumb: assets/images/reference/operators/combine/layoutGrid_thumb.png
  - name: mergeFields
    summary: Merges multiple vector fields, using different fields for each vector
      part.
  - name: mixColorFields
    status: beta
  - name: mixFields
  - name: shapedCombine
    summary: Combine two SDFs, using a 2D SDF to shape the blending region.
  - name: simpleDiff
    status: deprecated
    summary: Combines two SDFs using the difference operator.
    thumb: assets/images/reference/operators/combine/simpleDiff_thumb.png
  - name: simpleIntersect
    status: deprecated
    summary: Combines SDFs using the intersect operator.
    thumb: assets/images/reference/operators/combine/simpleIntersect_thumb.png
  - name: simpleUnion
    shortcuts:
    - su
    status: deprecated
    summary: Combines several SDFs using the union operator.
    thumb: assets/images/reference/operators/combine/simpleUnion_thumb.png
  - keywords:
    - blend
    name: switch
    summary: Switches or blends between several inputs, without the need to rebuild
      the shader, allowing for fast switching.
  - name: triPlanarCombine
    status: beta
    summary: Combines three 2D fields based on vectors like surface normals.
  - moduleName: raytkVolumes
    name: combineVolumes
    status: beta
  summary: 'Operators that take two or more inputs and combine them into a single

    output.'

---

# Combine Operators

Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.
