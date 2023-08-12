"use strict";
(self["webpackChunk_datalayer_jupyter_dashboard"] = self["webpackChunk_datalayer_jupyter_dashboard"] || []).push([["style_index_js"],{

/***/ "../../../../../node_modules/css-loader/dist/cjs.js!./style/base.css":
/*!***************************************************************************!*\
  !*** ../../../../../node_modules/css-loader/dist/cjs.js!./style/base.css ***!
  \***************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../../../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "../../../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../../../../node_modules/css-loader/dist/runtime/api.js */ "../../../../../node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, ".dsh-JupyterDashboard {\n    overflow: auto;\n  }\n  \n.dsh-DashboardWidget {\n  display: inline-flex;\n}\n\n.dsh-DashboardWidget .dsh-MarkdownOutput {\n  display: inline-block;\n}\n\n.dsh-EditableWidget {\n  outline: var(--jp-border-width) solid var(--jp-inverse-layout-color4);\n  outline-offset: calc(-1 * var(--jp-border-width));\n  background: var(--jp-layout-color0);\n  overflow: visible;\n  contain: none !important;\n}\n\n.dsh-EditableWidget > .dsh-DashboardWidgetChild {\n  pointer-events: none;\n}\n\n.dsh-EditableWidget:focus {\n  outline: var(--jp-border-width) solid var(--jp-brand-color1);\n  outline-offset: calc(-1 * var(--jp-border-width));\n}\n\n.dsh-EditableWidget:hover {\n  outline: var(--jp-border-width) solid var(--jp-brand-color1);\n  outline-offset: calc(-1 * var(--jp-border-width));\n  cursor: move;\n}\n\n.dsh-DashboardArea {\n  overflow: auto;\n}\n\n.dsh-Resizer {\n  display: none;\n  width: 4px;\n  height: 4px;\n  outline: 1px solid var(--jp-brand-color1);\n  z-index: 3;\n  background-color: var(--jp-layout-color0);\n  position: absolute;\n}\n\n.dsh-Resizer:hover {\n  background-color: var(--jp-brand-color1);\n}\n\n.dsh-ResizerBottomRight {\n  right: -2px;\n  bottom: -2px;\n  cursor: nwse-resize;\n}\n\n.dsh-ResizerBottomLeft {\n  left: -2px;\n  bottom: -2px;\n  cursor: nesw-resize;\n}\n\n.dsh-ResizerTopRight {\n  right: -2px;\n  top: -2px;\n  cursor: nesw-resize;\n}\n\n.dsh-ResizerTopLeft {\n  left: -2px;\n  top: -2px;\n  cursor: nwse-resize;\n}\n\n.dsh-DashboardWidgetChild {\n  /*\n  width: 100%;\n  height: 100%;\n  */\n  overflow: hidden;\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.dsh-EditableWidget:focus .dsh-Resizer {\n  display: block;\n}\n\n.dsh-Canvas {\n  pointer-events: none;\n}\n\n.dsh-Canvas.dsh-FreeLayout {\n  background-image: linear-gradient(\n      to right,\n      var(--jp-border-color2) 1px,\n      transparent 1px\n    ),\n    linear-gradient(to bottom, var(--jp-border-color2) 1px, transparent 1px);\n  background-color: var(--jp-cell-editor-background);\n  background-size: 10px 10px;\n}\n\n.dsh-Canvas.dsh-TiledLayout {\n  background-image: linear-gradient(\n      to right,\n      var(--jp-border-color2) 1px,\n      transparent 1px\n    ),\n    linear-gradient(to bottom, var(--jp-border-color2) 1px, transparent 1px);\n  background-color: var(--jp-cell-editor-background);\n  background-size: 32px 32px;\n}\n\n.dsh-OnboardingGif {\n  position: absolute;\n  visibility: hidden;\n  object-fit: contain;\n  left: 0;\n  top: 0;\n}\n\n.dsh-DashboardToolbar {\n  padding: 2px;\n}\n\n.jp-Toolbar-item.dsh-ToolbarModeSwitcher .jp-select-wrapper.jp-mod-focused {\n  border: none;\n  box-shadow: none;\n}\n\nselect.dsh-ToolbarSelector.jp-mod-styled {\n  height: 24px;\n  font-size: var(--jp-ui-font-size1);\n  line-height: 14px;\n  border-radius: 0;\n  display: block;\n  box-shadow: none;\n  border: none;\n}\n\n.dsh-ToolbarSelector.jp-mod-styled select {\n  height: 24px;\n  font-size: var(--jp-ui-font-size1);\n  line-height: 14px;\n  border-radius: 0;\n  display: block;\n  box-shadow: none;\n  border: none;\n}\n\n.dsh-DragImage {\n  box-shadow: var(--jp-elevation-z1);\n  outline: var(--jp-border-width) solid var(--jp-brand-color1);\n  outline-offset: calc(-1 * var(--jp-border-width));\n}\n", "",{"version":3,"sources":["webpack://./style/base.css"],"names":[],"mappings":"AAAA;IACI,cAAc;EAChB;;AAEF;EACE,oBAAoB;AACtB;;AAEA;EACE,qBAAqB;AACvB;;AAEA;EACE,qEAAqE;EACrE,iDAAiD;EACjD,mCAAmC;EACnC,iBAAiB;EACjB,wBAAwB;AAC1B;;AAEA;EACE,oBAAoB;AACtB;;AAEA;EACE,4DAA4D;EAC5D,iDAAiD;AACnD;;AAEA;EACE,4DAA4D;EAC5D,iDAAiD;EACjD,YAAY;AACd;;AAEA;EACE,cAAc;AAChB;;AAEA;EACE,aAAa;EACb,UAAU;EACV,WAAW;EACX,yCAAyC;EACzC,UAAU;EACV,yCAAyC;EACzC,kBAAkB;AACpB;;AAEA;EACE,wCAAwC;AAC1C;;AAEA;EACE,WAAW;EACX,YAAY;EACZ,mBAAmB;AACrB;;AAEA;EACE,UAAU;EACV,YAAY;EACZ,mBAAmB;AACrB;;AAEA;EACE,WAAW;EACX,SAAS;EACT,mBAAmB;AACrB;;AAEA;EACE,UAAU;EACV,SAAS;EACT,mBAAmB;AACrB;;AAEA;EACE;;;GAGC;EACD,gBAAgB;EAChB,oBAAoB;EACpB,mBAAmB;EACnB,uBAAuB;AACzB;;AAEA;EACE,cAAc;AAChB;;AAEA;EACE,oBAAoB;AACtB;;AAEA;EACE;;;;;4EAK0E;EAC1E,kDAAkD;EAClD,0BAA0B;AAC5B;;AAEA;EACE;;;;;4EAK0E;EAC1E,kDAAkD;EAClD,0BAA0B;AAC5B;;AAEA;EACE,kBAAkB;EAClB,kBAAkB;EAClB,mBAAmB;EACnB,OAAO;EACP,MAAM;AACR;;AAEA;EACE,YAAY;AACd;;AAEA;EACE,YAAY;EACZ,gBAAgB;AAClB;;AAEA;EACE,YAAY;EACZ,kCAAkC;EAClC,iBAAiB;EACjB,gBAAgB;EAChB,cAAc;EACd,gBAAgB;EAChB,YAAY;AACd;;AAEA;EACE,YAAY;EACZ,kCAAkC;EAClC,iBAAiB;EACjB,gBAAgB;EAChB,cAAc;EACd,gBAAgB;EAChB,YAAY;AACd;;AAEA;EACE,kCAAkC;EAClC,4DAA4D;EAC5D,iDAAiD;AACnD","sourcesContent":[".dsh-JupyterDashboard {\n    overflow: auto;\n  }\n  \n.dsh-DashboardWidget {\n  display: inline-flex;\n}\n\n.dsh-DashboardWidget .dsh-MarkdownOutput {\n  display: inline-block;\n}\n\n.dsh-EditableWidget {\n  outline: var(--jp-border-width) solid var(--jp-inverse-layout-color4);\n  outline-offset: calc(-1 * var(--jp-border-width));\n  background: var(--jp-layout-color0);\n  overflow: visible;\n  contain: none !important;\n}\n\n.dsh-EditableWidget > .dsh-DashboardWidgetChild {\n  pointer-events: none;\n}\n\n.dsh-EditableWidget:focus {\n  outline: var(--jp-border-width) solid var(--jp-brand-color1);\n  outline-offset: calc(-1 * var(--jp-border-width));\n}\n\n.dsh-EditableWidget:hover {\n  outline: var(--jp-border-width) solid var(--jp-brand-color1);\n  outline-offset: calc(-1 * var(--jp-border-width));\n  cursor: move;\n}\n\n.dsh-DashboardArea {\n  overflow: auto;\n}\n\n.dsh-Resizer {\n  display: none;\n  width: 4px;\n  height: 4px;\n  outline: 1px solid var(--jp-brand-color1);\n  z-index: 3;\n  background-color: var(--jp-layout-color0);\n  position: absolute;\n}\n\n.dsh-Resizer:hover {\n  background-color: var(--jp-brand-color1);\n}\n\n.dsh-ResizerBottomRight {\n  right: -2px;\n  bottom: -2px;\n  cursor: nwse-resize;\n}\n\n.dsh-ResizerBottomLeft {\n  left: -2px;\n  bottom: -2px;\n  cursor: nesw-resize;\n}\n\n.dsh-ResizerTopRight {\n  right: -2px;\n  top: -2px;\n  cursor: nesw-resize;\n}\n\n.dsh-ResizerTopLeft {\n  left: -2px;\n  top: -2px;\n  cursor: nwse-resize;\n}\n\n.dsh-DashboardWidgetChild {\n  /*\n  width: 100%;\n  height: 100%;\n  */\n  overflow: hidden;\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n}\n\n.dsh-EditableWidget:focus .dsh-Resizer {\n  display: block;\n}\n\n.dsh-Canvas {\n  pointer-events: none;\n}\n\n.dsh-Canvas.dsh-FreeLayout {\n  background-image: linear-gradient(\n      to right,\n      var(--jp-border-color2) 1px,\n      transparent 1px\n    ),\n    linear-gradient(to bottom, var(--jp-border-color2) 1px, transparent 1px);\n  background-color: var(--jp-cell-editor-background);\n  background-size: 10px 10px;\n}\n\n.dsh-Canvas.dsh-TiledLayout {\n  background-image: linear-gradient(\n      to right,\n      var(--jp-border-color2) 1px,\n      transparent 1px\n    ),\n    linear-gradient(to bottom, var(--jp-border-color2) 1px, transparent 1px);\n  background-color: var(--jp-cell-editor-background);\n  background-size: 32px 32px;\n}\n\n.dsh-OnboardingGif {\n  position: absolute;\n  visibility: hidden;\n  object-fit: contain;\n  left: 0;\n  top: 0;\n}\n\n.dsh-DashboardToolbar {\n  padding: 2px;\n}\n\n.jp-Toolbar-item.dsh-ToolbarModeSwitcher .jp-select-wrapper.jp-mod-focused {\n  border: none;\n  box-shadow: none;\n}\n\nselect.dsh-ToolbarSelector.jp-mod-styled {\n  height: 24px;\n  font-size: var(--jp-ui-font-size1);\n  line-height: 14px;\n  border-radius: 0;\n  display: block;\n  box-shadow: none;\n  border: none;\n}\n\n.dsh-ToolbarSelector.jp-mod-styled select {\n  height: 24px;\n  font-size: var(--jp-ui-font-size1);\n  line-height: 14px;\n  border-radius: 0;\n  display: block;\n  box-shadow: none;\n  border: none;\n}\n\n.dsh-DragImage {\n  box-shadow: var(--jp-elevation-z1);\n  outline: var(--jp-border-width) solid var(--jp-brand-color1);\n  outline-offset: calc(-1 * var(--jp-border-width));\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./style/index.js":
/*!************************!*\
  !*** ./style/index.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _base_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./base.css */ "./style/base.css");



/***/ }),

/***/ "./style/base.css":
/*!************************!*\
  !*** ./style/base.css ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../../../../../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "../../../../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../../../../../../node_modules/css-loader/dist/cjs.js!./base.css */ "../../../../../node_modules/css-loader/dist/cjs.js!./style/base.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ })

}]);
//# sourceMappingURL=style_index_js.637344595cf734495033.js.map