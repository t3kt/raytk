A material that is composed of one or more shading elements.

The shading contribution operators are intended to be used with this material,
including `diffuseContrib`, `specularContrib`, and `skyLightContrib`.
However any float or vector field operator can be used as a lighting element as long
as it's set up to use `MaterialContext`.

## Parameters

* `Enable`
* `Basecolor`
* `Uselightcolor`: Whether to apply the light color to the base color. This does not affect whether the shading elements use the light color.
* `Uselocalpos`
* `Enableao`

## Inputs

* `definition_in`: 
* `contrib_definition_in_1`:  First shading element.
* `contrib_definition_in_2`:  Second shading element.
* `contrib_definition_in_3`:  Third shading element.