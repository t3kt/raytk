---
layout: operator
title: atmosphereField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/atmosphereField
redirect_from:
  - /reference/opType/raytk.operators.field.atmosphereField/
op:
  category: field
  detail: 'This is primarily intended for use with the "Background Field" feature
    in `raymarchRender3d`.


    Example:


    ![glsl-atmosphere](https://raw.githubusercontent.com/wwwtyro/glsl-atmosphere/master/images/atmosphere.png)


    Based on [glsl-atmosphere](https://github.com/wwwtyro/glsl-atmosphere/).'
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
    label: Ray Direction Field
    name: ray_direction_field_in
    returnTypes:
    - vec4
  name: atmosphereField
  opType: raytk.operators.field.atmosphereField
  parameters:
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Sun Position
    name: Sunpos
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Sun Level
    name: Sunlevel
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Planet Radius
    name: Planetradius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Atmosphere Thickness
    name: Atmosthickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rayleigh Scattering Coefficient
    name: Rayleighcoeff
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rayleigh Scale Height
    name: Rayleighscale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Mie Scattering Coefficient
    name: Miecoeff
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Mie Scale Height
    name: Miescale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Mie Preferred Scattering Direction
    name: Mieprefdir
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Primary Steps
    name: Primarysteps
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Secondary Steps
    name: Secondarysteps
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Field that simulates a sun and sky.
  thumb: assets/images/reference/operators/field/atmosphereField_thumb.png

---


Field that simulates a sun and sky.

This is primarily intended for use with the "Background Field" feature in `raymarchRender3d`.

Example:

![glsl-atmosphere](https://raw.githubusercontent.com/wwwtyro/glsl-atmosphere/master/images/atmosphere.png)

Based on [glsl-atmosphere](https://github.com/wwwtyro/glsl-atmosphere/).