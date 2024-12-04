---
layout: operator
title: transformSequence
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/transformSequence
redirect_from:
  - /reference/opType/raytk.operators.filter.transformSequence/
op:
  category: filter
  detail: 'The first input is the primary input, which can either be an arbitrary
    operator which will get the transformed coordinates, or it can be a field whose
    values are transformed, or an SDF whose UV coordinates are transformed, etc.


    The second and later inputs are the sequence of transforms that are applied to
    the primary.

    The second input gets the coordinates/values to be transformed, and the vector
    that it produces gets passed into the next input, and so on.

    The output of the last connected input is used as the final value/coordinates.


    Many transform filters support a mode where they have no attached primary input,
    in which case they act as fields producing their coordinates as a vector.

    But for transform filters that require a primary input, a `positionField` can
    be attached to do the same thing.


    The looping feature allows this operator to behave like a custom-built version
    of `iteratedTransform`, repeating the sequence of transformations multiple times.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Primary Input
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - transform1
    - transform2
    - transform3
    - transform4
    - transform5
    - transform6
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 1
    name: transform1
    returnTypes:
    - vec4
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 2
    name: transform2
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform1
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 3
    name: transform3
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-2]
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 4
    name: transform4
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-3]
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 5
    name: transform5
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-4]
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Transform 6
    name: transform6
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-5]
    supportedVariables:
    - step
    - normstep
  keywords:
  - apply
  name: transformSequence
  opType: raytk.operators.filter.transformSequence
  parameters:
  - label: Enable
    name: Enable
  - label: Apply To
    menuOptions:
    - description: The transforms are applied to coordinates which then get passed
        to the primary input. This is equivalent to how common transform operators
        like `rotate` behave.
      label: Coordinates
      name: coords
    - description: The primary input is first called with un-transformed coordinates
        to produce an SDF result, then the transform sequence is applied to the primary
        UV coordinates of that result.
      label: SDF UV
      name: sdfuv
    - description: Similar to primary UVs but for the secondary UVs that are used
        in cases where two SDFs are blended.
      label: SDF Secondary UV
      name: sdfuv2
    - description: The transforms are applied to the UVs included in the material
        context that gets passed into the primary input, which would typically be
        something like a `diffuseContrib`.
      label: UV In Material
      name: matuv
    - description: The primary input is first called with un-transformed coordinates
        to produce a vector. Then the transform sequence is applied to that vector,
        which then gets produced as an output.
      label: Field Values
      name: value
    name: Target
    readOnlyHandling: baked
    regularHandling: baked
    summary: What the transforms should be applied to.
  - label: Reverse Order
    name: Reverseorder
    summary: Whether the transforms should be applied in reverse order, last to first.
  - label: Enable Loop
    name: Enableloop
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether the transforms sequence should be applied multiple times, similar
      to an `iteratedTransform`.
  - label: Iterations
    name: Iterations
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How many times to apply the transform sequence.
  status: beta
  summary: Applies one or more transform operators sequentially, to coordinates, field
    values, etc, with support for looping.
  variables:
  - label: Step Index
    name: step
    summary: The current loop index, 0, 1, 2, etc.
  - label: Normalized Step (0..1)
    name: normstep
    summary: The current loop index, scaled to a 0..1 range.

---


Applies one or more transform operators sequentially, to coordinates, field values, etc, with support for looping.

The first input is the primary input, which can either be an arbitrary operator which will get the transformed coordinates, or it can be a field whose values are transformed, or an SDF whose UV coordinates are transformed, etc.

The second and later inputs are the sequence of transforms that are applied to the primary.
The second input gets the coordinates/values to be transformed, and the vector that it produces gets passed into the next input, and so on.
The output of the last connected input is used as the final value/coordinates.

Many transform filters support a mode where they have no attached primary input, in which case they act as fields producing their coordinates as a vector.
But for transform filters that require a primary input, a `positionField` can be attached to do the same thing.

The looping feature allows this operator to behave like a custom-built version of `iteratedTransform`, repeating the sequence of transformations multiple times.