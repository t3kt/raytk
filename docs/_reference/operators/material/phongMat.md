---
layout: page
title: phongMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/phongMat
redirect_from:
  - /reference/opType/raytk.operators.material.phongMat/
---

# phongMat

Category: material



Material that uses phong shading.

## Parameters

* `Enable` *Enable*
* `Ambientcolor` *Ambient Color*: Base color applied to the surface regardless of lights.
* `Diffusecolor` *Diffuse Color*: Color reflected by matte surfaces.
* `Specularcolor` *Specular Color*: Color reflected by glossy surfaces.
* `Shine` *Shine*: Specular exponent, which adjusts the light curve of specular highlights.
* `Enableshadow` *Enable Shadow*: Whether to use shadows. When enabled, if the *Shadow Definition* input is provided, that will be used. Otherwise a default shadow function will be used.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`:  **(Required)**
* `shadow_definition_in` *Shadow Definition*:  Used to customize the behavior of shadows for the material. Only used if `Enableshadow` is on.