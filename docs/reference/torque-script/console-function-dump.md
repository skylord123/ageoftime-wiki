# Console Function Dump

This page is a verbatim dump of every TorqueScript console function exposed by
the *Age of Time* client at runtime, captured by running the engine's
built-in `dumpConsoleFunctions();` from the in-game console.

!!! note "Annotations"
    Almost every entry is hand-annotated with a `//` comment describing what
    it does and its arguments. Anything after a `//` is **not** part of the
    original engine output — it's a community note. `virtual Script` functions
    are *Age of Time* TorqueScript, documented from the decompiled DSO; the
    typed-return functions are stock Torque Game Engine builtins, documented
    from the TGE source (their usage strings are reproduced).

!!! tip "Reproducing this dump"
    Open the in-game console (the engine's standard tilde key in older
    Torque builds, or run the executable with the appropriate flag) and
    type:

    ```
    dumpConsoleFunctions();
    ```

    The engine will print the same listing shown below.

```cpp
==>dumpConsoleFunctions();
namespace Global {
   // (%val) F9 keybind. In Debug builds, cycles wireframe / interior-debug render modes (GLEnableOutline + setInteriorRenderMode). %val = key-down state.
   virtual Script cycleDebugRenderMode() {}
   // (%val) ctrl-o keybind. Pushes the optionsDlg when the key is pressed.
   virtual Script bringUpOptions() {}
   // (%val) F7 keybind. Sends 'DropPlayerAtCamera' to the server (teleport player to the fly camera).
   virtual Script dropPlayerAtCamera() {}
   // (%val) F8 keybind. Sends 'dropCameraAtPlayer' to the server (move fly camera to the player).
   virtual Script dropCameraAtPlayer() {}
   // (%val) F4 keybind. Calls stopDemoRecord() on key press.
   virtual Script stopRecordingDemo() {}
   // (%val) F3 keybind. Calls startDemoRecord() on key press.
   virtual Script startRecordingDemo() {}
   // (%val) 'p' keybind. Cycles the chat HUD size via cycleMessageHudSize().
   virtual Script resizeMessageHud() {}
   // (%val) pageDown keybind. Scrolls the chat HUD down a page.
   virtual Script pageMessageHudDown() {}
   // (%val) pageUp keybind. Scrolls the chat HUD up a page.
   virtual Script pageMessageHudUp() {}
   // (%val) alt-c keybind. Sends 'ToggleCamera' to the server (switch between player and fly camera).
   virtual Script toggleCamera() {}
   // (%val) tab keybind. Toggles $firstPerson view.
   virtual Script toggleFirstPerson() {}
   // (%val) 'z' keybind. Toggles or holds $mvFreeLook depending on $pref::Input::useFreeLookToggle.
   virtual Script toggleFreeLook() {}
   // (%val) 'f' keybind. Toggles $ZoomOn; sets FOV to $Pref::player::CurrentFOV (zoomed) or $pref::Player::defaultFov.
   virtual Script toggleZoom() {}
   // (%val) 'r' keybind. Calls toggleZoomFOV() to adjust the zoom field-of-view.
   virtual Script setZoomFOV() {}
   // (%val) Mouse block / alternate fire. Increments $mvTriggerCount1.
   virtual Script altTrigger() {}
   // (%val) Mouse button0 bind. Increments $mvTriggerCount0 (primary fire/attack).
   virtual Script mouseFire() {}
   // (%val) 'c' keybind. Increments $mvTriggerCount3 (crouch trigger).
   virtual Script crouch() {}
   // (%val) space keybind. Increments $mvTriggerCount2 (jump trigger).
   virtual Script jump() {}
   // (%val) Mouse y-axis. Adjusts $mvPitch by mouse delta * sensitivity (honors $pref::Input::MouseInvert).
   virtual Script pitch() {}
   // (%val) Mouse x-axis. Adjusts $mvYaw by mouse delta * sensitivity.
   virtual Script yaw() {}
   // (%val) -> float. Returns the mouse delta scaled by FOV: %val * ($cameraFov/90) * 0.01.
   virtual Script getMouseAdjustAmount() {}
   // (%val) Keyboard look-down pitch speed ($mvPitchUpSpeed).
   virtual Script panDown() {}
   // (%val) Keyboard look-up pitch speed ($mvPitchDownSpeed).
   virtual Script panUp() {}
   // (%val) Keyboard yaw-right speed ($mvYawLeftSpeed).
   virtual Script turnRight() {}
   // (%val) Keyboard yaw-left speed ($mvYawRightSpeed).
   virtual Script turnLeft() {}
   // (%val) Sets $mvDownAction = %val * $movementSpeed.
   virtual Script movedown() {}
   // (%val) Sets $mvUpAction = %val * $movementSpeed.
   virtual Script moveup() {}
   // (%val) Sets $mvBackwardAction = %val * $movementSpeed.
   virtual Script movebackward() {}
   // (%val) Sets $mvForwardAction = %val * $movementSpeed.
   virtual Script moveforward() {}
   // (%val) Sets $mvRightAction = %val * $movementSpeed.
   virtual Script moveright() {}
   // (%val) Sets $mvLeftAction = %val * $movementSpeed.
   virtual Script moveleft() {}
   // (%speed) Sets $movementSpeed (the multiplier applied to all move* actions).
   virtual Script setSpeed() {}
   // (%val) F2 keybind. Toggles the PlayerListGui (scoreboard).
   virtual Script showPlayerList() {}
   // () escape keybind. Pushes escapeMenuGui. (Legacy disconnect MessageBox path is dead-coded after an early return.)
   virtual Script escapeFromGame() {}
   // (%idx, %serverID) Server RPC. Assigns quick slot %idx to the client inv item identified by %serverID.
   virtual Script ClientCmdSetQuickSlot() {}
   // () Brick selector: show/hide the quick-slot assignment box.
   virtual Script BSD_ToggleQuickSlots() {}
   // (%idx) Assigns the currently clicked inv item to quick slot %idx and notifies the server ('SetQuickSlot').
   virtual Script BSD_AssignQuickSlot() {}
   // () Rebuilds BSD_List rows (name TAB category TAB subcategory) from $clientInv, then sorts.
   virtual Script BSD_PopulateList() {}
   // (%serverID, %quantity) Server RPC. Updates the displayed quantity for the inv item with %serverID.
   virtual Script clientCmdUpdateInvSOQuantity() {}
   // () Echoes every datablock and its class name to the console.
   virtual Script listAllDataBlocks() {}
   // () Execs ~/client/Favorites.cs and sets $FavoritesLoaded.
   virtual Script BSD_LoadFavorites() {}
   // (%idx) Loads favorite brick set %idx into the inventory icon slots.
   virtual Script BSD_BuyFavorites() {}
   // (%idx) Saves the current inventory icon slots as favorite set %idx and exports to Favorites.cs.
   virtual Script BSD_SaveFavorites() {}
   // (%idx) In "Set Favs" mode saves favorites %idx, otherwise buys favorite set %idx.
   virtual Script BSD_ClickFav() {}
   // () Toggles the "set favorites" helper mode / button label.
   virtual Script BSD_SetFavs() {}
   // () Closes the brick selector. (Legacy buy-bricks loop is dead-coded after a return.)
   virtual Script BSD_BuyBricks() {}
   // (%catID) Shows category tab %catID's scroll panel and hides the others.
   virtual Script BSD_showTab() {}
   // (%data) Legacy: pick/place a brick-data icon into the inventory grid.
   virtual Script BSD_ClickIcon() {}
   // (%index) Selects client inv item %index (highlights it; feeds the combine window as item 2).
   virtual Script BSD_ClickInv() {}
   // () Hides the combine window.
   virtual Script BSD_CancelCombine() {}
   // () Sends 'Combine' to the server with the two selected items' serverIDs.
   virtual Script BSD_FinalCombine() {}
   // () Refreshes the two combine-preview models, dye colors, and labels.
   virtual Script BSD_UpdateCombine() {}
   // () Starts a combine: sets combine slot 1 to the current item and opens the combine window.
   virtual Script BSD_Combine() {}
   // () Sends 'discard' for the currently clicked item (remembers its category to reselect after refresh).
   virtual Script BSD_Discard() {}
   // () PostOffice pick mode: stores the picked client-inv object, pops the dialog, and evals $BSD_PickCallback.
   virtual Script BSD_PostOfficeSelect() {}
   // () Sends 'use' for the currently clicked inv item (by serverID).
   virtual Script BSD_Use() {}
   // () Clears all legacy inventory icon slots.
   virtual Script BSD_ClickClear() {}
   // () (Disabled/legacy) builds the bottom inventory icon bar. Returns immediately.
   virtual Script BSD_CreateInventoryButtons() {}
   // () Deletes the BSD_InvBox inventory icon container.
   virtual Script BSD_KillInventoryButtons() {}
   // (%index) Builds the GUI preview button (model, dye, label, quantity) for inv item %index in its category box.
   virtual Script BSD_CreateBrickButton() {}
   // (%cat) Lays out subcategory headers and divider bars inside a category box.
   virtual Script BSD_createSubHeadings() {}
   // (%catObj, %subCatName) -> subcategory ScriptObject by name (or empty).
   virtual Script BSD_findSubCategory() {}
   // (%catName) -> category ScriptObject by name (or empty).
   virtual Script BSD_findCategory() {}
   // (%cat, %newSubCat) -> finds or creates the named subcategory under %cat and returns it.
   virtual Script BSD_addSubCategory() {}
   // (%newcat) Creates the named category ScriptObject if it does not already exist.
   virtual Script BSD_addCategory() {}
   // () Deletes all category/tab/scroll/inventory GUI objects and resets brick-selector counts.
   virtual Script BSD_KillBricks() {}
   // () Echoes all categories and their subcategories to the console (debug).
   virtual Script BSD_DumpCategories() {}
   // () Rebuilds the entire brick-selector UI from $clientInv (tabs, scrolls, buttons); reselects the last-discarded category.
   virtual Script bsd_loadBricks() {}
   // () Server RPC. Reloads bricks + favorites and rebuilds the inventory HUD.
   virtual Script clientCmdBSD_LoadBricks() {}
   // () Server RPC. Pushes the BrickSelectorDlg.
   virtual Script clientCmdBSD_Open() {}
   // (%title, %serverID) Server RPC. Opens WriteParchmentGui for object %serverID.
   virtual Script clientCmdWriteParchment() {}
   // () Sends appended parchment text to the server ('WriteParchmentAppend', chunked at 200 chars) then re-'use's the parchment.
   virtual Script PG_Append() {}
   // (%text) Server RPC. Appends %text to the currently open parchment and resizes the text control.
   virtual Script clientCmdAddParchmentText() {}
   // (%text, %serverID) Server RPC. Shows ParchmentGui with %text for object %serverID.
   virtual Script clientCmdOpenParchment() {}
   // () Server RPC. Pops the ChangePasswordGui (password change succeeded).
   virtual Script clientCmdPasswordChanged() {}
   // () Validates new password match, CRCs it, and sends 'changePassword' (old, new).
   virtual Script CPG_Submit() {}
   // () WinExec("doPatch.bat") to run the downloaded patch and relaunch.
   virtual Script AU_RunPatch() {}
   // (%timeS) -> string. Formats seconds as H:MM:SS, M:SS, or 0:SS.
   virtual Script getTimeString() {}
   // (%val) -> string. Rounds %val to two decimals with trailing-zero padding.
   virtual Script roundMegs() {}
   // (%newVersion) Connects to the patch server, downloads the %newVersion file, and writes patch.bat.
   virtual Script AU_GetUpdate() {}
   // () Connects to the version-check URL for the current $version to see if an update is required.
   virtual Script AU_start() {}
   // () Server RPC. Schedules a disconnect and opens the AutoUpdateGui.
   virtual Script clientCmdDoUpdates() {}
   // () Server RPC. Pops the saleGui (sale posted successfully).
   virtual Script clientCmdSaleSuccess() {}
   // () Validates quantity and price, then sends 'SellItem' (serverID, amount, price).
   virtual Script SG_Send() {}
   // () Opens the brick selector in PostOffice pick mode to choose the item to sell.
   virtual Script SG_SelectItem() {}
   // (%cost) Server RPC. Opens the saleGui showing the listing cost.
   virtual Script clientCmdOpenSaleGui() {}
   // () Server RPC. Pops PostOfficeGui and shows "Mail Sent".
   virtual Script clientCmdMailSuccess() {}
   // () Sends 'MailItem' (serverID, recipient name, anon flag).
   virtual Script POG_Send() {}
   // () Opens the brick selector in PostOffice pick mode to choose the item to mail.
   virtual Script POG_SelectItem() {}
   // (%cost) Server RPC. Opens PostOfficeGui showing the mailing cost.
   virtual Script clientCmdOpenPostOfficeGui() {}
   // () TCP-downloads the active .craft menu file from master.ageoftime.com.
   virtual Script craftDownload_GetFile() {}
   // () Server RPC. Refreshes the craft window and shows "Item Created".
   virtual Script clientCmdCraftingSuccess() {}
   // () Sends 'Craft' with the recipe index and the four picked component serverIDs.
   virtual Script Craft_Create() {}
   // (%index) Opens the brick selector in pick mode to choose recipe component %index.
   virtual Script Craft_SelectItem() {}
   // () Refreshes the component preview models/labels from the picked inv items.
   virtual Script Craft_Update() {}
   // (%idx) Sets the active recipe index ($Craft_Idx) and pushes CraftGui.
   virtual Script Craft_Open() {}
   // () Parses the active .craft file and builds recipe entries in the craft menu (cost, model, components, requirements).
   virtual Script Craft_OpenFile() {}
   // (%name) Pushes craftDownloadGui and downloads the named craft menu file.
   virtual Script Craft_DownloadMenu() {}
   // (%name, %crc) Server RPC. Opens craft menu %name; downloads it if the local file is missing or CRC mismatches.
   virtual Script clientCmdOpenCraftMenu() {}
   // () Reads the transaction amount, signs it by Withdraw/Deposit, and sends 'BankDeposit'.
   virtual Script Bank_Process() {}
   // (%val) Server RPC. Updates the bank balance and cash display.
   virtual Script clientCmdSetBank() {}
   // (%val) Server RPC. Opens BankGui showing balance %val (and current gold).
   virtual Script clientCmdOpenBankGui() {}
   // (%exp) Server RPC. Sets the experience bar ($SG_MaxExperience = 1000).
   virtual Script ClientCmdSetExp() {}
   // (%level,%burden,%maxBurden,%attack,%defense,%magicPower,%maxMana,%runSpeed,%jumpPower,%climbPower,%sexyness) Server RPC. Sets the status panel bars/text.
   virtual Script ClientCmdSetStatus() {}
   // (%name, %height, %weight) Server RPC. Sets the status panel's permanent name/height/weight text.
   virtual Script ClientCmdSetPermStatus() {}
   // (%name, %var, %maxValue) Resizes the named status bar control to the %var/%maxValue proportion (200px max height).
   virtual Script SG_UpdateBar() {}
   // (%string) Server RPC. Sets the 7 ability values (space-delimited) and their bars.
   virtual Script clientCmdSetAbilities() {}
   // (%maxLevel) Server RPC. Sets $SG_MaxLevel (scales the level bar).
   virtual Script clientCmdSetLevelingVars() {}
   // (%val, %test) Debug echo helper ("CRAP SAYS ...").
   virtual Script crap() {}
   // () Server RPC. Pushes the respawnArenaGui.
   virtual Script clientCmdRespawnArenaDlg() {}
   // () Server RPC. Pushes the respawnGui.
   virtual Script clientCmdRespawnDlg() {}
   // (%warnText, %btnText) Server RPC. Detags args and shows them in a MessageBoxOK.
   virtual Script clientCmdWarningBox() {}
   // (%junk0) Server RPC. Pushes the BuyConfirmGui.
   virtual Script clientCmdBuyConfirm() {}
   // () Server RPC. Pops the LoginGui and CreateCharacterGui (login succeeded).
   virtual Script clientCmdLoginSuccess() {}
   // () Server RPC. Pushes the LoginGui.
   virtual Script clientCmdStartLogin() {}
   // () Server RPC. Hides the bottom-print overlay.
   virtual Script clientCmdclearBottomPrint() {}
   // () Server RPC. Hides the center-print overlay.
   virtual Script clientCmdClearCenterPrint() {}
   // (%message, %time, %size) Server RPC. Shows bottom-print text for %time seconds at size class %size (1-3).
   virtual Script clientCmdBottomPrint() {}
   // (%message, %time, %size) Server RPC. Shows center-print text for %time seconds (default 3) at size class %size.
   virtual Script clientCmdCenterPrint() {}
   // () Server RPC. Shows and resets the full-screen blackout overlay.
   virtual Script clientCmdBlackOut() {}
   // (%pwd) Server RPC. Enables the compass HUD if %pwd matches the magic string.
   virtual Script clientCmdEnableCompass() {}
   // () Server RPC. Hides the compass HUD.
   virtual Script clientCmdDisableCompass() {}
   // (%amt) Server RPC. Sets the gold amount shown on the PlayGui.
   virtual Script clientCmdSetGold() {}
   // () Resets the center-print text control position to "0 0".
   virtual Script refreshCenterTextCtrl() {}
   // () Resets the bottom-print text control position to "0 0".
   virtual Script refreshBottomTextCtrl() {}
   // (%make) 'y' keybind. If %make, opens MessageHud in local ("say") mode.
   virtual Script localMessageHud() {}
   // (%make) 't' keybind. If %make, opens MessageHud in global mode.
   virtual Script toggleMessageHud() {}
   // () Cycles the chat HUD size (MainChatHud.nextChatHudLen()).
   virtual Script cycleMessageHudSize() {}
   // () Scrolls the chat HUD down one page.
   virtual Script pageDownMessageHud() {}
   // () Scrolls the chat HUD up one page.
   virtual Script pageUpMessageHud() {}
   // (%message) Plays any embedded "~w" sound, then adds the remaining text to the chat HUD.
   virtual Script onServerMessage() {}
   // (%message, %voice, %pitch) Like onServerMessage but with a voice folder and pitch for the sound.
   virtual Script onChatMessage() {}
   // (%message, %voice, %pitch) -> int. Parses a "~w<wav>" tag, plays the wav (length-limited); returns the tag offset or -1.
   virtual Script playMessageSound() {}
   // (%val) Applies graphics-detail preset %val (1-5) to all $pref graphics vars.
   virtual Script SetGraphicDetail() {}
   // (%val) Applies network preset %val to net prefs/sliders (>6 = custom; 0 = no-op).
   virtual Script SetConnectionType() {}
   // (%val) Keybind '0': uses quick slot 10 on press.
   virtual Script quickSlot10() {}
   // (%val) Keybind '9': uses quick slot 9 on press.
   virtual Script quickSlot9() {}
   // (%val) Keybind '8': uses quick slot 8 on press.
   virtual Script quickSlot8() {}
   // (%val) Keybind '7': uses quick slot 7 on press.
   virtual Script quickSlot7() {}
   // (%val) Keybind '6': uses quick slot 6 on press.
   virtual Script quickSlot6() {}
   // (%val) Keybind '5': uses quick slot 5 on press.
   virtual Script quickSlot5() {}
   // (%val) Keybind '4': uses quick slot 4 on press.
   virtual Script quickSlot4() {}
   // (%val) Keybind '3': uses quick slot 3 on press.
   virtual Script quickSlot3() {}
   // (%val) Keybind '2': uses quick slot 2 on press.
   virtual Script quickSlot2() {}
   // (%val) Keybind '1': uses quick slot 1 on press.
   virtual Script quickSlot1() {}
   // (%i) Sends 'use' with the serverID of the item in quick slot %i.
   virtual Script useQuickSlot() {}
   // (%varString, %min) Evals and decrements the named global var, clamped above %min.
   virtual Script decVar() {}
   // (%varString, %max) Evals and increments the named global var, clamped below %max.
   virtual Script incVar() {}
   // (%val) 'v' keybind. Pushes the VoiceMenuGui (emote/voice/animation/spell radial menu).
   virtual Script openVoiceMenu() {}
   // (%val) Pushes the admingui window.
   virtual Script openAdminWindow() {}
   // (%val) 'lshift' keybind. Toggles walk speed: $movementSpeed 0.4 while held, 1 otherwise; rescales current move actions.
   virtual Script Walk() {}
   // (%val) 'ctrl w' keybind. Auto-run: sets $mvForwardAction to full forward.
   virtual Script autoWalk() {}
   // (%val) 'ctrl k' keybind. Sends 'suicide' to the server.
   virtual Script Suicide() {}
   // (%val) 'ctrl e' keybind. Sends 'stopAction' to the server.
   virtual Script stopAction() {}
   // (%val) 'e' keybind. Sends 'action' to the server (interact/use-in-world).
   virtual Script Action() {}
   // (%val) 'o' keybind. Toggles the StatusGui.
   virtual Script openStatus() {}
   // (%val) 'i' keybind. Toggles the BrickSelectorDlg (inventory).
   virtual Script openInventory() {}
   // (%channel, %volume) Sets $pref::Audio::channelVolume[%channel] and plays a test sound.
   virtual Script OptAudioUpdateChannelVolume() {}
   // (%volume) Sets $pref::Audio::masterVolume (alxListenerf gain) and plays a test sound.
   virtual Script OptAudioUpdateMasterVolume() {}
   // () Refreshes the OpenAL vendor/version/renderer/extensions info text in the options dialog.
   virtual Script OptAudioUpdate() {}
   // (%command) -> int. Returns the $RemapCmd index whose command equals %command, or -1.
   virtual Script findRemapCmdIndex() {}
   // (%device, %action, %cmd, %oldIndex, %newIndex) Rebinds %cmd to %device/%action and refreshes both remap-list rows.
   virtual Script redoMapping() {}
   // (%index) -> string. Returns "RemapName TAB binding-display" for remap row %index.
   virtual Script buildFullMapString() {}
   // (%device, %action) -> string. Human-readable binding name (handles keyboard, mouse buttons, joystick buttons/POV).
   virtual Script getMapDisplayName() {}
   // () Deletes moveMap, re-execs default.bind.cs, and refills the remap list.
   virtual Script restoreDefaultMappings() {}
   // () Reads the RateToServer slider into $pref::Net::PacketRateToServer (and the custom pref when ConnectionType==7).
   virtual Script UpdateRateToServer() {}
   // () Reads the RateToClient slider into $pref::Net::PacketRateToClient (and custom pref when ConnectionType==7).
   virtual Script UpdateRateToClient() {}
   // () Reads the LagThreshold slider into $Pref::Net::LagThreshold (and custom pref when ConnectionType==7).
   virtual Script UpdateLagThreshold() {}
   // () Reads the PacketSize slider into $pref::Net::PacketSize (and custom pref when ConnectionType==7).
   virtual Script UpdatePacketSize() {}
   // () Clears HUD/audio/player lists, returns Canvas to MainMenuGui, clears texture holds, and purges resources.
   virtual Script disconnectedCleanup() {}
   // () Deletes the ServerConnection, runs disconnectedCleanup(), and destroys the local server.
   virtual Script disconnect() {}
   // (%junk0, %junk1, %msgError) MsgConnectionError callback. Stores $ServerConnectionErrorMessage.
   virtual Script handleConnectionErrorMessage() {}
   // (%junk0, %junk1) MsgLoadInfoDone callback (empty).
   virtual Script handleLoadInfoDoneMessage() {}
   // (%junk0, %junk1, %line, %image) MsgLoadDescription callback. Appends a description line and sets the loading-screen bitmap.
   virtual Script handleLoadDescriptionMessage() {}
   // (%junk0, %junk1, %mapName) MsgLoadInfo callback. Switches to LoadingGui, clears description queue, sets map name.
   virtual Script handleLoadInfoMessage() {}
   // () Mission download finished (empty hook).
   virtual Script onMissionDownloadComplete() {}
   // () Lighting phase complete: sets the loading bar to 100% and clears $lightingMission.
   virtual Script onPhase3Complete() {}
   // (%progress) Updates the loading bar during scene lighting.
   virtual Script onPhase3Progress() {}
   // () Phase 3 (lighting) start: resets bar, sets "LIGHTING MISSION".
   virtual Script onMissionDownloadPhase3() {}
   // (%fileName, %ofs, %size) Updates the loading bar/text while downloading a file from the server.
   virtual Script onFileChunkReceived() {}
   // () Phase 2 complete (empty hook).
   virtual Script onPhase2Complete() {}
   // (%progress) Updates the loading bar during ghost-object download.
   virtual Script onPhase2Progress() {}
   // () Phase 2 (objects) start: resets bar, sets "LOADING OBJECTS".
   virtual Script onMissionDownloadPhase2() {}
   // () Phase 1 complete (empty hook).
   virtual Script onPhase1Complete() {}
   // (%progress) Updates the loading bar during datablock download.
   virtual Script onPhase1Progress() {}
   // (%junk0, %junk1) Phase 1 (datablocks) start: closes MessageHud, resets bar, sets "LOADING DATABLOCKS".
   virtual Script onMissionDownloadPhase1() {}
   // (%junk0) Server RPC. Game ended: stops audio and fills EndGameGui with the final scoreboard.
   virtual Script clientCmdGameEnd() {}
   // (%junk0) Server RPC. Game started: zeroes all player scores.
   virtual Script clientCmdGameStart() {}
   // (%junk0) Server RPC. Day/night clock sync (empty stub in this build).
   virtual Script clientCmdSyncClock() {}
   // (%password) Sends 'SADSetPassword' (set super-admin password).
   virtual Script SADSetPassword() {}
   // (%password) Sends the super-admin login 'SAD' password.
   virtual Script SAD() {}
   // (%text) Server RPC. Adds a numbered NPC-dialog choice button (commands 'SelectBotChatOption').
   virtual Script clientCmdAddDialogOption() {}
   // () Server RPC. Pops the dialogGui (NPC conversation).
   virtual Script clientCmdCloseDialog() {}
   // (%question) Server RPC. Opens dialogGui showing %question.
   virtual Script clientCmdOpenDialog() {}
   // (%col) Sorts the server list numerically by column %col, toggling ascending/descending.
   virtual Script JS_sortNumList() {}
   // (%col) Sorts the server list alphabetically by column %col, toggling ascending/descending.
   virtual Script JS_sortList() {}
   // (%status, %msg, %value) Updates the join-server query progress UI (start/ping/query/done).
   virtual Script onServerQueryStatus() {}
   // () Connects to a manually-typed IP (manualjoin GUI) using the entered join password.
   virtual Script MJ_connect() {}
   // (%slot, %quantity) Server RPC. Sets the quantity for inventory slot %slot and updates its label.
   virtual Script clientCmdUpdateInvSlotQuantity() {}
   // () Server RPC. Deletes all client inventory objects and clears the quick slots.
   virtual Script clientCmdClearInventory() {}
   // (%name,%baseID,%slot,%quantity,%mat1..4) Server RPC. Updates an inventory slot's fields and reloads the brick UI.
   virtual Script clientCmdUpdateInvSlot() {}
   // (%slot) Server RPC. Deletes inventory slot %slot and shifts the remaining slots down, then reloads bricks.
   virtual Script clientCmdClearInvSlot() {}
   // (%serverID | %slot) Server RPC. Marks an inventory item as not-in-use (clears the in-use overlay).
   virtual Script clientCmdSetUnEquipped() {}
   // (%serverID | %slot) Server RPC. Marks an inventory item as in-use (shows the in-use overlay).
   virtual Script clientCmdSetEquipped() {}
   // (%serverID,%name,%baseID,%quantity,%mat1..4,%dyeColor) Creates a ClientInventorySO and appends it to $clientInv.
   virtual Script AddClientInvItem() {}
   // (%name,%baseID,%slot,%quantity,%mat1..4) Deprecated; errors out (kept for compatibility).
   virtual Script clientCmdAddInventoryItem() {}
   // (%serverID,%name,%baseID,%slot,%quantity,%mat1..4,%dyeColor) Server RPC. Creates/updates an inventory slot (by serverID or slot) and reloads bricks.
   virtual Script clientCmdSetInventoryItem() {}
   // () Syncs the in-use overlays on the inventory grid from each item's state.
   virtual Script invGuiRefreshInUse() {}
   // (%categoryName) Fills the inventory preview grid with items of the given category (Clothing/Weapon/Ammo/ItemData).
   virtual Script loadItemPreviews() {}
   // () Clears the model on every inventory preview control.
   virtual Script clearItemPreviews() {}
   // () Debug: fills the previews with a randomly-tinted shirt model.
   virtual Script testItemPreviews() {}
   // () Deletes all inventory preview/highlight/in-use/label GUI objects.
   virtual Script killItemPreviews() {}
   // (%idx, %val) Shows/hides the in-use overlay bitmap for preview %idx.
   virtual Script invGuiSetInUse() {}
   // (%idx) Highlights inventory preview %idx and sets $selectedInvSlot to its inv slot.
   virtual Script invGuiSetHilight() {}
   // (%ipIdx) Click handler for an inventory preview; highlights it.
   virtual Script clickItemPreview() {}
   // () Builds the 20x3 inventory preview grid (highlight, in-use, model view, name, quantity controls).
   virtual Script makeItemPreviews() {}
   // () Echoes the client inventory slots and item names to the console (debug).
   virtual Script dumpClientInv() {}
   // () Server RPC. Asks (MessageBoxYesNo) whether to overwrite an existing character, calling characterDone(1).
   virtual Script clientCmdConfirmCharacterOverWrite() {}
   // (%name, %statIndex, %time) Scheduled tick: incrementally raises abilities toward preset %name.
   virtual Script CCG_PresetTick() {}
   // (%name, %statIndex, %time) Scheduled tick: drains all abilities to 1 before applying preset %name, then hands off to CCG_PresetTick.
   virtual Script CCG_PresetDrainTick() {}
   // (%name) Applies an ability preset (Warrior/Archer/Mage) via the drain/raise tick schedule.
   virtual Script CCG_Preset() {}
   // (%name) Resizes the ability bar control for ability %name (height = value*20).
   virtual Script CCG_SetAbility() {}
   // () Resizes all seven ability bars and the remaining-points bar; refreshes sliders/menus.
   virtual Script CCG_RefreshAbilities() {}
   // (%name) Subtracts 1 from ability %name and refunds 1 point.
   virtual Script CCG_SubtractAbility() {}
   // (%name) Adds 1 to ability %name and spends 1 point.
   virtual Script CCG_AddAbility() {}
   // (%tabName) Switches the character-creation tab (General/Appearance/Abilities).
   virtual Script CCG_Tab() {}
   // (%sliderObj) Sets the slider to a random value within its range.
   virtual Script RandomizeSlider() {}
   // (%menuObj) Selects a random entry in the menu.
   virtual Script RandomizeMenu() {}
   // () Randomizes all character sliders and menus (scale, chest, posture, skin, hair, eyes, ears, face, glasses).
   virtual Script CC_Random() {}
   // () Applies face/hair/ears/glasses node visibility and hair/eye colors to the preview from the menus.
   virtual Script updateCharacterMenus() {}
   // () Applies scale/posture/chest/skin/lip slider values to the preview and computes displayed weight.
   virtual Script updateCharacterSliders() {}
   // () Cancels character creation: pops CreateCharacterGui, pushes LoginGui.
   virtual Script characterCancel() {}
   // (%overWrite) Validates the password, CRCs it, and sends 'newCharacter' with all appearance/ability fields.
   virtual Script characterDone() {}
   // (%menu) Selects the previous entry in %menu (wraps) and updates the preview.
   virtual Script decMenu() {}
   // (%menu) Selects the next entry in %menu (wraps) and updates the preview.
   virtual Script incMenu() {}
   // () Opens CreateCharacterGui (and pops LoginGui).
   virtual Script clickNewCharacter() {}
   // () Sends 'Login' with the entered name and CRC of the password.
   virtual Script clickLogin() {}
   // () Polls whether the StartupGui sequence is complete (startup splash flow; defined in startup GUI scripts).
   virtual Script checkStartupDone() {}
   // () Begins the StartupGui splash/intro sequence (defined in startup GUI scripts).
   virtual Script loadStartup() {}
   // () Connects to $Pref::ServerIP (retrieved from the master server) as a new GameConnection.
   virtual Script MM_Connect() {}
   // (%junk0, %junk1, %score, %clientId) MsgClientScoreChanged callback. Updates a player's score row.
   virtual Script handleClientScoreChanged() {}
   // (%junk0, %junk1, %clientName, %clientId) MsgClientDrop callback. Removes the player from the scoreboard and admin list.
   virtual Script handleClientDrop() {}
   // (%junk0,%junk1,%clientName,%clientId,%junk4,%score,%isAI,%isAdmin,%isSuperAdmin) MsgClientJoin callback. Adds/updates a player row.
   virtual Script handleClientJoin() {}
   // () Demo playback finished: disconnect, return to MainMenu, reopen recordings dialog.
   virtual Script demoPlaybackComplete() {}
   // () Stops the current demo recording.
   virtual Script stopDemoRecord() {}
   // () Starts recording a demo to the next free recordings/demoNNN.rec file.
   virtual Script startDemoRecord() {}
   // () Plays back the selected .rec demo from the recordings dialog.
   virtual Script StartSelectedDemo() {}
   // () F1 keybind (GlobalActionMap). Toggles HelpDlg for the current Canvas content's help page.
   virtual Script contextHelp() {}
   // (%helpName) Pushes HelpDlg and selects the named help file (or leaves the first).
   virtual Script getHelp() {}
   // () Shows and (if $cursorControlled) unlocks the mouse cursor.
   virtual Script cursorOn() {}
   // () Hides and (if $cursorControlled) locks the mouse cursor.
   virtual Script cursorOff() {}
   // (%val) 'ctrl p' keybind. On press: hides the HUD and takes a high-detail screenshot, then restores settings.
   virtual Script doScreenShot() {}
   // () Stops the movie frame-grab schedule.
   virtual Script stopMovie() {}
   // (%movieName, %frameNumber) Screenshots one numbered frame and reschedules the next.
   virtual Script movieGrabScreen() {}
   // (%movieName, %fps) Starts grabbing screenshots at %fps to build a movie.
   virtual Script recordMovie() {}
   // (%number) -> string. Zero-pads to 3 digits.
   virtual Script formatSessionNumber() {}
   // (%number) -> string. Zero-pads to 5 digits.
   virtual Script formatImageNumber() {}
   // () Pops the MessagePopupDlg.
   virtual Script CloseMessagePopup() {}
   // (%title, %message, %delay) Shows a popup message box; auto-closes after %delay ms if given.
   virtual Script MessagePopup() {}
   // (%title, %message, %yesCallback, %noCallback) Shows a Yes/No message box with callbacks.
   virtual Script MessageBoxYesNo() {}
   // (%title, %message, %callback, %cancelCallback) Shows an OK/Cancel message box with callbacks.
   virtual Script MessageBoxOKCancel() {}
   // (%title, %message, %callback) Shows an OK message box, eval'ing %callback on dismiss.
   virtual Script MessageBoxOK() {}
   // (%text, %frame, %msg) Sets %msg (center-justified) on text control %text and resizes %frame to fit.
   virtual Script MBSetText() {}
   // (%dlg, %callback) Pops dialog %dlg and evals %callback (message-box button handler).
   virtual Script MessageCallback() {}
   // (%expr) Toggles the FrameOverlayGui debug metrics overlay; %expr selects fps/time/terrain/texture/video/interior/water/vehicle/audio/debug.
   virtual Script metrics() {}
   // () -> string. Debug metrics overlay line (fps + primitives/textures/objects).
   virtual Script debugMetricsCallback() {}
   // () -> string. Audio metrics overlay line (open/looping/active stream counts).
   virtual Script audioMetricsCallback() {}
   // () -> string. Vehicle metrics overlay line (retry/search/poly/vertex counts).
   virtual Script vehicleMetricsCallback() {}
   // () -> string. Time metrics overlay line (sim time, sim time mod 32).
   virtual Script timeMetricsCallback() {}
   // () -> string. Water metrics overlay line (tri/point/haze counts).
   virtual Script waterMetricsCallback() {}
   // () -> string. Texture metrics overlay line (texels loaded, resident %, cache misses).
   virtual Script textureMetricsCallback() {}
   // () -> string. Interior metrics overlay line (primitives, textures, interior count).
   virtual Script interiorMetricsCallback() {}
   // () -> string. Video metrics overlay line (tri/prim counts per pass).
   virtual Script videoMetricsCallback() {}
   // () -> string. Terrain metrics overlay line (mip/texture/fog counts).
   virtual Script terrainMetricsCallback() {}
   // () -> string. FPS metrics overlay line (" FPS: <real>  mspf: <ms>").
   virtual Script fpsMetricsCallback() {}
   // () Callback registered at runtime but not present in the decompiled base scripts or exe symbols; exact purpose unverified (grouped with the editor/tools dialog helpers below).
   virtual Script doSACallback() {}
   // (%filespec, %callback, %currentFile, %overwritePrompt) Opens the native Save-File dialog (stock TGE common file-dialog helper).
   virtual Script getSaveFilename() {}
   // (%filespec, %callback, %currentFile) Opens the native Load-File dialog (stock TGE common file-dialog helper).
   virtual Script getLoadFilename() {}
   // () Populates the file-dialog list control from the current path/filter (stock TGE file-dialog helper).
   virtual Script fillFileList() {}
   // () Opens the scene/object tree inspector (stock TGE tools helper).
   virtual Script Tree() {}
   // () Applies edits from the object inspector back to the selected object (stock TGE tools helper).
   virtual Script InspectApply() {}
   // (%obj) Opens the object inspector on %obj (stock TGE tools helper).
   virtual Script inspect() {}
   // (%make) Toggles the in-game console GUI (ConsoleDlg). Bound to tilde.
   virtual Script ToggleConsole() {}
   // () Dumps all declared console classes to scriptClasses.txt via a ConsoleLogger.
   virtual Script writeOutClasses() {}
   // () Dumps all declared console functions to scriptFunctions.txt via a ConsoleLogger.
   virtual Script writeOutFunctions() {}
   // () lightScene completion callback: finishes phase 3 and sends 'MissionStartPhase3Ack'.
   virtual Script sceneLightingComplete() {}
   // () Polls $SceneLighting::lightingProgress into the loading bar while lighting; reschedules itself.
   virtual Script updateLightingProgress() {}
   // (%seq, %missionName) Server RPC. Phase 3: starts grass/client/foliage replication and scene lighting.
   virtual Script clientCmdMissionStartPhase3() {}
   // () Phase-2 callback: increments $ghostsRecvd and updates phase-2 progress.
   virtual Script onGhostAlwaysObjectReceived() {}
   // (%ghostCount) Phase-2 callback: records the total ghost count to track for.
   virtual Script onGhostAlwaysStarted() {}
   // (%seq, %missionName) Server RPC. Phase 2: purges resources, begins ghost download, sends ack.
   virtual Script clientCmdMissionStartPhase2() {}
   // (%index, %total) Phase-1 callback: reports datablock receive progress.
   virtual Script onDataBlockObjectReceived() {}
   // (%seq, %missionName, %musicTrack) Server RPC. Phase 1: begins datablock/target download, sends ack.
   virtual Script clientCmdMissionStartPhase1() {}
   // (%junk0) Server RPC. Mission ended: stops audio and terminates scene lighting.
   virtual Script clientCmdMissionEnd() {}
   // (%junk0) Server RPC. Mission start (empty stub in this build).
   virtual Script clientCmdMissionStart() {}
   // (%msgType,%msgString,%a1..%a10) Default handler registered for all server messages; routes to onServerMessage.
   virtual Script defaultMessageCallback() {}
   // (%msgType, %func) Registers %func as a callback for server messages of type %msgType (or "" for all).
   virtual Script addMessageCallback() {}
   // (%msgType,%msgString,%a1..%a10) Server RPC. Dispatches a tagged server message to all registered callbacks.
   virtual Script clientCmdServerMessage() {}
   // (%junk0,%voice,%pitch,%msgString,%a1..%a10) Server RPC. Detags the chat string and routes to onChatMessage.
   virtual Script clientCmdChatMessage() {}
   // () Shuts down the OpenAL driver.
   virtual Script OpenALShutdown() {}
   // () (Re)initializes the OpenAL driver and applies master/channel volumes; sets $Audio::initFailed on failure.
   virtual Script OpenALInit() {}
   // () Repaints the Canvas if it exists.
   virtual Script resetCanvas() {}
   // (%windowName) Sets gamma, creates the canvas/window, sets OpenGL prefs, execs core dialog GUIs, inits OpenAL.
   virtual Script initCanvas() {}
   // () Sets Canvas content to MainMenuGui and (unless $Pref::DontUpdate) opens the auto-updater.
   virtual Script loadMainMenu() {}
   // () Initializes the client: execs all client GUIs/scripts, sets net port/FOV, then loads the main menu or startup.
   virtual Script initClient() {}
   // (%modPath) Recursively execs each mod's main.cs from base upward (mod load order).
   virtual Script loadMods() {}
   // () Execs the server-side base scripts (audio, server, commands, mission load/download, game, etc.).
   virtual Script initBaseServer() {}
   // () Execs the client-side base scripts (message, mission, missionDownload, actionMap, scriptDoc).
   virtual Script initBaseClient() {}
   // () Execs the common base scripts (canvas, audio) and seeds the random number generator.
   virtual Script initCommon() {}
   // (%dir) Adds %dir to the mod path and execs %dir/main.cs (root bootstrap helper).
   virtual Script loadDir() {}
   // () Prints the command-line help message (root bootstrap; overridable by mods).
   virtual Script displayHelp() {}
   // () Hook for mods to process command-line args after the engine has parsed them (root bootstrap).
   virtual Script parseArgs() {}
   // () Called from C++ on shutdown; hook for mod cleanup (root bootstrap).
   virtual Script onExit() {}
   // () Called at the end of root main.cs after mods load; hook for mod startup (root bootstrap).
   virtual Script onStart() {}
   // () Activates the script-debugger package / enables debug instrumentation.
   virtual Script doEnableDebug() {}
   // (%list, %delim) -> string. Returns %list with its first %delim-delimited token removed (root bootstrap list helper).
   virtual Script popFront() {}
   // (%list, %token, %delim) -> string. Appends %token to %list using %delim (root bootstrap list helper).
   virtual Script pushBack() {}
   // (%list, %token, %delim) -> string. Prepends %token to %list using %delim (root bootstrap list helper).
   virtual Script pushFront() {}
   virtual void cls() {} // () Clear the console screen.
   virtual string getClipboard() {} // () Get text from the clipboard.
   virtual bool setClipboard() {} // (string text) Set the system clipboard.
   virtual void dumpConsoleClasses() {} // () Dumps all declared console classes to the console.
   virtual void dumpConsoleFunctions() {} // () Dumps all declared console functions to the console.
   virtual string ExpandFilename() {} // (string filename) Expand a path (e.g. "~/...") to a full filename.
   virtual int strcmp() {} // (string one, string two) Case-sensitive string compare.
   virtual int stricmp() {} // (string one, string two) Case-insensitive string compare.
   virtual int strlen() {} // (string str) Length of a string in characters.
   virtual int strstr() {} // (string one, string two) Index of substring two within one, or -1.
   virtual int strpos() {} // (string hay, string needle, int offset=0) Find needle in hay starting offset bytes in.
   virtual string ltrim() {} // (string value) Strip leading whitespace.
   virtual string rtrim() {} // (string value) Strip trailing whitespace.
   virtual string trim() {} // (string value) Strip leading and trailing whitespace.
   virtual string stripChars() {} // (string value, string chars) Remove all of chars from value.
   virtual string strlwr() {} // (string) Convert to lower case.
   virtual string strupr() {} // (string) Convert to upper case.
   virtual string strchr() {} // (string, char) Return the substring from the first occurrence of char onward.
   virtual string strreplace() {} // (string source, string from, string to) Replace all occurrences of from with to.
   virtual string getSubStr() {} // (string str, int start, int numChars) Substring of str from start for up to numChars.
   virtual string getWord() {} // (string text, int index) Return the space-delimited word at index.
   virtual string getWords() {} // (string text, int index, int endIndex=INF) Return words from index to endIndex.
   virtual string setWord() {} // (string text, int index, string replace) Replace the word at index.
   virtual string removeWord() {} // (string text, int index) Remove the word at index.
   virtual int getWordCount() {} // (string text) Number of space-delimited words.
   virtual string getField() {} // (string text, int index) Return the TAB-delimited field at index.
   virtual string getFields() {} // (string text, int index [, int endIndex]) Return fields from index to endIndex.
   virtual string setField() {} // (string text, int index, string replace) Replace the field at index.
   virtual string removeField() {} // (string text, int index) Remove the field at index.
   virtual int getFieldCount() {} // (string text) Number of TAB-delimited fields.
   virtual string getRecord() {} // (string text, int index) Return the newline-delimited record at index.
   virtual string getRecords() {} // (string text, int index [, int endIndex]) Return records from index to endIndex.
   virtual string setRecord() {} // (string text, int index, string replace) Replace the record at index.
   virtual string removeRecord() {} // (string text, int index) Remove the record at index.
   virtual int getRecordCount() {} // (string text) Number of newline-delimited records.
   virtual string firstWord() {} // (string text) Return the first word.
   virtual string restWords() {} // (string text) Return everything after the first word.
   virtual string NextToken() {} // (str, tokenVar, delim) Split off the first token (by delim) into tokenVar; returns the rest.
   virtual string detag() {} // (string textTagString) Resolve a tagged-string reference to its text (receive side).
   virtual string getTag() {} // (string textTagString) Return the numeric tag of a tagged string.
   virtual void echo() {} // (text [, ...]) Print text to the console.
   virtual void warn() {} // (text [, ...]) Print a warning (yellow) to the console.
   virtual void error() {} // (text [, ...]) Print an error (red) to the console.
   virtual string expandEscape() {} // (string text) Escape special characters in text.
   virtual string collapseEscape() {} // (string text) Unescape escaped characters in text.
   virtual void setLogMode() {} // (int mode) Set console logfile behavior (see main.cs comments).
   virtual void setEchoFileLoads() {} // (bool) Toggle echoing of file loads to the console.
   virtual void quit() {} // () End execution of Torque.
   virtual string call() {} // (string consoleFunction, args..) call torque script function with args
   virtual bool compile() {} // (string fileName) Compile a .cs file to a .dso.
   virtual bool exec() {} // (string fileName [, bool nocalls [, bool journalScript]]) Execute a script file.
   virtual string eval() {} // (string consoleString) Evaluate a string of TorqueScript and return the result.
   virtual void export() {} // (string searchString [, string fileName [, string append]]) export (dump) global variables matching searchString to file/console
   virtual void deleteVariables() {} // (string pattern) A string pattern that specifies which variables to delete. The pattern can include wildcard characters (*)
   virtual void trace() {} // (bool) Enable/disable function-call tracing.
   virtual string findFirstFile() {} // (string pattern) Returns the first file in the directory system matching the given pattern.
   virtual string findNextFile() {} // (string pattern) Returns the next file matching a search begun in findFirstFile.
   virtual int getFileCount() {} // (string pattern) Returns the number of files in the directory tree that match the given pattern
   virtual int getFileCRC() {} // (string filename) CRC32 of a file's contents.
   virtual int getStringCRC() {} // (string value) CRC32 of a string (used to hash passwords before sending).
   virtual void WinExec() {} // (string command) Launch an external program / batch file (Windows ShellExecute).
   virtual bool isFile() {} // (string filepath) Returns true if file exists otherwise false
   virtual bool isWriteableFileName() {} // (string filepath) check if file path is writeable
   virtual string fileExt() {} // (string fileName) Return the file extension (with dot).
   virtual string fileBase() {} // (string fileName) Return the base name (no path, no extension).
   virtual string fileName() {} // (string filePathName) Return the file name (no path).
   virtual string filePath() {} // (string fileName) Return the directory path (no file name).
   virtual void backtrace() {} // () Print the current script call stack.
   virtual bool isPackage() {} // (string packageName) True if the named package exists.
   virtual void activatePackage() {} // (string packageName) Activate (push) a package's function overrides.
   virtual void deactivatePackage() {} // (string packageName) Deactivate (pop) a package.
   virtual int nameToID() {} // (string object) Return the numeric SimObject ID for a name, or -1.
   virtual bool isObject() {} // (string object) True if the object exists.
   virtual void cancel() {} // (int eventId) Cancel a pending scheduled event.
   virtual bool isEventPending() {} // (int scheduleId) True if a scheduled event is still pending.
   virtual int schedule() {} // (time, refobject|0, command, <arg1...argN>) Schedule a console command after time ms; returns event id.
   virtual void deleteDataBlocks() {} // () Delete all downloaded datablocks (mission-change cleanup).
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
   virtual void setNPatch() {} // (float) Set the N-Patch (curved surface) tessellation level.
   virtual void toggleNPatch() {} // () Toggle N-Patch tessellation on/off.
   virtual void increaseNPatch() {} // () Increase the N-Patch tessellation level.
   virtual void decreaseNPatch() {} // () Decrease the N-Patch tessellation level.
   virtual int png2jpg() {} // (string pngName [, int quality=0-100]) Convert a PNG file to JPEG.
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
   virtual bool addMaterialMapping() {} // (string matName, ...) Set up a material mapping. See MaterialPropertyMap for details.
   virtual int aiConnect() {} // (...) Make a new AIConnection and pass args to the onConnect script callback.
   virtual void setPowerAudioProfiles() {} // (AudioProfile powerUp, AudioProfile powerDown) Set the ambient audio manager's power up/down profiles.
   virtual bool screenShot() {} // Take a screenshot. (string file, string format -- format One of JPEG or PNG.)
   virtual void gotoWebPage() {} // (string address) Open a web page in the user's default browser.
   virtual void deactivateDirectInput() {} // () Ungrab the mouse so the user can do other things.
   virtual void activateDirectInput() {} // () Grab the mouse again so the user can play.
   virtual void purgeResources() {} // Use the purgeResources function to purge all game resources (is called from mission phase loads)
   virtual bool lightScene() {} // (script_function completeCallback=NULL, string mode="") Relight the scene; mode "forceAlways"/"forceWritable".
   virtual string strToPlayerName() {} // (string) Convert a string to a valid player name.
   virtual string stripTrailingSpaces() {} // (string) Strip trailing spaces from a string.
   virtual void flushTextureCache() {} // () Flush the texture cache.
   virtual void setDefaultFov() {} // (float defaultFov) Set the camera's default field of view.
   virtual void setZoomSpeed() {} // (int speed) Set the zoom speed in ms per 90``deg FOV change.
   virtual void setFov() {} // (float fov) Set the camera's field of view.
   virtual string getControlObjectAltitude() {} // () Distance from the bottom of the controlled object to the terrain.
   virtual string getControlObjectSpeed() {} // () Speed (not velocity) of the controlled object.
   virtual void panoramaScreenShot() {} // (string file, string format) Take a panoramic screenshot (format JPEG or PNG).
   virtual string containerFindFirst() {} // (bitset type, Point3F point, float x,y,z) First object of type in a box; iterate with containerFindNext.
   virtual string containerFindNext() {} // () Next result from a previous containerFindFirst().
   virtual void snapeToggle() {} // () Toggle snap (editor grid snapping).
   virtual void lockMouse() {} // (bool isLocked) Lock/unlock the mouse to the window.
   virtual bool setNetPort() {} // (int port) Set the network port for the game to use.
   virtual bool createCanvas() {} // (string windowTitle) Create the game window/canvas with the given title.
   virtual void saveJournal() {} // (string filename) Save the input journal to a file.
   virtual void playJournal() {} // (string filename, bool break=false) Play back an input journal.
   virtual void setModPaths() {} // (string paths) Set the semicolon-delimited mod search paths.
   virtual string getModPaths() {} // () Return the current mod search paths.
   virtual int getVersionNumber() {} // () Engine build version number.
   virtual string getVersionString() {} // () Engine build version as a string.
   virtual string getCompileTimeString() {} // () Time the engine was compiled.
   virtual string getBuildString() {} // () Build type, "Debug" or "Release".
   virtual int getSimTime() {} // () Current sim time in ms (since the game started).
   virtual int getRealTime() {} // () Current real time in ms (platform-defined epoch).
   virtual void setShadowDetailLevel() {} // (float val 0..1) Set the shadow detail level.
   virtual void showShapeLoad() {} // (string shapeName, bool faceCamera) Show tool: load a shape.
   virtual void showSequenceLoad() {} // (string sequenceFile [, string sequenceName]) Show tool: load a sequence.
   virtual void showSelectSequence() {} // () Show tool: select the active sequence.
   virtual void showSetDetailSlider() {} // () Show tool: configure the detail slider.
   virtual void showUpdateThreadControl() {} // () Show tool: refresh the thread control UI.
   virtual void showPlay() {} // (int threadNum=-1) Show tool: play a thread.
   virtual void showStop() {} // (int threadNum=-1) Show tool: stop a thread.
   virtual void showSetScale() {} // (int threadNum, float scale) Show tool: set a thread's playback scale.
   virtual void showSetPos() {} // (int threadNum, float pos) Show tool: set a thread's position.
   virtual void showNewThread() {} // () Show tool: create a new thread.
   virtual void showDeleteThread() {} // (int threadNum) Show tool: delete a thread.
   virtual void showToggleRoot() {} // () Show tool: toggle root animation.
   virtual void showToggleStick() {} // () Show tool: toggle "stick" (freeze) of the shape.
   virtual void showSetCamera() {} // (char orbitShape) Show tool: 't'/'T' to orbit, else free-fly.
   virtual void showSetKeyboard() {} // (char moveShape) Show tool: set keyboard control ('t' or 'T').
   virtual void showTurnLeft() {} // (float amt) Show tool: turn the view left by amt.
   virtual void showTurnRight() {} // (float amt) Show tool: turn the view right by amt.
   virtual void showSetLightDirection() {} // () Show tool: set the light direction.
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
   virtual void getDayFraction() {} // () Fraction of the current day/night cycle elapsed (AoT sun/sky helper).
   virtual float calcExplosionCoverage() {} // (Point3F source, SceneObject originator, bitset coverageMask) Fraction of an object visible to an explosion at source.
   virtual void setColorTable() {} // (string name, colors...) Set the active brick/print color (paint) table (AoT/Blockland brick engine).
   virtual void setSprayCanDivision() {} // (int slot) Select the active spray-can color division/slot (AoT brick engine).
   virtual string getSprayCanDivisionName() {} // (int slot) Name of a spray-can color division (AoT brick engine).
   virtual int getSprayCanDivisionSlot() {} // (string name) Slot index of a named spray-can color division (AoT brick engine).
   virtual void setPrintTexture() {} // (string texture) Set the active brick "print" (decal) texture (AoT brick engine).
   virtual string getPrintTexture() {} // () Current brick print texture (AoT brick engine).
   virtual string getColorIDTable() {} // () Return the brick color-ID table (AoT/Blockland brick engine).
   virtual void updateTempBrickSettings() {} // () Apply pending temporary brick build settings (color/print/etc.) (AoT brick engine).
   virtual void StartFoliageReplication() {} // () Begin client-side foliage replication for the mission.
   virtual void StartGrassReplication() {} // () Begin client-side grass replication for the mission.
   virtual void StartClientReplication() {} // () Begin client-side object (brick) replication for the mission.
   virtual void StartServerReplication() {} // () Begin server-side object replication for the mission.
   virtual void StartSurfaceReferencer() {} // () Start the surface referencer (terrain/interior surface indexing) (AoT engine).
   virtual void commandToServer() {} // (string func, ...) Send a command (RPC) to the server.
   virtual void commandToClient() {} // (NetConnection client, string func, ...) Send a command (RPC) to a client.
   virtual void removeTaggedString() {} // (int tag) Decrement/remove a tagged string by tag.
   virtual string addTaggedString() {} // (string str) Register str in the net string table; returns its tag (send side).
   virtual string getTaggedString() {} // (int tag) Resolve a tag to its string (send side; see detag for receive side).
   virtual string buildTaggedString() {} // (string format, ...) Build a tagged string with %1..%9 substitutions.
   virtual void msg() {} // (NetConnection id, string message) Send a SimpleNetObject message to a connection.
   virtual void queryLanServers() {} // (port, flags, gameType, missionType, minPlayers, maxPlayers, ...) Query servers on the LAN.
   virtual void queryMasterServer() {} // (flags, gameType, missionType, minPlayers, maxPlayers, ...) Query the master server for game servers.
   virtual void querySingleServer() {} // (address, flags) Query a single server by address.
   virtual void cancelServerQuery() {} // () Cancel the in-progress server query.
   virtual void stopServerQuery() {} // () Stop the in-progress server query.
   virtual void startHeartbeat() {} // () Begin sending heartbeats to the master server (dedicated server).
   virtual void stopHeartbeat() {} // () Stop sending master-server heartbeats.
   virtual int getServerCount() {} // () Number of servers found by the last query.
   virtual bool setServerInfo() {} // (int index) Load the query result at index into the $ServerInfo:: vars.
   virtual string StripMLControlChars() {} // (string val) Strip TorqueML control characters, returning a clean string.
   virtual bool isPointInside() {} // (Point3F pos) or (float x, float y, float z) True if the point is inside the world container.
   virtual string VectorAdd() {} // (Vector3F a, Vector3F b) Returns a+b.
   virtual string VectorSub() {} // (Vector3F a, Vector3F b) Returns a-b.
   virtual string VectorScale() {} // (Vector3F a, float scalar) Returns a*scalar.
   virtual string VectorNormalize() {} // (Vector3F a) Returns a scaled to unit length.
   virtual float VectorDot() {} // (Vector3F a, Vector3F b) Dot product of a and b.
   virtual string VectorCross() {} // (Vector3F a, Vector3F b) Cross product of a and b.
   virtual float VectorDist() {} // (Vector3F a, Vector3F b) Distance between a and b.
   virtual float VectorLen() {} // (Vector3F v) Length of v.
   virtual string VectorOrthoBasis() {} // (AngAxisF aaf) Build an orthogonal basis matrix from the given angle/axis vector.
   virtual string MatrixCreate() {} // (Vector3F pos, Vector3F rot) Build a transform matrix from translation and rotation.
   virtual string MatrixCreateFromEuler() {} // (Vector3F e) Build a matrix from Euler rotations.
   virtual string MatrixMultiply() {} // (Matrix4F left, Matrix4F right) Multiply two matrices.
   virtual string MatrixMulVector() {} // (MatrixF xfrm, Point3F vector) Multiply the vector by the transform.
   virtual string MatrixMulPoint() {} // (MatrixF xfrm, Point3F pnt) Multiply pnt by the transform.
   virtual string getBoxCenter() {} // (Box b) Center point of a box.
   virtual void setRandomSeed() {} // (int seed=-1) Set the RNG seed; uses current time if omitted.
   virtual int getRandomSeed() {} // () Current random seed.
   virtual float getRandom() {} // (int a=1, int b=0) Random number between a and b.
   virtual float getGaussian() {} // ([float mean=0, float stdDev=1]) Random number with a Gaussian/normal distribution.
   virtual string mSolveQuadratic() {} // (a, b, c) Solve a*x^2+b*x+c=0; returns "sol x0 x1".
   virtual string mSolveCubic() {} // (a, b, c, d) Solve a*x^3+...=0; returns "sol x0 x1 x2".
   virtual string mSolveQuartic() {} // (a, b, c, d, e) Solve a*x^4+...=0; returns "sol x0 x1 x2 x3".
   virtual int mFloor() {} // (float v) Round v down to the nearest integer.
   virtual int mCeil() {} // (float v) Round v up to the nearest integer.
   virtual string mFloatLength() {} // (float v, int numDecimals) Format v with numDecimals decimal places.
   virtual float mAbs() {} // (float v) Absolute value.
   virtual float mSqrt() {} // (float v) Square root.
   virtual float mPow() {} // (float b, float p) b raised to the power p.
   virtual float mLog() {} // (float v) Natural logarithm.
   virtual float mSin() {} // (float th) Sine of th (radians).
   virtual float mCos() {} // (float th) Cosine of th (radians).
   virtual float mTan() {} // (float th) Tangent of th (radians).
   virtual float mAsin() {} // (float th) Arc-sine (radians).
   virtual float mAcos() {} // (float th) Arc-cosine (radians).
   virtual float mAtan() {} // (float rise, float run) Arc-tangent (slope) of a line (radians).
   virtual float mRadToDeg() {} // (float radians) Convert radians to degrees.
   virtual float mDegToRad() {} // (float degrees) Convert degrees to radians.
   virtual void FreeMemoryDump() {} // () Dump free-memory statistics (debug).
   virtual bool redbookOpen() {} // (string device=NULL) Open a Redbook (CD audio) device.
   virtual bool redbookClose() {} // () Close the current Redbook device.
   virtual bool redbookPlay() {} // (int track) Play the selected CD track.
   virtual bool redbookStop() {} // () Stop CD playback.
   virtual int redbookGetTrackCount() {} // () Number of CD tracks.
   virtual float redbookGetVolume() {} // () Current CD volume.
   virtual bool redbookSetVolume() {} // (float volume) Set CD playback volume.
   virtual int redbookGetDeviceCount() {} // () Number of Redbook devices.
   virtual string redbookGetDeviceName() {} // (int index) Name of a Redbook device.
   virtual string redbookGetLastError() {} // () Explanation of the last Redbook error.
   virtual bool setDisplayDevice() {} // (string deviceName, int width, int height=NULL, int bpp=NULL, bool fullScreen=NULL) Set the display device/mode.
   virtual bool setScreenMode() {} // ( int width, int height, int bpp, bool fullScreen )
   virtual bool toggleFullScreen() {} // () Toggle full-screen mode.
   virtual bool isFullScreen() {} // () True if running full-screen.
   virtual bool switchBitDepth() {} // () Switch between 16 and 32 bits (full screen only).
   virtual bool prevResolution() {} // () Switch to the previous resolution.
   virtual bool nextResolution() {} // () Switch to the next resolution.
   virtual string getRes() {} // () Current "width height bpp".
   virtual bool setRes() {} // (int width, int height, int bpp=NULL) Set the resolution.
   virtual string getDisplayDeviceList() {} // () TAB-delimited list of display devices.
   virtual string getResolutionList() {} // (string deviceName) List of supported resolutions for a device.
   virtual string getVideoDriverInfo() {} // () Video driver info string.
   virtual bool isDeviceFullScreenOnly() {} // (string deviceName) True if the device only supports full-screen.
   virtual void videoSetGammaCorrection() {} // (float gamma) Set gamma correction.
   virtual bool setVerticalSync() {} // (bool f) Enable/disable vsync.
   virtual void profilerMarkerEnable() {} // (string markerName, bool enable) Enable/disable a profiler marker.
   virtual void profilerEnable() {} // (bool enable) Enable/disable the profiler.
   virtual void profilerDump() {} // () Dump current profiler state to the console.
   virtual void profilerDumpToFile() {} // (string filename) Dump profiler stats to a file.
   virtual void profilerReset() {} // () Reset all profiler data.
   virtual void enableWinConsole() {} // (bool enable) Show/hide the separate Windows console window.
   virtual bool activateKeyboard() {} // () Activate keyboard input capture.
   virtual void deactivateKeyboard() {} // () Deactivate keyboard input capture.
   virtual bool enableMouse() {} // () Enable mouse input.
   virtual void disableMouse() {} // () Disable mouse input.
   virtual bool enableJoystick() {} // () Enable joystick input.
   virtual void disableJoystick() {} // () Disable joystick input.
   virtual void echoInputState() {} // () Echo the current input device state to the console.
   virtual bool isJoystickDetected() {} // () True if a joystick is present.
   virtual string getJoystickAxes() {} // (handle instance) Current joystick axis values.
   virtual void mathInit() {} // (DETECT|C|FPU|MMX|3DNOW|SSE|...) Install the math library with the given extensions.
   virtual void addCardProfile() {} // (vendor, renderer, ... , proFile) Register a video card profile with the card profile manager.
   virtual void addOSCardProfile() {} // (vendor, renderer, allowOpenGL, allowD3D, preferOpenGL) Register OS-specific card rendering preferences.
   virtual string getDesktopResolution() {} // () The desktop resolution "width height bpp".
   virtual bool isKoreanBuild() {} // () True if this is a Korean localization build.
   virtual void resetLighting() {} // () Reset GL lighting.
   virtual void allowConnections() {} // (bool) Allow or disallow incoming network connections.
   virtual void clearServerPaths() {} // () Clear cached server path information.
   virtual void pathOnMissionLoadDone() {} // () Load all path information from interiors after mission load.
   virtual void makeTestTerrain() {} // (string fileName, ...materials) Generate a test terrain file.
   virtual float getTerrainHeight() {} // (Point2I pos) Terrain height at the given position.
   virtual bool OpenALInitDriver() {} // () Initialize the OpenAL driver (call before any sounds).
   virtual void OpenALShutdownDriver() {} // () Shut down the OpenAL driver.
   virtual void OpenALRegisterExtensions() {} // () Register available OpenAL extensions.
   virtual string alGetString() {} // (string item) Wraps alGetString (AL_VENDOR/AL_VERSION/AL_RENDERER/AL_EXTENSIONS).
   virtual int alxGetWaveLen() {} // (string filename) Length of a wav file in milliseconds.
   virtual int alxCreateSource() {} // (profile) | (profile, x,y,z) | (description, filename) | (description, filename, x,y,z) Create an audio source; returns handle.
   virtual void alxSourcef() {} // (handle, ALenum, value) Set a float source property (e.g. AL_PITCH).
   virtual void alxSource3f() {} // (handle, ALenum, x, y, z) Set a 3-float source property.
   virtual void alxSourcei() {} // (handle, ALenum, value) Set an int source property.
   virtual float alxGetSourcef() {} // (handle, ALenum) Get a float source property.
   virtual string alxGetSource3f() {} // (handle, ALenum) Get a 3-float source property.
   virtual int alxGetSourcei() {} // (handle, ALenum) Get an int source property.
   virtual int alxPlay() {} // (handle) | (profile) | (profile, x,y,z) Play a source/profile; returns handle.
   virtual void alxStop() {} // (int handle) Stop a playing source.
   virtual void alxStopAll() {} // () Stop all playing sources.
   virtual bool alxIsPlaying() {} // (handle) True if the source is playing.
   virtual void alxListenerf() {} // (ALenum, value) Set a float listener property (e.g. AL_GAIN_LINEAR).
   virtual void alListener3f() {} // (ALenum, "x y z") | (ALenum, x, y, z) Set a 3-float listener property.
   virtual float alxGetListenerf() {} // (ALenum) Get a float listener property.
   virtual string alGetListener3f() {} // (ALenum) Get a 3-float listener property.
   virtual int alGetListeneri() {} // (ALenum) Get an int listener property.
   virtual int alxGetChannelVolume() {} // (int channel_id) Volume of an audio channel.
   virtual bool alxSetChannelVolume() {} // (int channel_id, float volume) Set an audio channel's volume (0.0-1.0).
};
```
