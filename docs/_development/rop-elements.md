---
layout: page
title: ROP Elements
nav_order: 7
---

# ROP Elements

There are several types of reusable sub-components that are used in various ROPs.

These components are treated as "elements", with a standardized data COMP nested inside them. The `opDefinition` locates these data COMPs and pulls settings from them, which contribute to the contents of the `opDefinition`.

Contributed elements include:

* Parameter specifications
* Macros
* Blocks of code that can be injected into the ROP code

## transformCodeGenerator

The `transformCodeGenerator` is used in elements that perform standard transformations (translate, rotate, scale, pivot). It generates a block of code that performs the transform with sections for each aspect (e.g. rotation) of the transform that's enabled and supported by the host ROP.

## aggregateCodeGenerator

The `aggregateCodeGenerator` is used in ROPs that repeat a chunk of code a variable number of times, depending on how many inputs are connected.

Examples include `simpleUnion`, `combineFields`, and `switch`.

## codeSwitcher

The `codeSwitcher` is used in ROPs that have a menu parameter that switches between different behaviors. Most menu parameters are implemented using this component, though some are manually written into the ROP code instead.

The switcher is based on a table of "options", where each option has:

* Name
* Label
* Code snippet
* Parameters that it uses
* Macros that it applies
* Optional other info that ROPs can use for things like changing `typeSpec` settings.

## combiner

The `combiner` is used in ROPs that combine SDF results (e.g. simple union, stair intersect, etc).

It is a wrapper around two `codeSwitcher`s, one which is for initial code to prepare parameters and the other is for performing the actual SDF combination.

## waveFunction

The `waveFunction` is used in ROPs that have repeating waves (sine, cosine, square, etc), such as `waveField` and `waveWarp`.

Similar to the `combiner`, It is a wrapper around two `codeSwitcher`s, one for preparing parameters and the other for calculating wave result values.
