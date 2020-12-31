---
layout: operator
title: translate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/translate
redirect_from:
  - /reference/opType/raytk.operators.filter.translate/
op:
  name: translate
  summary: Translates coordinates of the input ROP.
  detail: |
    Translate can be used in 2D or 3D.
    It can optionally use a vector field to apply variable amounts of translation based on coordinates.
    If a field is used, the field values are added to the Translate XYZ parameter.
  opType: raytk.operators.filter.translate
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: true
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf,Ray,Light]
    - name: translate_field_definition_in
      label: Translate Field
      required: false
      coordTypes: [vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4,Sdf]
      summary: |
        If provided, this field is used to control the amount of translation at each point in space. If the field returns a float (or SDF), the `Translate` parameter is *multiplied* by that value. If it returns a vec4, the parts are *added* to the `Translate` parameter parts.
  parameters:
    - name: Enable
      label: Enable
    - name: Translate
      label: Translate
      summary: |
        Amount of translation along each axis. For 2D, only X and Y are used.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# translate

Category: filter



Translates coordinates of the input ROP.

Translate can be used in 2D or 3D.
It can optionally use a vector field to apply variable amounts of translation based on coordinates.
If a field is used, the field values are added to the Translate XYZ parameter.