---
layout: operator
title: paramFilter
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/paramFilter
redirect_from:
  - /reference/opType/raytk.operators.utility.paramFilter/
op:
  category: utility
  name: paramFilter
  opType: raytk.operators.utility.paramFilter
  parameters:
  - label: Enable
    name: Enable
  - label: Filter Type
    menuOptions:
    - label: Gaussian Filter
      name: gauss
    - label: Lag
      name: lag
    - label: One Euro Filter
      name: oneeuro
    name: Filtertype
  - label: Filter Width
    name: Filterwidth
  - label: Lag
    name: Filterlag
  - label: Overshoot
    name: Filterovershoot
  - label: Cutoff Frequency (Hz)
    name: Filtercutoff
  - label: Speed Coefficient
    name: Filterspeedcoeff
  - label: Slope Cutoff Frequency (Hz)
    name: Filterslopecutoff
  - label: Reset
    name: Filterreset
  - label: Reset
    name: Filterresetpulse
  - label: Host OP
    name: Hostop
  - label: Filtered Parameters
    name: Filterpars
  - label: Filter Custom Params
    name: Filtercustom
  - label: Filter Built-In Params
    name: Filterbuiltin
  status: beta

---
