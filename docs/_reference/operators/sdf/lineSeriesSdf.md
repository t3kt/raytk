---
layout: operator
title: lineSeriesSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/lineSeriesSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.lineSeriesSdf/
op:
  category: sdf
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
    - vec3
    label: Point A Field
    name: pointAField
    returnTypes:
    - vec4
    supportedVariables:
    - RTK_raytk_operators_sdf_lineSeriesSdf_stepindex
    - RTK_raytk_operators_sdf_lineSeriesSdf_normstepindex
    - RTK_raytk_operators_sdf_lineSeriesSdf_normoffset
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
    - vec3
    label: Point B Field
    name: pointBField
    returnTypes:
    - vec4
    supportedVariables:
    - RTK_raytk_operators_sdf_lineSeriesSdf_stepindex
    - RTK_raytk_operators_sdf_lineSeriesSdf_normstepindex
    - RTK_raytk_operators_sdf_lineSeriesSdf_normoffset
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariables:
    - RTK_raytk_operators_sdf_lineSeriesSdf_stepindex
    - RTK_raytk_operators_sdf_lineSeriesSdf_normstepindex
    - RTK_raytk_operators_sdf_lineSeriesSdf_normoffset
  name: lineSeriesSdf
  opType: raytk.operators.sdf.lineSeriesSdf
  parameters:
  - label: Source
    menuOptions:
    - label: Parameters
      name: params
    - label: CHOPs
      name: chops
    - label: Fields
      name: fields
    name: Source
    readOnlyHandling: baked
    regularHandling: baked
  - label: Count
    name: Count
    readOnlyHandling: baked
    regularHandling: baked
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A CHOP
    name: Pointachop
  - label: Point B CHOP
    name: Pointbchop
  - label: Point A 1
    name: Pointa1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 1
    name: Pointb1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 2
    name: Pointa2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 2
    name: Pointb2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 3
    name: Pointa3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 3
    name: Pointb3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 4
    name: Pointa4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 4
    name: Pointb4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 5
    name: Pointa5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 5
    name: Pointb5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 6
    name: Pointa6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 6
    name: Pointb6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 7
    name: Pointa7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 7
    name: Pointb7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point A 8
    name: Pointa8
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point B 8
    name: Pointb8
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/lineSeriesSdf_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf_lineSeriesSdf_stepindex
    name: RTK_raytk_operators_sdf_lineSeriesSdf_stepindex
  - label: RTK_raytk_operators_sdf_lineSeriesSdf_normstepindex
    name: RTK_raytk_operators_sdf_lineSeriesSdf_normstepindex
  - label: RTK_raytk_operators_sdf_lineSeriesSdf_normoffset
    name: RTK_raytk_operators_sdf_lineSeriesSdf_normoffset

---
