Applies one or more transform operators sequentially, to coordinates, field values, etc, with support for looping.

The first input is the primary input, which can either be an arbitrary operator which will get the transformed coordinates, or it can be a field whose values are transformed, or an SDF whose UV coordinates are transformed, etc.

The second and later inputs are the sequence of transforms that are applied to the primary.
The second input gets the coordinates/values to be transformed, and the vector that it produces gets passed into the next input, and so on.
The output of the last connected input is used as the final value/coordinates.

Many transform filters support a mode where they have no attached primary input, in which case they act as fields producing their coordinates as a vector.
But for transform filters that require a primary input, a `positionField` can be attached to do the same thing.

The looping feature allows this operator to behave like a custom-built version of `iteratedTransform`, repeating the sequence of transformations multiple times.

## Parameters

* `Enable`
* `Target`: What the transforms should be applied to.
  * `coords`: The transforms are applied to coordinates which then get passed to the primary input. This is equivalent to how common transform operators like `rotate` behave.
  * `sdfuv`: The primary input is first called with un-transformed coordinates to produce an SDF result, then the transform sequence is applied to the primary UV coordinates of that result.
  * `sdfuv2`: Similar to primary UVs but for the secondary UVs that are used in cases where two SDFs are blended.
  * `matuv`: The transforms are applied to the UVs included in the material context that gets passed into the primary input, which would typically be something like a `diffuseContrib`.
  * `value`: The primary input is first called with un-transformed coordinates to produce a vector. Then the transform sequence is applied to that vector, which then gets produced as an output.
* `Reverseorder`: Whether the transforms should be applied in reverse order, last to first.
* `Enableloop`: Whether the transforms sequence should be applied multiple times, similar to an `iteratedTransform`.
* `Iterations`: How many times to apply the transform sequence.

## Inputs

* `definition_in`: 
* `transform1`: 
* `transform2`: 
* `transform3`: 
* `transform4`: 
* `transform5`: 
* `transform6`: 

## Variables

* `step`: The current loop index, 0, 1, 2, etc.
* `normstep`: The current loop index, scaled to a 0..1 range.