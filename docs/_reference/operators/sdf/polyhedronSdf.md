---
layout: operator
title: polyhedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/polyhedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.polyhedronSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: UVW Field
    name: uvwField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - radiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Face Radius Field
    name: faceRadiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - uvwField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Segment Radius Field
    name: segmentRadiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - uvwField
    - faceRadiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Segment Size Field
    name: segmentSizeField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - uvwField
    - faceRadiusField
    - segmentRadiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Vertex Radius Field
    name: vertexRadiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - uvwField
    - faceRadiusField
    - segmentRadiusField
    - segmentSizeField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Vertex Size Field
    name: vertexSizeField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - uvwField
    - faceRadiusField
    - segmentRadiusField
    - segmentSizeField
    - vertexRadiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Vertex Shape
    name: vertexShape
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - radiusField
    - uvwField
    - faceRadiusField
    - segmentRadiusField
    - segmentSizeField
    - vertexRadiusField
    - vertexSizeField
  name: polyhedronSdf
  opType: raytk.operators.sdf.polyhedronSdf
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
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Faces
    name: Enablefaces
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Face Radius
    name: Faceradius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Segments
    name: Enablesegments
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Segment Radius
    name: Segmentradius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Segment Size
    name: Segmentsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Vertices
    name: Enablevertices
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Vertex Radius
    name: Vertexradius
    readOnlyHandling: baked
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
    name: Combine
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Blend Radius
    name: Blendradius
  - label: Blend Number
    name: Blendnumber
  - label: Blend Offset
    name: Blendoffset
  - label: UVW Field
    name: Uvwfield
  - label: Face Radius Field
    name: Faceradiusfield
  - label: Segment Radius Field
    name: Segmentradiusfield
  - label: Segment Size Field
    name: Segmentsizefield
  - label: Vertex Radius Field
    name: Vertexradiusfield
  - label: Vertex Size Field
    name: Vertexsizefield
  thumb: assets/images/reference/operators/sdf/polyhedronSdf_thumb.png

---
