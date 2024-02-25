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
    readOnlyHandling: semibaked
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
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Angle Width
    name: Width
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Start Angle
    name: Start
    readOnlyHandling: baked
    regularHandling: runtime
  - label: End Angle
    name: End
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Invert
    name: Invert
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Smoothing
    name: Enablesmoothing
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to smooth the transition on each side of the slice down to a
      size of zero.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The amount of smoothing distance.
  thumb: assets/images/reference/operators/filter/radialSlice_thumb.png

---
