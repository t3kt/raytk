# Release Notes

## v0.18

### Highlights

* ...

### Details

* Improvements / additions
    * New ops
        * toggleSwitch (#658)
        * mergeToggle (#666)
        * arrange (#655)
        * axisLight (#663)
        * polarVectorField (#676)
        * waveVectorField (#671)
        * toonShadingContrib, for cel-shading in modular materials (#465)
        * magnetField (#680)
        * axisLight (#663)
    * New field inputs
        * Edge in stepField
        * Offset in combine (#684)
        * Size, shift, offset in modulo1D, modulo2D, modulo3D (#695)
        * Coordinate fields in all pattern ops (#254, #691)
        * Radius in octahedronSdf and generalizedPolyhedronSdf (#693)
        * Radius and thickness in torusSdf (#693)
    * New parameters
        * Limiting options for modulo2D and modulo3D (#660)
        * Mirroring support in modulo3D
        * Replace mode in modifyNormals (#673)
        * Optional coord type in iterationField (#672)
        * Ring mode in pieSdf2d, for pie chart-style shapes (#669)
        * Normal calculation exclusion for restrictStage (#667)
        * Flip option in planeSdf (#679)
        * Zoom and offset in render2d
        * Pivot in moduloPolar (#681)
        * Repeat option in bandField (#687)
    * Better index support in chopField (#613, #659)
    * New noise types in noiseField using the Wombat library
    * Added CHOP-based transforms in instance (#613)
    * Added CHOP input in constantField for a quick way to get up to 4 values into a field (#682)
    * Added new pattern variants to hexagonalTruchetPattern (#255)
    * Support for proper iteration for upstream fields in iteratedTransform (#705, #94)
* Changes (potentially breaking)
    * Mark combineChamfer, combineColumns, combineStairs as deprecated since their features are all supported in the combine op.
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
        * axisDistanceField, bandField, cellTileField, colorRampField, constantColorField, constantField, iterationField, waveField
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
* Keyword searching in palette: palette searches now show ops matching keywords in addition to matching names / initials. Try searching for "ring", and `torusSdf` will show up!
* Updated to TD v2021.14360.
* Breaking change: Fixed handling of the Period and Phase parameters in waveField. This may change the behavior and scaling of the field.
* Breaking change: Added "Iteration Type"  setting to moduloPolar, which replaces the previous "Iterate on Cells" toggle. Updating OPs will default to iteration being switched off, regardless of original toggle setting.

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
  * Some SDFs have a "UV Mode" option to generate shape-specific UVs, such as `boxSdf` and `sphereSdf`, as well as some 2D SDFs including `rectangleSdf`.
  * There's a "UV" output from renderers that accesses the UV coordinates for each surface point in the rendered output. This can be used for things like applying textures using post-processing with TOPs.
  * UV coordinates can be assigned to any surface using `assignUV`, and modified using `uvTransform`.
  * UV coordinates can be accessed within materials using operators like `uvField`.
* Surface colors
  * Surfaces can now have a "Color" attribute, which can be assigned using `assignColor`, either with a constant color or using a field.
  * Surface colors can be used by various types of materials.
  * Within modular materials (`modularMat`), the `surfaceColorContrib` operator provides access to the surface color values.
* Background fields
  * The `raymarchRender3d` operator now has a "Background Field" parameter which can be assigned to certain types of fields.
  * The background field is used to calculate a color for rays that don't hit any surface before they give up.
  * The `atmosphereField` is designed for use with the "Background Field" feature. It produces a simulation of a sky with a sun, including some advanced atmosphere-based coloration. It's great for creating sunsets.
  * The `texture3dField` also supports being used as a background field. It can be used to apply environment lighting with cube-maps and other types of 3D textures.
  * The background color is used for reflection-based rays as well as primary rays, so the background colors will show up on reflective surfaces.
  * The `rayField` operator can be used within background fields to access the direction of the ray that hit the background, as well as in materials where it uses the ray that hit the surface.

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
  * pointMapRender's SDF output will no longer contain material identifiers. The RGB channels will all contain the distance, with A indicating whether the point existed in the input. (#541)
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
    * NOTE: This is a breaking change. Shadows are no longer specified at the material level. Instead they are attached to the renderer.
  * Removed the deprecated customFilter and customGen
  * Disable the "Camera" parameter on raymarchRender3d. Instead, create a linkedCamera and connect it to the Camera input on the renderer. (#436)
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
* There was an issue with the "Update OP" tool, so for this release it won't work. For future upgrades from 0.12 and later to newer versions, it will work.

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
  * Separate custom parameters from customOp instances (#297). This may cause problems for instances of customOp from older versions.
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
  * Added "Update OP" parameter to ops, that can be used to upgrade ops to a newer toolkit version. *still in beta* (#19)
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
  * New palette for creating ops, replacing old createMenu, featuring integrated help, pinning, collapsible categories (#160)
  * Added linkedCamera and swap it into raymarchRender3d (#?????)
  * Support for marking ops as deprecated (#125)
  * Differentiate between required and optional inputs (#153)
  * Added sphereFbmSdf
* Changes
  * Got rid of `Usefield` param for round, combineChamfer, combineColumns, combineStairs, edgeEngrave, edgeGroove, edgePipe, rotate, scale, translate (#40). Note that this could change behavior if there's a round with a field connected but that parameter is switched off.
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
