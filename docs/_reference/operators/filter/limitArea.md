---
layout: operator
title: limitArea
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/limitArea
redirect_from:
  - /reference/opType/raytk.operators.filter.limitArea/
op:
  category: filter
  detail: 'Within the specified bounds, the value from the first input field is used.


    Outside the bounds, if there''s a second input field, that is used instead. Otherwise
    the `Outside Value` parameter is used for those areas.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Inside
    name: inside
    required: true
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Outside
    name: outside
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Bound Volume
    name: boundVolume
    required: true
    returnTypes:
    - float
    - Sdf
  name: limitArea
  opType: raytk.operators.filter.limitArea
  parameters:
  - label: Enable
    name: Enable
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offsets the edge of the bound area, expanding/collapsing it. This is
      equivalent to inserting a `round` operator.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Range over which to fade from the main field to the outside field/param.
  - label: Outside Value
    name: Outsidevalue
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Value to use outside the bounds, if there is no second field input.
  status: beta
  summary: Use an SDF to limit the area where a field produces values.

---


Use an SDF to limit the area where a field produces values.

Within the specified bounds, the value from the first input field is used.

Outside the bounds, if there's a second input field, that is used instead. Otherwise the `Outside Value` parameter is used for those areas.