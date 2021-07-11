---
layout: page
title: Troubleshooting
nav_order: 9
---

# Troubleshooting

If you encounter problems working with RayTK, there are a few ways to investigate the issue.

If there isn't a clear solution, don't hesitate to reach out for help!

## Render/Shader Errors vs Other Types of Bugs

There are two categories of problems that you might encounter when working with the toolkit.

1. Render/shader errors.
2. Unexpected behavior.

### Render/Shader Errors

If the renderer in your scene is producing a red and blue checkerboard pattern, it means that there's an error in the shader that's rendering the scene. This is either because the scene is configured incorrectly, or because the toolkit is broken in some manner. In this case there are some tools you can use to identify the error.

![Render error](/raytk/assets/images/guide/troubleshooting-render-error.png)

### Unexpected Behavior

If you are getting some sort of non-checkerboard output from the renderer, but it isn't what you want it to be, that falls into the "unexpected behavior" category. Tracking down the cause of these issues may be a bit more difficult. They may be due to bugs in the toolkit itself, or because of misunderstandings about how the toolkit works.

Either of those cases, you should still report the issue!

If it's a misunderstanding, that likely means that either the toolkit is not intuitive, or that the documentation isn't clear. Both of those are situations that should be reported and addressed!

## OP Validation Errors / Warnings

RayTK operators can detect many types of issues when they are connected to each other.

![OP errors / warnings](/raytk/assets/images/guide/troubleshooting-op-errors.png)

### Type Errors

The most common type of issue is when an operator's input is connected to the wrong type of operator.

In some cases this is straightforward. It doesn't make sense to `combine` a `boxSdf` and a `lookAtCamera`, or to use a `pointLight` as the "Radius Field" input of a `sphereSdf`.

In other cases, it's a matter of how a particular operator is configured. If a `noiseField` operator is set to use 3D coordinates, but it's connected to something that uses 2D coordinates, that will be treated as an error. In cases like that, you can often change the settings of the upstream operators so that they meet the requirements of what they're connected to. 

## The Inspector

The [Inspector](/raytk/guide/inspector) is a useful tool for investigating issues in scenes. To open it, select an operator and click the `Inspect` parameter. Start by doing that on the renderer at the end of a scene network. If you're dealing with a render/shader error, there are two tabs that can provide helpful information:

1. Validation
2. Shader

### The Validation Tab

The "Validation" tab shows any detected issues in the operator that you selected as well as in any operator upstream from that one in your scene. These are the same types of errors that will often show up on individual operators in the scene, but collected into a list with details. In some cases, an error may not be shown in the network editor on an operator, but will still show up in the inspector.

![Inspector Shader Errors](/raytk/assets/images/guide/troubleshooting-inspector-validation.png)

### The Shader Tab

The "Shader" tab shows the generated shader that the renderer is using, along with any error messages that TouchDesigner and/or the GPU driver produced when trying to compile and run the shader.

![Inspector Shader Errors](/raytk/assets/images/guide/troubleshooting-inspector-errors.png)

## Reporting Issues on GitHub

The best way to get help with RayTK is to [report the issue](https://github.com/t3kt/raytk/issues/new){:target="_blank"} on the GitHub.

You may want to try searching through [existing issues](https://github.com/t3kt/raytk/issues/){:target="_blank"} to see if your bug has been reported already. If it has, you can add a comment with details about how it manifested in your case. Or you can just file a new issue which can be de-duplicated later if needed.

Make sure to include the following information in your issue report:

* RayTK version (e.g. 0.15)
* Information from the inspector
  * Validation errors/warnings
  * Shader compile errors/warnings
* OS (e.g. Windows 10, macOS)
* GPU (e.g. Nvidia GTX 1080, AMD Radeon Pro 575)
* GPU driver version
  * [How to find your driver version](https://support.viewsonic.com/en/support/solutions/articles/33000221571-how-to-check-graphics-card-drivers-in-windows-){:target="_blank"}

## Requesting Features

You can also create a [GitHub issue](https://github.com/t3kt/raytk/issues/new){:target="_blank"} to request features or suggest improvements.

Please do this if you have ideas! We are always open to suggestions. There may also already be a way to do what you're trying to do that might just not be documented well.

When requesting a feature/improvement, you don't need to include all the details about your setup unless it seems relevant.

## Reaching Out to the Developers

If you'd like to talk to the developers about the toolkit, feel free to reach out!
