---
layout: page
title: Optimization Tips
nav_order: 12
---

# Optimizing RayTK Scenes

When creating scenes with RayTK, the performance of the renderer can vary widely depending on a number of different factors.

## RayTK Is Different Than The Rest of TouchDesigner

There are some core differences in how RayTK operates compared to almost everything else in TouchDesigner. That means that practices
that improve performance in regular networks may make RayTK networks perform worse. Conversely some practices that would cause
performance problems in regular networks can improve RayTK performance.

The most important difference between RayTK and regular TD is that operators don't contain values. In nearly all other TD operators,
each one produces some sort of value, which can then be used by other operators. For a CHOP, the value is a set of channels. For a
DAT it's cells or text. For a TOP it's an image. When a network is running, on each frame, the TD engine starts by requesting values
from certain operators. For each operator, it first makes sure all of the things that operator depends on have been evaluated. If
one of those dependencies has already been evaluated, the value within it is reused without having to repeat all the calculations
that produced that value. This caching is critical to TouchDesigner performance.

For example, let's say you have an `LFO CHOP` connected to both a `Filter CHOP` and a `Limit CHOP`, and both of those are connected
to a `Math CHOP` that multiplies the channels by each other. When TD is calculating a value for the `Math CHOP` it first has to get
values from the `Filter CHOP` and the `Limit CHOP`. When it gets the value for the `Filter CHOP`, it first has to get the value for
the `LFO CHOP`. Then, when getting a value for the `Limit CHOP`, it reuses the value it already calculated for the `LFO CHOP`.

But a ROP in a RayTK network has no equivalent of this sort of "value". Instead, a ROP represents a way to answer a question, such
as "what surface is closest to point P?". During the process of rendering the scene, an operator will be asked many different
variations of that question. For example, an SDF is asked about a series of points as a ray marches along. The answers that it
produces are different depending on the specific question being asked. The result is that when you connect a ROP to 2 different
inputs of another ROP, that first one gets asked twice as many questions, which means twice the performance cost.

## Performance Factors

There are a few categories of factors that impact RayTK performance:

- Complex operators that do a lot of calculations when asked for results.
- Things that result in operators being asked for results many times.

## Expensive Operators

There are some operators which are simply expensive. The `waveletNoiseField` (and other noise-related operators) are good examples
of this. Each time they are asked a question, they have to run a large amount of code to come up with a result.

The help for some operators will mention that they can be costly.

In other cases the best way to identify costly operators is to try swapping them with simpler alternatives and comparing the
performance. If you're using a `noiseField` for a material color, try swapping in a `constantField`. If the performance improves
dramatically, that means that the `noiseField` was contributing a lot to the performance cost.

### Strategy

- Be selective about when you use them, and use simpler alternatives when suitable.
- Be extra careful about using them in places where they will be run many times (see below).

## Calculation Multipliers

The most important performance factors are things that result in operators being run many times.

For any type of renderer, the resolution will have a major impact on performance. Remember that the shader will be running
its whole process for every pixel, in parallel. The more pixels, the more GPU resources that will consume.

### `raymarchRender3d`

When using `raymarchRender3d`, the whole network connected to the first input on the renderer is used to calculate an SDF result.

The renderer runs that whole network once for every step along a ray's path. That means that if the SDF network costs `C`,
marching a ray costs `C * S`, where `S` is the number of marching steps.

Once a ray hits a surface, it calculates the color. To do that, it runs the associated material, which includes everything
connected to secondary inputs on the material ROP.

For example, `basicMat` could have a `noiseField` connected to its "Base Color Field" input. That `noiseField` would need to be run
to come up with that color.

If the material is using surface normals (which almost all materials do), the renderer has to run the whole SDF network 4 more
times. It does this at slightly offset positions in order to calculate the slope of the surface.

If the material is using lighting (which almost all do), the renderer has to run the lighting network once.

If the material is using shadows, the renderer does a whole additional ray march to check if the light is blocked (shadowed) for
that point on the surface. That means another multiple of the cost of a ray march.

If the material is using reflection, for each reflection pass, the renderer does an entire render pass, which includes a ray march,
and also evaluating a material, possibly a shadow ray march, and so on.

If the renderer is using anti-aliasing, it runs that entire process (which may include numerous ray marches) multiple times, in
order to average the results.

So overall, the cost of the renderer would be:

```
{antialias steps}
*
(
	{camera cost}
	+
	(
		(1 + {reflection passes})
		*
	  (
	    ({SDF cost} * {march steps})
			+
			({SDF cost} * {march steps})   // for shadow
	    +
	    ({SDF cost} * 4)  // for normals
	    +
	    {material cost}
			+
			{light cost}
	  )
	)
)
```

Within an SDF network, certain operators like `radialClone` will run their input (and everything upstream) multiple times.

### Strategies

From most effective to least:

- Reduce antialiasing as much as you can without it looking bad
- Reduce resolution
- Avoid reflection if possible, and if so, reduce the number of reflection passes
- Avoid using shadows if possible
- Simplify SDF
    - Avoid operators like `radialClone`, `instance`, `flip` (when using merging)
- Simplify material
- Simplify light
- Simplify camera
