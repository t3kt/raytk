---
layout: operator
title: fieldVolume
parent: Volume Operators
grand_parent: Operators
permalink: /reference/operators/volume/fieldVolume
redirect_from:
  - /reference/opType/raytkVolumes.operators.volume.fieldVolume/
op:
  category: volume
  detail: Volumes must have a density, so the density input is required, but color
    is optional.
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
    - float
    - vec2
    - vec3
    - vec4
    label: Density Field
    name: density
    required: true
    returnTypes:
    - float
    summary: Float field that provides the density for the volume.
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
    - float
    - vec2
    - vec3
    - vec4
    label: Color Field
    name: color
    returnTypes:
    - float
    - vec4
    summary: Vector field that provides the color for the volume.
  moduleName: raytkVolumes
  name: fieldVolume
  opType: raytkVolumes.operators.volume.fieldVolume
  parameters:
  - label: Enable Color
    name: Enablecolor
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to assign a color, using either the parameter or the color field
      input.
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Creates a Volume based on a density field, and an optional color field.

---


Creates a Volume based on a density field, and an optional color field.

Volumes must have a density, so the density input is required, but color is optional.