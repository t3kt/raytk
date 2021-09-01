> Shine bright (or not, up to you)!

# Lights

Earlier in this section we said that lighting is one of the pieces of information that materials can use, but where does that lighting come from?

In other words, a light operator is asked:

- For this spot on this surface, what color is the light and where is it coming from?

## Types of Lights

There are a few different types of lights.

- The `pointLight` comes from a single point in space.
    - Regardless of where the `pointLight` is asked for lighting answers, it will always say that they are coming from a single position, which you set in the parameters.
    - It can optionally use distance attenuation, which limits how far the light goes before fading to nothing.
        - In other words, it will use the distance between where it is being asked and the light position to decide how much light it should include in its answer.
- The `directionalLight` comes from the same direction for all positions.
    - The reason that the light has to include where the light is coming from in its answers is that for things like directional lights, that position is different at different points. It's just the current position with that direction added to it.

## Limitations

- Each scene that uses `raymarchRender3D` has exactly one light source.
- Why only one light?
    - Remember that for each pixel, the shader casts out a ray, takes at least a few steps through the scene. At each step, it has to check all of the SDFs (and everything that feeds into those). Then when there's a surface hit, if shadows are being used, it does a whole secondary ray march from that spot to the light to see if it's blocked. If you add in reflections, it has to repeat that entire process multiple times.
    - You don't need to know all the details about that yet. The point is that additional lights require repeating whole portions of that complex process multiple times! Which can get really really costly unless the shader is really clever about how it does it.
    - Perhaps in the future the toolkit will support that, but for now, one light per scene.
- That said, there are other things that can approximate the appearance of lights.
    - For example, `basicMat` includes a "Sky Light" color and direction which applies color to parts of a surface that are facing some direction. It's basically like a really simple light that doesn't support shadows.

# Shadows

Shadows are calculated by trying to cast a ray from the surface point to the light source. If that ray hits anything before it gets to the light, then that spot on the surface is shadowed.

Most materials support using shadows, often with a "Enable shadows" parameter that's on by default. It's up to the material what it wants to do with that information, but most just darken the resulting color. You will also need to switch on the "Enable shadows" parameter on the `raymarchRender3d`.

Shadow operators answer the question:

- For this point on the surface, how much is it shadowed for that light over there?

There are two different shadow operators, which represent different ways that question can be answered.

- The `hardShadow` operator produces hard edges. Either a point is fully in shadow or not at all. This is the default type of shadow that's used if you don't override it. But using the `hardShadow` operator gives you some control over the settings that it uses.

![https://iquilezles.org/www/articles/rmshadows/gfx02.png](https://iquilezles.org/www/articles/rmshadows/gfx02.png)

- The `softShadow` operator produces, as one might expect, soft edges. Points can have varying amounts of shadow depending on how close the ray got to other surfaces while traveling to the light source.

![https://iquilezles.org/www/articles/rmshadows/gfx03.png](https://iquilezles.org/www/articles/rmshadows/gfx03.png)
