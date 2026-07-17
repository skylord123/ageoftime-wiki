# Global Variables Dump

This page is a dump of the global (`$`) TorqueScript variables present in the
*Age of Time* client at runtime, captured by exporting everything matching
`$*` from the in-game console. The entries below have been annotated with
descriptions of what each variable (or variable family) does.

!!! note "Snapshot, not a spec"
    These values are a **snapshot** taken from one running client. Many are
    session- or mission-specific (inventory IDs, FPS counters, the current
    mission file, audio handles, etc.) and will differ on your machine. Treat
    the list as a guide to which variables exist and their rough shape, not as
    fixed values.

!!! tip "Reproducing this dump"
    Open the in-game console and dump every global to the console:

    ```
    export("$*");
    ```

    Or write them to a file instead:

    ```
    export("$*", "base/variables.txt", false);
    ```

!!! info "A few interesting ones"
    - `$TSControl::frameCount` — increments every time a frame is drawn.
    - `$fps::real` / `$fps::virtual` — actual vs. time-scaled framerate.
    - The `$mv*` family **is** the player's input — set them from script to
      drive the player programmatically (see the annotations below).

```torquescript
// OpenGL capability flag, set once at startup by the renderer (winGL.cc).
// 1 = the GPU/driver supports anisotropic texture filtering. See the other
// *Supported flags below ($FogCoordSupported, $PalettedTextureSupported,
// $SwapIntervalSupported, $TextureCompressionSupported) - same mechanism.
$AnisotropySupported = "1";

// AutoUpdate dialog behavior flag (autoUpdate.cs / init.cs).
// 1 = the AutoUpdateGui closes itself automatically once the update check
// finishes; set to 0/false when the dialog is opened manually from the main
// menu so it stays open for the user.
$AU_AutoClose = 1;

// Sim handle of the sound currently playing from the audio options "test"
// button; 0 when nothing is playing. Used so a new test can stop the old one.
$AudioTestHandle = 0;

// 1 while a bottomPrint() HUD message is on screen, 0 otherwise (centerPrint.cs).
// Prevents overlapping bottom-of-screen prints.
$bottomPrintActive = 0;

// Fly/spectator (engine Camera object) movement speed in world units.
$Camera::movementSpeed = "40";

// Current camera field of view, in degrees.
$cameraFov = "90";

// --- Create Character GUI (CreateCharacterGui.cs) ---
// $CCG_MaxPoints   = total ability points you get to spend in the character
//                    creator.
// $CCG_Preset<Class>_<Stat> = flattened form of $CCG_Preset[Class, Stat]; the
//                    default point spread applied when you pick a class preset
//                    (Warrior / Archer / Mage) instead of distributing by hand.
$CCG_MaxPoints = 22;
$CCG_PresetArcher_Agility = 5;
$CCG_PresetArcher_Dexterity = 10;
$CCG_PresetArcher_Strength = 10;
$CCG_PresetMage_Agility = 5;
$CCG_PresetMage_Intelligence = 10;
$CCG_PresetMage_Wisdom = 10;
$CCG_PresetWarrior_Agility = 5;
$CCG_PresetWarrior_Stamina = 10;
$CCG_PresetWarrior_Strength = 10;

// 1 while a centerPrint() HUD message is on screen, 0 otherwise (centerPrint.cs).
$centerPrintActive = 0;

// Box/font heights (px) for the three centerPrint size levels
// (1 = small, 2 = medium, 3 = large). Flattened $CenterPrintSizes[n].
$CenterPrintSizes1 = 20;
$CenterPrintSizes2 = 36;
$CenterPrintSizes3 = 56;

// --- Client-side server query / join state ---
// $Client::GameTypeQuery / $Client::MissionTypeQuery are filters used when
// querying servers in the browser (LAN / master). $Client::MissionFile is the
// .mis mission the client last loaded / is currently loading.
$Client::GameTypeQuery = "AgeOfTime";
$Client::MissionFile = "base/data/missions/port.mis";
$Client::MissionTypeQuery = "Any";

// --- Client inventory (inventory.cs / brickSelectorDlg.cs) ---
// $numClientInvSlots = how many inventory slots are currently occupied. Walk
// the inventory with: for(%i = 0; %i < $numClientInvSlots; %i++).
// Each $clientInv<N> points to a "ClientInventorySO" ScriptObject describing
// one stack of items. Note: a slot index is NOT a stable identity - removing a
// stack deletes its object and COMPACTS the list (higher slots shift down,
// $numClientInvSlots drops by one). Use the serverID field as the stable handle.
// The useful data lives in these dynamic fields (set by the inventory sync cmds):
//   serverID      = "34020"       - The stack's stable server-side ID. This is
//                   the value you pass to server commands (use, Discard,
//                   SetQuickSlot, ...) and the only reliable way to identify a
//                   stack across inventory changes. It is a FIELD, not a Torque
//                   object id (so 34020.dump() will not work).
//   inUse         = "0"           - 1 if the item is currently equipped/active, else 0.
//   name          = "W. Pants"    - Display name of the item.
//   baseID        = "277"         - The item's base item / datablock ID (its type).
//                   Many stacks can share one baseID; serverID is unique per stack.
//   quantity      = "1"           - How many of the item are in this stack.
//   dyeColor      = "0 127 0 255" - The stack's dye color as "R G B A" (0-255 each).
//   ActiveBitmap  = "12206"       - Tagged-string ID for the item's "active" inventory icon.
//   InUseBitmap   = "12207"       - Tagged-string ID for the icon shown while in use.
//   quantityLabel = "12210"       - Tagged-string ID used to render the stack's quantity label.
//   mat1 - mat4   = "24"          - The item's material / ingredient slots. For crafted
//                   or dyed items these reference the materials used; for simple
//                   items they tend to repeat a single value.
// $BSD_CurrClickIndex (set elsewhere) = slot of the item last clicked in the
// inventory UI; $clientInv[$BSD_CurrClickIndex] is that selected ScriptObject.
// See also $serverToClientInv<serverID> below for the reverse (serverID -> object) lookup.
$clientInv0 = "4046";
$clientInv1 = "4047";
$clientInv10 = "4086";
$clientInv11 = "4087";
$clientInv2 = "4048";
$clientInv3 = "4049";
$clientInv4 = "4050";
$clientInv5 = "4051";
$clientInv6 = "4062";
$clientInv7 = "4063";
$clientInv8 = "4074";
$clientInv9 = "4085";

// --- Collision debug visualization (engine) ---
// Developer toggles to render/debug collision geometry. All 0 in normal play;
// they enable drawing collision boxes and testing the various poly-list paths.
$Collision::boxSize = "2";
$Collision::depthRender = "0";
$Collision::depthSort = "0";
$Collision::renderAlways = "0";
$Collision::testClippedPolyList = "0";
$Collision::testDepthSortList = "0";
$Collision::testExtrudedPolyList = "0";
$Collision::testPolytope = "0";

// --- Console subsystem (engine) ---
// $Con::File   = .gui used for the in-game console dialog.
// $Con::logBufferEnabled = keep a console log buffer (for console.log).
// $Con::printLevel = verbosity threshold for printed messages.
// $Con::prompt = console input prompt string.
// $Con::Root   = root mod directory ("base").
// $Con::warnUndefinedVariables = warn when reading an unset global (0 = off).
$Con::File = "base/ui/ConsoleDlg.gui";
$Con::logBufferEnabled = "1";
$Con::printLevel = "10";
$Con::prompt = "% ";
$Con::Root = "base";
$Con::warnUndefinedVariables = "0";

// The client's active GameConnection (ServerConnection) to the server, created
// on join (JoinServerGui.cs / manualjoin.cs). 2468 = the connection's object ID.
$conn = 2468;

// 1 if the in-game console dialog is currently open.
$ConsoleActive = 1;

// Active mod directory (TGE mod-loading). Used to build paths e.g. for
// recordings ($currentMod/recordings/*.rec).
$currentMod = "editor";

// 1 if the mouse cursor currently drives the UI (vs. locked for mouselook).
$cursorControlled = 1;

// Mod load list bootstrapped at startup (TGE mod chain): "editor;characters".
$defaultGame = "editor;characters";

// 1 if the help overlay/screen is currently displayed.
$displayHelp = 0;

// 1 to enable DirectInput (keyboard/mouse/joystick) capture on Windows.
$enableDirectInput = "1";

// --- Keyboard modifier bitmasks (engine input) ---
// Bit constants OR'd together to describe which modifier keys are held when an
// input event is matched against the action map. SHIFT/CTRL/ALT are the
// generic (either side) masks; L*/R* are the left/right-specific keys.
$EventModifier::ALT = "48";
$EventModifier::CTRL = "12";
$EventModifier::LALT = "16";
$EventModifier::LCTRL = "4";
$EventModifier::LSHIFT = "1";
$EventModifier::RALT = "32";
$EventModifier::RCTRL = "8";
$EventModifier::RSHIFT = "2";
$EventModifier::SHIFT = "3";

// Far clip / max render distance in world units.
$farDistance = "600";

// 1 = first-person camera, 0 = third-person.
$firstPerson = "1";

// OpenGL capability flag (EXT_fog_coord). See $AnisotropySupported.
$FogCoordSupported = "1";

// Current framerate. real = actual frames/sec, virtual = adjusted by the
// engine time scale (slow-mo/fast-forward).
$fps::real = "152.7";
$fps::virtual = "173.7";

// Process command-line arguments (engine main.cc). argc = count,
// argv0 = the executable path.
$Game::argc = "1";
$Game::argv0 = "C:\\Program Files (x86)\\AgeOfTimeOriginal\\AgeOfTime.exe";

// --- TelnetDebugger / remote script debugger (engine) ---
// Enable flag, password, and TCP port for attaching a remote TorqueScript
// debugger to the running client.
$GameDebugEnable = 0;
$GameDebugPassword = "password";
$GameDebugPort = 28040;

// ============================================================================
// Graphics-Detail presets ($GD_*) - optionsDlg.cs
// ----------------------------------------------------------------------------
// These are the built-in quality presets. $GD_<Setting><Level> is the
// flattened form of $GD_<Setting>[level], where level 1..5 runs from lowest to
// highest quality (chosen via SetGraphicDetail() / the "Select Detail" dialog,
// SelectDetailGui.gui). Applying a preset copies these values into the
// matching live $pref::* graphics variables. Each "Setting" family below is one
// rendering option swept across the 5 levels.
// ============================================================================
$GD_Anisotropy1 = 0;
$GD_Anisotropy2 = 0;
$GD_Anisotropy3 = 0;
$GD_Anisotropy4 = 4;
$GD_Anisotropy5 = 32;
$GD_CloudsOn1 = 0;
$GD_CloudsOn2 = 1;
$GD_CloudsOn3 = 1;
$GD_CloudsOn4 = 1;
$GD_CloudsOn5 = 1;
$GD_DecalsOn1 = 0;
$GD_DecalsOn2 = 0;
$GD_DecalsOn3 = 1;
$GD_DecalsOn4 = 1;
$GD_DecalsOn5 = 1;
$GD_EnvironmentMaps1 = 0;
$GD_EnvironmentMaps2 = 0;
$GD_EnvironmentMaps3 = 0;
$GD_EnvironmentMaps4 = 0;
$GD_EnvironmentMaps5 = 1;
$GD_Interior_DynamicLights1 = 0;
$GD_Interior_DynamicLights2 = 0;
$GD_Interior_DynamicLights3 = 1;
$GD_Interior_DynamicLights4 = 1;
$GD_Interior_DynamicLights5 = 1;
$GD_Interior_ShowEnvironmentMaps1 = 0;
$GD_Interior_ShowEnvironmentMaps2 = 0;
$GD_Interior_ShowEnvironmentMaps3 = 0;
$GD_Interior_ShowEnvironmentMaps4 = 1;
$GD_Interior_ShowEnvironmentMaps5 = 1;
$GD_PrecipitationOn1 = 0;
$GD_PrecipitationOn2 = 0;
$GD_PrecipitationOn3 = 1;
$GD_PrecipitationOn4 = 1;
$GD_PrecipitationOn5 = 1;
$GD_RenderMyItems1 = 1;
$GD_RenderMyItems2 = 1;
$GD_RenderMyItems3 = 1;
$GD_RenderMyItems4 = 1;
$GD_RenderMyItems5 = 1;
$GD_RenderMyPlayer1 = 0;
$GD_RenderMyPlayer2 = 0;
$GD_RenderMyPlayer3 = 1;
$GD_RenderMyPlayer4 = 1;
$GD_RenderMyPlayer5 = 1;
$GD_Shadows1 = 0;
$GD_Shadows2 = 0;
$GD_Shadows3 = 0;
$GD_Shadows4 = 1;
$GD_Shadows5 = 1;
$GD_Terrain_DynamicLights1 = 0;
$GD_Terrain_DynamicLights2 = 0;
$GD_Terrain_DynamicLights3 = 1;
$GD_Terrain_DynamicLights4 = 1;
$GD_Terrain_DynamicLights5 = 1;
$GD_Terrain_EnableDetails1 = 0;
$GD_Terrain_EnableDetails2 = 1;
$GD_Terrain_EnableDetails3 = 1;
$GD_Terrain_EnableDetails4 = 1;
$GD_Terrain_EnableDetails5 = 1;
$GD_Terrain_EnableEmbossBumps1 = 0;
$GD_Terrain_EnableEmbossBumps2 = 0;
$GD_Terrain_EnableEmbossBumps3 = 0;
$GD_Terrain_EnableEmbossBumps4 = 0;
$GD_Terrain_EnableEmbossBumps5 = 1;
// ScreenError: terrain LOD tolerance in pixels - higher = coarser terrain.
$GD_Terrain_ScreenError1 = 25;
$GD_Terrain_ScreenError2 = 10;
$GD_Terrain_ScreenError3 = 6;
$GD_Terrain_ScreenError4 = 4;
$GD_Terrain_ScreenError5 = 1;
// TexDetail: terrain texture-detail level (0 = best, higher = lower-res).
$GD_Terrain_TexDetail1 = 3;
$GD_Terrain_TexDetail2 = 2;
$GD_Terrain_TexDetail3 = 1;
$GD_Terrain_TexDetail4 = 0;
$GD_Terrain_TexDetail5 = 0;
$GD_Trilinear1 = 0;
$GD_Trilinear2 = 0;
$GD_Trilinear3 = 0;
$GD_Trilinear4 = 1;
$GD_Trilinear5 = 1;
// TS_DetailAdjust: TSShape (3D model) detail bias - higher keeps high LODs longer.
$GD_TS_DetailAdjust1 = 0.2;
$GD_TS_DetailAdjust2 = 0.5;
$GD_TS_DetailAdjust3 = 0.5;
$GD_TS_DetailAdjust4 = 0.75;
$GD_TS_DetailAdjust5 = 1;
$GD_TS_FogTexture1 = 0;
$GD_TS_FogTexture2 = 0;
$GD_TS_FogTexture3 = 0;
$GD_TS_FogTexture4 = 0;
$GD_TS_FogTexture5 = 1;
// VisibleDistanceMod: multiplier applied to the mission's visible distance.
$GD_VisibleDistanceMod1 = 0.5;
$GD_VisibleDistanceMod2 = 0.85;
$GD_VisibleDistanceMod3 = 1;
$GD_VisibleDistanceMod4 = 1;
$GD_VisibleDistanceMod5 = 1;

// Mission-load phase 2 (ghost download) progress (missionDownload.cs).
// $ghostCount  = total "ghost" (networked) objects the server will send.
// $ghostsRecvd = how many have arrived so far; the ratio drives the loading bar.
$ghostCount = "304";
$ghostsRecvd = 304;

// GUI system files: clipboard cache and the font cache directory.
$Gui::clipboardFile = "base/ui/cache/clipboard.gui";
$Gui::fontCacheDirectory = "base/ui/cache";

// Audio description "type" IDs used when playing sounds, so volume/effects are
// routed to the right channel group: $GuiAudioType (UI), $SimAudioType (world),
// $MessageAudioType (chat/voice messages). Compare $SimAudioType / $MessageAudioType below.
$GuiAudioType = 1;

// Leftover scratch global from a script loop (a stray $i counter). Harmless.
$i = 1;

// Engine Item-class network warp interpolation bounds (ticks). When a dropped/
// world item's position is corrected over the network, the client smooths
// ("warps") it over between min and max ticks instead of snapping.
$Item::maxWarpTicks = "3";
$Item::minWarpTicks = "0.5";

// chatHud.cs: recipient/target tag of the last HUD message line pushed; reset
// to 0 right after each line is added.
$LastHudTarget = 0;

// Scene-lighting bake state (mission.cs / missionDownload.cs).
// $lightingMission       = 1 while the current mission is baking scene lighting.
// $lightingProgressThread = schedule() handle of the progress-updater tick.
$lightingMission = 0;
$lightingProgressThread = "1175";

// Master-server address for the server browser ("" = none / direct connect only).
$MasterServerAddress = "";

// Maximum length (ms) of a recorded voice/message wav clip.
$MaxMessageWavLength = 5000;

// Audio type ID for chat/message sounds (see $GuiAudioType).
$MessageAudioType = 3;

// Debug render-mode toggle cycled by a developer keybind (default.bind.cs):
// 0 = normal, 1/2 = engine metrics / feature debug overlays.
$MFDebugRenderMode = 0;

// TGE mod-loading bookkeeping counter (-1 = unset).
$modcount = -1;

// Generic movement-speed scalar applied to player/camera input.
$movementSpeed = "1";

// Mission-load sequence number; echoed back to the server in the
// MissionStartPhase3Ack handshake (missionDownload.cs).
$MSeq = "1";

// --- Server-message callback registry (message.cs) ---
// addMessageCallback() registers handler function names here, keyed by message
// tag: flattened $MSGCB[tag, index]. $MSGCB<n>_0 entries are handlers bound to a
// tagged server message; $MSGCB_0 is the default (untagged) callback. Incoming
// server messages are dispatched through this table.
$MSGCB1_0 = "handleClientJoin";
$MSGCB2_0 = "handleClientDrop";
$MSGCB3_0 = "handleClientScoreChanged";
$MSGCB4_0 = "handleLoadInfoMessage";
$MSGCB5_0 = "handleLoadDescriptionMessage";
$MSGCB6_0 = "handleLoadInfoDoneMessage";
$MSGCB7_0 = "handleConnectionErrorMessage";
$MSGCB_0 = "defaultMessageCallback";

// ============================================================================
// Player "move" state ($mv*) - engine MoveManager (gameConnectionMoves.cc)
// ----------------------------------------------------------------------------
// These globals ARE the player's input. Each simulation tick (~32 Hz) the
// GameConnection's getNextMove() reads them, packs one Move struct, and sends
// it to the server. The action map (default.bind.cs) normally writes them from
// keyboard/mouse, but you can set them directly from script to drive the
// player programmatically (this is how a bot "presses keys").
//
// How getNextMove() assembles one move:
//   x (strafe)   = $mvRightAction   - $mvLeftAction
//   y (forward)  = $mvForwardAction - $mvBackwardAction
//   z (up/climb) = $mvUpAction      - $mvDownAction
//   pitch = $mvPitch + ($mvPitchUpSpeed   - $mvPitchDownSpeed)
//   yaw   = $mvYaw   + ($mvYawLeftSpeed    - $mvYawRightSpeed)
//   roll  = $mvRoll  + ($mvRollRightSpeed  - $mvRollLeftSpeed)
//
// IMPORTANT - two different kinds of look input:
//   * $mvYaw / $mvPitch / $mvRoll are ONE-SHOT DELTAS: the amount to turn THIS
//     tick. getNextMove() consumes them and RESETS each to 0 every move, so a
//     value you set applies once and then clears. This is how the mouse feeds
//     in (default.bind.cs accumulates into $mvYaw/$mvPitch each motion event).
//     To turn from script, ADD to them (e.g. $mvYaw += amt) right before/at the
//     tick - a value left set across ticks only fires once.
//   * $mv*Speed are PERSISTENT TURN RATES: they keep applying every tick until
//     you zero them (this is how held arrow-key turning works - keydown sets
//     the rate, keyup sets it back to 0).
//
// UNITS: yaw/pitch/roll (and the *Speed rates) are in RADIANS per move. Set
// degrees with mDegToRad(), e.g.  $mvYaw += mDegToRad(15);  to turn 15 deg left.
// Positive yaw = left, positive pitch = look up, positive roll = roll right.
// Angles are quantized to 16 bits and wrap over a full circle for net transit.
//
// The *Action magnitudes are analog, clamped to [-1, 1] (quantized to ~1/16
// steps); digital keys just use 0 or 1. AoT multiplies them by $movementSpeed.
$mvBackwardAction = "0";   // back  (subtracted from forward into move.y)
$mvDownAction = "0";       // descend/down (into move.z)
$mvForwardAction = "0";    // forward (into move.y); AoT sets to 1*$movementSpeed
$mvFreeLook = "0";         // bool: 1 = look around without turning the body
$mvLeftAction = "0";       // strafe left (subtracted from right into move.x)
$mvPitch = "0";            // one-shot pitch delta (radians); reset to 0 each tick
$mvPitchDownSpeed = "0";   // persistent pitch-down rate (radians/tick)
$mvPitchUpSpeed = "0";     // persistent pitch-up rate (radians/tick)
$mvRightAction = "0";      // strafe right (into move.x)
$mvRoll = "0";             // one-shot roll delta (radians); reset to 0 each tick
$mvRollLeftSpeed = "0";    // persistent roll-left rate (radians/tick)
$mvRollRightSpeed = "0";   // persistent roll-right rate (radians/tick)
// $mvTriggerCount<n> - press counters for the 6 trigger keys (MaxTriggerKeys).
// Each bound key bumps its counter on press AND release, so an ODD count means
// the trigger is currently held; the engine also catches a tap that both
// pressed and released within one tick. To "tap" a trigger from script,
// increment it (++). AoT trigger assignments (default.bind.cs):
//   0 = mouseFire (primary attack)   1 = altTrigger (block / alt-fire)
//   2 = jump                         3 = crouch
//   4, 5 = unused by default
$mvTriggerCount0 = "2";
$mvTriggerCount1 = "0";
$mvTriggerCount2 = "0";
$mvTriggerCount3 = "0";
$mvTriggerCount4 = "0";
$mvTriggerCount5 = "0";
$mvUpAction = "0";         // ascend/jump-jet/climb up (into move.z)
$mvYaw = "0";              // one-shot yaw delta (radians, +=left); reset each tick
$mvYawLeftSpeed = "0";     // persistent yaw-left rate (radians/tick)
$mvYawRightSpeed = "0";    // persistent yaw-right rate (radians/tick)

// ============================================================================
// Connection-type presets ($Net_*) - optionsDlg.cs / SelectNetworkGui.gui
// ----------------------------------------------------------------------------
// Lookup tables for the 6 built-in bandwidth profiles offered in the "Select
// Network Type" dialog and the options menu. $Net_<Param><n> is the flattened
// form of the script array $Net_<Param>[n], where n is the connection-type id:
//   1 = 14.4k Modem   2 = 28.8k Modem   3 = 56.6k Modem
//   4 = DSL / ADSL    5 = Cable         6 = T1 / LAN
// (id 7 = "Custom", which is NOT in these tables - it instead reads/writes the
//  user-tuned $pref::Net::Custom::* values.)
//
// These are just the menu of presets; they are not the live setting. Picking a
// profile calls SetConnectionType(n) (optionsDlg.cs), which COPIES that row
// into the active prefs the engine actually uses:
//   $pref::Net::PacketSize          <- $Net_PacketSize[n]
//   $pref::Net::PacketRateToClient  <- $Net_RateToClient[n]
//   $pref::Net::PacketRateToServer  <- $Net_RateToServer[n]
//   $Pref::Net::LagThreshold        <- $Net_LagThreshold[n]
// and stores the chosen id in $Pref::Net::ConnectionType.
//
// The four parameters:
//   LagThreshold = ms of round-trip latency before the client shows a "lag"
//                  warning. (Same 400 for every preset here.)
//   PacketSize   = max bytes per move/update packet. Bigger = fewer, fatter
//                  packets (needs more bandwidth headroom).
//   RateToClient = packets/sec the server is allowed to send THIS client (the
//                  downstream update rate; higher = smoother but more download).
//   RateToServer = packets/sec this client sends the server (upstream move
//                  rate; capped at the ~32 Hz tick rate).
// Note rows climb from slow dial-up (small packets, ~10 pps) to LAN (450 B,
// 32 pps) - i.e. higher id = more bandwidth assumed available.
$Net_LagThreshold1 = 400;
$Net_LagThreshold2 = 400;
$Net_LagThreshold3 = 400;
$Net_LagThreshold4 = 400;
$Net_LagThreshold5 = 400;
$Net_LagThreshold6 = 400;
$Net_PacketSize1 = 100;
$Net_PacketSize2 = 200;
$Net_PacketSize3 = 240;
$Net_PacketSize4 = 350;
$Net_PacketSize5 = 400;
$Net_PacketSize6 = 450;
$Net_RateToClient1 = 10;
$Net_RateToClient2 = 12;
$Net_RateToClient3 = 16;
$Net_RateToClient4 = 20;
$Net_RateToClient5 = 24;
$Net_RateToClient6 = 32;
$Net_RateToServer1 = 8;
$Net_RateToServer2 = 16;
$Net_RateToServer3 = 20;
$Net_RateToServer4 = 24;
$Net_RateToServer5 = 24;
$Net_RateToServer6 = 32;

// Number of $clientInv slots in use (see the client inventory block above).
$numClientInvSlots = 12;

// Pixel heights for the 3 chat-HUD size settings, toggled by resizeMessageHud /
// $pref::ChatHudLength (chatHud.cs). Flattened $outerChatLenY[n].
$outerChatLenY1 = 70;
$outerChatLenY2 = 134;
$outerChatLenY3 = 198;

// OpenGL capability flag (EXT_paletted_texture). See $AnisotropySupported.
$PalettedTextureSupported = "0";

// OS the client is running on (set by the engine): "windows".
$platform = "windows";

// Engine Player-class network tuning:
//   maxPredictionTicks = how far client-side movement prediction may run ahead.
//   min/maxWarpTicks    = bounds for smoothing ("warping") server position
//                         corrections instead of snapping.
$Player::maxPredictionTicks = "30";
$Player::maxWarpTicks = "3";
$Player::minWarpTicks = "0.5";

// ============================================================================
// User preferences ($pref::*) - persisted to the client config / prefs.cs and
// reloaded each launch. Grouped by subsystem below.
// ============================================================================

// Accessory:: - character cosmetic selections (code + color) for head, back,
// and visor attachments.
$pref::Accessory::BackCode = "1";
$pref::Accessory::BackColor = "1";
$pref::Accessory::headCode = "1";
$pref::Accessory::headColor = "1";
$pref::Accessory::visorCode = "1";
$pref::Accessory::VisorColor = "1";

// Audio:: - per-channel volumes (1-8), audio driver, master volume, and the
// environmental-audio (reverb) toggle.
$pref::Audio::channelVolume1 = "1";
$pref::Audio::channelVolume2 = "1";
$pref::Audio::channelVolume3 = 0.8;
$pref::Audio::channelVolume4 = 0.8;
$pref::Audio::channelVolume5 = 0.8;
$pref::Audio::channelVolume6 = 0.8;
$pref::Audio::channelVolume7 = 0.8;
$pref::Audio::channelVolume8 = 0.8;
$pref::Audio::driver = "OpenAL";
$pref::Audio::environmentEnabled = 0;
$pref::Audio::forceMaxDistanceUpdate = 0;
$pref::Audio::masterVolume = 0.8;

// Chat HUD size level (1-3), maps to $outerChatLenY[n].
$pref::ChatHudLength = 1;

// Sky/cloud rendering prefs.
$pref::CloudOutline = "0";
$pref::CloudsOn = "1";

// Player skin color index.
$pref::Color::skin = "1";

// Decal:: - ground/wall decal lifetime (ms), cap, and on/off.
$pref::Decal::decalTimeout = "5000";
$pref::Decal::maxNumDecals = "256";
$pref::decalsOn = "1";

// World/mission editor visible distance.
$pref::Editor::visibleDistance = "2100";

// Environment (reflection) maps on/off.
$pref::environmentMaps = "1";

// Server-browser filter: only show dedicated servers.
$Pref::Filter::Dedicated = "1";

// Current graphics-detail preset level (1-5); applies the $GD_* set. Here 5 = highest.
$Pref::GraphicDetail = "5";

// Fraction of grass billboards to replicate (0-1).
$pref::Grass::replicationRatio = 1;

// 1 if hosting a listen (multiplayer) server from this client.
$pref::HostMultiPlayer = "0";

// Number of chat/HUD message lines kept in the scrollback log.
$pref::HudMessageLogSize = 40;

// Input:: - device enables and sensitivities. JoystickEnabled/KeyboardEnabled/
// MouseEnabled, keyboard turn speed, mouse sensitivity (+ link flag for X/Y),
// and the free-look toggle-vs-hold setting.
$pref::Input::JoystickEnabled = "0";
$pref::Input::KeyboardEnabled = "1";
$pref::Input::KeyboardTurnSpeed = 0.1;
$pref::Input::LinkMouseSensitivity = 1;
$pref::Input::MouseEnabled = "0";
$pref::Input::MouseSensitivity = "0.452663";
$pref::Input::useFreeLookToggle = "0";

// Interior:: - interior (BSP building) rendering prefs: detail bias, dynamic
// lights + their update period, vertex-array locking, detail/env-map display,
// textured fog, and vertex lighting.
$pref::Interior::detailAdjust = "1";
$pref::Interior::DynamicLights = "1";
$pref::Interior::LightUpdatePeriod = "66";
$pref::Interior::lockArrays = "1";
$pref::interior::showdetailmaps = 0;
$pref::Interior::ShowEnvironmentMaps = "1";
$pref::Interior::TexturedFog = "0";
$pref::Interior::VertexLighting = "0";

// Master-server list entry 0 (server-browser master address slot).
$pref::Master0 = "1";

// Net:: - active networking settings (set by the chosen $Net_* profile, or
// custom). ConnectionType = which preset (1-7, 7 = custom), then the live
// lag threshold, packet rates to/from, packet size, and the game port.
$Pref::Net::ConnectionType = "6";
$Pref::Net::LagThreshold = "400";
$pref::Net::PacketRateToClient = "32";
$pref::Net::PacketRateToServer = "32";
$pref::Net::PacketSize = "450";
$pref::Net::Port = 28000;

// Cached path of the newest news/loading image fetched from the AoT website.
$Pref::newestPicture = "/images/2005/20050824l.jpg";

// Number of cloud layers to draw.
$pref::NumCloudLayers = "3";

// OpenGL:: - renderer feature toggles and per-card workaround switches
// (texture compression, tex-gen, anisotropy, multitexture/CVA/fog-coord
// disables, 16-bit/paletted forcing, gamma, hardware light limits, trilinear,
// etc.). Mostly auto-set from the detected video card profile.
$pref::OpenGL::allowCompression = "0";
$pref::OpenGL::allowTexGen = "1";
$pref::OpenGL::anisotropy = "0";
$pref::OpenGL::disableARBMultitexture = "0";
$pref::OpenGL::disableARBTextureCompression = "0";
$pref::OpenGL::disableEXTCompiledVertexArray = "0";
$pref::OpenGL::disableEXTFogCoord = "0";
$pref::OpenGL::disableEXTPalettedTexture = "0";
$pref::OpenGL::disableEXTTexEnvCombine = "0";
$pref::OpenGL::disableSubImage = "0";
$pref::OpenGL::force16BitTexture = "0";
$pref::OpenGL::forcePalettedTexture = "0";
$pref::OpenGL::gammaCorrection = "0.5";
$pref::OpenGL::maxDynLights = "5";
$pref::OpenGL::maxHardwareLights = "3";
$pref::OpenGL::noDrawArraysAlpha = "0";
$pref::OpenGL::noEnvColor = "0";
$pref::OpenGL::textureAnisotropy = "0";
$pref::OpenGL::textureTrilinear = "1";

// Player:: - view/render prefs: current & default FOV, display name, whether
// to render your own player/items in first person, and zoom speed.
$Pref::player::CurrentFOV = 45;
$pref::Player::defaultFov = 90;
$pref::Player::Name = "Fresh Meat";
$pref::Player::renderMyItems = "1";
$pref::Player::renderMyPlayer = "1";
$pref::Player::zoomSpeed = 0;

// Weather precipitation on/off.
$pref::precipitationOn = "1";

// 1 to auto-pause when the window loses focus.
$pref::prePause = "0";

// sceneLighting:: - lighting bake cache settings (enable, cache size/dir purge
// policy, terrain lighting level).
$pref::sceneLighting::cacheLighting = 1;
$pref::sceneLighting::cacheSize = 20000;
$pref::sceneLighting::purgeMethod = "lastCreated";
$pref::sceneLighting::terrainGenerateLevel = 1;

// Next screenshot file number (preferences copy).
$pref::screenshotNumber = 157;

// Server:: - dedicated/listen-server configuration (these matter when this
// client hosts): admin password, ban durations, version-mismatch message,
// flood protection, server info/name, max chat length, max dropped items,
// max players, port, region mask, password salt, and round time limit.
$Pref::Server::AdminPassword = "admin";
$Pref::Server::BanTime = 1800;
$Pref::Server::ConnectionError = "You do not have the correct version of the Age of Time or the related art needed to play on this server, please contact the server operator for more information.";
$Pref::Server::FloodProtectionEnabled = 1;
$Pref::Server::Info = "This is an Age of Time server.";
$Pref::Server::KickBanTime = 300;
$Pref::Server::MaxChatLen = 120;
$Pref::Server::MaxDroppedItems = 100;
$Pref::Server::MaxPlayers = 8;
$Pref::Server::Name = "Age of Time Server";
$Pref::Server::Port = 28000;
$Pref::Server::RegionMask = 2;
$Pref::Server::SaltString = "random letters";
$Pref::Server::TimeLimit = 0;

// Last / default server IP to connect to.
$Pref::ServerIP = "45.148.165.55";

// Shadows and sky rendering on/off.
$pref::shadows = "1";
$pref::SkyOn = "1";

// Terrain:: - terrain rendering prefs: dynamic lights, detail maps, emboss
// bumps, screen-error (LOD) tolerance, texture detail level, texture cache size.
$pref::Terrain::dynamicLights = "1";
$pref::Terrain::enableDetails = "1";
$pref::Terrain::enableEmbossBumps = "1";
$pref::Terrain::screenError = "1";
$pref::Terrain::texDetail = "0";
$pref::Terrain::textureCacheSize = "220";

// TS:: - TSShape (3D model) rendering/LOD prefs (engine tsShapeInstance):
// auto-detail, detail bias, fog texture, screen-error tolerance, and skip
// flags for fog/loading/rendering detail levels and triangle-vs-strip drawing.
$pref::TS::autoDetail = "1";
$pref::TS::detailAdjust = "1";
$pref::TS::fogTexture = "1";
$pref::TS::screenError = "0.001";
$pref::TS::skipFirstFog = "0";
$pref::TS::skipLoadDLs = "0";
$pref::TS::skipRenderDLs = "0";
$pref::TS::UseTriangles = "0";

// Video:: - display/renderer settings: allowed APIs (D3D/OpenGL), preferred
// API, applied-flag, clip-high, detected/profiled GPU vendor+renderer, context
// handling, vsync disable, display device, fullscreen, monitor index, 16-bit
// only, resolution, safe mode, screenshot format/session, and windowed res.
$pref::Video::allowD3D = "1";
$pref::Video::allowOpenGL = "1";
$pref::Video::appliedPref = "1";
$pref::Video::clipHigh = "0";
$pref::Video::defaultsRenderer = "NVIDIA GeForce GTX 1660 Ti/PCIe/SSE2";
$pref::Video::defaultsVendor = "NVIDIA Corporation";
$pref::Video::deleteContext = "1";
$pref::Video::disableVerticalSync = "1";
$pref::Video::displayDevice = "OpenGL";
$pref::Video::fullScreen = "0";
$pref::Video::monitorNum = 0;
$pref::Video::only16 = "0";
$pref::Video::preferOpenGL = "1";
$pref::Video::profiledRenderer = "NVIDIA GeForce GTX 1660 Ti/PCIe/SSE2";
$pref::Video::profiledVendor = "NVIDIA Corporation";
$pref::Video::resolution = "1280 720 32";
$pref::Video::safeModeOn = "1";
$pref::Video::screenShotFormat = "PNG";
$pref::Video::screenShotSession = 25;
$pref::Video::windowedRes = "800 600";

// Multiplier applied to the mission's visible distance (set by detail preset).
$pref::visibleDistanceMod = "1";

// --- Quick-slot hotbar (brickSelectorDlg.cs / PlayGui.updateQuickSlots) ---
// $QuickSlot0..9 hold the serverID of the item assigned to quickslots 1-10.
// Assigned via BSD_AssignQuickSlot() and synced to the server with the
// SetQuickSlot command. "" = the slot is unassigned.
$QuickSlot0 = "4051";
$QuickSlot1 = "4074";
$QuickSlot2 = "4063";
$QuickSlot3 = "";
$QuickSlot4 = "";
$QuickSlot5 = "";
$QuickSlot6 = "";
$QuickSlot7 = "";
$QuickSlot8 = "";
$QuickSlot9 = "";

// --- Action-map remap table (actionMap.cs / default.bind.cs / options remap) ---
// $RemapCmd<n>  = the bindable command/function name for entry n.
// $RemapName<n> = the human-readable label shown in the controls/remap menu.
// $RemapCount   = number of remappable entries. Index n pairs the two arrays.
$RemapCmd0 = "moveforward";
$RemapCmd1 = "walk";
$RemapCmd10 = "jump";
$RemapCmd11 = "crouch";
$RemapCmd12 = "mouseFire";
$RemapCmd13 = "altTrigger";
$RemapCmd14 = "setZoomFov";
$RemapCmd15 = "toggleZoom";
$RemapCmd16 = "toggleFreeLook";
$RemapCmd17 = "toggleFirstPerson";
$RemapCmd18 = "toggleMessageHud";
$RemapCmd19 = "localMessageHud";
$RemapCmd2 = "autoWalk";
$RemapCmd20 = "openVoiceMenu";
$RemapCmd21 = "action";
$RemapCmd22 = "stopAction";
$RemapCmd23 = "openInventory";
$RemapCmd24 = "openStatus";
$RemapCmd25 = "pageMessageHudUp";
$RemapCmd26 = "pageMessageHudDown";
$RemapCmd27 = "resizeMessageHud";
$RemapCmd28 = "showPlayerList";
$RemapCmd29 = "suicide";
$RemapCmd3 = "movebackward";
$RemapCmd30 = "toggleCamera";
$RemapCmd31 = "dropCameraAtPlayer";
$RemapCmd32 = "dropPlayerAtCamera";
$RemapCmd33 = "bringUpOptions";
$RemapCmd34 = "openAdminWindow";
$RemapCmd35 = "doScreenShot";
$RemapCmd36 = "quickSlot1";
$RemapCmd37 = "quickSlot2";
$RemapCmd38 = "quickSlot3";
$RemapCmd39 = "quickSlot4";
$RemapCmd4 = "moveleft";
$RemapCmd40 = "quickSlot5";
$RemapCmd41 = "quickSlot6";
$RemapCmd42 = "quickSlot7";
$RemapCmd43 = "quickSlot8";
$RemapCmd44 = "quickSlot9";
$RemapCmd45 = "quickSlot10";
$RemapCmd5 = "moveright";
$RemapCmd6 = "turnLeft";
$RemapCmd7 = "turnRight";
$RemapCmd8 = "panUp";
$RemapCmd9 = "panDown";
$RemapCount = 46;
$RemapName0 = "Forward";
$RemapName1 = "Walk";
$RemapName10 = "Jump";
$RemapName11 = "Crouch";
$RemapName12 = "Attack";
$RemapName13 = "Block";
$RemapName14 = "Adjust Zoom";
$RemapName15 = "Toggle Zoom";
$RemapName16 = "Free Look";
$RemapName17 = "Switch 1st/3rd";
$RemapName18 = "Global Chat";
$RemapName19 = "Local Chat";
$RemapName2 = "Auto Run";
$RemapName20 = "Voice Menu";
$RemapName21 = "Action";
$RemapName22 = "Stop Sction";
$RemapName23 = "Open Inventory";
$RemapName24 = "Open Status";
$RemapName25 = "Message Hud PageUp";
$RemapName26 = "Message Hud PageDown";
$RemapName27 = "Resize Message Hud";
$RemapName28 = "Show Scores";
$RemapName29 = "Suicide";
$RemapName3 = "Backward";
$RemapName30 = "Toggle Camera";
$RemapName31 = "Drop Camera at Player";
$RemapName32 = "Drop Player at Camera";
$RemapName33 = "Open Options Dialog";
$RemapName34 = "Open Admin Window";
$RemapName35 = "Take Screenshot";
$RemapName36 = "QuickSlot 1";
$RemapName37 = "QuickSlot 2";
$RemapName38 = "QuickSlot 3";
$RemapName39 = "QuickSlot 4";
$RemapName4 = "Strafe Left";
$RemapName40 = "QuickSlot 5";
$RemapName41 = "QuickSlot 6";
$RemapName42 = "QuickSlot 7";
$RemapName43 = "QuickSlot 8";
$RemapName44 = "QuickSlot 9";
$RemapName45 = "QuickSlot 10";
$RemapName5 = "Strafe Right";
$RemapName6 = "Turn Left";
$RemapName7 = "Turn Right";
$RemapName8 = "Look Up";
$RemapName9 = "Look Down";

// Engine ShapeBase HUD-effect decay rates (shapeBase.cc):
//   DFDec = damage-flash (red hit flash) fade-out amount per second.
//   WODec = whiteout (e.g. blast/blind) fade-out amount per second.
$SB::DFDec = "0.007";
$SB::WODec = "0.007";

// Scene-lighting bake progress (0-1) and a flag to abort the bake early.
$SceneLighting::lightingProgress = "0";
$sceneLighting::terminateLighting = "0";

// Running counter for screenshot filenames (engine copy; see $pref::screenshotNumber).
$screenshotNumber = 0;

// Terrain LOD "screen size" metric (engine terrRender) controlling detail.
$screenSize = "45";

// 1 if this process is running as a dedicated server (no client rendering).
$Server::Dedicated = 0;

// Message shown to a client whose game version / art doesn't match the server.
$ServerConnectionErrorMessage = "You do not have the correct version of the Age of Time or the related art needed to play on this server, please contact the server operator for more information.";

// --- Reverse inventory lookup (inventory) ---
// Keyed by server item-stack ID: $serverToClientInv<serverID> = the $clientInv
// ScriptObject ID for that stack. Lets client commands that arrive with a
// server stack ID find the matching local inventory object. Inverse of the
// $clientInv* table above.
$serverToClientInv34569 = "4046";
$serverToClientInv34570 = "4047";
$serverToClientInv34571 = "4048";
$serverToClientInv34572 = "4049";
$serverToClientInv34573 = "4050";
$serverToClientInv34574 = "4051";
$serverToClientInv34575 = "4062";
$serverToClientInv34576 = "4063";
$serverToClientInv34577 = "4074";
$serverToClientInv34578 = "4085";
$serverToClientInv34579 = "4086";
$serverToClientInv34580 = "4087";

// --- Status GUI character stats (statusGui.cs) ---
// $SG_Ability[<Stat>] = the current character's ability scores, parsed from a
// server status message (Strength/Stamina/Dexterity/Agility/Intelligence/
// Wisdom/Charisma). $SG_MaxLevel = character max level. Used to fill the
// status-window bars.
$SG_AbilityAgility = "0";
$SG_AbilityCharisma = "0";
$SG_AbilityDexterity = "0";
$SG_AbilityIntelligence = "0";
$SG_AbilityStamina = "0";
$SG_AbilityStrength = "0";
$SG_AbilityWisdom = "0";
$SG_MaxLevel = "";

// Engine "show" move state - the mirror of the $mv* move inputs used while
// playing back a recorded demo (.rec).
$showBackwardAction = "0";
$showDownAction = "0";
$showForwardAction = "0";
$showLeftAction = "0";
$showMovementSpeed = "1";
$showPitch = "0";
$showRightAction = "0";
$showUpAction = "0";
$showYaw = "0";

// Engine simulation time in seconds (virtual milliseconds / 1000).
$Sim::Time = "257.667999";

// Audio type ID for general in-world/sim sounds (see $GuiAudioType).
$SimAudioType = 2;

// Special-fog rendering mode flag (engine SceneGraph::useSpecial).
$specialFog = "0";

// Networking stats: bits received/sent in the last sample and ghost-update count.
$Stats::netBitsReceived = "58";
$Stats::netBitsSent = "450";
$Stats::netGhostUpdates = "637";

// OpenGL capability flag (WGL swap-interval / vsync control). See $AnisotropySupported.
$SwapIntervalSupported = "1";

// Terrain (v2) texture manager counts: live dynamic vs. cached static textures.
$T2::dynamicTextureCount = "270";
$T2::staticTextureCount = "105059";

// OpenGL capability flag (texture compression). See $AnisotropySupported.
$TextureCompressionSupported = "1";

// ID of the GUI control that last fired a callback (sliders / text-edit boxes
// set this so their command can find the source control).
$ThisControl = "1100";

// Number of frames the 3D viewport (TSControl) has drawn; increments each
// rendered frame.
$TSControl::frameCount = "1038";

// --- Object type bitmasks (engine) ---
// Each constant is a single bit identifying an engine object class. OR them
// together to build a type mask for containerFindObjects / raycasts / queries
// (e.g. PlayerObjectType | ItemObjectType to find players and items).
$TypeMasks::CameraObjectType = "4096";
$TypeMasks::CorpseObjectType = "1048576";
$TypeMasks::DamagableItemObjectType = "268435456";
$TypeMasks::DebrisObjectType = "4194304";
$TypeMasks::EnvironmentObjectType = "2";
$TypeMasks::ExplosionObjectType = "524288";
$TypeMasks::GameBaseObjectType = "1024";
$TypeMasks::InteriorObjectType = "8";
$TypeMasks::ItemObjectType = "32768";
$TypeMasks::MarkerObjectType = "64";
$TypeMasks::PhysicalZoneObjectType = "8388608";
$TypeMasks::PlayerObjectType = "16384";
$TypeMasks::ProjectileObjectType = "262144";
$TypeMasks::RoomMarkerObjectType = "33554432";
$TypeMasks::ShapeBaseObjectType = "2048";
$TypeMasks::StaticObjectType = "1";
$TypeMasks::StaticRenderedObjectType = "134217728";
$TypeMasks::StaticShapeObjectType = "8192";
$TypeMasks::StaticTSObjectType = "16777216";
$TypeMasks::TerrainObjectType = "4";
$TypeMasks::TriggerObjectType = "32";
$TypeMasks::VehicleBlockerObjectType = "131072";
$TypeMasks::VehicleObjectType = "65536";
$TypeMasks::WaterObjectType = "16";

// Mod load list selected by the user (TGE mod chain): "editor;characters".
$userMods = "editor;characters";

// Leftover scratch global from a script (a stray $value temp). Harmless.
$value = "32.000000";

// AoT client/protocol version (30). Sent in the connect handshake
// ($conn.setConnectArgs) and used to fetch the matching update manifest
// (/aot/updates/<version>.txt in autoUpdate.cs).
$version = 30;

// Video texture residency/cache stats: texels loaded, resident percentage,
// and texture cache misses (-1 = not measured).
$Video::numTexelsLoaded = "0";
$Video::texResidentPercentage = "-1.000000";
$Video::textureCacheMisses = "-1";

// ============================================================================
// Voice / command radial menu data ($Voice*) - VoiceMenuGui
// ----------------------------------------------------------------------------
// The voice menu is a nested radial menu: a Default menu branches into Emotes,
// Voice, Animation, and Spells submenus. For each menu <M> and slot n:
//   $VoiceCommand<M>_n = the console command run when that slot is chosen
//                        (usually CommandToServer(...) then VoiceMenuGui.Exit()).
//   $VoiceText<M>_n    = the on-screen button label.
//   $VoiceLetter<M>_n  = the hotkey letter for that slot.
//   $VoiceItemCount<M> = how many slots menu <M> has.
// ============================================================================
$VoiceCommandAnimation_0 = "CommandToServer(\'sit\');VoiceMenuGui.Exit();";
$VoiceCommandAnimation_1 = "CommandToServer(\'lounge\');VoiceMenuGui.Exit();";
$VoiceCommandAnimation_2 = "CommandToServer(\'sleep\');VoiceMenuGui.Exit();";
$VoiceCommandAnimation_3 = "VoiceMenuGui.Exit();";
$VoiceCommandDefault_0 = "VoiceMenuGui.LoadMenu(\"Emotes\");";
$VoiceCommandDefault_1 = "VoiceMenuGui.LoadMenu(\"Voice\");";
$VoiceCommandDefault_2 = "VoiceMenuGui.LoadMenu(\"Animation\");";
$VoiceCommandDefault_3 = "VoiceMenuGui.LoadMenu(\"Spells\");";
$VoiceCommandDefault_4 = "VoiceMenuGui.Exit();";
$VoiceCommandEmotes_0 = "CommandToServer(\'Love\');VoiceMenuGui.Exit();";
$VoiceCommandEmotes_1 = "CommandToServer(\'Hate\');VoiceMenuGui.Exit();";
$VoiceCommandEmotes_2 = "CommandToServer(\'WTF\');VoiceMenuGui.Exit();";
$VoiceCommandEmotes_3 = "VoiceMenuGui.Exit();";
$VoiceCommandSpells_0 = "CommandToServer(\'cast\', ball);VoiceMenuGui.Exit();";
$VoiceCommandSpells_1 = "CommandToServer(\'cast\', burn);VoiceMenuGui.Exit();";
$VoiceCommandSpells_2 = "CommandToServer(\'cast\', fireball);VoiceMenuGui.Exit();";
$VoiceCommandSpells_3 = "CommandToServer(\'cast\', light);VoiceMenuGui.Exit();";
$VoiceCommandSpells_4 = "CommandToServer(\'cast\', cloak);VoiceMenuGui.Exit();";
$VoiceCommandSpells_5 = "VoiceMenuGui.Exit();";
$VoiceCommandVoice_0 = "CommandToServer(\'voice\', yes);VoiceMenuGui.Exit();";
$VoiceCommandVoice_1 = "CommandToServer(\'voice\', no);VoiceMenuGui.Exit();";
$VoiceCommandVoice_2 = "CommandToServer(\'voice\', Help);VoiceMenuGui.Exit();";
$VoiceCommandVoice_3 = "CommandToServer(\'voice\', stop);VoiceMenuGui.Exit();";
$VoiceCommandVoice_4 = "CommandToServer(\'voice\', greet1);VoiceMenuGui.Exit();";
$VoiceCommandVoice_5 = "CommandToServer(\'voice\', greet2);VoiceMenuGui.Exit();";
$VoiceCommandVoice_6 = "CommandToServer(\'voice\', greet3);VoiceMenuGui.Exit();";
$VoiceCommandVoice_7 = "VoiceMenuGui.Exit();";
$VoiceItemCountAnimation = "4";
$VoiceItemCountDefault = "5";
$VoiceItemCountEmotes = "4";
$VoiceItemCountSpells = "6";
$VoiceItemCountVoice = "8";
$VoiceLetterAnimation_0 = "S";
$VoiceLetterAnimation_1 = "L";
$VoiceLetterAnimation_2 = "E";
$VoiceLetterAnimation_3 = "Escape";
$VoiceLetterDefault_0 = "E";
$VoiceLetterDefault_1 = "V";
$VoiceLetterDefault_2 = "A";
$VoiceLetterDefault_3 = "S";
$VoiceLetterDefault_4 = "Escape";
$VoiceLetterEmotes_0 = "L";
$VoiceLetterEmotes_1 = "H";
$VoiceLetterEmotes_2 = "W";
$VoiceLetterEmotes_3 = "Escape";
$VoiceLetterSpells_0 = "B";
$VoiceLetterSpells_1 = "V";
$VoiceLetterSpells_2 = "F";
$VoiceLetterSpells_3 = "L";
$VoiceLetterSpells_4 = "C";
$VoiceLetterSpells_5 = "Escape";
$VoiceLetterVoice_0 = "Y";
$VoiceLetterVoice_1 = "N";
$VoiceLetterVoice_2 = "E";
$VoiceLetterVoice_3 = "S";
$VoiceLetterVoice_4 = "G";
$VoiceLetterVoice_5 = "H";
$VoiceLetterVoice_6 = "J";
$VoiceLetterVoice_7 = "Escape";
$VoiceTextAnimation_0 = "Sit";
$VoiceTextAnimation_1 = "Lounge";
$VoiceTextAnimation_2 = "Sleep";
$VoiceTextAnimation_3 = "Exit";
$VoiceTextDefault_0 = "Emotes";
$VoiceTextDefault_1 = "Voice";
$VoiceTextDefault_2 = "Animation";
$VoiceTextDefault_3 = "Spells";
$VoiceTextDefault_4 = "Exit";
$VoiceTextEmotes_0 = "Love";
$VoiceTextEmotes_1 = "Hate";
$VoiceTextEmotes_2 = "WTF";
$VoiceTextEmotes_3 = "Exit";
$VoiceTextSpells_0 = "Ball";
$VoiceTextSpells_1 = "Burn";
$VoiceTextSpells_2 = "Fireball";
$VoiceTextSpells_3 = "Light";
$VoiceTextSpells_4 = "Cloak";
$VoiceTextSpells_5 = "Exit";
$VoiceTextVoice_0 = "Yes";
$VoiceTextVoice_1 = "No";
$VoiceTextVoice_2 = "Help";
$VoiceTextVoice_3 = "Stop";
$VoiceTextVoice_4 = "Greet 1";
$VoiceTextVoice_5 = "Greet 2";
$VoiceTextVoice_6 = "Greet 3";
$VoiceTextVoice_7 = "Exit";
```
