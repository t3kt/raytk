---
layout: operator
title: arcSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/arcSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.arcSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Orientation Field
    name: orientationField
    returnTypes:
    - float
    summary: Field used to offset the orientation angle, in degrees.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Aperture Field
    name: apertureField
    returnTypes:
    - float
    summary: Field used to override the aperture angle, in degrees.
    supportedVariableInputs:
    - orientationField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    summary: Field used to multiply the circle radius.
    supportedVariableInputs:
    - orientationField
    supportedVariables:
    - normangle
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    summary: Field used to multiply the thickness of the arc.
    supportedVariableInputs:
    - orientationField
    - radiusField
    supportedVariables:
    - normangle
  name: arcSdf2d
  opType: raytk.operators.sdf2d.arcSdf2d
  parameters:
  - label: Orientation
    name: Orientation
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Angle of the center of the arc in degrees.
  - label: Aperture
    name: Aperture
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Range of the arc in degrees.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Radius of the circle which the arc is taken from.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the arc.
  summary: Radial arc, a segment of a circular path, with rounded ends.
  thumb: assets/images/reference/operators/sdf2d/arcSdf2d_thumb.png
  variables:
  - label: Normalized Angle (0..1)
    name: normangle
    summary: Angle from one end of the arc to the other, normalized to a 0..1 range.

---


Radial arc, a segment of a circular path, with rounded ends.