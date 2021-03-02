Converts a solid SDF to a thin shell of the surface.

The shell is created centered on the surface, with half of the `Thickness` going toward the outside and the other half on the inside. This has the effect of increasing the size of the outside of the shape.

Without somehow slicing through the shell, using things like `knife` or `slice`, you generally won't be able to tell the difference between this and `round`, in that it will seem to just increase the size of the shape.

See https://www.shadertoy.com/view/MlcBDj

## Parameters

* `Enable`
* `Thickness`: Thickness of the shell, centered on the input surface.

## Inputs

* `definition_in`: 