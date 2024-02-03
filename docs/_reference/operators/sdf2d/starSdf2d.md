---
layout: operator
title: starSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/starSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.starSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - pointsField
    supportedVariables:
    - normangle
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
    label: Tightness Field
    name: tightnessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    supportedVariables:
    - normangle
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
    label: Points Field
    name: pointsField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - tightnessField
    supportedVariables:
    - normangle
  name: starSdf2d
  opType: raytk.operators.sdf2d.starSdf2d
  parameters:
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The distance from the center to each outer point on the star.
  - label: Points
    name: Points
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The number of points for the star. When this is a non-integer value there
      will be one point that is partially cut off at the bottom.
  - label: Tightness
    name: Tightness
    readOnlyHandling: macro
    regularHandling: runtime
    summary: How much the inner points of the start are pulled towards the center.
      At zero this will produce a polygon with two sides for each point. At one it
      will produce thin lines radiating from the center.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Cartesian
      name: cartesian
    - label: Polar
      name: polar
    name: Uvmode
    readOnlyHandling: constant
    regularHandling: constant
  summary: SDF for a 2D star shape.
  thumb: assets/images/reference/operators/sdf2d/starSdf2d_thumb.png
  variables:
  - label: normangle
    name: normangle

---


SDF for a 2D star shape.