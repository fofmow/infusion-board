/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/scripts/components/menu.js":
/*!****************************************!*\
  !*** ./src/scripts/components/menu.js ***!
  \****************************************/
/***/ (() => {

const mapRoot = document.getElementById('js-root');
console.log('1212312')
const map = document.createElement('div');
const mapTitle = document.createElement('h2');
const mapStateBox = document.createElement('div');
const mapStateBoxScoreLeft = document.createElement('span');
const mapStateBoxScoreRight = document.createElement('span');
const mapMolBox = document.createElement('div');
const mapMolTextBox = document.createElement('div');
const mapMolImg = document.createElement('img');
const mapRoad = document.createElement('div');
const mapRoadStage1 = document.createElement('div');
const mapRoadStage2 = document.createElement('div');
const mapRoadStage3 = document.createElement('div');
const mapRoadStage4 = document.createElement('div');
const mapRoadStage1Point = document.createElement('img');
const mapRoadStage2Point = document.createElement('img');
const mapRoadStage3Point = document.createElement('img');
const mapRoadStage4Point = document.createElement('img');
const mapRoadStage1TextBox = document.createElement('div');
const mapRoadStage2TextBox = document.createElement('div');
const mapRoadStage3TextBox = document.createElement('div');
const mapRoadStage4TextBox = document.createElement('div');
const mapRoadStage1TextTitle = document.createElement('h3');
const mapRoadStage2TextTitle = document.createElement('h3');
const mapRoadStage3TextTitle = document.createElement('h3');
const mapRoadStage4TextTitle = document.createElement('h3');
const mapRoadStage1TextDescr = document.createElement('span');
const mapRoadStage2TextDescr = document.createElement('span');
const mapRoadStage3TextDescr = document.createElement('span');
const mapRoadStage4TextDescr = document.createElement('span');
const mapRoadStage1TextScore = document.createElement('span');
const mapRoadStage2TextScore = document.createElement('span');
const mapRoadStage3TextScore = document.createElement('span');
const mapRoadStage4TextScore = document.createElement('span');
const mapMood = document.createElement('div');
const mapMoodTitle = document.createElement('h3');
const mapMoodCircleList = document.createElement('div');
const mapMoodCircleItem = document.createElement('div');
const mapNextLesson = document.createElement('button');

mapRoot.append(map)
map.append(mapTitle)
map.append(mapStateBox)
mapStateBox.append(mapTitle)
mapStateBox.append(mapStateBoxScoreLeft)
mapStateBox.append(mapStateBoxScoreLeft)
map.append(mapMolBox)
mapMolBox.append(mapMolTextBox)
mapMolBox.append(mapMolImg)









































































/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be in strict mode.
(() => {
"use strict";
/*!*****************************!*\
  !*** ./src/scripts/main.js ***!
  \*****************************/
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _components_menu__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./components/menu */ "./src/scripts/components/menu.js");
/* harmony import */ var _components_menu__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_components_menu__WEBPACK_IMPORTED_MODULE_0__);


})();

/******/ })()
;
//# sourceMappingURL=main.js.map