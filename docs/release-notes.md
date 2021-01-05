# Release Notes

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
