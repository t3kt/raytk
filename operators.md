# Operators

## Camera category


Operators that are used in raymarching to determine which
direction rays should travel, effectively behaving as cameras.

These operators are generally specialized for use in the raymarching
`CameraContext`, and may not support being fed through filters
or other OPs.

### basicCamera



### fisheyeCamera

A 360 fisheye camera, that shows all directions from a specific point in space.

### lookAtCamera

A camera that focuses on a specific point in space.

### orthoCamera

An orthographic (non-perspective) camera, which can be used for flattened front/side/etc views.

### splitCamera

A camera that splits the viewport into several zones, each using a separate camera.

## Combine category


Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.

### blend



### boundLimit `BETA`



### combineChamfer

Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.

Radius is the size of the blend region. This can alternately be controlled by a float value field input.

### combineColumns

Columns SDF combine, producing n-1 circular columns at a 45 degree angles along the blend region.

Number is the number of columns.
Radius is the size of the blend region.

### combineFields

Combines float or vector fields using one of several mathematical operations.

### combineStairs

Stair SDF combine, producing steps along the blend region.

Number is the number of steps.
Radius is the size of the blend region.
Offset shifts the steps along the blend region, with 0 being no shift, and 1 being a full shift of the total number of steps.

### edgeEngrave



### edgeGroove



### edgePipe

Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.

Creates an entirely new SDF result, removing any materials and other settings from the inputs.
Radius is the size of the blend region. This can alternately be controlled by a float value field input.

### iterationSwitch



### simpleDiff

Combines two SDFs using the difference operator.
Produces the area of the first shape minus any areas overlapped by the second (or vice versa).

### simpleIntersect

Combines SDFs using the intersect operator.
Produces the areas where all input shapes overlap.

### simpleUnion

Combines several SDFs using the union operator.
The resulting shape is the combined areas of each of the inputs.

### smoothUnion

Combines SDFs using a smooth union operator.
Produces the combined areas of the input shapes, blended to smooth out the intersections.

Can use an additional float field input to provide variable amounts of smoothing for different positions in space.

### switch

Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.

## Convert category


Operators that convert between different types of coordinates and
return types (SDF, float/vector field, etc).

### coordTo2D



### coordTo3D



### extrude



### floatToSdf



### floatToVector



### revolve



### sdfToFloat



### vectorToFloat



## Custom category


### customOp



## Field category


Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.

### axisDistanceField

A float field that provides the distance from a specific point along a single axis.

### cellTileField

A value field that provides an approximation of repeating cellular (voronoi) noise.

Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).
Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable by ensuring the objects wrap around the edges.
It isn't perfect but it is low cost.

### chopField `BETA`



### colorRampField

A vector field that maps an input field to values from a range of colors.

### constantColorField

A vector field that evaluates to a constant color value.

This is the same as `constantField`, but the parameter is specified as a color instead of arbitrary float values.

### constantField

A float or vector field that evaluates to a constant value.

### contextValueField

Field that returns various fields from the context, from a downstream OP.

### iterationField

Field that returns the current iteration, from a downstream OP.

### multiPointDistanceField

A vector field that provides the distance from 4 specific points in space (one for each part of the vector).

### noiseField

A float or vector field that uses one of several noise functions.

### pointDistanceField

A float field that provides the distance from a specific point in space.

### positionField

A vector field that evaluates to the coordinates in space.

### reorderField



### textureField

A float or vector field that looks up values from a texture.

### timeField



### waveField

A field that uses a periodic wave.

If there is an input, that rop is used to get the coordinate that is fed into the wave function.
Without an input, the Axis is used to run the wave function on the position along the selected axis.

## Filter category


Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.

### bend

Bends space, along a main axis, towards a second axis.

For example, bends sideways (towards X) depending on the vertical position (along Y).

* `Enable` - Enables or disables the op.
* `Direction` - Chooses the axis to bend along and the axis to bend towards.
* `Amount` - Amount of bending.
* `Shift` - Shifts the center of the bending along the main axis.

### elongate

Splits a shape into pieces, moves them apart, and connects them.

For example, a capsule is an elongated version of a sphere.

It is based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Ml3fWj).

* `Enable` - Enables or disables the op.
* `Size` - The distance that that parts are pushed apart from the origin.

### fieldExpr



### flip



### fold



### invert

Invert an SDF, so that the inside is the outside.

If used on a box, this can create an empty room with the shape filling all the space outside the room.

### iteratedTransform

Performs a transform multiple times, optionally reflecting across axes in between the steps.

This can be used to create KIFS fractals (kaleidoscopic iterated function systems).

### knife

Cuts off an SDF along a plane.

### limitField



### magnet



### mirrorOctant

Mirror coordinates across two axes and the diagonals.

### modulo1D



### modulo2D

Repeats space along 2 axes.

### modulo3D

Repeats space along all 3 axes.

### moduloPolar

Repeats space radially, like a kaleidoscope.

* `Axis` - The axis around which space is sliced.
* `Repetitions` - The number of angle repetitions. For example, a value of 6 would mean 6 slices of space, each with a 60 degree width.
* `Round To Integer` - Whether to round the `Repetitions` (and `Limit Low` and `Limit High`) to whole integers.
* `Pre Rotate` - Rotation applied before slicing.
* `Rotate` - Rotation applied after slicing.
* `Mirror Type` - Whether to flip every other slice. This is useful to avoid hard breaks at edges. It will result in the appearance of half as many slices, since half of them will be flipped.
* `Offset` - Distance to shift the shape before slicing it.
* `Use Limit` - Whether to limit the range of repetitions. Space outside that range will be left as it is.
* `Limit Low` - Start or the repetition range, in terms of the number of repetitions.
* `Limit High` - End or the repetition range, in terms of the number of repetitions.
* `Iterate On Cells` - Whether to expose the slice number as an "iteration" value for upstream ops.

### onion



### quantizeCoords

Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.

### quantizeValue



### radialClone

Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.

### reflect

Reflects space across a plane.

Can optionally expose which side of the plane a point is on as an iteration value for upstream ops.

### reorderCoords



### rescaleField



### rotate



### round

Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.

Based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Mt3BDj).

* `Amount` - positive numbers increase and round out the shape, negative numbers shrink it.
* `Use Field` - whether to use the second input to determine the amount of rounding using a value field so various positions can use different amounts of rounding.

### scale



### slice



### transform

Transform the coordinates of the input, with rotation, scaling, and translation.

Various parts of the transform can be switched off to improve performance, and the sequence of transform steps can be reordered.
It either uses the origin (0,0,0) as the pivot point, or can use another pivot point.

### translate

Translates coordinates of the input ROP.

It can optionally use a vector field to apply variable amounts of translation based on coordinates.
If a field is used, the field values are added to the Translate XYZ parameter.

### twist



## Function category


### addFn



### almostIdentityFn



### chopFn



### crossFn



### cubicPulseFn



### easeFn



### flipFn



### gainFn



### impulseFn



### modulateFn



### multiplyFn



### parabolaFn



### pennerEasingFn



### powerCurveFn



### sincCurveFn



### stepFn



### waveFn

A function that uses a periodic wave, with the position as the parameter.

## Light category


Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.

These operators are generally specialized for use in the raymarching `LightContext`
and may not support being fed through other OPs like filters.

### hardShadow

A simple hard-edged shadow.

### pointLight

Light eminating from a single point in space, with optional distance attentuation.

### softShadow

A soft-edged shadow.

## Material category


Material operators that are used by renderers to determine the
color of points on the surface of geometry.

These operators are specialized to work with a particular type
of output renderer. So a `sampledPointMat` can only be used with
a `pointMapRender`, and a `phongMat` can only be used with a
`raymarchRender3d`.

These operators are specialized to work in the `MaterialContext`
and may not support being fed through other OPs like filters.

### basicMat



### checkerboardMat



### fieldMat

A material that uses a vector field input to determine
the color. Essentially this is a conversion from a
field to a material, with no other features.

### phongMat



### sampledPointMat



## Misc category


Assorted operators that don't fit into other categories.

### customFilter



### customGen



## Output category


Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.

The most common one is `raymarchRender3d`, which takes in a chain of OPs
that produces an SDF in 3D space, and applies raymarching to render an
image.

### customRender `BETA`



### functionGraphRender



### pointMapRender



### raymarchRender3D



### render2D



### renderSelect



## Post category


### depthMap



### worldPosMap



## Sdf category


Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.

### amazingSurfaceSdf



### apollonianSdf



### boxFrameSdf

SDF for the squared frame of the edges of a box.

### boxSdf

SDF for a box, optionally infinite one one axis.

### capsuleSdf



### coneSdf

Defines a cone or capped cone shape.

* `Shape` - choose between a regular cone and a capped cone without a tip.
* `Translate` - moves the shape.
* `Height` - the height of the cone.
* `Radius` - the radius of the base of the cone.
* `Radius 2` - the radius of the top of the cone, if using a capped cone.

### crossSdf

An SDF for a 3D cross of infinite length along each axis.

* `Translate` - shifts the center of the cross.
* `Size` - the width of the arms of the cross.
* `Smooth Radius` - smooths the intersections between the arms.

### cylinderSdf

SDF for a cylinder along the Y axis, centered at the origin.

* `Translate` - shifts the center of the cylinder.
* `Radius` - the radius of the cylinder.
* `Height` - the height of the cylinder, which extends above and below the origin.

### discSdf

A flat disc facing the Y axis.

Because the disc is infinitely thin, it will only appear as a line when viewed from the side.

* `Translate` - shifts the center of the disc.
* `Radius` - the radius of the disc.

### dodecahedronFractalSdf `BETA`



### generalizedPolyhedronSdf

Generates one of several different types of polyhedra.

Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf) by Akleman and Chen.

* `Shape` - chooses between several different predefined types of polyhedra, or `Custom`, which uses the `Begin` and `End` parameters to generate different shapes.
* `Begin` - only used when the `Custom` shape. It's a bit hard to describe, so it's best to just experiment with it and see how it behaves.
* `End` - used along with `Begin`.
* `Translate` - shifts the center of the shape.
* `Radius` - the size of the shape.
* `Use Exponent` - enables the use of the `Exponent`, which controls the sharpness of the edges. When this is switched off, the shape will have sharp edges.
* `Exponent` - controls the sharpness or smoothness of the edges.

### geodesicSdf



### gridSdf

An infinite grid shape, along two axes.

* `Coord Type` - allows the shape to be used in a 2D context.
* `Cross Section Shape` - choose the shape of the bars of the grid. Not available in 2D mode.
* `Axis` - choose which axis the grid should face.
* `Spacing` - spacing between the bars of the grid. If this value is very small and the `Thickness` is high enough, the bars can merge into a solid surface. But if it is set to zero the grid will disappear due to a calculation error.
* `Axis Offset` - shifts the grid forwards or backwards along the `Axis` that it is facing. Not available in 2D mode.
* `Offset` - shifts the grid along its plane.
* `Thickness` - the thickness of the bars.
* `Context Type` - advanced parameter that should usually just be set to `Context`

### gyroidSdf



### juliaSdf



### kaliGeneratorSdf

Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).

### linkSdf

SDF for a chain link shape (an elongated loop).

### mandelbulbSdf



### mengerSpongeSdf



### mobiusRingSdf

SDF for a squared mobius ring.

### octahedronSdf

An octahedron, with its corners facing the axes.

* `Translate` - shifts the center of the shape.
* `Radius` - the size of the shape.
* `Shape Type` - advanced parameter that chooses between different types of calculations. The `Exact` option provides more accuracy but can produce roughness around the edges.

### petalSdf



### planeSdf

An infinite plane on the x, y, or z axis.

* `Axis` - chooses which axis the plane faces.
* `Offset` - shifts the plane forwards or backwards along the axis that it faces.

### prismSdf



### pyramidSdf



### sierpinskiTetrahedronSdf `BETA`



### solidAngleSdf



### sphereSdf

SDF in 3D space for a uniform sphere.

### spiralSdf



### tetrahedronSdf



### torusSdf

SDF for a torus or partial torus with end caps.

## Sdf2d category


Signed distances functions which define geometry in 2D space, by calculating
the distance from the edge of the shape at any given point.

These operators can be used either in 2D workflows, or can be converted to
3D geometry such as by extrusion.

### circleSdf



### crossSdf2d



### parabolaSdf2d



### pieSdf2d



### polygonSdf2d



### rectangleSdf



### rhombusSdf2d



### roundedRectangleSdf2d



### starSdf2d



### superQuadSdf2d



### triangleSdf2d



### vesicaSdf2d



## Utility category


Advanced operators that change how ROP chains behave.

### extractDebugValues



### extractIteration

A field that returns the current iteration, from a downstream
operator.

### injectGlobalPosition

Calls its input using the untransformed global position.

This can be used for fields that are passed to other ops that are using downstream transforms to have the field use the raw global position while being used on an op that is transformed.

### injectObjectId

Assigns an arbitrary value to the objectId field of an SDF, which can later
be extracted from rendered output.

This can be used to identify which object is shown at any given pixel in
the output.
