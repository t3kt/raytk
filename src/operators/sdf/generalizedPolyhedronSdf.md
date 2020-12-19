Generates one of several different types of polyhedra.

Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf) by Akleman and Chen.

## Parameters

* `Shape`: Chooses between several different predefined types of polyhedra, or `Custom`, which uses the `Begin` and `End` parameters to generate different shapes.
  * `custom`
  * `octahedron`
  * `dodecahedron`
  * `icosahedron`
  * `truncatedoctahedron`
  * `truncatedicosahedron`
* `Begin`: Only used when the `Custom` shape. It's a bit hard to describe, so it's best to just experiment with it and see how it behaves.
* `End`: Used along with `Begin`.
* `Translate`: Shifts the center of the shape.
* `Radius`: The size of the shape.
* `Useexponent`: Enables the use of the `Exponent`, which controls the sharpness of the edges. When this is switched off, the shape will have sharp edges.
* `Exponent`: Controls the sharpness or smoothness of the edges.
* `Inspect`