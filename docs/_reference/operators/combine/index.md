---
layout: operatorCategory
title: Combine Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/combine/
cat:
  name: combine
  summary: |
    Operators that take two or more inputs and combine them into a single
    output.
  detail: |
    This includes operations that merge SDFs (union, diff, intersect), as
    well as more generic things like switches and cross-fade blending.
  operators:
    - op:
      name: blend
      summary: Smoothly blends/morphs between up to 4 SDFs.
    - op:
      name: combine
      summary: Combines SDFs in various ways.
    - op:
      name: combineChamfer
      summary: Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.
    - op:
      name: combineColumns
      summary: Columns SDF combine, producing n-1 circular columns/ridges at a 45 degree angles along the blend region.
    - op:
      name: combineFields
      summary: Combines float or vector fields using one of several mathematical operations.
    - op:
      name: combineStairs
      summary: Stair SDF combine, producing steps along the blend region.
    - op:
      name: edgeEngrave
      summary: Carves a v-shaped groove where the second input intersects with the first.
    - op:
      name: edgeGroove
      summary: Creates a raised bar or indented groove where the second input intersects with the first.
    - op:
      name: edgePipe
      summary: Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.
    - op:
      name: iterationSwitch
    - op:
      name: layoutGrid
      summary: Slices space into a grid, and places each input in a separate cell.
    - op:
      name: simpleDiff
      summary: Combines two SDFs using the difference operator.
    - op:
      name: simpleIntersect
      summary: Combines SDFs using the intersect operator.
    - op:
      name: simpleUnion
      summary: Combines several SDFs using the union operator.
    - op:
      name: smoothUnion
      summary: Combines SDFs using a smooth union operator.
    - op:
      name: switch
      summary: Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.

---

# Combine Operators

Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.
