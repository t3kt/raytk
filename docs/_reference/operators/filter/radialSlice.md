---
layout: operator
title: radialSlice
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/radialSlice
redirect_from:
  - /reference/opType/raytk.operators.filter.radialSlice/
op:
  category: filter
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
    - vec3
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
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
    - vec3
    label: Center Angle Field
    name: centerField
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
    - vec2
    - vec3
    label: Angle Width Field
    name: widthField
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
    - vec2
    - vec3
    label: Start Angle Field
    name: startField
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
    - vec2
    - vec3
    label: End Angle Field
    name: endField
    returnTypes:
    - float
  name: radialSlice
  opType: raytk.operators.filter.radialSlice
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: constant
    regularHandling: runtime
    summary: The axis around which to take the slice.
  - label: Angle Mode
    menuOptions:
    - label: Center & Width
      name: width
    - label: Start & End
      name: sides
    name: Anglemode
  - label: Center Angle
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Angle Width
    name: Width
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Start Angle
    name: Start
    readOnlyHandling: macro
    regularHandling: runtime
  - label: End Angle
    name: End
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Invert
    name: Invert
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: constant
    regularHandling: runtime
    summary: Whether to smooth the transition on each side of the slice down to a
      size of zero.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The amount of smoothing distance.
  thumb: assets/images/reference/operators/filter/radialSlice_thumb.png

---
