---
layout: operator
title: sampledPointMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/sampledPointMat
redirect_from:
  - /reference/opType/raytk.operators.material.sampledPointMat/
op:
  category: material
  detail: This is intended for use with `pointMapRender`. It isn't useful for `raymarchRender3d`
    since that renderer only evaluates materials at points on the surface of the shape,
    and not inside/outside the shape.
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec2
    - vec3
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Fill Color Field
    name: fillColorField
    returnTypes:
    - float
    - vec4
    summary: Optional field used to control the color within the shape.
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Edge Color Field
    name: edgeColorField
    returnTypes:
    - float
    - vec4
    summary: Optional field used to control the color at the surface.
  name: sampledPointMat
  opType: raytk.operators.material.sampledPointMat
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Fill
    name: Enablefill
    summary: Whether to apply a color to points within the shape.
  - label: Fill Color
    name: Fillcolor
    summary: The color used within the shape.
  - label: Enable Edge
    name: Enableedge
    summary: Whether to apply a color to points that are at/near the surface of the
      shape.
  - label: Edge Color
    name: Edgecolor
    summary: The color applied to points at/near the surface.
  - label: Edge Thickness
    name: Edgethickness
    summary: The thickness of the area inside/outside the surface where the `Edge
      Color` is applied.
  - label: Blending
    name: Blending
    summary: The distance over which to blend between the inside color and the edge
      color.
  - label: Use Local Position
    name: Uselocalpos
    summary: Whether to use the "local" position relative to the input shape when
      looking up colors using the `Color Field` input. If enabled, the coordinates
      used for the color field will be "before" any downstream transformations are
      applied. When disabled, the final global position where a point ends up in the
      render is used instead.
  - label: Use Surface Color
    name: Usesurfacecolor
  - label: Offset
    name: Offset
  status: beta
  summary: A material that produces color for volumetric points relative to the input
    shape.
  variables:
  - label: surfacecolor
    name: surfacecolor
  - label: surfaceuv
    name: surfaceuv
  - label: normal
    name: normal
  - label: sdf
    name: sdf

---


A material that produces color for volumetric points relative to the input shape.

This is intended for use with `pointMapRender`. It isn't useful for `raymarchRender3d` since that renderer only evaluates materials at points on the surface of the shape, and not inside/outside the shape.