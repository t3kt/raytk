---
layout: operator
title: mirrorAxes
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorAxes
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorAxes/
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
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    - vec4
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
    label: Direction Field
    name: directionField
    returnTypes:
    - float
    - vec4
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
    label: Flip Sides Field
    name: flipSideField
    returnTypes:
    - float
    - vec4
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
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    - vec4
  name: mirrorAxes
  opType: raytk.operators.filter.mirrorAxes
  parameters:
  - label: Enable
    name: Enable
  - label: Axes
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    - label: XYZ
      name: xyz
    name: Axes
  - label: Direction X
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Dirx
    readOnlyHandling: constant
    regularHandling: constant
  - label: Direction Y
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Diry
    readOnlyHandling: constant
    regularHandling: constant
  - label: Direction Z
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Dirz
    readOnlyHandling: constant
    regularHandling: constant
  - label: Flip X On Side
    menuOptions:
    - label: None
      name: none
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Flipsidex
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Flip Y On Side
    menuOptions:
    - label: None
      name: none
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Flipsidey
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Flip Z On Side
    menuOptions:
    - label: None
      name: none
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Flipsidez
    readOnlyHandling: constant
    regularHandling: runtime
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Enable Blend
    name: Enableblend
    readOnlyHandling: constant
    regularHandling: constant
  - label: Blending
    name: Blending
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
  thumb: assets/images/reference/operators/filter/mirrorAxes_thumb.png
  variables:
  - label: sides
    name: sides

---
