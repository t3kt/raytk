Combines two SDFs in ways that use the intersection areas.

## Parameters

* `Enable`
* `Combine`
  * `engrave`: Cuts an angled groove into the first SDF in places where the second SDF overlaps it.
  * `groove`: Cuts a squared groove into the first SDF in places where the second SDF overlaps it.
  * `tongue`: Raises a squared region from the first SDF in places where the second SDF overlaps it.
  * `pipe`: Creates a rounded pipe in the places where both SDFs overlap.
* `Swapinputs`
* `Radius`: Width of the edge overlap area.
* `Depth`: Depth of the groove / tongue.

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `radiusField`: 
* `depthField`: 