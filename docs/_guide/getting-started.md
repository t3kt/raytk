---
layout: page
title: Getting Started With RayTK
nav_order: 1
---

## Download the Library

The first step to using RayTK is to download the latest tox file, from the [repository](https://github.com/t3kt/raytk/releases).

Note that there are many source files in the repository itself, but these are only needed for development purposes.
Feel free to take a look through them if you want, but if you only want to *use* the library rather than *modify* it, use the release tox file.

## Load the Library

Drag the tox file into the project.

## Creating a Network

To create your first ROP, use the keyboard shortcut `alt + r` to open up the editor tools popup. It will show a list of available ROPs, organized into categories. You can search by typing a name. This popup is like the main TouchDesigner "OP Create Dialog" (using `tab`), but it shows the available ROPs rather than the standard TouchDesigner OPs.

![Create OP Menu](/raytk/assets/images/guide/intro-createOpMenu.png)

1. Choose a `boxFrameSdf`, and a new COMP will be created in the network editor.
1. Create a `raymarchRender3d` and connect the output of your `boxFrameSdf` to the input of the `raymarchRender3d`.
1. Connect a `Null TOP` to the first output of `raymarchRender3d`.
1. Play around with the parameters of the `boxFrameSdf`.

You've just created your first RayTK network!

![Basic RayTK Network](/raytk/assets/images/guide/intro-basicNetwork.png)

The `boxFrameSdf` is an `SDF` (signed distance function) operator, which is how you define geometry. It's equivalent to `SOP`s like `Sphere`, `Box`, etc.

The `raymarchRender3d` is an "Output OP" or renderer. It's equivalent to a `Render TOP`. It generates and runs a shader that renders the scene.

## Camera and Light

By default, the renderer uses a built-in camera and light. To override those, attach camera and light operators.

1. Create a `lookAtCamera` and connect it to the second ("Camera") input of the `raymarchRender3d`.
1. Create a `pointLight` and connect it to the third ("Light") input of the `raymarchRender3d`.
1. Try changing the settings of the `lookAtCamera` and `pointLight`.

![Basic RayTK Network](/raytk/assets/images/guide/intro-basicNetwork2.png)

## Filters

Now that you have a complete render setup, you can use filters to modify the SDF.

1. Add a `twist` between the `boxFrameSdf` and the `raymarchRender3d`.
1. Adjust the "Amount" parameter and watch the box twist in the output.
1. Try changing the "Axis" parameter to twist around another axis.

![Basic RayTK Network](/raytk/assets/images/guide/intro-basicNetwork3.png)

You've just created your first "filter" ROP! It modifies the behavior of another ROP.

## Materials

By default, the renderer uses a built-in material. To override it, insert a material operator.

1. Add a `basicMat` between the `twist` and the `raymarchRender3d`.
2. Try out different color settings.

![Basic RayTK Network](/raytk/assets/images/guide/intro-basicNetwork4.png)

You've just created your first "material" ROP. It assigns a material to an SDF, which is used to determine what colors it should use.

## Cleanup

Now that you've set up your scene, you don't need to keep the main toolkit tox loaded in the project if you don't want to.

All the ROPs are totally self-contained! That means that if you save out scenes as tox files, you can drop those into any project and they'll work, without having to load the toolkit itself.

However some editing tools such as the Palette and the [Inspector] are only available if the toolkit itself is loaded

[Inspector]: /raytk/guide/inspector
