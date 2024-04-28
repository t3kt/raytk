Limits the brightness of a light using distance attenuation or a bounding SDF (or both).

Attenuation makes the light full brightness at the position of the light and after a distance it tapers off to darkness.

Bounding SDFs do something similar but instead of using distance from the light source, they use an SDF that defines an area within which the light is at full brightness.

The optimization feature tells the renderer that in places where attentuation / bounding says the light should be totally off, the renderer can skip attempting to use that light at all for any materials there.

## Parameters

* `Enable`
* `Enableattenuation`: Whether to use distance from the light source to dim the light.
* `Attenuationdistance`: Range within which the light is at full brightness.
* `Attenuationfade`: Width of the transition from light to dark for distance attenuation. This fading is centered on the range from the distance parameter, so half the fade will be inside that range and half will be extending beyond that range.
* `Enablebounds`: Whether to use an SDF to dim the light outside an area.
* `Boundsoffset`: Expands or shrinks the bounding area from the SDF, equivalent to inserting a `round` operator between the SDF and the `limitLight`.
* `Boundsblending`: Width of the transition from light to dark from the bounding SDF.
* `Optimizeoutside`: Whether to tell the renderer it can skip material calculations for the light in areas outside the attenuation / bounding SDF.

## Inputs

* `light`: Light whose brightness is to be limited.
* `bounds`: SDF that defines an area for the light to be at full brightness.