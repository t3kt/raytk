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
  - label: Sun Position
    name: Sunpos
  - label: Sun Level
    name: Sunlevel
  - label: Planet Radius
    name: Planetradius
  - label: Atmosphere Thickness
    name: Atmosthickness
  - label: Rayleigh Scattering Coefficient
    name: Rayleighcoeff
  - label: Rayleigh Scale Height
    name: Rayleighscale
  - label: Mie Scattering Coefficient
    name: Miecoeff
  - label: Mie Scale Height
    name: Miescale
  - label: Mie Preferred Scattering Direction
    name: Mieprefdir
  - label: Primary Steps
    name: Primarysteps
  - label: Secondary Steps
    name: Secondarysteps
  status: beta
  summary: Field that simulates a sun and sky.
  thumb: assets/images/reference/operators/field/atmosphereField_thumb.png

---


Field that simulates a sun and sky.

This is primarily intended for use with the "Background Field" feature in `raymarchRender3d`.

Example:

![glsl-atmosphere](https://raw.githubusercontent.com/wwwtyro/glsl-atmosphere/master/images/atmosphere.png)

Based on [glsl-atmosphere](https://github.com/wwwtyro/glsl-atmosphere/).