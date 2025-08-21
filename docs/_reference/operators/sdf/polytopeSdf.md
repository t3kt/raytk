---
layout: operator
title: polytopeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/polytopeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.polytopeSdf/
op:
  category: sdf
  detail: Based on (Regular 4D Polytopes by Syntopia)[https://www.shadertoy.com/view/XdfGW4]
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Segment Size Field
    name: segmentSizeField
    returnTypes:
    - float
    sourceParamLabel: Segment Size Field
    sourceParamName: Segmentsizefield
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Vertex Size Field
    name: vertexSizeField
    returnTypes:
    - float
    sourceParamLabel: Vertex Size Field
    sourceParamName: Vertexsizefield
  name: polytopeSdf
  opType: raytk.operators.sdf.polytopeSdf
  parameters:
  - label: Type
    name: Type
    readOnlyHandling: baked
    regularHandling: runtime
  - label: U
    name: U
    readOnlyHandling: baked
    regularHandling: runtime
  - label: V
    name: V
    readOnlyHandling: baked
    regularHandling: runtime
  - label: W
    name: W
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Segments
    name: Enablesegments
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Segment Size
    name: Segmentsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Vertices
    name: Enablevertices
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Vertex Size
    name: Vertexsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Combine
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
      name: simpleDiff
    - label: Smooth Union
      name: smoothUnion
    - label: Smooth Intersect
      name: smoothIntersect
    - label: Smooth Difference
      name: smoothDiff
    - label: Round Union
      name: roundUnion
    - label: Round Intersect
      name: roundIntersect
    - label: Round Difference
      name: roundDiff
    - label: Chamfer Union
      name: chamferUnion
    - label: Chamfer Intersect
      name: chamferIntersect
    - label: Chamfer Difference
      name: chamferDiff
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    - label: Simple XOR
      name: simpleXOR
    - label: Smooth Avoid
      name: smoothAvoid
    name: Combine
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Blend Radius
    name: Blendradius
  - label: Blend Number
    name: Blendnumber
  - label: Blend Offset
    name: Blendoffset
  - label: Segment Size Field
    name: Segmentsizefield
  - label: Vertex Size Field
    name: Vertexsizefield
  - label: Blend Gutter
    name: Blendgutter
  status: beta
  summary: 4D polytope SDF.
  thumb: assets/images/reference/operators/sdf/polytopeSdf_thumb.png

---


4D polytope SDF.

Based on (Regular 4D Polytopes by Syntopia)[https://www.shadertoy.com/view/XdfGW4]