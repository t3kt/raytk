---
layout: operator
title: rimContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/rimContrib
redirect_from:
  - /reference/opType/raytk.operators.material.rimContrib/
op:
  category: material
  detail: 'This is similar to the Rim Light feature in a standard Phong MAT.


    Using rim shading can result in aliasing issues, since it''s essentially highlighting
    the areas that are most likely to have aliasing.'
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec2
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariables:
    - normangle
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - thicknessField
    supportedVariables:
    - normangle
  - contextTypes:
    - MaterialContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - thicknessField
    - blendingField
    supportedVariables:
    - normangle
  name: rimContrib
  opType: raytk.operators.material.rimContrib
  parameters:
  - label: Enable
    name: Enable
    summary: When off, this shading will produce values of 0, meaning no contribution
      to shading.
  - label: Level
    name: Level
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Brightness of the shading, which is used as a multiplier for the Color.
  - label: Use Color
    name: Usecolor
    summary: Whether to produce color or just a brightness value.
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Color of the shading.
  - label: Use Surface Color
    name: Usesurfacecolor
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether this shading should take into account the surface color attribute
      on the SDF (if present).
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to apply the shadow to the color/level produced by this element.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width of the highlight area on the sides.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of fading between highlighted and not highlighted areas.
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Shading that is applied to the edges of a surface relative to where it's
    viewed from.
  thumb: assets/images/reference/operators/material/rimContrib_thumb.png
  variables:
  - label: Normalized Surface Angle (0..1)
    name: normangle

---


Shading that is applied to the edges of a surface relative to where it's viewed from.

This is similar to the Rim Light feature in a standard Phong MAT.

Using rim shading can result in aliasing issues, since it's essentially highlighting the areas that are most likely to have aliasing.