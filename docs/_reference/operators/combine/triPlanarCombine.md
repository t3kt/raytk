---
layout: operator
title: triPlanarCombine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/triPlanarCombine
redirect_from:
  - /reference/opType/raytk.operators.combine.triPlanarCombine/
op:
  category: combine
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
    label: UV Field
    name: uvField
    required: true
    returnTypes:
    - vec4
    summary: Alternative way to provide the coordinates used by the fields rather
      than just using the position in space. Each input field gets two of the axes
      of the coordinates provided (e.g. the XY field gets the x and y).
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
    label: Normals Field
    name: normalField
    required: true
    returnTypes:
    - vec4
    summary: Field that provides the surface normals used to adjust the influence
      of each plane. Typically this should be a `normalField` or a `variableReference`
      that accesses a surface normal within a material.
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
    - vec2
    label: XY Plane
    name: xyField
    returnTypes:
    - float
    - vec4
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
    - vec2
    label: YZ Plane
    name: yzField
    returnTypes:
    - float
    - vec4
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
    - vec2
    label: ZX Plane
    name: zxField
    returnTypes:
    - float
    - vec4
  name: triPlanarCombine
  opType: raytk.operators.combine.triPlanarCombine
  parameters:
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Use Normals
    name: Usenormals
    summary: Modifies the amount of each field that's used based on how directly the
      surface normals are facing that plane. For example, the XY field is used most
      on parts that are facing forwards or backwards.
  - label: Blend Mode
    menuOptions:
    - label: Add Axes
      name: add
    - label: Maximum Axes
      name: max
    - label: Average Axes
      name: avg
    name: Blendmode
    summary: How the values from each field are combined.
  - label: Return Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  status: beta
  summary: Combines three 2D fields based on vectors like surface normals.

---


Combines three 2D fields based on vectors like surface normals.