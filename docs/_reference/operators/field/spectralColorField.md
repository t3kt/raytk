---
layout: operator
title: spectralColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/spectralColorField
redirect_from:
  - /reference/opType/raytk.operators.field.spectralColorField/
op:
  category: field
  detail: 'There are several spectrum types to choose from which balance the colors
    in different ways.


    The field will produce a color based on either the Wavelength parameter, or values
    from the wavelength input field.'
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
    label: Wavelength Field
    name: wavelengthField
    returnTypes:
    - float
    summary: Field that provides the wavelengths that the colors are based on.
  name: spectralColorField
  opType: raytk.operators.field.spectralColorField
  parameters:
  - label: Wavelength
    name: Wavelength
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Constant value to use as the wavelength to map to a color. This is only
      used when there is no wavelength input field.
  - label: Wavelength Unit
    menuOptions:
    - description: Normalized to a 0..1 range.
      label: Normalized (0..1)
      name: norm
    - description: Nanometers.
      label: Nanometer (400..700)
      name: nm
    name: Wavelengthunit
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How wavelength values should be interpreted.
  - label: Spectrum Type
    menuOptions:
    - label: Zucconi
      name: zucconi
    - label: Zucconi 6
      name: zucconi6
    - label: MATLAB Jet Color Scheme
      name: jet
    - label: GPU Gems
      name: gems
    - label: Bruton
      name: bruton
    - label: Spektre
      name: spektre
    name: Spectrumtype
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Produces colors using rainbow spectrum patterns.
  thumb: assets/images/reference/operators/field/spectralColorField_thumb.png

---


Produces colors using rainbow spectrum patterns.

There are several spectrum types to choose from which balance the colors in different ways.

The field will produce a color based on either the Wavelength parameter, or values from the wavelength input field.