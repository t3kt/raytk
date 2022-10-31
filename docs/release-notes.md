# Release Notes

## v0.28

### Highlights

### Details

* Improvements / additions
  * New OPs
    * circleWaveSdf2d
    * circularRepeat (#962)
    * hilbertCurveTransform (#963)
    * rotate4D (#966)
  * New OP features
    * bandField - faster axis/blending/reverse changes, allow selecting axis for coordinate input field
    * gridSdf - thickness and spacing field inputs (#693)
    * matCapContrib - rotation param and field input
    * mobiusRingSdf - radius field input (#693)
    * moduloSpherical - variables, shift field, offset field, repetitions field (#746), mirroring
    * pbrMat - enable reflection setting (#971)
    * petalSdf - thickness and radius field input (#693)
    * polyhedronSdf - radius, face radius, segment radius, segment size, vertex radius, vertex size, uvw field inputs (#693)
    * prismSdf - variable support (#950), arbitrary side count (#951), UV coordinates (#952)
    * raymarchRender3D - faster changes for max dist, surface dist, step limit, near hit, pass counts (#970)
    * solidAngleSdf - radius, angle field inputs (#693)
    * stepField - faster axis/blending/reverse changes, allow selecting axis for coordinate input field
    * sweep - path Sdf / position variables
    * uvField - auto coord mode
    * waveField - faster axis changes, allow selecting axis for coordinate input field
  * Snippets (#132)
    * assignColor
    * assignUV
    * moduloSpherical
* Fixes
  * directionalLight shadow distance bug (#960)
  * impulseFn error (#959)
  * lfoGenerator channel count bug (#955)
  * pointMapRender coord type error for SDFs (#956)
  * pointMapRender macro error
  * pyramidSdf fix broken height field
  * variableReferences broken during snippet build (#954)
  * variableReference default value error
  * variable typedef macro error (#957)
* Changes (potentially breaking)
  * mobiusRingSdf - remove support for 1D coords in thickness field (same thing can be done with variables), and stop combining the thickness parameter with the field (it now only uses field or parameter).
  * moduloSpherical - swap the x and y axes for the input so it makes more sense (Y = outward)
* Infrastructure / internals
  * Remove code filtering pragmas since they weren't helping (#710)
  * Remove incomplete support for using separate uniforms for parameters (#863)
  * Vulkan specialization constants! (#970)
  * Type-prefixed symbols to share things like menu option names across instances within a scene
  * Use opState approach for variables (#939)

## v0.27

### Highlights

* Internal overhaul that should improve performance when creating / editing / deleting operators
* Lots of new OP snippets
* Optimized mode for some operators (especially composeSdf)

### Details

* Improvements / additions
  * New OPs
    * providePosition
    * shadingProperty
    * truchetPattern (#948)
  * New OP snippets (#132)
    * axisLight
    * boxSdf
    * capsuleSdf
    * cartesianToPolar
    * cellTileField
    * combine
    * crossSdf
    * discSdf
    * edgeCombine
    * geodesicSdf
    * iridesenceContrib
    * logPolarRepeat
    * matCapContrib
    * rangeTransform
    * reflect
    * reorderCoords
    * segmentedLineSdf
    * skyLightContrib
    * softShadow
    * spiralZoom
    * texture3dField
    * translate
    * trapezoidSdf2d
    * truchetPattern
  * Optimized mode for OPs (#943)
    * arrange
    * combineFields
    * compositeSdf - significant performance improvement
    * extrude - replaced implementation (no Optimize toggle)
    * rotate
  * New OP features
    * compositeFields - new modes (atop, over, under, xor), blend field
    * cylinderSdf - hollow mode, thickness field
    * hexagonalWeavePattern - color settings, variables
    * iridesenceContrib - spread param, period param
    * lfoGenerator - value offset param
    * lineSegmentSdf2d - thickness, variable
    * prismSdf - hollow mode, thickness field
    * truchetPattern - alternate formats and variables (#948)
    * waveWarp - phase offset param
    * vectorToFloat - length(xy) mode
  * Editor tools (#772)
    * add depthMap
  * Inspector individual ROP code viewing
  * Added developer/systems documentation (#31)
* Fixes
  * Fix 2D support in rangeTransform (#942)
  * Fix snippet navigator window positioning (#132)
  * Fix compile error in lfoField (#944)
  * Fix defaultExpr for enable on shapedCombine
  * Fix broken swap inputs in combine when using optimized/read-only mode (#947)
  * Fix local positioning in modularMat (#916)
* Changes (potentially breaking)
  * Update to TD 2022.28040
  * Remove 1D coord support from fields in iteratedTransform
    * Instead, use variableReference to access iteration index
  * Add shadow field parameter in raymarchRender3d, which will eventually replace the Shadow input
* Infrastructure / internals
  * Replaced large portions of opDefition and shaderBuilder with more Python-based implementations. (#939)
    * Significant reduction of the number of OPs inside each ROP
    * Reduced build size
    * Restructured shader construction code to perform more in a single operation vs spreading it across many operators.
    * Removal of unused infrastructure
    * Cleanup in shared components including aggregateCodeGenerator, codeSwitcher, combiner, transformCodeGenerator, waveFunction
  * Remove support for global macros in shaderBuilder
  * Alternative "Optimize" mode for some operators that uses codegen
    * Produces only the needed parts of code and inlines as much as possible
  * Remove unnecessary supportDetector
    * https://forum.derivative.ca/t/2022-26590-long-freeze-when-loading-raytk-scene/277745/6

## v0.26

### Highlights

* Operator snippets! Usage examples that show different ways to use operators.
* New pattern generators (tilingPattern, snubQuadrilePattern) and field-based pattern controls
* New OP (composeSdf) for building SDFs composed of multiple other SDFs
* New iridescence shading element
* New pattern operators and field inputs for pattern operators.

### Details

* Improvements / additions
  * OP Snippets (#132, #845)
    * New tox containing examples of how to use operators
    * combine: switch
    * convert: extrude, revolve
    * field: atmosphereField, axisDistanceField, bandField, colorRampField, colorSwitchField, metaballField, multiPointDistanceField, sdfField
    * filter: adjustColor, elongate, flip, instance, invert, kink, knife, mirrorOctant, mobiusTransform, modulo1D, onion, quantizeValue, restrictStage, round
    * light: lightVolume, pointLight, volumetricRayCast
    * material: diffuseContrib, toonShadingContrib
    * pattern: brickPattern
    * sdf: boxSdf, coneSdf, cylinderSdf, planeSdf
    * sdf2d: lineSegmentSdf2d, pieSdf2d
  * New field inputs (#812, #588, #921, #693)
    * brickPattern - blending, shift, thickness
    * gyroidSdf - bias, phase1-2, thickness
    * hexagonalGridPattern - blending, thickness, colors
    * hexagonalWeavePattern - thickness
    * mengerSpongeSdf - cross scale, box scale, step offset
    * rosettePattern - glow, radius, spread
    * spiralZoom - phase, twist
    * weavePattern - thickness
  * New ops
    * composeSdf (#678)
    * fieldCamera (#228)
    * iridescenceContrib (#864)
    * snubQuadrilePattern (#254, #926)
    * tilingPattern (#923)
    * waveGreekFriezePattern (#930)
  * New op features
    * hexagonalGridPattern - separate blending and thickness, raw distance output, color settings (#254)
    * limitField - single-sided limit modes (#931)
    * mengerSpongeSdf - step offset, step variables (#698)
    * metaballField - auto coord type
    * multiLight - bounding volume limits (#908)
    * multiPointDistanceField - auto coord type
    * raymarchRender3d - option to disable showing background color for ray misses
    * reorderCoords - option to zero out axes (#213)
    * rosettePattern - spread and radius
* Fixes
  * Fix rotate angle scaling in orthoCamera (#918)
  * Fix coord type collapsing in projectPlane (#920)
  * Show errors out both outputs of render2d (#922)
  * Fix how render depth enable/disable is handled in raymarchRender3d
  * Fix logPolarRepeat not applying spatial remapping (#928)
  * Fix Swap Inputs not working in arrange
* Changes (potentially breaking)
  * Disable shadows by default in raymarchRender3d
  * Remove stage init code support from customOp (#933)
* Infrastructure / internals
  * Added support for adding mode-specific macros in codeSwitcher
  * Toolkit editor support for opElements (#925)
  * Lots of test cleanup
  * Remove bendRay and ray modifier functionality
  * Start a separate project file for op snippets (#132)
  * Remove support for stage init code (#933)
  * Remove unused settings in inputHandler (#933)
  * Add a build process for op snippets (#132)
  * Build process crash reduction (#935)
    * Spreading deletions over more frames
  * Reduce unnecessary cruft in common infrastructure (#933, #935)
  * Move inputValidation out of inputHandler into opDefinition (#933)

## v0.25

### Highlights

* Updated to TD 2022.25370 Vulkan build.
* Lots of bug fixes.
* New field inputs for lots of operators.
* Improved blending options in switch.

### Details

* Improvements / additions
  * New field inputs (#812, #588)
    * adjustColor - brightness/contrast, hue/saturation
    * flip - shift, offset
    * injectObjectId - id
    * jointSdf2d - bend, length, thickness
    * kink - amount, offset, spread
    * knife - offset
    * kochSnowflakeSdf2d - steps
    * modularMat - more shading elements
    * rotateNormals - rotate
    * stepField - values
    * wedgeSdf2d - end points, center point
  * Variables
    * normalized cell coordinates for modulo1d/2d/3d (#898)
    * pbrMat - light color, light position, surface color, surface uv, shaded level, surface normal
  * Show toolkit version in palette header
  * New op features
    * circleSdf - parameterized UV mode (#903)
    * knife - axis setting (#191)
    * scale - pivot setting
    * sdfField - option to return UVs
    * switch - input blending, replaces (now deprecated) blend operator (#905)
* Changes (potentially breaking)
  * Updated to TD 2022.25370 Vulkan build. The toolkit will no longer be compatible with pre-Vulkan TD builds.
  * Remove deprecated light and camera parameters in raymarchRender3d. The `Light` parameter is no longer supported. To get similar functionality use a `linkedLight`.
  * Remove deprecated ops
    * goochMat - replaced by goochShadingContrib / modularMat
    * smoothUnion - replaced by combine
* Fixes
  * Fix incorrect selection of default param page after palette creation and in toolkit editor (#109)
  * Fix merge type bug in flip (#892)
  * Fix param enable states in generalizedPolyhedronSdf (#896)
  * Fix handling of float fields in assignColor (#894)
  * Fix defaultExpr being set to invalid expression when geodesicSdf is created (#895)
  * Fix normals output in pointMapRender (#904)
  * Fix error tolerance in variableReference menu sources
  * Fix render2d erroring when no input is attached (#911)
  * Fix default alignment for render2d (#911)
  * Fix coord type menu labels in noiseFIeld (#913)
  * Fix error with camera / light return types in switch
  * Fix coord mode handling in chopField (#914)
  * Fix outdated TD palette components (#912)
* Infrastructure / internals
  * Add development-only network boxes in infra components
  * Replace all remaining uses of old param list tables, and param opDef settings
  * Incomplete changes to how parameters are collected into vectors, current inactive (#907)
  * Cleaning up lots of tests
  * Reduce use of opFind DATs in ROPs and development tools

## v0.24

### Highlights

* Parameter optimization. For many parameters, if they're marked as read-only, RayTK will bake them into the shader. 
  * This significantly improves performance, but means that if they change the shader has to recompile.
  * The new `sceneState` component helps with switching scenes between a "locked" optimized state and an "unlocked"
    editing state.
* New SDFs and other operators.
* New parameters and field inputs.

### Details

* Improvements / additions
  * Faster parameter switching (#571)
    * combine, combineFields, compositeFields, simpleDiff, simpleIntersect, simpleUnion, smoothUnion
    * colorRampField
    * modulo1d, modulo2d, reflect
    * crossSdf
    * lfoField, timeField, timeShift
  * Conditional parameter optimization (#571, #629)
    * Most operators
  * Variable support
    * cylinderSdf - angle (#856)
    * assignColor, assignUV, round - SDF (#865)
    * texture3DField, textureField - resolution (#847, #848)
    * Support accessing fields from SDF variables (#865)
  * New parameters
    * assignUV - center position (#875)
    * colorSwitchField - index scaling
    * colorRampField - coordinate range (#844)
    * elongate - axis masking (#858)
    * pieSdf2d - infinite mode (#801)
    * rectangleSdf - uv modes
    * switch - index and extend modes (#860)
    * waveWarp - amplitude multiplier (#734)
  * Editor actions (#772)
    * Sub-menus for diffuseContrib and specularContrib
    * Action for combining SDFs with arrange
    * Parameter locking actions (#869)
  * Support 3+ inputs in combineFields
  * Scene locking tool (sceneState) (#869)
  * Field inputs
    * diffuseContrib, specularContrib - color (#866)
    * generalizedPolyhedronSdf (#821)
    * slice - offset, thickness (#812)
    * spiralSdf2d (#588)
  * New operators
    * crescentSdf
    * jointSdf (#527)
    * kochSnowflakeSdf (#884)
    * mandelbrotSdf2d (#883)
    * sceneState - utility for working with parameter locking (#869)
* Changes (potentially breaking)
  * Changes to default unit (ratio instead of radians) in polarCoordField and cartesianToPolar
  * Change to input numbering in switch when some inputs are missing (#860)
* Fixes
  * Fix 2d coord handling in iteratedTransform (#846)
  * Fix coord type handling in colorRampField (#849)
  * Fix amplitude multipliers in lfoGenerator (#851)
  * Fix parameter optimization in diffuseContrib and specularContrib (#852)
  * Fix depthMap's buffer selection (#855, #436)
  * Fix field input on magnet (#861)
  * Fix type macro error in exposeValue
  * Fix enable bypass in radialClone (#882)
* Infrastructure / internals
  * opElements which generalize and automate the code gen features of codeSwitcher, combiner, aggregateCodeGenerator, etc.
    * Include in yaml specs
  * Stop using parameter part aliases (except for special params) (#857)
  * Inline typedefs by default
  * New table-based parameter definitions.
    * Supports conditional optimization of parameters (#571, #629)

## v0.23

### Highlights

* Matcap materials
* Multiple light sources!
* Faster parameter changes for lots of operators

### Details

* Improvements / additions
  * New ops
    * matCapContrib (#798)
    * multiLight!!! (#711)
  * New feaures in existing ops
    * Infinite height option for cylinderSdf and prismSdf (#648)
    * Enable toggles in arrange (#755), mostly deprecating mergeToggle
    * Shadow toggles in axisLight, directionalLight, linkedLight, pointLight, spotLight (#711)
    * Index variable in arrange
    * Variable support basicMat
    * Coord field input in axisDistanceField (#829)
  * More flexible variable types and access to fields (#833)
  * Faster parameter changes (#629, #586)
    * instance - combine modes
    * axisLight, pointLight, spotLight - attenuation (#405)
    * boxSdf - infinite axis
    * axisDistanceField, axisLight, coneSdf, cylinderSdf, discSdf, gridSdf, helixSdf, planeSdf, polarCoordField,
      prismSdf, pyramidSdf, slice, spiralSdf, spiralZoom, twist - axis
    * flip, orthoCamera - direction
    * textureField - plane
* Changes (potentially breaking)
  * Changes to variable type handling may cause compatibility issues for variableReference operators. To fix this,
    re-create them, which will assign the correct types.
  * The scale operator no longer rescales float values, only coordinates (#840)
  * Removed deprecated operators
    * ggxMat, orenNayarMat, sdfToFloat (replaced with sdfField)
  * Mark operators as deprecated
    * normalField
    * phongMat
    * uvField
* Fixes
  * matCapContrib should have been included in the previous release but wasn't (#798)
  * scale operator should not rescale float values (#840)
* Infrastructure / internals

## v0.22

### Highlights

* Faster enable/disable for lots of filters
* New 2D and 3D SDFs

### Details

* Improvements / additions
  * New ops
    * arbitraryPolygonSdf2d (#816)
    * cutDiscSdf2d / cutSphereSdf (#817)
    * matCapContrib (#798)
    * moonSdf2d
    * stairSdf2d (#815)
  * New field inputs (#812)
    * bend - shift
    * curlNoiseField - coordinates (#829)
    * elongate/extend - size, center
    * fold - distance
    * mobiusTransform - center, point
    * reflect - shift, offset
    * waveletNoiseField (#829)
  * New parameters
    * transformSequence - reverse order (#819)
  * Runtime bypass - faster enable/disable for filters (#755)
    * adjustColor
    * assignColor
    * assignUV
    * bend
    * cartesianToPolar
    * elongate
    * extend
    * fieldFunction
    * flip
    * fold
    * instance
    * iteratedTransform
    * invert
    * kink
    * knife
    * limitField
    * mirrorAxes
    * mirrorOctant
    * mirrorQuadrant
    * mobiusTransform
    * modifyNormals
    * modulo1D / modulo2D / modulo3D / moduloDistance / moduloPolar / moduloSpherical
    * onion
    * polarToCartesian
    * quadTreeRepeat
    * quantizeCoords / quantizeValue
    * radialClone
    * rangeTransform
    * reflect
    * remapCoords
    * rescaleField
    * restrictStage
    * rotate
    * rotateNormals
    * round
    * scale
    * slice
    * sphericalMobiusTransform
    * spiralZoom
    * transform
    * transformSequence
    * translate
    * twist
    * uvTransform
    * waveWarp
    * basicMat / goochMat / modularMat / pbrMat / phongMat / reflectMat / refractMat / sampledPointMat
  * UV support in cylinderSdf (#830)
  * Documentation
    * Added optimization guide (#750)
* Changes (potentially breaking)
  * Remove deprecated operators
    * spin
  * Change how rotate handles 2D coords (#821)
    * This may cause behavior changes for 2d.
    * Instead of automatically using axis-based rotation when the input is 2d, instead use the mode parameter to choose
      between types (like for 3d). For 3d, only the Z axis rotation is used.
* Fixes
  * Fix broken "Create render select" editor action (#822, #772)
  * Fix coord type resolution in coordTo2D and coordTo3D (#717)
  * Fix 1D coord support in modulo1D (#823)
  * Fix compile error in simpleIntersect
  * Fix for version error in raymarchPreviewPanel (#827, #436)
* Infrastructure / internals
  * Part way through migration to yaml-based ROP definitions (#76)

## v0.21

### Highlights

* Editor actions are contextual actions available in a menu using the new `ALT+SHIFT+R` shortcut. They include things
  like:
  * Add common material elements when a `modularMat` is selected.
  * Add a `lookAtCamera` or `pointLight` when a `raymarchRender3d` is selected.
  * Combine selected SDFs or fields.
  * Navigating to the source of a `variableReference`.
  * Converting a vector field to a float field, and vice versa.
  * Exposing and binding parameters on the parent COMP.
  * Adding animation to parameters.
* Transform sequences are a new way to apply groups of transforms to spatial coordinates or uv coordinates, including
  support for repeating the transforms in a loop! It's like a much more flexible version of `iteratedTransform`.
* Standardized SDF combine options across various ROPs that combine SDFs. This means that the full features like stair
  union with offset control are available in ROPs like `flip` or `radialClone`.
* Standardized wave function options across various ROPs. This means that `waveField`, `waveFunction`, `lfoField`, etc
  all have the same wave shape options.
* Control utility components are a set of general-purpose tools that can be used with RayTK or non-RayTK operators. Most
  of them have associated editor actions, including:
  * `lfoGenerator` which can be applied to any numeric parameter using the "Animate with LFO" action.
  * `speedGenerator` which can be applied to any numeric parmaeter using the "Animate with Speed" action.

### Details

* Improvements / additions
  * Variables (#574)
    * arcSdf2d
    * discSdf
    * mandelbulbSdf
    * provideVariable - support Sdf values
  * New ops
    * crossSection (#214, #759)
    * lfoGenerator (#788)
    * speedGenerator (#788)
    * transformSequence (#791)
  * New field inputs (#588, #693, #806)
    * arcSdf2d - orientation, aperture
    * cellTileField - coords
    * diffuseContrib - roughness, albedo
    * horseshoeSdf2d - angle, radius, length
    * linkSdf - length, radius, thickness
    * mandelbulbSdf - shift
    * mirrorAxes - flip sides (#641, #668)
    * onion - iterations, thickness
    * provideVariable - value
    * specularContrib - shininess, roughness, fresnel
    * tetrahedronSdf - scale
    * trapezoidSdf2d - height, width, points
  * New parameters
    * mirrorAxes side flipping (#641, #668)
    * torusSdf capped mode - note that UVs and variable scaling may be incorrect for capped mode (#221)
  * Standardized SDF combining across the toolkit, with new modes and parameters (#784)
    * arrange
    * combine
    * flip - compatiblity warning: this changes the menu options for the Merge Type parameter, so updates may reset it
    * instance
    * polyhedronSdf
    * radialClone - compatiblity warning: Merge Type parameter opions changed
  * Standardized wave functions across the toolkit, with new shapes and parameters (#787)
    * lfoField
    * waveField
    * waveFn
    * waveVectorField
    * waveWarp
    * additive square waves
    * wave shape function inputs
  * Editor actions (#772)
    * Append null (works for ROPs or regular CHOP/DAT/etc)
    * Inspect
    * Update OPs
    * Convert SDF to float
    * Convert vector to float for various parts
    * Rescale field
    * Rescale field with conversion to vector
    * Add diffuseContrib/specularContrib for modularMat
    * Add lookAtCamera/pointLight for raymarchRender3d
    * Extrude/Revolve 2D SDF
    * Colorize 2D SDF
    * Combine 2 SDFs
    * Combine 2 fields
    * Reference variable
    * Animate param with speedGenerator/lfoGenerator
    * Expose parameter on parent COMP
    * Customize shader config
    * Add render2D for 2D SDFs
    * Go to
      * Variable source
      * Variable references
  * Control utility components (#788)
    * lfoGenerator
    * paramFilter
    * speedGenerator
  * Custom and debug output buffers in render2d
  * Transform sequences / loops (#791)
    * bend
    * fold
    * kink
    * mirrorAxes
    * mirrorOctant
    * mirrorQuadrant
    * rangeTransform
    * reflect
    * rotate
    * scale
    * transform
    * twist
    * waveWarp
  * Vector output for lfoField when wave function input returns a vector
* Changes (potentially breaking)
  * Remove deprecated operators
    * combineChamfer, combineColumns, combineStairs, edgeEngrave, edgeGroove, edgePipe
* Fixes
  * Fix iteration index bug in instance operator (#785)
  * Fix height field bug in prismSdf
  * Fix coordinate type bug in stepField
  * Fix axis swaping in discSdf - compatibility warning, axis behavior changed
  * Fix bug with filter text and shortcuts in palette (#795)
  * Fix 2d support in mirrorAxes (#799)
  * Fix broken field input in scale (#805)
* Infrastructure / internals
  * Move most columns out of the definition tables passed between ROPs (#758)
  * Help support for variables (#763)

## v0.20

### Highlights

* Thumbnail images in the palette!
  * The palette now has a toggle to enable showing thumbnail images next to each type of operator. These make it easier
    to find the operators you're looking for, and see what's available. Not all operators have thumnbnails (e.g. it's
    hard to represent things like floatToVector in an image).
* Shortcuts in the palette.
  * Common operators now have shortcuts that can be typed into the palette for quick access.
  * Shortcuts are shown in the palette next to operator names.
* Variables are a whole new way to control and vary the behavior of operators.
  * These will eventually replace Iteration.
  * They use more explicit connections and support multiple levels of values. For example, you can repeat a shape
    radially using modulorPolar, then repeat that in a grid using modulo2d, and the input shapes can be based on both
    the grid cell and the radial slice.
  * Operators that support them have a "Variables" parameter page with buttons to create references to them which can be
    used by upstream operators.

### Details

* Improvements / additions
  * Variables (#574, #712)
    * bend
    * bezierSdf
    * bezierSdf2d
    * capsuleSdf
    * cylinderSdf
    * extrude
    * flip
    * flowerSdf2d
    * helixSdf
    * instance
    * iteratedTransform
    * logPolarRepeat
    * mirrorOctant
    * mirrorQuadrant
    * mobiusSdf
    * modularMat
    * modulo1d
    * modulo2d
    * modulo3d
    * moduloDistance
    * moduloPolar
    * pieSdf2d
    * providePosition
    * provideVariable
    * quadTreeRepeat
    * radialClone
    * reflect
    * revolve
    * starSdf2d
    * torusSdf
    * variableReference
    * Helper buttons to create references
    * Validation for references
  * New ops
    * exposeValue (#499)
    * flowerSdf2d (#748)
    * mirrorAxes (#641)
    * moduloSpherical
    * provideVariable
    * variableReference
    * wedgeSdf2d
  * New field inputs (#588)
    * bezierSdf and bezierSdf2d point field inputs (#726)
    * blend seprate source field parameter (#413)
    * blobbyCrossSdf2d
    * crossSdf2d
    * dogBoneSdf2d
    * flowerSdf2d
    * parabolaSdf2d
    * parallelogramSdf2d
    * pieSdf2d
    * planeSdf2d
    * quadSdf2d
    * spikeSdf2d
    * starSdf2d
    * switch (#413)
    * vesicaSdf2d
  * New parameters
    * cellTileField coord types (#766)
    * headSdf blinking (#116)
    * spikeSdf2d direction and center
    * reflect blending (#53)
  * Picker improvements
    * Thumbnail images (#62, #751)
    * Help text improvements
    * Help tooltips
  * Improve type handling in compositeField (#743)
  * Add help to some operators
  * Show thumbnail images in the doc site
  * Surface normal output in render2D (#560)
  * Shortcut parameters to create renderSelects similar to the variable shortcuts
  * Shortcuts for common operators in the palette (#764)
* Changes (potentially breaking)
  * Move spikeSdf2d to the correct category. This will break Update OP for those operators.
  * Reflect handling of Offset changed, resulting in slightly reduced offsets.
  * Remove 1D coord support in cylinderSdf, since variables do the same thing (#521, #574)
  * renderSelect menu handling has changed a bit, so updates may break operators. Use the "Select..." shortcuts on the
    renderer to create replacements. (#598)
* Fixes
  * Fix broken help in palette (#731)
  * Fix broken color output in pointMapRender (#757)
  * Fix height field input in cylinderSdf (#767)
  * Fix compile error in adjustColor (#775)
  * Fix parameter ordering in fieldRender
  * Fix compile error in quantizeValue
  * Fix compile error in waveletNoiseField
  * Don't show an error on combine when only first input is connected (#777)
  * Detach inspector when target op is destroyed or window closes.
  * Fix issues with output buffer menu in renderSelect (#598)
* Infrastructure / internals
  * Support for variables and references (#574, #712)
  * Refactoring and cleanup of token replacement in opDefinition
  * Support for alternate styling for ops (used for variableReference) (#753)
  * Clean up prototypes
  * Thumbnail images (#62, #751)
    * Generate thumbnails from tests
  * Log files for builds with verbosity settings (#732)
  * Consolidate input name columns in op definition tables (#299)
  * Standardize use of type aliases for primary function declarations

## v0.19

### Highlights

* New 3D bezierSdf to create arbitrary curved paths
* New headSdf based on tdhooper's model
* New polyhedronSdf with lots of controls and support for custom SDFs on vertices, similar to geodesicSdf
* Lots of new field inputs to customize various filters and SDFs
* Various optimizations

### Details

* Improvements / additions
  * New ops
    * 3D bezierSdf (#726)
    * backgroundFieldContrib (#733)
    * constantSwitchField
    * headSdf based on tdhooper's model (#116)
    * logPolarRepeat (#738)
    * polarCoordField (#699)
    * polyhedronSdf (#715)
    * quadTreeRepeat (#725)
    * sdfNormalField
    * spikeSdf2d
  * New field inputs
    * Face offset input field for geodesicSdf (#693)
    * Smooth radius and size in crossSdf (#693)
    * Scale in ellipsoidSdf (#693)
    * Offset in planeSdf (#693)
    * Radius and thickness in discSdf (#693)
    * Shift and offset in modulo1D (#722)
    * Blend radius in instance (#721)
  * New parameters
    * Reverse parameter in helixSdf (#704)
    * Expand to vec4 / collapse to float in rescaleField
    * Enable toggle in bandField (#724)
    * Logarithmic conversions in cartesianToPolar (#738)
  * Optimization
    * Skip material processing, property blending when it isn't needed (e.g. in shadow checks and calculating normals)
* Fixes
  * Fix missing translate parameters in arrange (#709)
  * Fix hidden built-in parameters in panel comps (#708)
* Infrastructure / internals
  * Code filtering, which reduces the amount of shader code sent to the GPU, which should help with recompile times.
    Currently disabled by default. (#710)
  * Improved test handling in toolkit editor
  * Simplification and optimization in shaderBuilder
  * Clean up buffer/texture table format
  * Reduce build / tox size
    * Remove unnecessary copies of shared python
    * Python code cleanup
    * Remove unnecessary data and copies of operator tables
    * Clean out internal metadata during build
    * Strip out full help DATs during build
  * Support for variables / references, as a more flexible alternative to iteration values (#574, #712)

## v0.18

### Highlights

* Easier workflows with CHOPs, including instance positioning, easier indexing in chopField, and CHOP input in
  constantField
* Cel-shading for modular materials with toonShadingContrib
* Easier coordinate mapping of pattern operators
* New noise types in noiseField
* New field inputs to customize SDFs and filters
* Convenience operators for managing scene elements, like arrange, mergeToggle, and toggleSwitch

### Details

* Improvements / additions
  * New ops
    * arrange (#655)
    * axisLight (#663)
    * magnetField (#680)
    * mergeToggle (#666)
    * polarVectorField (#676)
    * toggleSwitch (#658)
    * toonShadingContrib, for cel-shading in modular materials (#465)
    * waveVectorField (#671)
  * New field inputs
    * Coordinate fields in all pattern ops (#254, #691)
    * Edge in stepField
    * Offset in combine (#684)
    * Radius and thickness in torusSdf (#693)
    * Radius in octahedronSdf and generalizedPolyhedronSdf (#693)
    * Size, shift, offset in modulo1D, modulo2D, modulo3D (#695)
  * New parameters
    * Flip option in planeSdf (#679)
    * Limiting options for modulo2D and modulo3D (#660)
    * Mirroring support in modulo3D
    * Normal calculation exclusion for restrictStage (#667)
    * Optional coord type in iterationField (#672)
    * Pivot in moduloPolar (#681)
    * Repeat option in bandField (#687)
    * Replace mode in modifyNormals (#673)
    * Ring mode in pieSdf2d, for pie chart-style shapes (#669)
    * Zoom and offset in render2d
  * Better index support in chopField (#613, #659)
  * New noise types in noiseField using the Wombat library
  * Added CHOP-based transforms in instance (#613)
  * Added CHOP input in constantField for a quick way to get up to 4 values into a field (#682)
  * Added new pattern variants to hexagonalTruchetPattern (#255)
  * Support for proper iteration for upstream fields in iteratedTransform (#705, #94)
* Changes (potentially breaking)
  * Mark combineChamfer, combineColumns, combineStairs as deprecated since their features are all supported in the
    combine op.
* Fixes
  * Fix swapped inputs in pbrMat
  * Fix underside of pyramidSdf (#677)
  * Fix bypass indicator in opImage (#700)
  * Fix type handling bugs in mergeFields
* Infrastructure / internals
  * Replaced all inputHandlers with new implementation
  * Improvements to multiInputHandler
  * Improvements to aggregateCodeGenerator
  * Support for compute shaders
  * Added build / test support for experimental builds (#674)
  * Reduced lots of redundant copies of python modules, decreasing tox size (#701)
  * Remove deprecated type settings in opDefinition
  * Support for experimental builds (#674)

## v0.17

### Highlights

* PBR Materials (#636)
* Volumetric lighting (experimental) (#637, #11)
* Simple raymarch preview panel (#543)
* Compile speed optimizations

### Details

* Improvements / additions
  * Improved runtime menu switching (#571, #586)
    * assignUV
    * cartesianToPolar
    * cornerSdf2d
    * octahedronSdf
    * planeSdf2d
    * polarToCartesian
    * polygonSdf2d
    * prismSdf
    * sweep
    * triangleSdf2d
  * Auto-disable Inspect/Updateop parameter when unavailable (#630)
  * New fields/functions
    * colorSwitchField (#647)
    * pausingWaveFn
  * Specialized UV support in SDFs
    * sphereSdf (#526)
  * Consolidate edgeEngrave, edgeGroove, edgePipe into a single edgeCombine op (#635)
  * Added pbrMat (#636)
  * Volumetric lighting (#637, #11)
    * lightVolume
    * volumetricRayCast
  * Improve type handling
    * addFields, combineFields, compositeFields
    * blend, iterationSwitch, switch
    * circleSdf
    * axisDistanceField, bandField, cellTileField, colorRampField, constantColorField, constantField, iterationField,
      waveField
    * combine, combineChamfer, combineColumns, combineStairs
    * fieldRender, pointMapRender
    * moduloPolar, rotate
  * New control field inputs in ops
    * Phase input for waveField (#644)
  * Option to use surface color in diffuseContrib and specularContrib (#645)
  * Added simplified raymarch preview panel (#543)
  * Added projectPlane, a simplified version of coordTo3D (#214)
  * New SDFs
    * latticeSdf
* Changes (potentially breaking)
  * Support for auto-choosing a coordinate type, as well as manually specifying one to force auto-typed inputs
    * fieldRender
    * pointMapRender
* Fixes
  * Fix parameter state management in diffuseContrib (#633)
  * Fix menu optimization in combine (#634)
  * Fix coord type handling in spin (#638)
  * Fix typedef and parameter alias inlining options for shaderBuilder (#650)
* Infrastructure / internals
  * Cleanup and refactoring in opDefinition parameter handling
  * Migrate more ops to aggregateCodeGenerator
  * Type handling cleanup in many operators
  * Starting migration to new inputHandler
  * Support for generating snapshot images from tests to use in docs (#643)
  * Move code out of shared libraries and split it into more granular units to reduce unnecessary code (#70, #13)
    * almostIdentityFn, colorPaletteFn, cubicPulseFn, easeFn, extendFn, gainFn, impulseFn, sincCurveFn
    * archSdf, chainSdf, generalizePolyhedronSdf, geodesicSdf, prismSdf
    * bend, elongate, kink, moduloPolar, onion, sphericalMobiusTransform, spiralZoom
    * chopField, chopFn
    * colorRampField, curlNoiseField, domainColorField, valuePointsField
    * compositeFields
    * diffuseContrib, ggxMat, orenNayarMat, phongMat, pbrMat, specularContrib
    * iterationSwitch
    * limitField
    * polygonSdf2d, rhombusSdf2d, trapezoidSdf2d, triangleSdf2d
    * quantizeCoords, quantizeValue
    * texture3dField, textureField, triPlanarTextureField
    * waveField, waveWarp, waveFn, lfoField

## v0.16

### Highlights

* Faster switching for menu parameters with optional optimization for parameters marked as read-only.
* New field inputs to control lots of operators.
* Keyword searching in palette: palette searches now show ops matching keywords in addition to matching names /
  initials. Try searching for "ring", and `torusSdf` will show up!
* Updated to TD v2021.14360.
* Breaking change: Fixed handling of the Period and Phase parameters in waveField. This may change the behavior and
  scaling of the field.
* Breaking change: Added "Iteration Type"  setting to moduloPolar, which replaces the previous "Iterate on Cells"
  toggle. Updating OPs will default to iteration being switched off, regardless of original toggle setting.

### Details

* Improvements / additions
  * Show bypass indicator in opImages (#599)
  * Added "Customize Shader Config" to renderers (#594)
  * Option to change the palette shortcut and manually trigger the palette (#552)
  * Improved runtime menu switching (#571, #586)
    * combine
    * combineChamfer
    * combineColumns
    * combineFields
    * combineStairs
    * compositeFields
    * coneSdf
    * diffuseContrib
    * specularContrib
    * waveField
    * waveFn
  * New filters / combines
    * addFields (#606)
    * adjustColor (#587)
    * kink (variation on bend)
    * fieldFunction
    * modifyNormals (#403, #620)
  * New SDFs
    * arrowSdf2d (#612)
    * quadSdf2d
  * New fields
    * domainColorField (#401)
  * Added field inputs to operators (#588)
    * capsuleSdf
    * circleSdf
    * chamferBoxSdf (#627)
    * moduloPolar (#624)
    * noiseField (#619)
    * polygonSdf2d
    * rhombusSdf2d
    * roundedRectangleSdf2d
    * starSdf2d
    * superQuadSdf2d
  * New parameters in operators
    * colorizeSdf2d phase (#608)
    * rescaleField multiplier and post-add
  * Automatic coord/context type settings for operators
    * timeField (#141)
  * Keyword support in palette and generated docs (#378)
  * New convenience operators, which simplify common operations
    * spin
    * waveWarp
* Changes
  * Fixed handling of the Period and Phase parameters in waveField (#604).
  * New iteration type setting in moduloPolar replaces toggle (#622)
  * Update to TD v2021.14360
* Fixes
  * Workaround for color banding issue in reflections (#579)
  * Fixed breakage and incorrect SDF output in fieldRender (#611)
  * Possible fix for feature support detection for AMD GPUs (#589, #34)
  * Pass surface attributes through from input SDF in geodesicSdf (#615)
  * Fixed 2D handling in flip (#609)
  * Fixed edge discontinuity with textureFields (#617)
  * Remove workaround for parameter page issue now that TD has fixed the bug (#487)
  * Fixed parameter defaults and state handling in scale (#623)

## v0.15

### Highlights

* Materials in 2D rendering
  * 2D SDFs can now be rendered using materials, instead of with conversions like `colorizeSdf2d`.
  * The `sampledPointMat` can be used with 2D shapes similar to how it works with `pointMapRender`.
  * Not all materials work for 2D shapes, and things like surface normals and lighting are not available.
* Surface UVs
  * Surfaces can now have UV coordinates, which can be used by materials for things like texture lookups.
  * Some SDFs have a "UV Mode" option to generate shape-specific UVs, such as `boxSdf` and `sphereSdf`, as well as some
    2D SDFs including `rectangleSdf`.
  * There's a "UV" output from renderers that accesses the UV coordinates for each surface point in the rendered output.
    This can be used for things like applying textures using post-processing with TOPs.
  * UV coordinates can be assigned to any surface using `assignUV`, and modified using `uvTransform`.
  * UV coordinates can be accessed within materials using operators like `uvField`.
* Surface colors
  * Surfaces can now have a "Color" attribute, which can be assigned using `assignColor`, either with a constant color
    or using a field.
  * Surface colors can be used by various types of materials.
  * Within modular materials (`modularMat`), the `surfaceColorContrib` operator provides access to the surface color
    values.
* Background fields
  * The `raymarchRender3d` operator now has a "Background Field" parameter which can be assigned to certain types of
    fields.
  * The background field is used to calculate a color for rays that don't hit any surface before they give up.
  * The `atmosphereField` is designed for use with the "Background Field" feature. It produces a simulation of a sky
    with a sun, including some advanced atmosphere-based coloration. It's great for creating sunsets.
  * The `texture3dField` also supports being used as a background field. It can be used to apply environment lighting
    with cube-maps and other types of 3D textures.
  * The background color is used for reflection-based rays as well as primary rays, so the background colors will show
    up on reflective surfaces.
  * The `rayField` operator can be used within background fields to access the direction of the ray that hit the
    background, as well as in materials where it uses the ray that hit the surface.

### Details

* Improvements / additions
  * Material support in 2D rendering (#531)
  * Surface UVs (#526, #2, #345)
    * uvField
    * assignUV
    * UV support in:
      * boxFrameSdf
      * boxSdf
      * circleSdf
      * ellipseSdf2d
      * extrude
      * jointSdf2d
      * planeSdf
      * quadSdf
      * rectangleSdf
      * render2D
      * roundedRectangleSdf
      * sphereSdf
      * starSdf2d
      * torusSdf
    * UV output in raymarchRender3D and render2D (#345)
    * uvTransform
    * UV field input in triPlanarTextureField (#370)
  * CHOP-based buffers
  * New SDFs
    * chainSdf
    * ellipsoidSdf (#533)
    * segmentedLineSdf (#119)
    * trapezoidSdf2d
  * New fields
    * atmosphereField (#402)
    * rayField
    * stepField (#547)
  * Added offset parameter in sampledPointMat (#549)
  * Added field inputs
    * revolve (#556)
    * extrude (#567)
    * rectangleSdf (#588)
  * New filters
    * modifyNormals (#403)
    * mirrorQuadrant (#558)
  * Added normal smoothing in raymarchRender3d and pointMapRender (#559)
  * Expose iteration value in extrude and revolve (#556, #567)
  * Added assignable color attribute (#553)
  * Added background fields in raymarchRender3d (#580)
  * Added shadowContrib that can be used in modular materials to customize the coloration of shadows (#576)
  * Added troubleshooting guide (#336)
* Changes
* Fixes
  * Fixed "Create camera" bug in linkedCamera (#536)
  * Fixed context type handling
    * blend (#568)
    * many other operators (#564)
    * reorderField (#555)
    * rotate (#164)
  * Lower default surface distance in raymarchRender3d (#563)
  * Fixed axis display in inspector (#217)
  * Fixed reflection support in modular materials with reflectionContrib (#575)
  * Fixed some reflection banding issues (#579)
  * Fixed parmaeter handling and other issues in fieldExpr (#102)
* Infrastructure / development
  * Standardize processing of output buffers (#489)
  * Added support for parameter-based inputs (#565)

## v0.14

### Highlights

* Volumetric point map rendering
* Reflection material and reflection support in modular materials! (#9, #481)
* Lots of new SDFs

### Details

* Improvements / additions
  * Added invert option for slice (#461)
  * Added 2D SDFs:
    * parallelogramSdf2d
    * arcSdf2d
    * heartSdf2d
    * horseshoeSdf2d
    * bezierSdf2d (#472)
    * blobbyCrossSdf2d (#476)
    * planeSdf2d (#513)
    * ellipseSdf2d (#524)
    * jointSdf2d (#525)
    * quadSdf (#532)
  * Added 3D SDFs:
    * segmentedLineSdf (#119)
    * archSdf (#510)
  * Added hsvColorField (#464)
  * Add spotLight! (#47)
  * Add option to switch off color rendering in raymarchRender3d, which can improve performance when only using other
    types of output like depth (#477)
  * Added 1D support in coordTo2D (#475)
  * Added reflectionContrib (#9, #481)
  * Added field inputs in iteratedTransform (#480)
  * Added axis parameter in colorRampField
  * Added color field input in directionalLight
  * Added period and phase parameter in colorPaletteFn (#486)
  * Added object ID output in pointMapRender (#491)
  * Added material support in pointMapRender (#492)
  * Added bandField (#500)
  * Added unidirectional limits in modulo1D (#309)
  * Added restrictStage (#417, #503)
  * Added field inputs in cylinderSdf (#508)
  * Added invert in stepFn (#507)
  * Added axis limiting in pointDistanceField (#506)
  * Added sdfField for converting SDFs to fields (#516)
  * Added rainbowFn (#517)
  * Added offset parameter in combineColumns (#391)
  * Added shapedCombine (#444)
  * Added infinite height option in cylinderSdf (#520)
* Changes
  * pointMapRender's SDF output will no longer contain material identifiers. The RGB channels will all contain the
    distance, with A indicating whether the point existed in the input. (#541)
* Fixes
  * Fix inspector support for inputs 5-8
  * Fix errors in blend (#469)
  * Fix issue with normal directions for reflectMat (#9, #481)
  * Fix parameter handling issues in customOp (#297)
  * Fix logic around enabling and disabling shadows
  * Fix bugs in 2D support in transform, iteratedTransform, and rangeTransform
  * Fix axis normalization in rotate
  * Fix coordinate handling in helixSdf
  * Fix translate in boxFrameSdf (#490)
  * Fix parameter enabling in bend (#493)
  * Fix 2D issues in magnet (#494)
  * Fix depth compositing issue with antialiasing (#502)
  * Fix attenuation issues in linkedLight (#504)
  * Fix axis bug in mobiusRingSdf (#514)
* Infrastructure / development
  * Large-scale restructuring of how data types are handled throughout the toolkit. Operators can now support multiple
    variations of coordinate, context, and return types, which downstream operators can restrict and eventually resolve
    to single concrete types.
    * The main user-facing result is that fields don't need to specify their context type since whatever they're fed
      into can automatically switch it to the right type.

## v0.13

### Highlights

* Whole new modular material system!
  * Create customized combinations of different parts of materials.
  * Lots more options for filters, texturing, and field-based variation.
* Improvements to support for 2D SDFs and ways to use 2D SDFs in 3D scenes.
* Lots more documentation.
* NOTE: The way that shadows are handled has changed. Shadows are no longer specified at the material level.
  * Instead they are attached to the "Shadow" input on raymarchRender3d.
  * Materials now have a "Use shadow" setting to opt them in/out of shadows.

### Details

* Improvements / additions
  * Added remapCoords (#379)
  * Added 2 axis support for crossSdf (#324)
  * Added pivot support to rotate (#175) and rangeTransform (#389)
  * Added 2d spiral SDF
  * Added sweep operator (#382)
  * Added chamferBoxSdf (#383)
  * Added field inputs for boxSdf (#385), sphereSdf (#386), boxFrameSdf (#433)
  * Added sphericalMobiusTransform (#387)
  * Added easing function support for rangeTransform (#390)
  * Improve how validation errors are aggregated (#388)
  * Added iteration support for modulo3d (#317)
  * Added 2D support
    * pointMapRender (#166)
    * reflect (#439)
  * Added axis setting
    * pyramidSdf (#394)
    * positionField (#422)
    * spiralSdf (#451)
  * Added mergeFields operator (#313)
  * Added field inputs to control pointLight (#406)
  * New materials
    * Added orenNayarMat (#407)
    * Added goochMat (#409)
  * Added modular material system (#410)
    * Added specularContrib
    * Added diffuseContrib
    * Added skyLightContrib
    * Added goochShadingContrib (#409)
    * Added option to control use of light color in fieldMat
    * Added normalField (#293)
    * Added texture3DField (#430)
    * Added rotateNormals (#430, #410)
  * Added support for switching based on field input in blend (#413)
  * Added reshapeValues (#414)
  * Added compositeFields (#415)
  * Added extendFn (#419)
  * Added lineSegmentSdf2d (#424)
  * Added support for 8 inputs in switch, iterationSwitch, simpleIntersect (#101)
  * Added option to show axes in functionGraphRender (#447)
  * Added documentation for lots of operators
  * Added colorPaletteFn (#399)
  * Added multi-step support in onion (#457)
* Changes
  * Restructure the whole shadow system. (#445, #427).
    * NOTE: This is a breaking change. Shadows are no longer specified at the material level. Instead they are attached
      to the renderer.
  * Removed the deprecated customFilter and customGen
  * Disable the "Camera" parameter on raymarchRender3d. Instead, create a linkedCamera and connect it to the Camera
    input on the renderer. (#436)
* Fixes
  * Fix performance issue with shader support detection (#418, #34)
  * Fix iteration values not working for material field inputs (#397)
  * Fix cameras and lights not working with blend and switch (#421)
  * Fix transform errors for 2D (#425)
  * Fix 1D support for colorRampField, scale (#428), floatToVector (#429)
  * Fix range issues for 1D field inputs for mobiusRingSdf so that the period is now from 0..1 (#287)
  * Fix line thickness issues in functionGraphRender (#49, #447)
  * Use 2D renderer for 1D fields that return vector values, shown as a color gradient (#450)
* Infrastructure / development
  * Improved support for nested ROPs in the build process (#436)
  * Improvements to toolkit editing tools, build process, and testing system

## v0.12

### Highlights

* Fix bug when attaching a camera input in raymarchRender3D! (#185)
* Improve detection of support for `#include`, which should help for some older AMD GPUs (#34)
* Show validation errors directly on the ops where they occur, making debugging easier (#319)
* Support inspecting 2D/3D value fields using instanced geometry. (#148)
* There was an issue with the "Update OP" tool, so for this release it won't work. For future upgrades from 0.12 and
  later to newer versions, it will work.

### Details

* Improvements / additions
  * Added toolkit viewer image with version info. (#284)
  * UV map option for render2D (#261)
  * Option to output normals from pointMapRender (#290)
  * Added more noise functions in noiseField
  * Added curlNoiseField, though it is very very costly for performance (#292)
  * Added horizontal/vertical bar option in gridSdf (#291)
  * Added flashing help message about palette shortcut on toolkit load
  * Added documentation for customOp
  * 1D support for positionField
  * Added offset field input for mirrorOctant (#307)
  * Added documentation about iteration (#42)
  * Added rangeTransform (#282)
  * Added documentation for various operators
  * Added field inputs for radius/height in prismSdf (#326)
  * Added "reverse" parameter in lfoField (#327)
  * Added documentation for iteration (#42)
  * Clean up instance op and remove beta tag (#279)
  * Support 2+ inputs in iterationSwitch, add more extend modes (#335)
  * Clean up fieldRender and move to beta (#148, #7)
  * Add location position support for basicMat and fieldMat (#341)
  * Add extend modes to colorRampField
  * Add axis and thickness parameters for discSdf (#352)
  * Palette filter improvements, including search by initials (#347)
  * Add support for separate textures in triPlanarTextureField (#349)
  * Added uniform scale options in transform and iteratedTransform (#325)
* Changes
  * Separate custom parameters from customOp instances (#297). This may cause problems for instances of customOp from
    older versions.
  * Cleanup and redesign of iteration value handling throughout toolkit (#310)
  * Inverted the meaning of the Bulge parameter on dogBoneSdf2d to match the name
* Fixes
  * Fix build error in TD2021.10330 related to `op.parTuple` (#288)
  * Attempted fix for `#include` error for older AMD GPUs. (#34)
  * Fix bugs in limitField (#305)
  * Fix broken "clear filter" button in opPicker (#308)
  * Fix bug in the "smooth diff" mode in `combine` (#321)
  * Fix missing descriptions for parameter menu options in doc site (#322)
  * Fix missing op status tags in doc site (#329)
  * Fix extend mode bugs in chopField / chopFn (#231, #331)
  * Centralize Updateop logic, which will help for updates to the *next* toolkit version (#332)
  * Fix errors after renaming ROPs (#295)
  * Fix coordinate handling issues in render2D (#342)
  * Fix extend mode issue in triPlanarTextureField (#348)
  * Fix broken default expression in round (#356)
  * Fix keyboard navigation in palette (#357)
  * Fix duplicate typedef macro bug in shaderBuilder (#358)
  * Fix input handling in addFn (#363)
  * Fix parameter handling in rescaleField (#360)
* Infrastructure / development
  * Documentation for infrastructure and shared components (#98, #100)
  * Documentation about ROP code, build process (#31)
  * Added create ROP type dialog in toolkit editor (#6, #151)
  * Lots more automated testing.
  * Improve error details in automated testing.
  * Clean up handling of texture inputs.
  * Improved developer tool support for non-ROP COMPs (#107)

## v0.11

* Improvements / additions
  * Feature guide (#192)
  * Rotate axis field input for mirrorOctant (#201)
  * Added wave type parameter to lfoField (#205)
  * Added joinFn
  * Added offset and amplitude parameters to noiseField (#215)
  * Axis parameters for cylinderSdf and coneSdf (#209, #210)
  * Added period field input to waveField (#218)
  * Added origin distance mode to waveField (#212)
  * Added directional light (#48)
  * Added axis parameters to various SDFs (#219, #246, #263)
  * Added helixSdf (#222, #223)
  * Texture-based camera switching in splitCamera (#144)
  * Pixel format settings for renderers (#230)
  * LinkedLight, still in beta (#183)
  * UV field input for textureField (#2)
  * Triplanar texture mapping (#233)
  * Reflection support, *still in beta* (#9)
  * bunnySdf! (#241)
  * waveletNoiseField (#243)
  * dogBoneSdf2d (#253)
  * Added a new category of 2D pattern generators (#254, #255, #256, #277, #278)
  * spiralZoom *still in beta* (#258)
  * mobiusTransform *still in beta* (#259)
  * Added coordinate controls in render2D *still in beta* (#179, #260)
  * More documentation for value fields (#35)
  * Added uniform scale option in scale operator, which preserves SDF properties (#267)
  * More controls for behavior of raymarch near hit output (#268)
  * cornerSdf2d
  * Added instance op *still in beta* (#279)
* Changes
  * Colorization settings have been removed from render2D. To use that feature, insert the new colorizeSdf2d operator
    before the render2D. (#18)
  * Fix swapping issue in simpleDiff (#220) - this could be a breaking change if relying on the old behavior.
* Fixes
  * Fix issues in timeField (#202, #203)
  * Fix parameter enable states in noiseField (#216)
  * Fix rescaling in splitCamera (#224)
  * Fix resolution issues (#230)
  * Fix raymarch step count output (#72)
  * Fix raymarch near hit output (#268, #11)
* Infrastructure / development
  * New development editor system (#151)
  * New component test editor system (#151)
  * Ability to set minimum required inputs for multi-input ops (#225)
  * Added op icons for viewers in networks (#235, #41)
  * Added "Update OP" parameter to ops, that can be used to upgrade ops to a newer toolkit version. *still in beta* (
    #19)
  * Added macros tab in inspector (#248)

## v0.10

* Improvements / additions
  * Improve customOp initialization (#71)
  * Distance modulo is now ready for use (#59)
  * Added thickness field for mobiusRing (#120)
  * Improved documentation site
  * Documentation for parameters integrated with site (#121)
  * Documentation for inputs integrated with site (#122)
  * Added documentation for many ops
  * Launch help from any op (#106)
  * Added color and shine settings to phongMat (#33)
  * Added metaballField (#137)
  * New time OPs for efficient access to time entirely within the shader (#146)
  * Documentation for data types and vector fields (#37)
  * New palette for creating ops, replacing old createMenu, featuring integrated help, pinning, collapsible categories (
    #160)
  * Added linkedCamera and swap it into raymarchRender3d (#?????)
  * Support for marking ops as deprecated (#125)
  * Differentiate between required and optional inputs (#153)
  * Added sphereFbmSdf
* Changes
  * Got rid of `Usefield` param for round, combineChamfer, combineColumns, combineStairs, edgeEngrave, edgeGroove,
    edgePipe, rotate, scale, translate (#40). Note that this could change behavior if there's a round with a field
    connected but that parameter is switched off.
* Fixes
  * Fix twist operator: got the shift parameter working (#114)
  * Fix antialias changing depth values (#103)
  * Fix tetrahedron scaling (#124)
  * Fix input handling issue in layoutGrid (#128)
  * Fix unnecessary spikes in geodesicSdf
  * Fix radius offset in radialClone (#149)
* Infrastructure / development
  * Added splash screens to tools (#110)
  * Updated documentation processing systems (#39, #91, #86, #121, #122)
  * Cleanup and standarization of macros (#73, #87)
  * Reset parameters to defaults when creating ops from palette (#142)
  * Initial implementation of ROP devel editor (#151)
  * Automated unit testing (#173)
