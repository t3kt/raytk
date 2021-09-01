> Locally sourced free-range parameters!

# Field concepts

- Think back to the `twist` operator. It's basically a `rotate` operator (using single axis rotation), but it uses a different amount of rotation for different points along the axis.
- But with `twist`, you don't have much control over how the setting varies over space. It's always based on that axis.
- Field operators let you do something similar, but with much more control.
- Coming back to the "ROPs answer questions about points in space" concept, field operators can be used to answer questions like: At this point in space, how much rotation should be applied?
- In fact, the `rotate` operator has a second "Rotate Field" input which you can use to do just that! When combined with a field operator like `axisDistanceField`, you can reproduce the same behavior as `twist`!

# Ways fields are used

- The kind of question asked of field operators depends on what's using them. For `rotate`, the question is just "how much rotation?".
- But other operators use fields to answer different questions.
- For example, the `translate` operator asks "how much translation should be used in XYZ?"
- Remember the `smoothUnion`'s mysterious third input that we discussed earlier? It takes in a field that it uses to decide how much smoothing to apply at each point.
- There are lots of different operators that use fields in different ways. In a lot of cases, like `rotate`, `translate`, and `smoothUnion`, operators will have one or two "primary" inputs, and then some additional field inputs to control their behavior.
- There are two types of answers that fields operators can produce: float and vector.
    - Float fields produce a single number (a "floating point" value).
    - Vector fields produce a set of 4 values. Sometimes those are treated as RGBA, or as XYZW (where W is the mystical 4th spatial dimension.. or just another abstract number, depending on one's viewpoint).

# Visualizing fields

- The inspector provides tools for visualizing fields using either color or scaling of a grid of cubes.

TODO: haven't mentioned inspector yet, so maybe have a basic intro to it earlier on.

# Common fields

- The `positionField` just returns whatever position where it's checked. When used with 3D coordinates, produces a vector with X, Y, and Z, (and W set to 0). We'll discuss other types of coordinates in a later section. Or you can pick a single axis to return.
- The `pointDistance` returns a single float value that is the distance between where it's being checked and some other point that you set with its parameters.
- The `axisDistanceField` is like `pointDistance`, but it only pays attention to a single axis.
- The `waveField` uses the position along an axis but applies a repeating wave pattern along that axis.
    - For example, it can produce a sine wave that oscillates between -1 and 1 for points along that axis.
    - You can attach this to a `rotate` to make something like `twist` but with the rotation smoothly switching directions periodically.

# Adapting field values

- The values that are produced by a field aren't always in the range that you may want them to be. For example, using `axisDistanceField` to control a `rotate` will barely have any effect at all, since the rotation is in degrees. So the difference between the rotation at `0,-5,0` and `0,5,0` would only be 10 degrees.
- You can think of this similarly to working with CHOPs. Sometimes you need to rescale the values.
- The `rescaleField` operator will take in a field and rescale the values that come out of it to another range. It's like the "Range" parameters on the `Math CHOP`.
- You can also use the `combineFields` operator with "Multiply" mode and a `constantField` to multiply a field's values by some amount.
- The `floatToVector` lets you create a vector field out of one or more float fields. It's useful when you have something like `translate` that expects a vector field, and you want to pass in a value for Y but not for X or Z.
- There's also a `vectorToFloat` operator that takes a vector field and pulls one of the channels out of it so you can use it as a float field.

# Combining fields

Similar to combining SDFs, there are some operators that let you combine multiple fields.

- The `combineFields` operator can combine fields using operations like adding, subtraction, multiplication, averaging, etc. It can work with either float value fields or vector fields.
- The `compositeFields` operator provides a variety of different color composition operations similar to the `Composite TOP` or Photoshop blend modes.

Combiners like `switch` and `blend` also work with fields, though they do expect all the fields to have the same types (coordinates, float vs vector, etc).
