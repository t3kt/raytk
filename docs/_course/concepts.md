# Raymarching

- You don't need to know all the details of how raymarching works to use the toolkit (in fact that's kind of the point!). But it is still useful to have a general understand of it when learning how to use the toolkit.
- Raymarching simulates rays of light going backwards from the camera into the scene (instead of going from the scene into the camera, but the logic is the same).
- Each pixel of the rendering casts out a ray into the scene, and the shader marches along that ray, stopping at points along the way until the ray hits a surface.

![https://adrianb.io/img/2016-10-01-raymarching/figure3.png](https://adrianb.io/img/2016-10-01-raymarching/figure3.png)

[https://adrianb.io/2016/10/01/raymarching.html](https://adrianb.io/2016/10/01/raymarching.html)

- When the ray hits a surface, the shader then casts another ray from that point towards the light source to figure out how much light is hitting that point (and bouncing off it towards the camera).
- The shader then uses that light information and other properties of the surface to decide what color it is.
- That color is what shows up in the rendering for that pixel.
- 
[Shadertoy](https://www.shadertoy.com/view/4lyBDV)

The main thing to take away from this section is:

- The raymarching process is based around focusing on points in space and examining the scene at each point.

# Toolkit Concepts

In the previous section, we discussed how ROPs are used in raymarching shaders.

The roles of operators in a RayTK scene can be summarized as:

- ROPs answer various types of questions about points in space. We will sometimes use the shorthand `p` to refer to those points.

If you're familiar with traditional text-based programming (or mathematics), you can think of a ROP as a "function" that takes in a parameter `p`, and returns some sort of value. In fact, inside each ROP is a snippet of shader code the defines such a function in GLSL!

- Output OPs like `raymarchRender3D` ask ROPs these questions about points along the path of rays that it casts through the scene.
- Many ROPs, when asked a question about a point, will turn around and ask another ROP either the same question, or a different question, about either that same point, or possibly even a different point, and use the answer they got to produce their own answer.
- There are a variety of different types of questions that ROPs can be asked.
- Different ROPs support different kinds of questions and different kinds of answers.

If it helps, you can think of the process as a discussion:

- Shader: "Hey ROP, what's the closest thing to this point here?"
- ROP: "A sphere, but it's pretty far away"
- Shader: "Ok, and what about the closest thing to this other point that's further along?"
- ROP: "A sphere and it's so close that it's basically hitting the surface!"
- Shader: "Thanks! I'm gonna go decide what color that should be!"

# Output OPs vs ROPs

- As mentioned previously, Output OPs take in one or more ROPs, generate a shader, and run it in a `GLSL TOP` to produce some outputs.
- Nearly all of the actual work done to render a scene happens inside the Output OP at the end of the scene network.
- The network of ROPs that connect into the Output OP produce Definitions that specify how they behave, and parameters that the Output OP gathers together to use in the shader.
- Most of the time, there is basically no work going on in most ROPs, except when you change certain types of settings on them (which cause their Definition to change). Changes to most parameters don't result in changes to the Definition.
- There are a few different types of Output OPs.
    - The main one that we've been discussing so far is `raymarchRender3D`.
    - There are others that we'll discuss later, such as `render2D`, `pointMapRender`, and `functionGraphRender`.
