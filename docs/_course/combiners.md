> Shapes, and how to have more than one of them.

# Combiner concepts

- So far, we've been working with a single SDF `ROP` at a time. Even in cases where transform filters cause it to appear in multiple locations, it's still just one SDF.
- The Combine operators take in two (or in some cases more) SDFs and combine them to form a new SDF. As far as anything downstream in the graph is concerned, it's just a single SDF, even though it's based on multiple input SDFs.

# Simple boolean operators

- The simplest example of this is `simpleUnion`, which works kind of like the `merge SOP`, in that the result includes both of the shapes fed into it. Another way to think about this is like the `boolean SOP` when using the "Union" setting, equivalent to a logical "OR". It produces all of the area that is either inside one shape, or is inside the other (or both). This operator supports up to 8 inputs. If you need to combine more than 8, you can chain them.
    - This is commonly used when you just have mulitple things in your scene that you want to appear together, without any special interactions between them.
- Similarly, the `simpleIntersect` behaves like the `boolean SOP` but with the "Intersect" mode, equivalent to a logical "AND". It produces only the areas where all the input shapes overlap. Similarly to `simpleUnion`, this operator supports up to 4 inputs.
- The `simpleDiff` is like the `boolean SOP` with the "A minus B" setting. It produces the area of the first input, with the second input's area subtracted from it. You can also use the "Swap Inputs" parameter to flip them to behave like "B minus A".
- With these three operators, you can work with what's known as "Constructive Solid Geometry" (or CSG). This technique uses shapes and boolean operators to construct new more complex shapes.

    [Constructive solid geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry)

![https://iquilezles.org/www/articles/distfunctions/gfx45.png](https://iquilezles.org/www/articles/distfunctions/gfx45.png)

[https://iquilezles.org/www/articles/distfunctions/distfunctions.htm](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm)

# Combiners with intersection blending

- The `smoothUnion` operator is similar to `simpleUnion` but instead of just combining both areas, it smoothes out the places where the surfaces intersect. The "Amount" parameter controls the size of the smoothing region.
    - This can be used to create "metaball"-style effects, where objects merge and melt into each other.
    - It's important to note that, while `smoothUnion` does have 3 inputs, the third one is treated differently. We'll discuss that in the "Fields" section later.
- The `combineStairs` operator is like `smoothUnion`, but instead of rounding out the places where the inputs intersect, it creates a stair pattern going from one surface to the other.
    - You can control the number of steps, and you can control the offset of the steps, which gives you a kind of escalator look where the steps move along from one shape to the other, but the blend area as a whole stays in the same place.
    - It also lets you choose what kind of boolean operator it uses (union, intersect, or difference).

    ![http://mercury.sexy/hg_sdf/bool_small/fOpUnionStairs.png](http://mercury.sexy/hg_sdf/bool_small/fOpUnionStairs.png)

    ![http://mercury.sexy/hg_sdf/bool_small/fOpIntersectionStairs.png](http://mercury.sexy/hg_sdf/bool_small/fOpIntersectionStairs.png)

    ![http://mercury.sexy/hg_sdf/bool_small/fOpDifferenceStairs.png](http://mercury.sexy/hg_sdf/bool_small/fOpDifferenceStairs.png)

- The `combineColumns` operator is similar to `combineStairs`, and it has the same parameters, but instead of right angle stairs, it uses curved ridges.

    ![http://mercury.sexy/hg_sdf/bool_small/fOpUnionColumns.png](http://mercury.sexy/hg_sdf/bool_small/fOpUnionColumns.png)

- The `combineChamfer` operator uses a flat blending area at a 45° angle.

    ![http://mercury.sexy/hg_sdf/bool_small/fOpUnionChamfer.png](http://mercury.sexy/hg_sdf/bool_small/fOpUnionChamfer.png)

# The `combine` operator and choosing combiners

- The `combine` operator is sort of like the swiss army knife of combiners. It supports a bunch of different modes, including smooth, stairs, columns, and a number of other similar types of intersection blending.
    - It doesn't necessarily give you all the special features for each one, but it can do the basics for all of them.
- So when you're trying to decide between the different combiners:
    - If you need to just merge a few things, use `simpleUnion`.
    - If you want to get the overlap between a few things, use `simpleIntersect`.
    - If you want to subtract one shape from another, use `simpleDiff`.
    - If you want to make some neat stairs between things, and you want to do special stuff like making the stairs move like an escalator, use `combineStairs`.
        - Note: The `combine` operator now supports some of this functionality.
    - If you want to do the stair thing, but rounded, use `combineColumns`.
    - Otherwise, use `combine`.

# Blending and switching

- The `blend` operator is different than the other combiners. It's more like a `cross TOP` that has a parameter that cross-fades from one input to another.
    - You can use `blend` like a `blend SOP` that doesn't care about topology or points. So if you've ever been frustrated trying to use `blend SOP` where the inputs don't line up perfectly, the `blend` ROP is the answer!
- The `switch` operator is basically the same thing as a `Switch DAT` or `Switch CHOP` etc.
    - Since the definitions that are passed between ROPs are just DATs, you **can** use a `Switch DAT`. But be ready for some frame drops when you change it. That's because when you swap out different parts of the network like that, the whole shader has to be rebuilt.
    - The `switch` ROP works around that, to allow you to quickly switch between ROPs without it having to rebuild the whole shader. It does that by including the code for all the things connected to it, and picking between them while it's running inside that shader.

# Unusual combiners

There are also some stranger combiners that sort of stretch the meaning of the term "combiner".

- The `edgeCombine` operator applies one of several types of modification and/or creates new shapes based on intersections.
    - The "pipe" mode produces a round tube in the parts where the inputs hit each other. The result is just the border between the two, without either of the original shapes.
    - The "groove" and "engrave" modes produce their first input shape, but with different kinds of indentations along the border where the second input hit the first. They are sort of like subtracting the "pipe" from the first shape.
    - The "tongue" mode is similar to "groove", but it offsets outward rather than cutting inward.
