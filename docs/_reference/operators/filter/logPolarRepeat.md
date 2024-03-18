---
layout: operator
title: logPolarRepeat
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/logPolarRepeat
redirect_from:
  - /reference/opType/raytk.operators.filter.logPolarRepeat/
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - rhoOffsetField
    - thetaOffsetField
    supportedVariables:
    - RTK_raytk_operators_filter_logPolarRepeat_cellcoord
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
    label: Rho Offset Field
    name: rhoOffsetField
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
    label: Theta Offset Field
    name: thetaOffsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - rhoOffsetField
  keywords:
  - log
  - modulo
  - polar
  - radial
  - repeat
  - spiral
  name: logPolarRepeat
  opType: raytk.operators.filter.logPolarRepeat
  parameters:
  - label: Enable
    name: Enable
  - label: Mode
    menuOptions:
    - label: Log Polar
      name: logpolar
    name: Mode
  - label: Axis
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Rho Offset
    name: Rhooffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Theta Offset
    name: Thetaoffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radial Repetitions
    name: Radialreps
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Distance Spacing
    name: Distspacing
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    - label: Grid
      name: grid
    name: Mirrortype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Iteration Type
    menuOptions:
    - label: None
      name: none
    - label: Cell Coordinates
      name: cellcoord
    - label: Alternating Cell Coordinates On Axes (0-1, 0-1)
      name: alternatingcoord
    - label: Cell Coordinate for Distance and Ratio for Radial
      name: cellcoordandratio
    name: Iterationtype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  status: beta
  thumb: assets/images/reference/operators/filter/logPolarRepeat_thumb.png
  variables:
  - label: RTK_raytk_operators_filter_logPolarRepeat_cellcoord
    name: RTK_raytk_operators_filter_logPolarRepeat_cellcoord

---
