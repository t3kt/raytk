We're now going to walk through how a raymarching scene works with all the parts we've discussed so far.

If you want to skip ahead you can but it may be useful for understanding how things fit together.

Let's say the network is:

- A `sphereSdf`, connected to a `basicMat`
- The `basicMat` also has a `textureField` hooked up to its "base color field" input
- The `basicMat` also has a `softShadow` hooked up to its "shadow" input
- The `basicMat` is connected to a `translate`
- The `translate` is connected to a `raymarchRender3D`
- The `raymarchRender3D` also has a `pointLight` connected to its "light" input

# Act 1: The ray is cast!

- `raymarchRender3D` to `translate`: Hey what's the closest thing to `p`?
- `translate`: Just a sec, gotta ask `basicMat`...
- `translate`: Hey `basicMat`, what's the closest thing to this other point that's shifted from `p`?
- `basicMat`: Just a sec, gotta ask `sphereSdf`...
- `sphereSdf`: It's a sphere and it's really close to that point you asked about!
- `basicMat`: Hey `translate`, I checked and the closest thing is a sphere that's really close and also btw check back with me if you want to figure out the color for it.
- `translate`: Hey `raymarchRender3D`, apparently the closest thing is a sphere which is super close to `p`, and also `basicMat` says to check with them when you are figuring out the color!
- `raymarchRender3D`: Thanks!

# Act 2: The light shines!

- `raymarchRender3D`: Whoa. That sphere so close to `p` that the ray is actually hitting the surface! That means I need to figure out a color coming off of it, and we'll probably need info about a light for that...
- `raymarchRender3D`: Hey `pointLight`, I got a ray that hit this sphere in this spot. What light are you gonna give me for that spot?
- `pointLight`: That spot is pretty close to me, so it's going to get a bunch of light. Also that light is purple and it's coming from my position here.

# Act 3: A color begins to emerge!

- `raymarchRender3D`: Hm... so I've got this point on the surface of a sphere that's facing that direction, and there's a bunch of purple light on it coming from that position there. I remember that the `basicMat` said to ask it about the color for that surface...
- `raymarchRender3D`: Hey `basicMat`, you said to ask you about the color.. So what color is it when its facing that direction and is getting a bunch of purple light?
- `basicMat`: Just a sec... gotta check some stuff.

# Act 4: Shadow falls (also a side-quest!)

- `basicMat`: Hey `softShadow` If the light is coming from over there to this point on the surface, is there anything blocking it?
- `softShadow`: Just a sec... I'm gonna take a walk over there to check.
- The `softShadow` goes on a brief walk towards the light. Along the way it encounters `sphereSdf`.
    - `softShadow`: Hey `sphereSdf`, over here on this spot on the path to the light, how close is  that to your shape?
    - `sphereSdf`: It gets pretty close. It doesn't actually hit though.
    - TODO: FIX THIS
- `softShadow`: The light is blocked a little bit. But not fully blocked it. I'd say 30% blocked.
- `basicMat`: Hm... so a bunch of purple light, but it's 30% blocked, so 30% less purple light.

# Act 5: The texture sage is consulted

- `basicMat`: Hm... To answer that, I also need to check what color the surface is painted at that spot...
- `basicMat`: Hey `textureField`, for this spot on the surface, what color would you say the paint is?
- `textureField`: It's red.

# Act 6: Success! Color!

- `basicMat`: Ok, `raymarchRender3D`, I have an answer! Since the surface is red, and there's 70% purple light on it... I'm gonna say that spot is magenta!
- `raymarchRender3D` to `basicMat`: Thanks! I'm totes going to use that for my pixel!
