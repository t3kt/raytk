A material that is composed of one or more shading elements.

The shading contribution operators are intended to be used with this material,
including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.
However any float or vector field operator can be used as a lighting element as long
as it's set up to use `MaterialContext`.

## Parameters

* `Enable`
* `Basecolor`
* `Uselightcolor`
* `Uselocalpos`
* `Enableao`
* `Enableshadow`

## Inputs

* `definition_in`: 
* `shadow_definition_in`: Shadow function.
* `contrib_definition_in_1`: First shading element.
* `contrib_definition_in_2`: Second shading element.