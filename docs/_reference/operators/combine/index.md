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
  - name: blend
    summary: Smoothly blends/morphs between up to 4 SDFs.
  - name: combine
    summary: Combines SDFs in various ways.
  - name: combineChamfer
    summary: Chamfer SDF combine, producing a flat surface at a 45 degree angle along
      the blend region.
  - name: combineColumns
    summary: Columns SDF combine, producing n-1 circular columns/ridges at a 45 degree
      angles along the blend region.
  - name: combineFields
    summary: Combines float or vector fields using one of several mathematical operations.
  - name: combineStairs
    summary: Stair SDF combine, producing steps along the blend region.
  - name: compositeFields
    summary: Combines two vector fields using color compositing.
  - name: edgeEngrave
    summary: Carves a v-shaped groove where the second input intersects with the first.
  - name: edgeGroove
    summary: Creates a raised bar or indented groove where the second input intersects
      with the first.
  - name: edgePipe
    summary: Produces a cylindrical pipe along the blend region, replacing the input
      shapes entirely.
  - name: iterationSwitch
    summary: Switches between inputs based on the iteration value provided by a downstream
      operator.
  - name: layoutGrid
    summary: Slices space into a grid, and places each input in a separate cell.
  - name: mergeFields
    summary: Merges multiple vector fields, using different fields for each vector
      part.
  - name: shapedCombine
    summary: Combine two SDFs, using a 2D SDF to shape the blending region.
  - name: simpleDiff
    summary: Combines two SDFs using the difference operator.
  - name: simpleIntersect
    summary: Combines SDFs using the intersect operator.
  - name: simpleUnion
    summary: Combines several SDFs using the union operator.
  - name: smoothUnion
    summary: Combines SDFs using a smooth union operator.
  - name: switch
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
