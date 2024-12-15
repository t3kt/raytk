---
layout: operator
title: sdfVolume
parent: Volume Operators
grand_parent: Operators
permalink: /reference/operators/volume/sdfVolume
redirect_from:
  - /reference/opType/raytkVolumes.operators.volume.sdfVolume/
op:
  category: volume
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF
    name: sdf
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Density Field
    name: density
    returnTypes:
    - float
    supportedVariableInputs:
    - sdf
    supportedVariables:
    - sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Offset Field
    name: offset
    returnTypes:
    - float
    supportedVariableInputs:
    - sdf
    - densityField
    supportedVariables:
    - sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Blending Field
    name: blending
    returnTypes:
    - float
    supportedVariableInputs:
    - sdf
    - densityField
    - offsetField
    supportedVariables:
    - sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Thickness Field
    name: thickness
    returnTypes:
    - float
    supportedVariableInputs:
    - sdf
    - densityField
    - offsetField
    - blendingField
    supportedVariables:
    - sdf
  moduleName: raytkVolumes
  name: sdfVolume
  opType: raytkVolumes.operators.volume.sdfVolume
  parameters:
  - label: Use SDF Density
    name: Usesdfdensity
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Use the density attribute of the SDF if it has one. When enabled, the
      area of the SDF is ignored.
  - label: Density
    name: Density
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Density value used to fill the SDF area.
  - label: Fill Mode
    menuOptions:
    - description: Fills the inside of the SDF.
      label: Inside
      name: inside
    - description: Fills the outside of the SDF (basically inverting it).
      label: Outside
      name: outside
    - description: Doesn't adjust the density at all, just uses the value everywhere.
      label: Everywhere
      name: everywhere
    - description: Fills a hollow shell of the SDF, with blending on the inside and
        outside.
      label: Surface
      name: surface
    - description: ': Fills a hollow shell of the SDF, with blending only on the inside
        and a hard edge on the outside.'
      label: Surface Interior Blend Only
      name: surfaceinside
    - description: Fills a hollow shell of the SDF, with blending only on the outside
        and hard edge on the inside.
      label: Surface Exterior Blend Only
      name: surfaceoutside
    name: Fillmode
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How the density value (or field input) should fill the area of the SDF.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Surface offset (equivalent to inserting a round operator).
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the hollow shell.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of blending between the filled and non-filled areas.
  - label: Color Source
    menuOptions:
    - description: Doesn't assign a color.
      label: No Color
      name: none
    - description: Assigns a color taken from the SDF, optionally applying density
        to it.
      label: Color From SDF
      name: sdf
    - description: Uses the color parameter, optionally applying density to it.
      label: Color From Parameter
      name: param
    name: Colorsource
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Where to get the color to assign to the volume.
  - label: Color
    name: Color
    summary: Constant color for the volume.
  - label: Apply Density To Color
    name: Applydensitytocolor
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to multiply the color by the density, which causes it to be darker
      in areas with lower density.
  status: beta
  summary: Creates a Volume with density based on an SDF.
  variables:
  - label: SDF
    name: sdf

---


Creates a Volume with density based on an SDF.