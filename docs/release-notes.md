# Release Notes

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
