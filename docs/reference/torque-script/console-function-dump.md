# Console Function Dump

This page is a verbatim dump of every TorqueScript console function exposed by
the *Age of Time* client at runtime, captured by running the engine's
built-in `dumpConsoleFunctions();` from the in-game console.

!!! note "Annotations"
    A handful of entries have been hand-annotated with `//` comments to
    describe what they do or their expected arguments. Anything after a
    `//` on a line is **not** part of the original engine output — it's a
    community note. Console functions without a comment are
    listed exactly as the engine reported them, with no documented
    signature.

!!! tip "Reproducing this dump"
    Open the in-game console (the engine's standard tilde key in older
    Torque builds, or run the executable with the appropriate flag) and
    type:

    ```
    dumpConsoleFunctions();
    ```

    The engine will print the same listing shown below.

```torquescript
==>dumpConsoleFunctions();
namespace Global {
   virtual Script cycleDebugRenderMode() {}
   virtual Script bringUpOptions() {}
   virtual Script dropPlayerAtCamera() {}
   virtual Script dropCameraAtPlayer() {}
   virtual Script stopRecordingDemo() {}
   virtual Script startRecordingDemo() {}
   virtual Script resizeMessageHud() {}
   virtual Script pageMessageHudDown() {}
   virtual Script pageMessageHudUp() {}
   virtual Script toggleCamera() {}
   virtual Script toggleFirstPerson() {}
   virtual Script toggleFreeLook() {}
   virtual Script toggleZoom() {}
   virtual Script setZoomFOV() {}
   virtual Script altTrigger() {}
   virtual Script mouseFire() {}
   virtual Script crouch() {}
   virtual Script jump() {}
   virtual Script pitch() {}
   virtual Script yaw() {}
   virtual Script getMouseAdjustAmount() {}
   virtual Script panDown() {}
   virtual Script panUp() {}
   virtual Script turnRight() {}
   virtual Script turnLeft() {}
   virtual Script movedown() {}
   virtual Script moveup() {}
   virtual Script movebackward() {}
   virtual Script moveforward() {}
   virtual Script moveright() {}
   virtual Script moveleft() {}
   virtual Script setSpeed() {}
   virtual Script showPlayerList() {}
   virtual Script escapeFromGame() {}
   virtual Script ClientCmdSetQuickSlot() {}
   virtual Script BSD_ToggleQuickSlots() {}
   virtual Script BSD_AssignQuickSlot() {}
   virtual Script BSD_PopulateList() {}
   virtual Script clientCmdUpdateInvSOQuantity() {}
   virtual Script listAllDataBlocks() {}
   virtual Script BSD_LoadFavorites() {}
   virtual Script BSD_BuyFavorites() {}
   virtual Script BSD_SaveFavorites() {}
   virtual Script BSD_ClickFav() {}
   virtual Script BSD_SetFavs() {}
   virtual Script BSD_BuyBricks() {}
   virtual Script BSD_showTab() {}
   virtual Script BSD_ClickIcon() {}
   virtual Script BSD_ClickInv() {}
   virtual Script BSD_CancelCombine() {}
   virtual Script BSD_FinalCombine() {}
   virtual Script BSD_UpdateCombine() {}
   virtual Script BSD_Combine() {}
   virtual Script BSD_Discard() {}
   virtual Script BSD_PostOfficeSelect() {}
   virtual Script BSD_Use() {}
   virtual Script BSD_ClickClear() {}
   virtual Script BSD_CreateInventoryButtons() {}
   virtual Script BSD_KillInventoryButtons() {}
   virtual Script BSD_CreateBrickButton() {}
   virtual Script BSD_createSubHeadings() {}
   virtual Script BSD_findSubCategory() {}
   virtual Script BSD_findCategory() {}
   virtual Script BSD_addSubCategory() {}
   virtual Script BSD_addCategory() {}
   virtual Script BSD_KillBricks() {}
   virtual Script BSD_DumpCategories() {}
   virtual Script bsd_loadBricks() {}
   virtual Script clientCmdBSD_LoadBricks() {}
   virtual Script clientCmdBSD_Open() {}
   virtual Script clientCmdWriteParchment() {}
   virtual Script PG_Append() {}
   virtual Script clientCmdAddParchmentText() {}
   virtual Script clientCmdOpenParchment() {}
   virtual Script clientCmdPasswordChanged() {}
   virtual Script CPG_Submit() {}
   virtual Script AU_RunPatch() {}
   virtual Script getTimeString() {}
   virtual Script roundMegs() {}
   virtual Script AU_GetUpdate() {}
   virtual Script AU_start() {}
   virtual Script clientCmdDoUpdates() {}
   virtual Script clientCmdSaleSuccess() {}
   virtual Script SG_Send() {}
   virtual Script SG_SelectItem() {}
   virtual Script clientCmdOpenSaleGui() {}
   virtual Script clientCmdMailSuccess() {}
   virtual Script POG_Send() {}
   virtual Script POG_SelectItem() {}
   virtual Script clientCmdOpenPostOfficeGui() {}
   virtual Script craftDownload_GetFile() {}
   virtual Script clientCmdCraftingSuccess() {}
   virtual Script Craft_Create() {}
   virtual Script Craft_SelectItem() {}
   virtual Script Craft_Update() {}
   virtual Script Craft_Open() {}
   virtual Script Craft_OpenFile() {}
   virtual Script Craft_DownloadMenu() {}
   virtual Script clientCmdOpenCraftMenu() {}
   virtual Script Bank_Process() {}
   virtual Script clientCmdSetBank() {}
   virtual Script clientCmdOpenBankGui() {}
   virtual Script ClientCmdSetExp() {}
   virtual Script ClientCmdSetStatus() {}
   virtual Script ClientCmdSetPermStatus() {}
   virtual Script SG_UpdateBar() {}
   virtual Script clientCmdSetAbilities() {}
   virtual Script clientCmdSetLevelingVars() {}
   virtual Script crap() {}
   virtual Script clientCmdRespawnArenaDlg() {}
   virtual Script clientCmdRespawnDlg() {}
   virtual Script clientCmdWarningBox() {}
   virtual Script clientCmdBuyConfirm() {}
   virtual Script clientCmdLoginSuccess() {}
   virtual Script clientCmdStartLogin() {}
   virtual Script clientCmdclearBottomPrint() {}
   virtual Script clientCmdClearCenterPrint() {}
   virtual Script clientCmdBottomPrint() {}
   virtual Script clientCmdCenterPrint() {}
   virtual Script clientCmdBlackOut() {}
   virtual Script clientCmdEnableCompass() {}
   virtual Script clientCmdDisableCompass() {}
   virtual Script clientCmdSetGold() {}
   virtual Script refreshCenterTextCtrl() {}
   virtual Script refreshBottomTextCtrl() {}
   virtual Script localMessageHud() {}
   virtual Script toggleMessageHud() {}
   virtual Script cycleMessageHudSize() {}
   virtual Script pageDownMessageHud() {}
   virtual Script pageUpMessageHud() {}
   virtual Script onServerMessage() {}
   virtual Script onChatMessage() {}
   virtual Script playMessageSound() {}
   virtual Script SetGraphicDetail() {}
   virtual Script SetConnectionType() {}
   virtual Script quickSlot10() {}
   virtual Script quickSlot9() {}
   virtual Script quickSlot8() {}
   virtual Script quickSlot7() {}
   virtual Script quickSlot6() {}
   virtual Script quickSlot5() {}
   virtual Script quickSlot4() {}
   virtual Script quickSlot3() {}
   virtual Script quickSlot2() {}
   virtual Script quickSlot1() {}
   virtual Script useQuickSlot() {}
   virtual Script decVar() {}
   virtual Script incVar() {}
   virtual Script openVoiceMenu() {}
   virtual Script openAdminWindow() {}
   virtual Script Walk() {}
   virtual Script autoWalk() {}
   virtual Script Suicide() {}
   virtual Script stopAction() {}
   virtual Script Action() {}
   virtual Script openStatus() {}
   virtual Script openInventory() {}
   virtual Script OptAudioUpdateChannelVolume() {}
   virtual Script OptAudioUpdateMasterVolume() {}
   virtual Script OptAudioUpdate() {}
   virtual Script findRemapCmdIndex() {}
   virtual Script redoMapping() {}
   virtual Script buildFullMapString() {}
   virtual Script getMapDisplayName() {}
   virtual Script restoreDefaultMappings() {}
   virtual Script UpdateRateToServer() {}
   virtual Script UpdateRateToClient() {}
   virtual Script UpdateLagThreshold() {}
   virtual Script UpdatePacketSize() {}
   virtual Script disconnectedCleanup() {}
   virtual Script disconnect() {}
   virtual Script handleConnectionErrorMessage() {}
   virtual Script handleLoadInfoDoneMessage() {}
   virtual Script handleLoadDescriptionMessage() {}
   virtual Script handleLoadInfoMessage() {}
   virtual Script onMissionDownloadComplete() {}
   virtual Script onPhase3Complete() {}
   virtual Script onPhase3Progress() {}
   virtual Script onMissionDownloadPhase3() {}
   virtual Script onFileChunkReceived() {}
   virtual Script onPhase2Complete() {}
   virtual Script onPhase2Progress() {}
   virtual Script onMissionDownloadPhase2() {}
   virtual Script onPhase1Complete() {}
   virtual Script onPhase1Progress() {}
   virtual Script onMissionDownloadPhase1() {}
   virtual Script clientCmdGameEnd() {}
   virtual Script clientCmdGameStart() {}
   virtual Script clientCmdSyncClock() {}
   virtual Script SADSetPassword() {}
   virtual Script SAD() {}
   virtual Script clientCmdAddDialogOption() {}
   virtual Script clientCmdCloseDialog() {}
   virtual Script clientCmdOpenDialog() {}
   virtual Script JS_sortNumList() {}
   virtual Script JS_sortList() {}
   virtual Script onServerQueryStatus() {}
   virtual Script MJ_connect() {}
   virtual Script clientCmdUpdateInvSlotQuantity() {}
   virtual Script clientCmdClearInventory() {}
   virtual Script clientCmdUpdateInvSlot() {}
   virtual Script clientCmdClearInvSlot() {}
   virtual Script clientCmdSetUnEquipped() {}
   virtual Script clientCmdSetEquipped() {}
   virtual Script AddClientInvItem() {}
   virtual Script clientCmdAddInventoryItem() {}
   virtual Script clientCmdSetInventoryItem() {}
   virtual Script invGuiRefreshInUse() {}
   virtual Script loadItemPreviews() {}
   virtual Script clearItemPreviews() {}
   virtual Script testItemPreviews() {}
   virtual Script killItemPreviews() {}
   virtual Script invGuiSetInUse() {}
   virtual Script invGuiSetHilight() {}
   virtual Script clickItemPreview() {}
   virtual Script makeItemPreviews() {}
   virtual Script dumpClientInv() {}
   virtual Script clientCmdConfirmCharacterOverWrite() {}
   virtual Script CCG_PresetTick() {}
   virtual Script CCG_PresetDrainTick() {}
   virtual Script CCG_Preset() {}
   virtual Script CCG_SetAbility() {}
   virtual Script CCG_RefreshAbilities() {}
   virtual Script CCG_SubtractAbility() {}
   virtual Script CCG_AddAbility() {}
   virtual Script CCG_Tab() {}
   virtual Script RandomizeSlider() {}
   virtual Script RandomizeMenu() {}
   virtual Script CC_Random() {}
   virtual Script updateCharacterMenus() {}
   virtual Script updateCharacterSliders() {}
   virtual Script characterCancel() {}
   virtual Script characterDone() {}
   virtual Script decMenu() {}
   virtual Script incMenu() {}
   virtual Script clickNewCharacter() {}
   virtual Script clickLogin() {}
   virtual Script checkStartupDone() {}
   virtual Script loadStartup() {}
   virtual Script MM_Connect() {}
   virtual Script handleClientScoreChanged() {}
   virtual Script handleClientDrop() {}
   virtual Script handleClientJoin() {}
   virtual Script demoPlaybackComplete() {}
   virtual Script stopDemoRecord() {}
   virtual Script startDemoRecord() {}
   virtual Script StartSelectedDemo() {}
   virtual Script contextHelp() {}
   virtual Script getHelp() {}
   virtual Script cursorOn() {}
   virtual Script cursorOff() {}
   virtual Script doScreenShot() {}
   virtual Script stopMovie() {}
   virtual Script movieGrabScreen() {}
   virtual Script recordMovie() {}
   virtual Script formatSessionNumber() {}
   virtual Script formatImageNumber() {}
   virtual Script CloseMessagePopup() {}
   virtual Script MessagePopup() {}
   virtual Script MessageBoxYesNo() {}
   virtual Script MessageBoxOKCancel() {}
   virtual Script MessageBoxOK() {}
   virtual Script MBSetText() {}
   virtual Script MessageCallback() {}
   virtual Script metrics() {}
   virtual Script debugMetricsCallback() {}
   virtual Script audioMetricsCallback() {}
   virtual Script vehicleMetricsCallback() {}
   virtual Script timeMetricsCallback() {}
   virtual Script waterMetricsCallback() {}
   virtual Script textureMetricsCallback() {}
   virtual Script interiorMetricsCallback() {}
   virtual Script videoMetricsCallback() {}
   virtual Script terrainMetricsCallback() {}
   virtual Script fpsMetricsCallback() {}
   virtual Script doSACallback() {}
   virtual Script getSaveFilename() {}
   virtual Script getLoadFilename() {}
   virtual Script fillFileList() {}
   virtual Script Tree() {}
   virtual Script InspectApply() {}
   virtual Script inspect() {}
   virtual Script ToggleConsole() {}
   virtual Script writeOutClasses() {}
   virtual Script writeOutFunctions() {}
   virtual Script sceneLightingComplete() {}
   virtual Script updateLightingProgress() {}
   virtual Script clientCmdMissionStartPhase3() {}
   virtual Script onGhostAlwaysObjectReceived() {}
   virtual Script onGhostAlwaysStarted() {}
   virtual Script clientCmdMissionStartPhase2() {}
   virtual Script onDataBlockObjectReceived() {}
   virtual Script clientCmdMissionStartPhase1() {}
   virtual Script clientCmdMissionEnd() {}``
   virtual Script clientCmdMissionStart() {}
   virtual Script defaultMessageCallback() {}
   virtual Script addMessageCallback() {}
   virtual Script clientCmdServerMessage() {}
   virtual Script clientCmdChatMessage() {}
   virtual Script OpenALShutdown() {}
   virtual Script OpenALInit() {}
   virtual Script resetCanvas() {}
   virtual Script initCanvas() {}
   virtual Script loadMainMenu() {}
   virtual Script initClient() {}
   virtual Script loadMods() {}
   virtual Script initBaseServer() {}
   virtual Script initBaseClient() {}
   virtual Script initCommon() {}
   virtual Script loadDir() {}
   virtual Script displayHelp() {}
   virtual Script parseArgs() {}
   virtual Script onExit() {}
   virtual Script onStart() {}
   virtual Script doEnableDebug() {}
   virtual Script popFront() {}
   virtual Script pushBack() {}
   virtual Script pushFront() {}
   virtual void cls() {}
   virtual string getClipboard() {}
   virtual bool setClipboard() {}
   virtual void dumpConsoleClasses() {}
   virtual void dumpConsoleFunctions() {}
   virtual string ExpandFilename() {}
   virtual int strcmp() {}
   virtual int stricmp() {}
   virtual int strlen() {}
   virtual int strstr() {}
   virtual int strpos() {}
   virtual string ltrim() {}
   virtual string rtrim() {}
   virtual string trim() {}
   virtual string stripChars() {}
   virtual string strlwr() {}
   virtual string strupr() {}
   virtual string strchr() {}
   virtual string strreplace() {}
   virtual string getSubStr() {}
   virtual string getWord() {}
   virtual string getWords() {}
   virtual string setWord() {}
   virtual string removeWord() {}
   virtual int getWordCount() {}
   virtual string getField() {}
   virtual string getFields() {}
   virtual string setField() {}
   virtual string removeField() {}
   virtual int getFieldCount() {}
   virtual string getRecord() {}
   virtual string getRecords() {}
   virtual string setRecord() {}
   virtual string removeRecord() {}
   virtual int getRecordCount() {}
   virtual string firstWord() {}
   virtual string restWords() {}
   virtual string NextToken() {}
   virtual string detag() {}
   virtual string getTag() {}
   virtual void echo() {}
   virtual void warn() {}
   virtual void error() {}
   virtual string expandEscape() {}
   virtual string collapseEscape() {}
   virtual void setLogMode() {}
   virtual void setEchoFileLoads() {}
   virtual void quit() {}
   virtual string call() {} // (string consoleFunction, args..) call torque script function with args
   virtual bool compile() {}
   virtual bool exec() {}
   virtual string eval() {}
   virtual void export() {} // (string searchString [, string fileName [, string append]]) export (dump) global variables matching searchString to file/console
   virtual void deleteVariables() {} // (string pattern) A string pattern that specifies which variables to delete. The pattern can include wildcard characters (*)
   virtual void trace() {}
   virtual string findFirstFile() {} // (string pattern) Returns the first file in the directory system matching the given pattern.
   virtual string findNextFile() {} // (string pattern) Returns the next file matching a search begun in findFirstFile.
   virtual int getFileCount() {} // (string pattern) Returns the number of files in the directory tree that match the given pattern
   virtual int getFileCRC() {}
   virtual int getStringCRC() {}
   virtual void WinExec() {}
   virtual bool isFile() {} // (string filepath) Returns true if file exists otherwise false
   virtual bool isWriteableFileName() {} // (string filepath) check if file path is writeable
   virtual string fileExt() {}
   virtual string fileBase() {}
   virtual string fileName() {}
   virtual string filePath() {}
   virtual void backtrace() {}
   virtual bool isPackage() {}
   virtual void activatePackage() {}
   virtual void deactivatePackage() {}
   virtual int nameToID() {}
   virtual bool isObject() {}
   virtual void cancel() {}
   virtual bool isEventPending() {}
   virtual int schedule() {}
   virtual void deleteDataBlocks() {}
    //-----------------------------------------------------------------------------
    // Function: telnetSetParameters
    // Description:
    // Initializes and opens the telnet console with specified parameters.
    //
    // Parameters:
    // - port: Port to listen on for console connections (0 shuts down listening).
    // - consolePass: Password for read/write access.
    // - listenPass: Password for read access.
    // - remoteEcho (optional): Enable echo back to the client, off by default.
    //
    // Usage:
    // telnetSetParameters( port, consolePass, listenPass [, remoteEcho] );
    //-----------------------------------------------------------------------------
   virtual void telnetSetParameters() {}
    //-----------------------------------------------------------------------------
    // Function: dbgSetParameters
    // Description:
    // Opens a debug server port with specified parameters.
    //
    // Parameters:
    // - port: The port to open for the debug server.
    // - password: The password required for access.
    // - waitForClient (optional): If true, waits for a debug client to connect.
    //
    // Usage:
    // dbgSetParameters( port, password [, waitForClient] );
    //-----------------------------------------------------------------------------
   virtual void dbgSetParameters() {}
    //-----------------------------------------------------------------------------
    // Enables or disables logging for the DNet networking layer.
    //
    // Parameters:
    //     %enable - Set to true to enable logging, false to disable.
    //
    // Usage:
    //     DNetSetLogging(true); // Enables DNet logging
    //     DNetSetLogging(false); // Disables DNet logging
    //-----------------------------------------------------------------------------
   virtual void DNetSetLogging() {}
   virtual void setNPatch() {}
   virtual void toggleNPatch() {}
   virtual void increaseNPatch() {}
   virtual void decreaseNPatch() {}
   virtual int png2jpg() {}
    //-----------------------------------------------------------------------------
    // Function: setOpenGLMipReduction
    // Adjusts the mipmap reduction level for OpenGL textures.
    //
    // Parameters:
    //    n - Mipmap reduction level, ranging from 0 (no reduction, full detail)
    //        to 5 (maximum reduction, least detail).
    //
    // Description:
    //    This function sets the level of mipmap reduction to adjust texture detail
    //    in OpenGL environments. Lower levels retain more texture detail at a distance,
    //    while higher levels reduce texture detail to improve performance. The function
    //    ensures the specified level is within the valid range of 0 to 5.
    //-----------------------------------------------------------------------------
   virtual void setOpenGLMipReduction() {}
    //-----------------------------------------------------------------------------
    // Function: setOpenGLSkyMipReduction
    // Sets the mipmap reduction level for sky textures in OpenGL.
    //
    // Parameters:
    //    level - Mipmap reduction level, ranges from 0 (full quality) to 5 (highest reduction).
    //-----------------------------------------------------------------------------
   virtual void setOpenGLSkyMipReduction() {}
    //-----------------------------------------------------------------------------
    // Function: setOpenGLInteriorMipReduction
    // Adjusts the mipmap reduction level for OpenGL interior textures.
    //
    // Parameters:
    //    level - Mipmap reduction level, between 0 (no reduction) and 5 (max reduction).
    //-----------------------------------------------------------------------------
   virtual void setOpenGLInteriorMipReduction() {}
    //-----------------------------------------------------------------------------
    // Function: setOpenGLTextureCompressionHint
    // Sets the texture compression hint for OpenGL.
    //
    // Parameters:
    //    hint - Can be "GL_DONT_CARE", "GL_FASTEST", or "GL_NICEST".
    //           Determines texture compression trade-offs.
    //-----------------------------------------------------------------------------
   virtual void setOpenGLTextureCompressionHint() {}
    //-----------------------------------------------------------------------------
    // Function: setOpenGLAnisotropy
    // Sets the level of anisotropic filtering for textures.
    //
    // Parameters:
    //    level - Anisotropy level, between 0.0 (off) and the maximum supported value.
    //            Enhances texture quality at steep viewing angles.
    //-----------------------------------------------------------------------------
   virtual void setOpenGLAnisotropy() {}
    //-----------------------------------------------------------------------------
    // Function: clearTextureHolds
    // Clears textures marked for holding without an actual reference count.
    //
    // Description:
    //   This function goes through all textures marked as held and checks if they
    //   have a reference count. If a texture does not have a reference count, it
    //   is freed; otherwise, the holding flag is cleared, allowing the texture to
    //   be freed later. The function returns the number of textures freed.
    //
    // Returns:
    //   The number of textures freed during the operation.
    //-----------------------------------------------------------------------------
   virtual int clearTextureHolds() {}
   virtual bool addMaterialMapping() {}
   virtual int aiConnect() {}
   virtual void setPowerAudioProfiles() {}
   virtual bool screenShot() {} // Take a screenshot. (string file, string format -- format One of JPEG or PNG.)
   virtual void gotoWebPage() {}
   virtual void deactivateDirectInput() {}
   virtual void activateDirectInput() {}
   virtual void purgeResources() {} // Use the purgeResources function to purge all game resources (is called from mission phase loads)
   virtual bool lightScene() {}
   virtual string strToPlayerName() {}
   virtual string stripTrailingSpaces() {}
   virtual void flushTextureCache() {}
   virtual void setDefaultFov() {}
   virtual void setZoomSpeed() {}
   virtual void setFov() {}
   virtual string getControlObjectAltitude() {}
   virtual string getControlObjectSpeed() {}
   virtual void panoramaScreenShot() {}
   virtual string containerFindFirst() {}
   virtual string containerFindNext() {}
   virtual void snapeToggle() {}
   virtual void lockMouse() {}
   virtual bool setNetPort() {}
   virtual bool createCanvas() {}
   virtual void saveJournal() {}
   virtual void playJournal() {}
   virtual void setModPaths() {}
   virtual string getModPaths() {}
   virtual int getVersionNumber() {}
   virtual string getVersionString() {}
   virtual string getCompileTimeString() {}
   virtual string getBuildString() {}
   virtual int getSimTime() {}
   virtual int getRealTime() {}
   virtual void setShadowDetailLevel() {}
   virtual void showShapeLoad() {}
   virtual void showSequenceLoad() {}
   virtual void showSelectSequence() {}
   virtual void showSetDetailSlider() {}
   virtual void showUpdateThreadControl() {}
   virtual void showPlay() {}
   virtual void showStop() {}
   virtual void showSetScale() {}
   virtual void showSetPos() {}
   virtual void showNewThread() {}
   virtual void showDeleteThread() {}
   virtual void showToggleRoot() {}
   virtual void showToggleStick() {}
   virtual void showSetCamera() {}
   virtual void showSetKeyboard() {}
   virtual void showTurnLeft() {}
   virtual void showTurnRight() {}
   virtual void showSetLightDirection() {}
   // clientCmdSyncStartTime(%time)
   // Set %time from 0 to 3599999 (one full daylight cycle = 3,600,000 ms = 1 hr real-time).
   // Sweeps the fxSunLight elevation linearly: elevation = (70 + 360 * %time/3600000), wrapped to (-180, 180].
   // Azimuth tracks non-linearly because the engine derives it via atan2 on the rotating sun vector
   // (see fxSunLight::interpolateTick -> MathUtils::getAnglesFromVector) and discontinuously flips when
   // elevation crosses zenith/nadir.
   //
   // Times of day (assuming this mission's StartElevation=70 and RotationTime=3600s):
   //   %time = 200000   -> elev =  90    NOON     (sun directly overhead, brightest)
   //   %time = 1100000  -> elev = 180    SUNSET   (sun at horizon, descending)
   //   %time = 2000000  -> elev = -90    MIDNIGHT (sun directly below, darkest)
   //   %time = 2900000  -> elev =   0    SUNRISE  (sun at horizon, ascending)
   //
   // Sampled:
   //   %time = 0        SunAzimuth=40 SunElevation=70       (mid-morning)
   //   %time = 900000   SunAzimuth=60 SunElevation=160.018  (mid-afternoon, descending)
   //   %time = 1800000  SunAzimuth=0  SunElevation=-109.984 (deep night, past midnight)
   //   %time = 2700000  SunAzimuth=20 SunElevation=-19.9835 (pre-dawn)
   virtual void clientCmdSyncStartTime(%time) {}
   virtual void getDayFraction() {}
   virtual float calcExplosionCoverage() {}
   virtual void setColorTable() {}
   virtual void setSprayCanDivision() {}
   virtual string getSprayCanDivisionName() {}
   virtual int getSprayCanDivisionSlot() {}
   virtual void setPrintTexture() {}
   virtual string getPrintTexture() {}
   virtual string getColorIDTable() {}
   virtual void updateTempBrickSettings() {}
   virtual void StartFoliageReplication() {}
   virtual void StartGrassReplication() {}
   virtual void StartClientReplication() {}
   virtual void StartServerReplication() {}
   virtual void StartSurfaceReferencer() {}
   virtual void commandToServer() {}
   virtual void commandToClient() {}
   virtual void removeTaggedString() {}
   virtual string addTaggedString() {}
   virtual string getTaggedString() {}
   virtual string buildTaggedString() {}
   virtual void msg() {}
   virtual void queryLanServers() {}
   virtual void queryMasterServer() {}
   virtual void querySingleServer() {}
   virtual void cancelServerQuery() {}
   virtual void stopServerQuery() {}
   virtual void startHeartbeat() {}
   virtual void stopHeartbeat() {}
   virtual int getServerCount() {}
   virtual bool setServerInfo() {}
   virtual string StripMLControlChars() {}
   virtual bool isPointInside() {}
   virtual string VectorAdd() {}
   virtual string VectorSub() {}
   virtual string VectorScale() {}
   virtual string VectorNormalize() {}
   virtual float VectorDot() {}
   virtual string VectorCross() {}
   virtual float VectorDist() {}
   virtual float VectorLen() {}
   virtual string VectorOrthoBasis() {}
   virtual string MatrixCreate() {}
   virtual string MatrixCreateFromEuler() {}
   virtual string MatrixMultiply() {}
   virtual string MatrixMulVector() {}
   virtual string MatrixMulPoint() {}
   virtual string getBoxCenter() {}
   virtual void setRandomSeed() {}
   virtual int getRandomSeed() {}
   virtual float getRandom() {}
   virtual float getGaussian() {}
   virtual string mSolveQuadratic() {}
   virtual string mSolveCubic() {}
   virtual string mSolveQuartic() {}
   virtual int mFloor() {}
   virtual int mCeil() {}
   virtual string mFloatLength() {}
   virtual float mAbs() {}
   virtual float mSqrt() {}
   virtual float mPow() {}
   virtual float mLog() {}
   virtual float mSin() {}
   virtual float mCos() {}
   virtual float mTan() {}
   virtual float mAsin() {}
   virtual float mAcos() {}
   virtual float mAtan() {}
   virtual float mRadToDeg() {}
   virtual float mDegToRad() {}
   virtual void FreeMemoryDump() {}
   virtual bool redbookOpen() {}
   virtual bool redbookClose() {}
   virtual bool redbookPlay() {}
   virtual bool redbookStop() {}
   virtual int redbookGetTrackCount() {}
   virtual float redbookGetVolume() {}
   virtual bool redbookSetVolume() {}
   virtual int redbookGetDeviceCount() {}
   virtual string redbookGetDeviceName() {}
   virtual string redbookGetLastError() {}
   virtual bool setDisplayDevice() {}
   virtual bool setScreenMode() {} // ( int width, int height, int bpp, bool fullScreen )
   virtual bool toggleFullScreen() {}
   virtual bool isFullScreen() {}
   virtual bool switchBitDepth() {}
   virtual bool prevResolution() {}
   virtual bool nextResolution() {}
   virtual string getRes() {}
   virtual bool setRes() {}
   virtual string getDisplayDeviceList() {}
   virtual string getResolutionList() {}
   virtual string getVideoDriverInfo() {}
   virtual bool isDeviceFullScreenOnly() {}
   virtual void videoSetGammaCorrection() {}
   virtual bool setVerticalSync() {}
   virtual void profilerMarkerEnable() {}
   virtual void profilerEnable() {}
   virtual void profilerDump() {}
   virtual void profilerDumpToFile() {}
   virtual void profilerReset() {}
   virtual void enableWinConsole() {}
   virtual bool activateKeyboard() {}
   virtual void deactivateKeyboard() {}
   virtual bool enableMouse() {}
   virtual void disableMouse() {}
   virtual bool enableJoystick() {}
   virtual void disableJoystick() {}
   virtual void echoInputState() {}
   virtual bool isJoystickDetected() {}
   virtual string getJoystickAxes() {}
   virtual void mathInit() {}
   virtual void addCardProfile() {}
   virtual void addOSCardProfile() {}
   virtual string getDesktopResolution() {}
   virtual bool isKoreanBuild() {}
   virtual void resetLighting() {}
   virtual void allowConnections() {}
   virtual void clearServerPaths() {}
   virtual void pathOnMissionLoadDone() {}
   virtual void makeTestTerrain() {}
   virtual float getTerrainHeight() {}
   virtual bool OpenALInitDriver() {}
   virtual void OpenALShutdownDriver() {}
   virtual void OpenALRegisterExtensions() {}
   virtual string alGetString() {}
   virtual int alxGetWaveLen() {}
   virtual int alxCreateSource() {}
   virtual void alxSourcef() {}
   virtual void alxSource3f() {}
   virtual void alxSourcei() {}
   virtual float alxGetSourcef() {}
   virtual string alxGetSource3f() {}
   virtual int alxGetSourcei() {}
   virtual int alxPlay() {}
   virtual void alxStop() {}
   virtual void alxStopAll() {}
   virtual bool alxIsPlaying() {}
   virtual void alxListenerf() {}
   virtual void alListener3f() {}
   virtual float alxGetListenerf() {}
   virtual string alGetListener3f() {}
   virtual int alGetListeneri() {}
   virtual int alxGetChannelVolume() {}
   virtual bool alxSetChannelVolume() {}
};
```
