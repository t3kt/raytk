---
layout: operator
title: colorizeSdf2d
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/colorizeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.material.colorizeSdf2d/
op:
  category: material
  detail: 'This pattern is useful for debugging purposes.

    While this is not a regular "material", it is used to convert an SDF to a color
    output.'
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - float
    - Sdf
  name: colorizeSdf2d
  opType: raytk.operators.material.colorizeSdf2d
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Edge
    name: Enableedge
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to show a border at the suface of the shape.
  - label: Edge Thickness
    name: Edgethickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the shape border.
  - label: Edge Blending
    name: Edgeblending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of blending applied to each side of the shape border.
  - label: Edge Color
    name: Edgecolor
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The color for the shape border.
  - label: Inside Period
    name: Insideperiod
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The tightness of the stripes inside the shape.
  - label: Inside Color 1
    name: Insidecolor1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The first stripe color inside the shape.
  - label: Inside Color 2
    name: Insidecolor2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The second stripe color inside the shape.
  - label: Outside Period
    name: Outsideperiod
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The tightness fo the stripes outside the shape.
  - label: Outside Color 1
    name: Outsidecolor1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The first stripe color outside the shape.
  - label: Outside Color 2
    name: Outsidecolor2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The second stripe color outside the shape.
  - label: Inside Phase
    name: Insidephase
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Outside Phase
    name: Outsidephase
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Converts a 2D SDF to a striped distance pattern.

---


Converts a 2D SDF to a striped distance pattern.

This pattern is useful for debugging purposes.
While this is not a regular "material", it is used to convert an SDF to a color output.