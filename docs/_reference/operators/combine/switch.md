---
layout: operator
title: switch
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/switch
redirect_from:
  - /reference/opType/raytk.operators.combine.switch/
op:
  category: combine
  detail: Note that inputs that are not connected are skipped over when assigning
    numbers to them, so if inputs 1, 2, and 4 are connected, they will use indices
    0, 1, 2.
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
    label: Input 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 5
    name: definition_in_5
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 6
    name: definition_in_6
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 7
    name: definition_in_7
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Input 8
    name: definition_in_8
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
    label: Index Field
    name: indexField
    returnTypes:
    - float
    sourceParamLabel: Index Field
    sourceParamName: Indexfield
    summary: Field used to choose the source index
  keywords:
  - blend
  name: switch
  opType: raytk.operators.combine.switch
  parameters:
  - label: Enable
    name: Enable
  - label: Source
    name: Source
    readOnlyHandling: baked
    regularHandling: runtime
    summary: When 0, the first source is used, 1 for the second, etc.
  - label: Blend Between Inputs
    name: Blend
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Index Field
    name: Indexfield
  - label: Index Mode
    menuOptions:
    - label: Index (0 .. N-1)
      name: zeroindex
    - label: Index (1 .. N)
      name: oneindex
    - label: Normalized (0 .. 1)
      name: norm
    name: Indexmode
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Extend
    menuOptions:
    - label: Clamp
      name: clamp
    - label: Loop
      name: loop
    - label: Zig-Zag
      name: zigzag
    name: Extend
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Switches between several inputs, without the need to rebuild the shader,
    allowing for fast switching.

---


Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.

Note that inputs that are not connected are skipped over when assigning numbers to them, so if inputs 1, 2, and 4 are connected, they will use indices 0, 1, 2.