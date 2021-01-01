A geodesic polyhedron, optionally with a spike on each face.

Based on [Geodesic domain manipulation](https://www.shadertoy.com/view/4tG3zW) by tdhooper.

## Parameters

* `Enable`
* `Shape`: The type of polyhedron.
  * `icosahedron`
  * `dodecahedron`
* `Divisions`: Number of divisions of the faces. Increasing this will result in more sides on the shape.
* `Enablefaces`: Whether to include the flat surfaces on each face.
* `Faceoffset`: Distance of the faces from the center point.
* `Enablespikes`: Whether to include a spike on each face.
* `Spikelength`: The length of the spikes.
* `Spikeoffset`: The distance from the center point of the base of each spike.
* `Spikeradius`: The base radius of each spike.

## Inputs

* `definition_in_1`:  Optional SDF that is placed at the tip of each spike.