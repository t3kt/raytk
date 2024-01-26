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
    supportedVariableInputs:
    - inputOp1
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
    supportedVariableInputs:
    - inputOp1
    - centerField
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
    supportedVariableInputs:
    - inputOp1
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
    supportedVariableInputs:
    - inputOp1
    - startField
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
  - label: Angle Width
    name: Width
  - label: Start Angle
    name: Start
  - label: End Angle
    name: End
  - label: Invert
    name: Invert
  - label: Enable Smoothing
    name: Enablesmoothing
    summary: Whether to smooth the transition on each side of the slice down to a
      size of zero.
  - label: Smooth Radius
    name: Smoothradius
    summary: The amount of smoothing distance.
  thumb: assets/images/reference/operators/filter/radialSlice_thumb.png

---
