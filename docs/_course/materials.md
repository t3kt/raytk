> Making shapes pretty! Or at least visible!

# Materials

In keeping with the theme of "ROPs answer questions about space", materials answer questions, but unlike other ROPs, they are actually asked two different questions at different points in the rendering process:

- What's the closest surface to point P?
    - This is the standard SDF question. The material answers it by asking the same question of its input, and then altering the answer to include a setting telling it which material to use.
- Then, later on, the `raymarchRender3D` asks it *another* question:
    - For this point where a ray hit a surface (which is assigned to the material that you set up), what color should that produce?

## MaterialContext and Contexts in General

When the material is being asked that second question, there's more relevant information beyond just a position. For example, what surface the ray hit, what direction the surface is facing (the normal), where and what color the light is, etc.

That extra information comes packaged in a `MaterialContext`.

There are different types of contexts, which have different info about why and how a question is being asked. So far we've dealt with the default `Context` which is what's used when rays are being cast. It has stuff like the iteration value from downstream operators.

When that second question is asked, some materials can use field inputs for things like base color. When they do that, they include the `MaterialContext` along with the position.

Anything connected to that field input on the material needs to be set up to work with `MaterialContext` instead of `Context`. Usually what that means is that you need to change the "Context Type" parameter on things connected to those inputs (and things connected to their inputs, etc), though many operators automatically use the appropriate context type.

## Common materials

The most commonly used materials are the ones that use shading models that are roughly based on how light behaves in the physical world.

The `basicMat` material uses specular lighting. It also has a secondary "Sky light" feature that is sort of like a secondary directional "light" that applies different amounts of color based on surface normals. The "sky light" is not a real fully featured light with shadows and so on, but it is a cheap way to apply some secondary coloration.

The `phongMat` is similar to `basicMat`. It uses the [Phong](https://en.wikipedia.org/wiki/Phong_shading) shading model, which is one of the most common types of shading. It uses a combination of ambient, diffuse, and specular lighting, each of which have their own color settings.

The `goochMat` is a bit different from other materials, in that it isn't intended to produce realistic light-based results. Instead it uses directional coloration to demonstrate the details of shapes.

![https://warezovvvblog.files.wordpress.com/2017/01/gooch.png](https://warezovvvblog.files.wordpress.com/2017/01/gooch.png)

[https://warezovvvblog.wordpress.com/2017/01/17/gooch-shading/](https://warezovvvblog.wordpress.com/2017/01/17/gooch-shading/)

## Modular materials

The `modularMat` takes a different approach than most other materials.

Most materials package together a few different features and combine the colors they produce. For example, `basicMat` has specular lighting, base color, and the "sky light" feature. But these materials are limited to a specific combination of features.

In contrast, the `modularMat` lets you combine the coloration produced by customizable combinations of various contributing elements. It has inputs that take in one or more ROPs that produce colors, and adds up their results.

There are a few operators that are designed to work with `modularMat`:

- The `specularContrib` operator provides one of several different types of specular lighting elements.
- The `diffuseContrib` operator provides types of diffuse lighting elements.
- The `skyLightContrib` operator is a reusable version of the "sky light" feature in `basicMat`.
- The `surfaceColorContrib` operator accesses the color attribute set on the surface by the `assignColor` operator.

If you want to combine more than two lighting elements, you can use a `combineFields` or `compositeFields` operator to merge their results before passing them to `modularMat`.

## Material Blending

When two SDFs are combined with something like `simpleUnion`, if they each have different materials, the response from the `simpleUnion` will use the material of whichever surface is closest to the point.

But for some combining methods, like `smoothUnion` or `combineStairs`, there will be parts of the surface that are partially from one SDF and partially from the other. When those operators are asked for a surface hit, their answer will include information about both materials, and about how much to blend from one to the other.

When the shader is figuring out the color for a surface hit, if there are multiple materials involved, it will check both, and blend between their answers. The result is a smooth linear transition from one material to the other.

It's worth noting that using blending does mean doing all the work for both materials, though only for surface hits that are along the blend regions. So it can have some added performance cost, though less than one might expect.

# Texturing

Many of the materials have field inputs that they can use to look up colors for spots of surfaces.

The `textureField` operator uses a `TOP` to look up colors. So you can use it with materials to color surfaces using images or other `TOP` sources. It has options for picking which axes to use to choose UV coordinates when asked about points in 3D space.

While `textureField` is useful for applying textures to flat surfaces, the textures will be stretched out for surfaces that are facing other directions. The `triPlanarTextureField` addresses that by applying the texture three different times, once from each axis. For each of those textures, it blends based on how close a point is to facing each axis. It can either use the same texture for all three or it can use separate textures for each axis.

![https://www.martinpalko.com/wp-content/uploads/2014/03/TriplanarMapped.jpg](https://www.martinpalko.com/wp-content/uploads/2014/03/TriplanarMapped.jpg)

[http://www.martinpalko.com/triplanar-mapping/](http://www.martinpalko.com/triplanar-mapping/)

## UV Coordinates

TODO: write this

When using a `textureField`, the operator needs to determine which pixel in the texture it should use for the surface position that's being rendered. In other words, it needs UV coordinates.

The simplest approach to this is to base the UV on the spatial coordinates of the surface hit. For example, using `p.x` for U and `p.y` for V. The `textureField` operator has a menu that lets you chose from different variations of this approach, such as using y and z, etc.

While this can work for some cases, it doesn't necessarily line up with the actual shape of the surface. For example, if you have a sphere, using XY will look like a projector facing one side...... 

In a traditional render setup, these

## Bump Mapping

As mentioned earlier, part of the preparation for running the material calculations involves coming up with the surface normal vector.

Shading contribution operators (and other material operators) use the normal vectors for their shading calculations.

By inserting a `modifyNormals` or `rotateNormals` operator between these operators and the `modularMat` that uses them, you can alter the normals that the shading operators get, which alters how they shade the surface.

The `modifyNormals` operator takes in a vector field, which it applies to the original normals. By attaching a `textureField`, you can apply a normal (bump) map texture to a surface.
