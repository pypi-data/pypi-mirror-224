"use strict";
(self["webpackChunk_deshaw_jupyterlab_pyflyby"] = self["webpackChunk_deshaw_jupyterlab_pyflyby"] || []).push([["lib_index_js"],{

/***/ "./style/tidy-import.svg":
/*!*******************************!*\
  !*** ./style/tidy-import.svg ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 512 512\"><!-- Font Awesome Pro 5.15.4 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) --><path d=\"M224 96l16-32 32-16-32-16-16-32-16 32-32 16 32 16 16 32zM80 160l26.66-53.33L160 80l-53.34-26.67L80 0 53.34 53.33 0 80l53.34 26.67L80 160zm352 128l-26.66 53.33L352 368l53.34 26.67L432 448l26.66-53.33L512 368l-53.34-26.67L432 288zm70.62-193.77L417.77 9.38C411.53 3.12 403.34 0 395.15 0c-8.19 0-16.38 3.12-22.63 9.38L9.38 372.52c-12.5 12.5-12.5 32.76 0 45.25l84.85 84.85c6.25 6.25 14.44 9.37 22.62 9.37 8.19 0 16.38-3.12 22.63-9.37l363.14-363.15c12.5-12.48 12.5-32.75 0-45.24zM359.45 203.46l-50.91-50.91 86.6-86.6 50.91 50.91-86.6 86.6z\"/></svg>");

/***/ }),

/***/ "./lib/cellUtils.js":
/*!**************************!*\
  !*** ./lib/cellUtils.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   couldBeCode: () => (/* binding */ couldBeCode),
/* harmony export */   couldBeImportStatement: () => (/* binding */ couldBeImportStatement),
/* harmony export */   findCell: () => (/* binding */ findCell),
/* harmony export */   findLinePos: () => (/* binding */ findLinePos),
/* harmony export */   normalizeMultilineString: () => (/* binding */ normalizeMultilineString),
/* harmony export */   safeToinsertImport: () => (/* binding */ safeToinsertImport)
/* harmony export */ });
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _constants__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./constants */ "./lib/constants.js");


// FIXME: There's got to be a better Typescript solution
// for distinguishing between members of a union type at runtime.
const normalizeMultilineString = (source) => {
    // Multilinestring can be an array of strings or string
    return typeof source === 'string' ? source.split('\n') : source;
};
/**
 * Very hacky code snippets to check if a line could be a code statement.
 * This could go wrong in a lot of ways and will just work in the
 * most common use cases.
 *
 * Expected to return true for import and code blocks
 */
const couldBeCode = (line) => {
    return (!(line.startsWith('#') ||
        line.startsWith('"""') ||
        line.trim() === '' ||
        line.match(/^\s.*$/)) || line.startsWith('%'));
};
const couldBeImportStatement = (line) => {
    return (couldBeCode(line) &&
        (line.includes('__future__') ||
            line.split(' ').indexOf('import') !== -1 ||
            line.includes('import_all_names')));
};
/**
 * It is safe to insert import only if current line is empty or doesn't start with a whitespace
 * */
const safeToinsertImport = (line) => {
    return line.trim() === '' || !line.match(/^\s.*$/);
};
/**
 * Takes in a list of cell models and returns
 * the first *code* cell that
 *
 * - doesn't start with a line or cell magic
 *   (If it is line magic, should we inspect the following block of code?)
 * - isn't all import blocks and comments.
 *
 * @param cellModels - an array of cell models
 */
const findCell = (cellModels) => {
    const cellsArray = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.toArray)(cellModels);
    for (let i = 0; i < cellsArray.length; i++) {
        const cellModel = cellsArray[i];
        if (cellModel.type === 'code') {
            const lines = normalizeMultilineString(cellModel.toJSON().source);
            // FIXME: Deal with line magics better.
            if (lines.length > 0 &&
                !lines[0].startsWith('%') &&
                !lines[0].startsWith('"""')) {
                for (let j = 0; j < lines.length; j++) {
                    if (couldBeCode(lines[j])) {
                        return i;
                    }
                }
            }
        }
    }
    return -1;
};
/**
 * Find the last import in a cell and return the position after that.
 *
 * If no imports exist, but code does, return 0.
 *
 * Else, it is likely an empty cell or a comment cell. Return -1.
 *
 * If we decide to reformat on each import, we can change this to
 * insert at the end of any code cell and just
 *
 * @param cell - a cell model
 */
const findLinePos = (cell) => {
    const lines = normalizeMultilineString(cell.toJSON().source);
    for (let i = lines.length - 1; i >= 0; i--) {
        // If PYFLYBY_END_MSG is found, add new import statement above it
        if (lines[i] === _constants__WEBPACK_IMPORTED_MODULE_1__.PYFLYBY_END_MSG.substr(0, _constants__WEBPACK_IMPORTED_MODULE_1__.PYFLYBY_END_MSG.length - 1)) {
            let pos = 0;
            for (let j = 0; j < i - 1; j++) {
                pos += lines[j].length + 1;
            }
            return pos;
        }
    }
    for (let i = lines.length - 1; i >= 0; i--) {
        if (couldBeImportStatement(lines[i]) &&
            (i === lines.length - 1 || safeToinsertImport(lines[i + 1]))) {
            let pos = 0;
            for (let j = 0; j <= i; j++) {
                pos += lines[j].length + 1;
            }
            return pos;
        }
    }
    // Cell contains only comments or magics, so return -1.
    // These imports will be moved to next cell
    return -1;
};


/***/ }),

/***/ "./lib/constants.js":
/*!**************************!*\
  !*** ./lib/constants.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   PYFLYBY_CELL_TAG: () => (/* binding */ PYFLYBY_CELL_TAG),
/* harmony export */   PYFLYBY_COMMS: () => (/* binding */ PYFLYBY_COMMS),
/* harmony export */   PYFLYBY_END_MSG: () => (/* binding */ PYFLYBY_END_MSG),
/* harmony export */   PYFLYBY_START_MSG: () => (/* binding */ PYFLYBY_START_MSG)
/* harmony export */ });
/** Constants */
const PYFLYBY_CELL_TAG = 'pyflyby-cell';
const PYFLYBY_START_MSG = '# THIS CELL WAS AUTO-GENERATED BY PYFLYBY\n';
const PYFLYBY_END_MSG = '# END AUTO-GENERATED BLOCK\n';
const PYFLYBY_COMMS = {
    MISSING_IMPORTS: 'pyflyby.missing_imports',
    FORMAT_IMPORTS: 'pyflyby.format_imports',
    INIT: 'pyflyby.init_comms',
    TIDY_IMPORTS: 'pyflyby.tidy_imports'
};


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'pyflyby', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _style_tidy_import_svg__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../style/tidy-import.svg */ "./style/tidy-import.svg");
/* harmony import */ var debug__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! debug */ "webpack/sharing/consume/default/debug/debug");
/* harmony import */ var debug__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(debug__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _cellUtils__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./cellUtils */ "./lib/cellUtils.js");
/* harmony import */ var _constants__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./constants */ "./lib/constants.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/**
 * Basic workflow -
 * 1. Connects to comms created by pyflyby
 * 2. Recieves imports added by pyflyby via PYFLYBY_COMMS.MISSING_IMPORTS
 * 3. Sends import statements recived in previous step to kernel for formatting using tidy_imports
 * 4. Recieves formatted imports via PYFLYBY_COMMS.FORMAT_IMPORTS which are added at suitable location in notebook
 *
 * Selecting cell where imports are added -
 * 1. First cell with 'pyflyby-cell' tag, if not  present then next step.
 * 2. First code cell which does not contain magic command
 * 3. If selected cell doesn't contain any import statement, add a new cell above the code cell.
 *
 * Selecting insert location inside the cell -
 * 1. If PYFLYBY_END_MSG is present, import is added above it.
 * 2. Added import after last import statement in code cell. Identifying import statement is
 *    is done by simple heuristics. This step can be shifted to pyflyby where python parser can be used to
 *    determine it accurately.
 */
// Lumino imports









// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore



// relative imports



const log = (0,debug__WEBPACK_IMPORTED_MODULE_9__.debug)('PYFLYBY:');
class CommLock {
    constructor(_lockTimeout, sessionContext) {
        this._lockTimeout = _lockTimeout;
        this._activeTimeout = null;
        this.requestedLockCount = 0;
        this.clearedLockCount = 0;
        this._releaseLock = {};
        this.promise = { 0: Promise.resolve() };
        this._timeoutSignal = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__.Signal(this);
        this._sessionContext = sessionContext;
        this._sessionContext.statusChanged.connect(this.kernelStateRecorder, this);
        this._timeoutSignal.connect(this.timeoutExpireHandler, this);
    }
    kernelStateRecorder(sender, args) {
        this._recentKernelState = args;
    }
    _clearTimeout() {
        window.clearTimeout(this._activeTimeout);
        this._activeTimeout = null;
    }
    /*
      If the kernel was busy the last time, we assume it was busy executing
      code and we restart the timeout.
    */
    timeoutExpireHandler(sender, id) {
        this._clearTimeout();
        if (this._recentKernelState === 'busy') {
            console.debug('Extending Timeout For: ', id);
            this.createTimeout(id);
        }
        else {
            this.release(id);
        }
    }
    async acquire() {
        const lastLockPromise = this.promise[this.requestedLockCount];
        this.requestedLockCount++;
        const lockId = this.requestedLockCount;
        this.promise[lockId] = new Promise(resolve => {
            this._releaseLock[lockId] = resolve;
        });
        await lastLockPromise;
        return new Promise((res, rej) => res(lockId));
    }
    release(lockId) {
        var _a, _b;
        this.clearedLockCount = lockId;
        (_b = (_a = this._releaseLock)[lockId]) === null || _b === void 0 ? void 0 : _b.call(_a);
        delete this._releaseLock[lockId];
        this._clearTimeout();
        if (this.clearedLockCount < this.requestedLockCount) {
            this.createTimeout(lockId + 1);
        }
    }
    createTimeout(id) {
        this._activeTimeout = setTimeout(() => {
            this._timeoutSignal.emit(id);
        }, this._lockTimeout);
    }
}
// We'd like to show the notification only once per session, not for each notebook
let _userWasNotified = false;
/**
 * An extension that adds pyflyby integration to a single notebook widget
 */
class PyflyByWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget {
    constructor(context, panel, settingRegistry) {
        super();
        this._context = null;
        this._sessionContext = null;
        this._settings = null;
        this._comms = {};
        // get a reference to the settings registry
        settingRegistry.load('@deshaw/jupyterlab-pyflyby:plugin').then((settings) => {
            this._settings = settings;
            const enabled = settings.get('enabled').user || settings.get('enabled').composite;
            if (enabled) {
                this._sessionContext.kernelChanged.connect(this._handleKernelChange, this);
                this._sessionContext.statusChanged.connect(this._handleKernelStatusChange, this);
            }
            const _lockTimeout = 1000 *
                (settings.get('lockTimeout').user ||
                    settings.get('lockTimeout').composite);
            this._lock = new CommLock(_lockTimeout, this._sessionContext);
        }, (err) => {
            log('PYFLYBY extension has been disabled');
        });
        this._context = context;
        this._sessionContext = context.sessionContext;
    }
    async _launchDialog(imports) {
        /**
         * Since we are making the first import, create a new dialog
         */
        const dialog = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Dialog({
            title: 'PYFLYBY',
            body: `PYFLYBY will be adding imports to the first code cell in the notebook.
            To disable the PYFLYBY extension or to disable this notification in future, go
            to Settings -> Advanced Settings Editor and choose PYFLYBY preferences tab`,
            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Dialog.okButton()]
        });
        try {
            await dialog.launch();
            return imports;
        }
        catch (e) {
            console.error(e);
        }
    }
    /**
     * All the logic related to finding the right cell
     */
    _findAndSetImportCoordinates() {
        const { model } = this._context;
        let pyflybyCellIndex = _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.ArrayExt.findFirstIndex((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.toArray)(model.cells), (cell, index) => {
            const tags = cell.metadata.get('tags');
            return !!(tags && tags.indexOf(_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_CELL_TAG) !== -1);
        });
        /**
         * Since the cell doesn't exist, we make one or, if the first
         * code cell contains an import block, put it below that.
         */
        if (pyflybyCellIndex === -1) {
            pyflybyCellIndex = (0,_cellUtils__WEBPACK_IMPORTED_MODULE_11__.findCell)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.toArray)(model.cells));
        }
        let cell = model.cells.get(pyflybyCellIndex);
        let position = (0,_cellUtils__WEBPACK_IMPORTED_MODULE_11__.findLinePos)(model.cells.get(pyflybyCellIndex));
        if (position === -1) {
            cell = this._context.model.contentFactory.createCodeCell({
                cell: {
                    source: `${_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_START_MSG}\n\n${_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_END_MSG}`,
                    cell_type: 'code',
                    metadata: {}
                }
            });
            this._context.model.cells.insert(pyflybyCellIndex, cell);
            position = _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_START_MSG.length + 1;
        }
        cell.metadata.set('tags', [_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_CELL_TAG]);
        return { cellIndex: pyflybyCellIndex, position };
    }
    /**
     * Adds the import block to the appropriate cell at the appropriate
     * location.
     *
     * @param importBlock - the import statement or block of import statements
     */
    _insertImport(imports) {
        let p = null;
        if (!_userWasNotified && !this._settings.get('disableNotification').user) {
            p = this._launchDialog(imports);
            _userWasNotified = true;
        }
        else {
            p = Promise.resolve(imports);
        }
        // creates the cell for imports
        this._findAndSetImportCoordinates();
        return p;
    }
    _sendFormatCodeMsg(imports, lockId) {
        const pyflybyCellIndex = _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.ArrayExt.findFirstIndex((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.toArray)(this._context.model.cells), (cell, index) => {
            const tags = cell.metadata.get('tags');
            return !!(tags && tags.indexOf(_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_CELL_TAG) !== -1);
        });
        if (pyflybyCellIndex !== -1) {
            const cellSource = this._context.model.cells
                .get(pyflybyCellIndex)
                .toJSON().source;
            const comm = this._comms[_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.FORMAT_IMPORTS];
            if (comm && !comm.isDisposed) {
                comm.send({
                    msg_id: lockId,
                    input_code: cellSource,
                    imports: imports,
                    type: _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.FORMAT_IMPORTS
                });
            }
        }
    }
    async sendTidyImportRequest() {
        const cellArray = this._getCellArray();
        const comm = this._comms[_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.TIDY_IMPORTS];
        if (comm && !comm.isDisposed) {
            comm.send({
                type: _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.TIDY_IMPORTS,
                cellArray: cellArray,
                checksum: this._getHashOfCodeInNotebook()
            });
        }
    }
    _getCellArray() {
        const cells = this._context.model.cells;
        const cellArray = [];
        for (let i = 0; i < cells.length; ++i) {
            cellArray.push({
                text: cells.get(i).value.text,
                type: cells.get(i).type
            });
        }
        return cellArray;
    }
    restoreNotebookAfterTidyImports(cellArray, imports) {
        const { cellIndex } = this._findAndSetImportCoordinates();
        const cells = this._context.model.cells;
        for (let i = 0; i < cellArray.length; ++i) {
            const cell = cells.get(i);
            cell.value.remove(0, cell.value.text.length);
            cell.value.insert(0, cellArray[i].text.trim());
        }
        const joined_imports = imports.join('\n').trim();
        if (cells.get(0).value.text.length === 0) {
            cells.get(0).value.insert(0, joined_imports);
        }
        else {
            const cell = this._context.model.contentFactory.createCodeCell({
                cell: {
                    source: joined_imports,
                    cell_type: 'code',
                    metadata: {
                        trusted: true
                    }
                }
            });
            cells.insert(cellIndex, cell);
        }
    }
    _fastStringHash(str) {
        let hash = 0;
        for (let i = 0, len = str.length; i < len; i++) {
            const chr = str.charCodeAt(i);
            hash = (hash << 5) - hash + chr;
            hash |= 0; // Convert to 32bit integer
        }
        return hash;
    }
    _getHashOfCodeInNotebook() {
        const cellArray = this._getCellArray();
        let joinedText = '';
        for (let i = 0; i < cellArray.length; ++i) {
            joinedText = joinedText + cellArray[i].text;
        }
        return this._fastStringHash(joinedText);
    }
    _getCommMsgHandler() {
        return async (msg) => {
            const msgContent = msg.content.data;
            switch (msgContent.type) {
                case _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.MISSING_IMPORTS: {
                    const itd = msgContent['missing_imports'];
                    this._insertImport(itd).then(async (imports) => {
                        // Acquire new lock but wait for previous lock to expire
                        const currentLockId = await this._lock.acquire();
                        this._sendFormatCodeMsg(imports, currentLockId);
                    });
                    break;
                }
                case _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.FORMAT_IMPORTS: {
                    this._formatImports(msgContent);
                    const { msg_id: lockId } = msgContent;
                    this._lock.release(lockId);
                    break;
                }
                case _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.INIT: {
                    this._initializeComms().catch(console.error);
                    break;
                }
                case _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.TIDY_IMPORTS: {
                    const { cells, imports, checksum } = msgContent;
                    if (checksum === this._getHashOfCodeInNotebook()) {
                        this.restoreNotebookAfterTidyImports(cells, imports);
                    }
                    else {
                        await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.showDialog)({
                            title: 'TidyImports Interrupted',
                            body: 'TidyImports could not be run because code in the notebook has been changed',
                            buttons: [
                                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Dialog.okButton({
                                    label: 'Ok'
                                })
                            ],
                            defaultButton: 0
                        });
                    }
                    break;
                }
                default:
                    break;
            }
        };
    }
    async _initializeComms() {
        if (!this._sessionContext.session) {
            return;
        }
        const { kernel } = this._sessionContext.session;
        if (!kernel) {
            return;
        }
        // Open the comm
        const targetName = _constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.MISSING_IMPORTS;
        const comm = kernel.createComm(targetName);
        comm.onMsg = this._getCommMsgHandler();
        try {
            comm.open();
        }
        catch (e) {
            console.error(`Unable to open PYFLYBY comm - ${e}`);
        }
        const formatMsgComm = kernel.createComm(_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.FORMAT_IMPORTS);
        formatMsgComm.onMsg = this._getCommMsgHandler();
        formatMsgComm.onClose = (msg) => {
            const commId = msg.content.comm_id;
            delete this._comms[commId];
        };
        this._comms[_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.FORMAT_IMPORTS] = formatMsgComm;
        try {
            formatMsgComm.open();
        }
        catch (e) {
            console.error(`Unable to open PYFLYBY comm - ${e}`);
        }
        const tidyImportsComm = kernel.createComm(_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.TIDY_IMPORTS);
        tidyImportsComm.onMsg = this._getCommMsgHandler();
        this._comms[_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.TIDY_IMPORTS] = tidyImportsComm;
        try {
            tidyImportsComm.open();
        }
        catch (e) {
            console.error(`Unable to open PYFLYBY comm - ${e}`);
        }
        kernel.registerCommTarget(_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_COMMS.INIT, (comm, msg) => {
            comm.onMsg = this._getCommMsgHandler();
        });
        return Promise.resolve();
    }
    _formatImports(msgData) {
        const { formatted_code: formattedCode } = msgData;
        const pyflybyCellIndex = _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.ArrayExt.findFirstIndex((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.toArray)(this._context.model.cells), (cell, index) => {
            const tags = cell.metadata.get('tags');
            return !!(tags && tags.indexOf(_constants__WEBPACK_IMPORTED_MODULE_12__.PYFLYBY_CELL_TAG) !== -1);
        });
        if (pyflybyCellIndex !== -1) {
            const cell = this._context.model.cells.get(pyflybyCellIndex);
            cell.value.remove(0, cell.value.text.length);
            cell.value.insert(0, formattedCode);
        }
    }
    async _handleKernelChange(sender, kernelChangedArgs) {
        return await this._initializeComms();
    }
    _handleKernelStatusChange(sender, args) {
        if (args === 'restarting') {
            return this._initializeComms();
        }
        return null;
    }
}
/**
 * An extension that adds pyflyby integration to a notebook widget
 */
class PyflyByWidgetExtension {
    constructor(settingRegistry) {
        this._settingRegistry = null;
        // get a reference to the settings registry
        // This is shared between all notebooks. I.e. not possible to
        // have different pyflyby settings for different notebooks
        this._settingRegistry = settingRegistry;
        this._loadSettings().catch(console.error);
    }
    async _loadSettings() {
        try {
            await this._settingRegistry.load('@deshaw/jupyterlab-pyflyby:plugin');
            log('Successfully loaded PYFLYBY extension settings');
        }
        catch (e) {
            console.error('Settings could not be loaded');
        }
    }
    createNew(panel, context) {
        pyflybyWidget = new PyflyByWidget(context, panel, this._settingRegistry);
        return pyflybyWidget;
    }
}
async function isPyflybyInstalled() {
    const pyflybyStatus = await (0,_handler__WEBPACK_IMPORTED_MODULE_13__.requestAPI)('pyflyby-status');
    return pyflybyStatus.status;
}
async function installPyflyby() {
    try {
        await (0,_handler__WEBPACK_IMPORTED_MODULE_13__.requestAPI)('install-pyflyby', { method: 'POST' });
    }
    catch (err) {
        const errMsg = await err.json();
        console.error(errMsg.result);
    }
}
async function disableJupyterlabPyflyby(registry) {
    try {
        await (0,_handler__WEBPACK_IMPORTED_MODULE_13__.requestAPI)('disable-pyflyby', {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'include',
            headers: { 'Content-type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams('installDialogDisplayed=true')
        });
    }
    catch (err) {
        const errMsg = await err.json();
        console.error(errMsg.result);
    }
    await registry.reload('@deshaw/jupyterlab-pyflyby:plugin');
}
const installationBody = (react__WEBPACK_IMPORTED_MODULE_10___default().createElement("div", null,
    react__WEBPACK_IMPORTED_MODULE_10___default().createElement("p", null,
        "To use @deshaw/jupyterlab-pyflyby,",
        ' ',
        react__WEBPACK_IMPORTED_MODULE_10___default().createElement("a", { href: "https://github.com/deshaw/pyflyby/blob/master/README.rst", style: { color: '#0000EE' }, target: "_blank", rel: "noopener noreferrer" }, "pyflyby"),
        ' ',
        "ipython extension needs to be installed."),
    react__WEBPACK_IMPORTED_MODULE_10___default().createElement("br", null),
    react__WEBPACK_IMPORTED_MODULE_10___default().createElement("p", null, "Clicking on \"Install\" will run following command"),
    react__WEBPACK_IMPORTED_MODULE_10___default().createElement("div", { style: {
            font: 'monospace',
            color: '#ffffff',
            backgroundColor: '#000000',
            marginTop: '5px'
        } }, "$ py pyflyby.install_in_ipython_config_file"),
    react__WEBPACK_IMPORTED_MODULE_10___default().createElement("br", null)));
class TidyImportButtonExtension {
    createNew(widget, context) {
        const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ToolbarButton({
            className: 'tidy-import-button',
            tooltip: 'Run tidy-imports on this notebook',
            icon: TidyImportsIcon,
            onClick: () => pyflybyWidget.sendTidyImportRequest()
        });
        widget.toolbar.insertItem(10, 'tidy-imports', button);
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_6__.DisposableDelegate(() => {
            button.dispose();
        });
    }
}
const TidyImportsIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.LabIcon({
    name: 'TidyImports',
    svgstr: _style_tidy_import_svg__WEBPACK_IMPORTED_MODULE_8__["default"]
});
let pyflybyWidget = null;
const djsTidyImportsCommand = 'djs:run-tidy-imports';
const extension = {
    id: '@deshaw/jupyterlab-pyflyby:plugin',
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_4__.INotebookTracker, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ICommandPalette],
    activate: async function (app, registry, tracker, palette) {
        console.log('JupyterLab extension @deshaw/jupyterlab-pyflyby is activated!');
        app.commands.addCommand(djsTidyImportsCommand, {
            execute: () => pyflybyWidget.sendTidyImportRequest(),
            icon: TidyImportsIcon,
            label: 'Run tidy-imports on Notebook'
        });
        palette.addItem({
            command: djsTidyImportsCommand,
            category: 'Notebook'
        });
        const settings = await registry.load('@deshaw/jupyterlab-pyflyby:plugin');
        const enabled = settings.get('enabled').user || settings.get('enabled').composite;
        const dialogDisplayedEarlier = settings.get('installDialogDisplayed').user;
        if (enabled) {
            const response = await isPyflybyInstalled();
            if (response !== 'loaded') {
                if (dialogDisplayedEarlier) {
                    // Dialog to install pyflyby ipython extensions was displayed earlier,
                    // install it since user is trying to use pyflyby by manually enabling
                    // jupyterlab-pyflyby
                    await installPyflyby();
                }
                else {
                    const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.showDialog)({
                        title: 'Installation required',
                        body: installationBody,
                        buttons: [
                            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Dialog.okButton({
                                label: 'Install'
                            }),
                            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.Dialog.cancelButton({ label: 'Cancel', displayType: 'default' })
                        ],
                        defaultButton: 0
                    });
                    result.button.accept
                        ? await installPyflyby()
                        : await disableJupyterlabPyflyby(registry);
                }
            }
        }
        app.docRegistry.addWidgetExtension('Notebook', new PyflyByWidgetExtension(registry));
        app.docRegistry.addWidgetExtension('Notebook', new TidyImportButtonExtension());
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.be73e084bd6e8366f0c0.js.map