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
  name: spectralColorField
  opType: raytk.operators.field.spectralColorField
  parameters:
  - label: Wavelength
    name: Wavelength
  - label: Wavelength Unit
    menuOptions:
    - label: Normalized (0..1)
      name: norm
    - label: Nanometer (400..700)
      name: nm
    name: Wavelengthunit
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
  status: beta
  thumb: assets/images/reference/operators/field/spectralColorField_thumb.png

---
