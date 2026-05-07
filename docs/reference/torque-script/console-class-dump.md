# Console Class Dump

This page is a verbatim dump of every TorqueScript console class exposed by
the *Age of Time* client at runtime, captured by running the engine's
built-in `dumpConsoleClasses();` from the in-game console.

!!! tip "Reproducing this dump"
    Open the in-game console (the engine's standard tilde key in older
    Torque builds, or run the executable with the appropriate flag) and
    type:

    ```
    dumpConsoleClasses();
    ```

    The engine will print the same listing shown below.

```torquescript
==>dumpConsoleClasses();
class  SimObject {
  public:
   virtual void setName() {}
   virtual string getName() {}
   virtual string getClassName() {}
   virtual int getId() {}
   virtual int getGroup() {}
   virtual void delete() {}
   virtual int schedule() {}
   virtual void clearTaggedFields() {}
};

class  ScriptObject : public SimObject {
  public:

   /*! @name Classes
   
   Script objects have the ability to inherit and have class information.
   @{ */
   /*!
   Class of object.
   
    */
   string class;
   /*!
   Superclass of object.
   
    */shapeFile
   string superClass;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ClientInventorySO : public ScriptObject {
  public:
};

class  SimSet : public SimObject {
  public:
   virtual void listObjects() {}
   virtual void add() {}
   virtual void remove() {}
   virtual void clear() {}
   virtual int getCount() {}
   virtual int getObject() {}
   virtual bool isMember() {}
   virtual void bringToFront() {}
   virtual void pushToBack() {}
};

class  SimGroup : public SimSet {
  public:
};

class  GuiControl : public SimGroup {
  public:
   virtual Script getHelpPage() {}
   virtual void setValue() {}
   virtual string getValue() {}
   virtual void setActive() {}
   virtual bool isActive() {}
   virtual void setVisible() {}
   virtual void makeFirstResponder() {}
   virtual bool isVisible() {}
   virtual bool isAwake() {}
   virtual void setProfile() {}
   virtual void resize() {}
   virtual string getPosition() {}
   virtual string getExtent() {}
   virtual string getMinExtent() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  GuiTextCtrl : public GuiControl {
  public:
   virtual void setText() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
};

class  GuiPopUpMenuCtrl : public GuiTextCtrl {
  public:
   virtual void add() {}
   virtual void addScheme() {}
   virtual void setText() {}
   virtual string getText() {}
   virtual void clear() {}
   virtual void sort() {}
   virtual void forceOnAction() {}
   virtual void forceClose() {}
   virtual int getSelected() {}
   virtual void setSelected() {}
   virtual string getTextById() {}
   virtual void setEnumContent() {}
   virtual int findText() {}
   virtual int size() {}
   virtual void replaceText() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
   /*!
    */
   int maxPopupHeight;
};

class  GuiControlListPopUp : public GuiPopUpMenuCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
   /*!
    */
   int maxPopupHeight;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  NewGuiDialogClass : public GuiControlListPopUp {
  public:
};

class  GuiTextEditCtrl : public GuiTextCtrl {
  public:
   virtual int getCursorPos() {}
   virtual void setCursorPos() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
   /*!
    */
   string validate;
   /*!
    */
   string escapeCommand;
   /*!
    */
   int historySize;
   /*!
    */
   bool password;
   /*!
    */
   bool tabComplete;
   /*!
    */
   AudioProfilePtr deniedSound;
   /*!
    */
   bool sinkAllKeyEvents;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  NewGuiDialogName : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  NewGuiDialog : public GuiControl {
  public:
};

class  GuiInspector : public GuiControl {
  public:
   virtual Script addDynamicField() {}
   virtual Script setAllGroupStateScript() {}
   virtual Script toggleGroupScript() {}
   virtual Script toggleDynamicGroupScript() {}
   virtual void inspect() {}
   virtual void apply() {}
   virtual void toggleGroupExpand() {}
   virtual void toggleDynamicGroupExpand() {}
   virtual void setAllGroupState() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   int editControlOffset;
   /*!
    */
   int entryHeight;
   /*!
    */
   int textExtent;
   /*!
    */
   int entrySpacing;
   /*!
    */
   int maxMenuExtent;
   /*!
    */
   bool useFieldGrouping;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorInspectFields : public GuiInspector {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorInspectName : public GuiTextEditCtrl {
  public:
};

class  GuiArrayCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  GuiTreeViewCtrl : public GuiArrayCtrl {
  public:
   virtual void open() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   bool allowMultipleSelections;
   /*!
    */
   bool recurseSets;
};

class  GuiEditorTreeView : public GuiTreeViewCtrl {
  public:
   virtual Script onSelect() {}
};

class  GuiEditCtrl : public GuiControl {
  public:
   virtual void setRoot() {}
   virtual void addNewCtrl() {}
   virtual void select() {}
   virtual void setCurrentAddSet() {}
   virtual void toggle() {}
   virtual void justify() {}
   virtual void bringToFront() {}
   virtual void pushToBack() {}
   virtual void deleteSelection() {}
   virtual void moveSelection() {}
   virtual void saveSelection() {}
   virtual void loadSelection() {}
   virtual void selectAll() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  GuiEditor : public GuiEditCtrl {
  public:
   virtual Script onSelect() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorContent : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorRegion : public GuiControl {
  public:
};

class  GuiScrollCtrl : public GuiControl {
  public:
   virtual void scrollToTop() {}
   virtual void scrollToBottom() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   bool willFirstRespond;
   /*!
    */
   enumval hScrollBar;
   /*!
    */
   enumval vScrollBar;
   /*!
    */
   bool constantThumbHeight;
   /*!
    */
   Point2I childMargin;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorScroll : public GuiScrollCtrl {
  public:
};

class  GuiEditorRuler : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   string refCtrl;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorLeftRuler : public GuiEditorRuler {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorTopRuler : public GuiEditorRuler {
  public:
};

class  GuiEditorResList : public GuiPopUpMenuCtrl {
  public:
   virtual Script onSelect() {}
};

class  GuiEditorContentList : public GuiPopUpMenuCtrl {
  public:
   virtual Script onSelect() {}
};

class  GuiEditorClassPopup : public GuiControlListPopUp {
  public:
   virtual Script onSelect() {}
};

class  GuiMenuBar : public GuiControl {
  public:
   virtual void clearMenus() {}
   virtual void addMenu() {}
   virtual void addMenuItem() {}
   virtual void setMenuItemEnable() {}
   virtual void setMenuItemChecked() {}
   virtual void setMenuText() {}
   virtual void setMenuVisible() {}
   virtual void setMenuItemText() {}
   virtual void setMenuItemVisible() {}
   virtual void setMenuItemBitmap() {}
   virtual void removeMenuItem() {}
   virtual void clearMenuItems() {}
   virtual void removeMenu() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  GuiEditorMenuBar : public GuiMenuBar {
  public:
   virtual Script onMenuItemSelect() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GuiEditorGui : public GuiControl {
  public:
};

class  GuiTSCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;
};

class  GameTSCtrl : public GuiTSCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  noHudGui : public GameTSCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  escapeMenuGui : public GuiControl {
  public:
};

class  BSD_category {
  public:
   virtual Script onRemove() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_CombineText2 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_CombineText1 : public GuiTextCtrl {
  public:
};

class  GuiObjectView : public GuiTSCtrl {
  public:
   virtual void setMouse() {}
   virtual void setObject() {}
   virtual void mountObject() {}
   virtual void unMountObject() {}
   virtual void setEmpty() {}
   virtual void loadDSQ() {}
   virtual void setSequence() {}
   virtual void setThreadPos() {}
   virtual void hideNode() {}
   virtual void unHideNode() {}
   virtual void setIflFrame() {}
   virtual void setScale() {}
   virtual void setNodeColor() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;
   /*!
    */
   Point3F lightDirection;
   /*!
    */
   ColorF lightColor;
   /*!
    */
   ColorF ambientColor;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_CombinePreview2 : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_CombinePreview1 : public GuiObjectView {
  public:
};

class  GuiWindowCtrl : public GuiTextCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
   /*!
    */
   bool resizeWidth;
   /*!
    */
   bool resizeHeight;
   /*!
    */
   bool canMove;
   /*!
    */
   bool canClose;
   /*!
    */
   bool canMinimize;
   /*!
    */
   bool canMaximize;
   /*!
    */
   Point2I minSize;
   /*!
    */
   string closeCommand;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_CombineWindow : public GuiWindowCtrl {
  public:
};

class  GuiTextListCtrl : public GuiArrayCtrl {
  public:
   virtual int getSelectedId() {}
   virtual void setSelectedById() {}
   virtual void setSelectedRow() {}
   virtual void clearSelection() {}
   virtual int addRow() {}
   virtual void setRowById() {}
   virtual void sort() {}
   virtual void sortNumerical() {}
   virtual void clear() {}
   virtual int rowCount() {}
   virtual int getRowId() {}
   virtual string getRowTextById() {}
   virtual int getRowNumById() {}
   virtual string getRowText() {}
   virtual void removeRowById() {}
   virtual void removeRow() {}
   virtual void scrollVisible() {}
   virtual int findTextIndex() {}
   virtual void setRowActive() {}
   virtual bool isRowActive() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   bool enumerate;
   /*!
    */
   bool resizeCell;
   /*!
    */
   intList columns;
   /*!
    */
   bool fitParentWidth;
   /*!
    */
   bool clipColumnText;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_List : public GuiTextListCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_TabBox : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_ScrollBox : public GuiControl {
  public:
};

class  GuiSwatchCtrl : public GuiControl {
  public:
   virtual void setColor() {}
   virtual string getColor() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   ColorI color;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_QuickSlotBox : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_ModeNormal : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_ModePostOffice : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BSD_Window : public GuiWindowCtrl {
  public:
};

class  BrickSelectorDlg : public GuiControl {
  public:
   virtual Script onSleep() {}
   virtual Script setMode() {}
   virtual Script onWake() {}
   virtual Script toggle() {}
};

class  GuiMLTextCtrl : public GuiControl {
  public:
   virtual Script onURL() {}
   virtual void setText() {}
   virtual string getText() {}
   virtual void addText() {}
   virtual bool setCursorPosition() {}
   virtual void scrollToTag() {}
   virtual void scrollToTop() {}
   virtual void forceReflow() {}
   virtual void setAlpha() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   int lineSpacing;
   /*!
    */
   bool allowColorChars;
   /*!
    */
   int maxChars;
   /*!
    */
   AudioProfilePtr deniedSound;
   /*!
    */
   caseString text;
};

class  GuiMLTextEditCtrl : public GuiMLTextCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   int lineSpacing;
   /*!
    */
   bool allowColorChars;
   /*!
    */
   int maxChars;
   /*!
    */
   AudioProfilePtr deniedSound;
   /*!
    */
   caseString text;
   /*!
    */
   string escapeCommand;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  WriteParchment_BodyText : public GuiMLTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  WriteParchment_TitleText : public GuiTextEditCtrl {
  public:
};

class  WriteParchmentGui : public GuiControl {
  public:
   virtual Script Write() {}
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ParchmentTextAppend : public GuiMLTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ParchmentText : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ParchmentScroll : public GuiScrollCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ParchmentGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CPG_ConfirmNewPassword : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CPG_NewPassword : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CPG_OldPassword : public GuiTextEditCtrl {
  public:
};

class  ChangePasswordGui : public GuiControl {
  public:
   virtual Script onWake() {}
};

class  patchTCPobj {
  public:
   virtual Script onBinChunk() {}
   virtual Script onLine() {}
   virtual Script onConnectFailed() {}
   virtual Script onDNSFailed() {}
   virtual Script onConnected() {}
};

class  TCPObject : public SimObject {
  public:
   virtual void send() {}
   virtual void listen() {}
   virtual void connect() {}
   virtual void disconnect() {}
   virtual void saveBufferToFile() {}
   virtual void setBinary() {}
};

class  verTCPobj : public TCPObject {
  public:
   virtual Script onLine() {}
   virtual Script onConnectFailed() {}
   virtual Script onDNSFailed() {}
   virtual Script onConnected() {}
};

class  GuiButtonBaseCtrl : public GuiControl {
  public:
   virtual void performClick() {}
   virtual void setText() {}
   virtual string getText() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString text;
   /*!
    */
   int groupNum;
   /*!
    */
   enumval buttonType;
   /// @}

};

class  GuiButtonCtrl : public GuiButtonBaseCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString text;
   /*!
    */
   int groupNum;
   /*!
    */
   enumval buttonType;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Done : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Time : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Speed : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Data : public GuiTextCtrl {
  public:
};

class  AU_Text : public GuiMLTextCtrl {
  public:
   virtual Script echo() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Cancel : public GuiButtonCtrl {
  public:
};

class  GuiProgressCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Progress : public GuiProgressCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  AU_Window : public GuiWindowCtrl {
  public:
};

class  AutoUpdateGui : public GuiControl {
  public:
   virtual Script done() {}
   virtual Script onSleep() {}
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_Price : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_Amount : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_Cost : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_Preview : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_Label : public GuiTextCtrl {
  public:
};

class  saleGui : public GuiControl {
  public:
   virtual Script UpdateItem() {}
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_Cost : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_To : public GuiTextEditCtrl {
  public:
};

class  GuiCheckBoxCtrl : public GuiButtonBaseCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString text;
   /*!
    */
   int groupNum;
   /*!
    */
   enumval buttonType;
   /// @}

};

class  GuiRadioCtrl : public GuiCheckBoxCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString text;
   /*!
    */
   int groupNum;
   /*!
    */
   enumval buttonType;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_Anon : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_You : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_Preview : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_Quantity : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_Label : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  POG_DontWrite : public GuiTextEditCtrl {
  public:
};

class  PostOfficeGui : public GuiControl {
  public:
   virtual Script UpdateItem() {}
   virtual Script onWake() {}
};

class  craftTCPobj {
  public:
   virtual Script onLine() {}
   virtual Script onConnectFailed() {}
   virtual Script onDNSFailed() {}
   virtual Script onDisconnect() {}
   virtual Script onConnected() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CraftDownload_Progress : public GuiProgressCtrl {
  public:
};

class  CraftDownload_Text : public GuiMLTextCtrl {
  public:
   virtual Script echo() {}
};

class  craftDownloadGui : public GuiControl {
  public:
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_DescR : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Blocker0 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Blocker1 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Blocker3 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Blocker2 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Desc3 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Desc1 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Desc0 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Desc2 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Cost : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_QuantityR : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_LabelR : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_PreviewR : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Preview3 : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Quantity3 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Label3 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Quantity2 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Label2 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Preview2 : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Quantity1 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Label1 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Preview1 : public GuiObjectView {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Quantity0 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Label0 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Craft_Preview0 : public GuiObjectView {
  public:
};

class  CraftGui : public GuiControl {
  public:
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CraftMenu_Box : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CraftMenu_Scroll : public GuiScrollCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CraftMenu_Window : public GuiWindowCtrl {
  public:
};

class  CraftMenuGui : public GuiControl {
  public:
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Bank_Deposit : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Bank_Withdraw : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Bank_Transaction : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Bank_Cash : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Bank_Bank : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BankGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextSexyness : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextAccuracy : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextMagicPower : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextClimbPower : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextJumpPower : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextRunSpeed : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextMaxMana : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextDefense : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextAttack : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextBurden : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextWeight : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextHeight : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_TextName : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarLevel : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarExperience : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarStrength : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarStamina : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarDexterity : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarAgility : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarIntelligence : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarWisdom : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SG_BarCharisma : public GuiSwatchCtrl {
  public:
};

class  StatusGui : public GuiControl {
  public:
   virtual Script toggle() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  VoiceMenuText : public GuiMLTextCtrl {
  public:
};

class  GuiBitmapCtrl : public GuiControl {
  public:
   virtual void setValue() {}
   virtual void setBitmap() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool center;
   /*!
    */
   bool wrap;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  VoiceMenuBox : public GuiBitmapCtrl {
  public:
};

class  VoiceMenuGui : public GuiControl {
  public:
   virtual Script ClearMenu() {}
   virtual Script LoadMenu() {}
   virtual Script onInputEvent() {}
   virtual Script exit() {}
   virtual Script onSleep() {}
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SelectDetailGui : public GuiControl {
  public:
};

class  SelectNetworkGui : public GuiControl {
  public:
   virtual Script onSleep() {}
};

class  OptPlayerHeadMenu {
  public:
   virtual Script onSelect() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  dialog_Question : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  dialog_Window : public GuiWindowCtrl {
  public:
};

class  dialogGui : public GuiControl {
  public:
   virtual Script clear() {}
};

class  BtnDiscard {
  public:
   virtual Script click() {}
};

class  BtnUse {
  public:
   virtual Script click() {}
};

class  BtnItems {
  public:
   virtual Script click() {}
};

class  BtnAmmo {
  public:
   virtual Script click() {}
};

class  BtnWeapons {
  public:
   virtual Script click() {}
};

class  BtnClothes {
  public:
   virtual Script click() {}
};

class  filtersGui : public GuiControl {
  public:
   virtual Script onSleep() {}
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MJ_txtJoinPass : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MJ_btnConnect : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MJ_txtIP : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  manualJoin : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LOAD_MapDescription : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  respawnArenaGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  respawnGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BtnWarning : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtWarning : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  WarningBoxGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BtnNewCharacter : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BtnLogin : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtLoginPass : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtLoginName : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LoginGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BtnCharacterCancel : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CC_BtnRandom : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BtnCharacterDone : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GlassesBlocker2 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  HairColorBlocker2 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CheckGlasses : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MenuHairStyle : public GuiPopUpMenuCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtWeight : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MenuFace : public GuiPopUpMenuCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MenuHairColor : public GuiPopUpMenuCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MenuEyeColor : public GuiPopUpMenuCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtPosture : public GuiTextCtrl {
  public:
};

class  GuiSliderCtrl : public GuiControl {
  public:
   virtual float getValue() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Slider
   @{ */
   /*!
    */
   Point2F range;
   /*!
    */
   int ticks;
   /*!
    */
   float value;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderPosture : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtChest : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderChest : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtYScale : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderYScale : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtZScale : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderZScale : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtLipTone : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderLipTone : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtSkinTone : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderSkinTone : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  HairColorBlocker1 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtXScale : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderXScale : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MenuEarStyle : public GuiPopUpMenuCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ChestBlocker : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GlassesBlocker1 : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MinHeightBlocker : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_TabAppearance : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarWisdom : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarPoints : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarIntelligence : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarAgility : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarDexterity : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarStamina : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarStrength : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_BarCharisma : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_TabAbilities : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  RadioFemale : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  RadioMale : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtConfirmPassword : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtPassword : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtName : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_TabGeneral : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CCG_Scroll : public GuiScrollCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  preview : public GuiObjectView {
  public:
};

class  CreateCharacterGui : public GuiControl {
  public:
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  tab_items : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  tab_ammo : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  tab_weapons : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  tab_clothes : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  inventoryScrollBG : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  inventoryScroll : public GuiScrollCtrl {
  public:
};

class  InventoryGUI2 : public GuiControl {
  public:
   virtual Script onSleep() {}
   virtual Script onWake() {}
   virtual Script toggle() {}
};

class  GuiFadeinBitmapCtrl : public GuiBitmapCtrl {
  public:
   virtual void reset() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool center;
   /*!
    */
   bool wrap;
   /// @}

   /*!
    */
   int fadeinTime;
   /*!
    */
   int waitTime;
   /*!
    */
   int fadeoutTime;
   /*!
    */
   bool done;
};

class  StartupGui : public GuiFadeinBitmapCtrl {
  public:
   virtual Script click() {}
};

class  GuiInputCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  OptRemapInputCtrl : public GuiInputCtrl {
  public:
   virtual Script onInputEvent() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptRemapText : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptRemapDlg : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  RemapDlg : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  VertexLightingBlocker : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsTrilinearToggle : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptPlayerRenderPlayer : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsPrecipitationToggle : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsDecalsToggle : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsCloudsToggle : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsTexturedFog : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsVertexLighting : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsEnvMaps : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsEnvMapToggle : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptPlayerPane : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptControlsMouseInvert : public GuiCheckBoxCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderControlsMouseSensitivity : public GuiSliderCtrl {
  public:
};

class  OptRemapList : public GuiTextListCtrl {
  public:
   virtual Script doRemap() {}
   virtual Script fillList() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptControlsPane : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType7 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType6 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType5 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType4 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType3 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType2 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_ConnectionType1 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CustomNetworkBlocker : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderRateToServer : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  RateToServerDisplay : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderRateToClient : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  RateToClientDisplay : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LagThresholdDisplay : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderLagThreshold : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  PacketSizeDisplay : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderPacketSize : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptNetworkPane : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderGraphicsDistanceMod : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_GraphicDetail5 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SliderGraphicsAnisotropy : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_GraphicDetail4 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_GraphicDetail3 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_GraphicDetail2 : public GuiRadioCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OPT_GraphicDetail1 : public GuiRadioCtrl {
  public:
};

class  OptScreenshotMenu : public GuiPopUpMenuCtrl {
  public:
   virtual Script init() {}
};

class  OptGraphicsBPPMenu : public GuiPopUpMenuCtrl {
  public:
   virtual Script init() {}
};

class  OptGraphicsResolutionMenu : public GuiPopUpMenuCtrl {
  public:
   virtual Script init() {}
};

class  OptGraphicsDriverMenu : public GuiPopUpMenuCtrl {
  public:
   virtual Script onSelect() {}
};

class  OptGraphicsFullscreenToggle : public GuiCheckBoxCtrl {
  public:
   virtual Script onAction() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptGraphicsPane : public GuiControl {
  public:
};

class  OptAudioDriverList : public GuiPopUpMenuCtrl {
  public:
   virtual Script onSelect() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptAudioInfo : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptAudioVolumeShell : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptAudioVolumeMaster : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptAudioVolumeSim : public GuiSliderCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OptAudioPane : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BtnOK : public GuiButtonCtrl {
  public:
};

class  optionsDlg : public GuiControl {
  public:
   virtual Script applyPlayer() {}
   virtual Script applyGraphics() {}
   virtual Script onSleep() {}
   virtual Script onWake() {}
   virtual Script setPane() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  EndGameGuiList : public GuiTextListCtrl {
  public:
};

class  GuiChunkedBitmapCtrl : public GuiControl {
  public:
   virtual void setBitmap() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool useVariable;
   /*!
    */
   bool tile;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  EndGameGui : public GuiChunkedBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LoadingProgressTxt : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LoadingProgress : public GuiProgressCtrl {
  public:
};

class  LoadingGui : public GuiChunkedBitmapCtrl {
  public:
   virtual Script onSleep() {}
   virtual Script onWake() {}
   virtual Script onAdd() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_connecttoip : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtServerTotals : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_statusText : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_statusBar : public GuiProgressCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_cancelQuery : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_queryStatus : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_serverList : public GuiTextListCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_joinServer : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_queryLan : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  JS_queryMaster : public GuiButtonCtrl {
  public:
};

class  JoinServerGui : public GuiChunkedBitmapCtrl {
  public:
   virtual Script update() {}
   virtual Script exit() {}
   virtual Script join() {}
   virtual Script cancel() {}
   virtual Script queryLan() {}
   virtual Script query() {}
   virtual Script onWake() {}
};

class  aboutText : public GuiMLTextCtrl {
  public:
   virtual Script onURL() {}
};

class  aboutDlg : public GuiControl {
  public:
   virtual Script onWake() {}
};

class  motdTCPObj : public TCPObject {
  public:
   virtual Script readContent() {}
   virtual Script onLine() {}
   virtual Script onConnected() {}
};

class  masterTCPObj : public TCPObject {
  public:
   virtual Script readContent() {}
   virtual Script onLine() {}
   virtual Script onConnected() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MM_ServerStatus : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MM_Version : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MM_Title : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MM_MOTD : public GuiMLTextCtrl {
  public:
};

class  MainMenuGui : public GuiChunkedBitmapCtrl {
  public:
   virtual Script getMOTD() {}
   virtual Script queryMaster() {}
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  PlayerListGuiList : public GuiTextListCtrl {
  public:
};

class  PlayerListGui : public GuiControl {
  public:
   virtual Script zeroScores() {}
   virtual Script clear() {}
   virtual Script toggle() {}
   virtual Script remove() {}
   virtual Script updateScore() {}
   virtual Script update() {}
};

class  MessageHud_Edit : public GuiTextEditCtrl {
  public:
   virtual Script eval() {}
   virtual Script onEscape() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MessageHud_Text : public GuiTextCtrl {
  public:
};

class  GuiBitmapBorderCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MessageHud_Frame : public GuiBitmapBorderCtrl {
  public:
};

class  MessageHud : public GuiControl {
  public:
   virtual Script toggleState() {}
   virtual Script close() {}
   virtual Script open() {}
};

class  GuiMessageVectorCtrl : public GuiControl {
  public:
   virtual bool attach() {}
   virtual void detach() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   int lineSpacing;
   /*!
    */
   int lineContinuedIndex;
   /*!
    */
   string allowedMatches;
   /*!
    */
   ColorI matchColor;
   /*!
    */
   int maxColorIndex;
};

class  ChatHud : public GuiMessageVectorCtrl {
  public:
   virtual Script pageDown() {}
   virtual Script pageUp() {}
   virtual Script addLine() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ChatScrollHud : public GuiScrollCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  chatPageDown : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  OuterChatHud : public GuiBitmapBorderCtrl {
  public:
};

class  MainChatHud : public GuiControl {
  public:
   virtual Script nextChatHudLen() {}
   virtual Script setChatHudLength() {}
   virtual Script onWake() {}
};

class  GuiCompassCtrl : public GuiBitmapCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool center;
   /// @}

   /*!
    */
   filename OuterRingBitmap;
   /*!
    */
   filename NeedleBitmap;
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  PlayGuiCompass : public GuiCompassCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtGold : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  w : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtSlot2 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtSlot1 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtSlot3 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtSlot4 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TxtSlot5 : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LagIcon : public GuiBitmapCtrl {
  public:
};

class  BottomPrintText : public GuiMLTextCtrl {
  public:
   virtual Script onResize() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BottomPrintDlg : public GuiBitmapCtrl {
  public:
};

class  CenterPrintText : public GuiMLTextCtrl {
  public:
   virtual Script onResize() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CenterPrintTextShadow : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  CenterPrintDlg : public GuiBitmapCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  PlayGui_QuickSlotBox : public GuiSwatchCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  PlayGui_Blackout : public GuiFadeinBitmapCtrl {
  public:
};

class  PlayGui : public GameTSCtrl {
  public:
   virtual Script updateQuickSlots() {}
   virtual Script onSleep() {}
   virtual Script onWake() {}
};

class  GuiConsoleTextCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;relo
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString expression;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  TextOverlayControl : public GuiConsoleTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  FrameOverlayGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BitsSent : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GhostUpdates : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  GhostsActive : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  BitsReceived : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  PacketLoss : public GuiTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Latency : public GuiTextCtrl {
  public:
};

class  GuiGraphCtrl : public GuiControl {
  public:
   virtual void addDatum() {}
   virtual float getDatum() {}
   virtual void addAutoPlot() {}
   virtual void removeAutoPlot() {}
   virtual void setGraphType() {}
   virtual void matchScale() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  NetGraph : public GuiGraphCtrl {
  public:
   virtual Script toggleKey() {}
   virtual Script updateStats() {}
   virtual Script toggleNetGraph() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  NetGraphGui : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  DR_StartDemoBtn : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  DR_CancelBtn : public GuiButtonCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  RecordingsDlgList : public GuiTextListCtrl {
  public:
};

class  recordingsDlg : public GuiControl {
  public:
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  HelpText : public GuiMLTextCtrl {
  public:
};

class  HelpFileList : public GuiTextListCtrl {
  public:
   virtual Script onSelect() {}
};

class  HelpDlg : public GuiControl {
  public:
   virtual Script onWake() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MessagePopText : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MessagePopFrame : public GuiWindowCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MessagePopupDlg : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MBOKCancelText : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MBOKCancelFrame : public GuiWindowCtrl {
  public:
};

class  MessageBoxOKCancelDlg : public GuiControl {
  public:
   virtual Script onSleep() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MBYesNoText : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MBYesNoFrame : public GuiWindowCtrl {
  public:
};

class  MessageBoxYesNoDlg : public GuiControl {
  public:
   virtual Script onSleep() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MBOKText : public GuiMLTextCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  MBOKFrame : public GuiWindowCtrl {
  public:
};

class  MessageBoxOKDlg : public GuiControl {
  public:
   virtual Script onSleep() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SA_nameEdit : public GuiTextEditCtrl {
  public:
};

class  SA_fileList : public GuiTextListCtrl {
  public:
   virtual Script onSelect() {}
};

class  SA_directoryList : public GuiPopUpMenuCtrl {
  public:
   virtual Script onSelect() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  SaveFileDlg : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  loadFileList : public GuiTextListCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  LoadFileDlg : public GuiControl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectAddFieldName : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectAddFieldValue : public GuiTextEditCtrl {
  public:
};

class  InspectAddFieldDlg : public GuiControl {
  public:
   virtual Script doAction() {}
};

class  InspectTreeView : public GuiTreeViewCtrl {
  public:
   virtual Script onSelect() {}
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectTreeTitle : public GuiWindowCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectFields : public GuiInspector {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectObjectName : public GuiTextEditCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectTitle : public GuiWindowCtrl {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  InspectDlg : public GuiControl {
  public:
};

class  GuiConsoleEditCtrl : public GuiTextEditCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
   /*!
    */
   string validate;
   /*!
    */
   string escapeCommand;
   /*!
    */
   int historySize;
   /*!
    */
   bool password;
   /*!
    */
   bool tabComplete;
   /*!
    */
   AudioProfilePtr deniedSound;
   /*!
    */
   bool sinkAllKeyEvents;

   /*! @name Misc
   @{ */
   /*!
    */
   bool useSiblingScroller;
   /// @}

};

class  ConsoleEntry : public GuiConsoleEditCtrl {
  public:
   virtual Script eval() {}
};

class  GuiConsole : public GuiArrayCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  testArrayCtrl : public GuiConsole {
  public:
};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  ConsoleDlg : public GuiControl {
  public:
};

class  GuiCanvas : public GuiCanvas {
  public:
   virtual Script popLayer() {}
   virtual Script popDialog() {}
   virtual Script pushDialog() {}
   virtual Script setContent() {}
   virtual Script checkCursor() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

/// Stub class
/// 
/// @note This is a stub class to ensure a proper class hierarchy. No 
///       information was available for this class.
class  Canvas : public GuiCanvas {
  public:
};

class  editor {
  public:
   virtual Script checkActiveLoadDone() {}
   virtual Script onAdd() {}
   virtual Script create() {}
};

class  ScriptGroup : public SimGroup {
  public:

   /*! @name Classes
   @{ */
   /*!
    */
   string class;
   /*!
    */
   string superClass;
   /// @}

};

class  SimDataBlock : public SimObject {
  public:
};

class  MaterialPropertyMap : public SimObject {
  public:
};

class  NetObject : public SimObject {
  public:
};

class  SceneObject : public NetObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

};

class  AudioEmitter : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name profile
   @{ */
   /*!
    */
   AudioProfilePtr profile;
   /*!
    */
   bool useProfileDescription;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   AudioDescriptionPtr description;
   /*!
    */
   filename fileName;
   /*!
    */
   int type;
   /// @}


   /*! @name sound
   @{ */
   /*!
    */
   float volume;
   /*!
    */
   bool outsideAmbient;
   /*!
    */
   float referenceDistance;
   /*!
    */
   float maxDistance;
   /// @}


   /*! @name Looping
   @{ */
   /*!
    */
   bool isLooping;
   /*!
    */
   bool is3D;
   /*!
    */
   int loopCount;
   /*!
    */
   int minLoopGap;
   /*!
    */
   int maxLoopGap;
   /// @}


   /*! @name Sound Cone
   @{ */
   /*!
    */
   int coneInsideAngle;
   /*!
    */
   int coneOutsideAngle;
   /*!
    */
   float coneOutsideVolume;
   /*!
    */
   Point3F coneVector;
   /// @}

};

class  GameBaseData : public SimDataBlock {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
};

class  ShapeBaseData : public GameBaseData {
  public:
   virtual bool checkDeployPos() {}
   virtual string getDeployTransform() {}
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

};

class  CameraData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

};

class  DebrisData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Display
   @{ */
   /*!
    */
   string Texture;
   /*!
    */
   filename shapeFile;
   /*!
    */
   bool render2D;
   /// @}


   /*! @name Datablocks
   @{ */
   /*!
    */
   ParticleEmitterDataPtr emitters;
   /*!
    */
   ExplosionDataPtr Explosion;
   /// @}


   /*! @name Physical Properties
   @{ */
   /*!
    */
   float elasticity;
   /*!
    */
   float friction;
   /*!
    */
   int numBounces;
   /*!
    */
   int bounceVariance;
   /*!
    */
   float minSpinSpeed;
   /*!
    */
   float maxSpinSpeed;
   /*!
    */
   float gravModifier;
   /*!
    */
   float terminalVelocity;
   /*!
    */
   float velocity;
   /*!
    */
   float velocityVariance;
   /*!
    */
   float lifetime;
   /*!
    */
   float lifetimeVariance;
   /*!
    */
   bool useRadiusMass;
   /*!
    */
   float baseRadius;
   /// @}


   /*! @name Behavior
   @{ */
   /*!
    */
   bool explodeOnMaxBounce;
   /*!
    */
   bool staticOnMaxBounce;
   /*!
    */
   bool snapOnMaxBounce;
   /*!
    */
   bool fade;
   /*!
    */
   bool ignoreWater;
   /// @}

};

class  SimDataBlockEvent {
  public:
};

class  Sim2DAudioEvent {
  public:
};

class  Sim3DAudioEvent {
  public:
};

class  SetMissionCRCEvent {
  public:
};

class  GuiNoMouseCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  ItemData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   string pickUpName;
   /*!
    */
   float friction;
   /*!
    */
   float elasticity;
   /*!
    */
   bool sticky;
   /*!
    */
   float gravityMod;
   /*!
    */
   float maxVelocity;
   /*!
    */
   int dynamicType;
   /*!
    */
   enumval lightType;
   /*!
    */
   ColorF lightColor;
   /*!
    */
   int LightTime;
   /*!
    */
   float lightRadius;
   /*!
    */
   bool lightOnlyStatic;
   /*!
    */
   string mat1Name;
   /*!
    */
   string mat2Name;
   /*!
    */
   string mat3Name;
   /*!
    */
   string mat4Name;
   /*!
    */
   string catName;
   /*!
    */
   string subCatName;
   /*!
    */
   string dyeMeshName;
};

class  MissionMarkerData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

};

class  GameBase : public SceneObject {
  public:
   virtual int getDataBlock() {}
   virtual bool setDataBlock() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  ShapeBase : public GameBase {
  public:
   virtual void unHideNode(nodeName) {}
   virtual void hideNode(nodeName) {}
   virtual void setNodeColor() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  MissionMarker : public ShapeBase {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  WayPoint : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString name;
   /*!
    */
   WaypointTeam team;
   /// @}

};

class  SpawnSphere : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name dimensions
   @{ */
   /*!
    */
   float radius;
   /// @}


   /*! @name Weight
   @{ */
   /*!
    */
   float sphereWeight;
   /*!
    */
   float indoorWeight;
   /*!
    */
   float outdoorWeight;
   /// @}

};

class  MazeSpawner : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Maze Info
   @{ */
   /*!
    */
   int xCells;
   /*!
    */
   int yCells;
   /*!
    */
   int cellSize;
   /*!
    */
   bool trim;
   /*!
    */
   bool noRelight;
   /*!
    */
   caseString interiorBaseName;
   /*!
    */
   caseString mazFile;
   /*!
    */
   caseString intFile;
   /*!
    */
   bool placeDoors;
   /*!
    */
   GameBaseDataPtr door;
   /*!
    */
   float doorOffsetX;
   /*!
    */
   float doorOffsetY;
   /*!
    */
   float doorOffsetZ;
   /*!
    */
   string triggerScale;
   /// @}

};

class  GoldSpawner : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name dimensions
   @{ */
   /*!
    */
   float radius;
   /// @}


   /*! @name Weight
   @{ */
   /*!
    */
   float sphereWeight;
   /*!
    */
   float indoorWeight;
   /*!
    */
   float outdoorWeight;
   /// @}


   /*! @name Gold
   @{ */
   /*!
    */
   int minAmount;
   /*!
    */
   int maxAmount;
   /*!
    */
   int goldCount;
   /*!
    */
   bool placeOnTerrain;
   /*!
    */
   bool avoidWater;
   /// @}

};

class  NPCSpawner : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name NPC Data
   @{ */
   /*!
    */
   caseString CharacterName;
   /*!
    */
   caseString BotChatScriptName;
   /// @}

};

class  RoomMarker : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Room Data
   @{ */
   /// @}

};

class  DestructableSpawner : public MissionMarker {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name dimensions
   @{ */
   /*!
    */
   float radius;
   /// @}


   /*! @name Destructables
   @{ */
   /*!
    */
   GameBaseDataPtr ShapeDataBlock;
   /*!
    */
   caseString LootName;
   /*!
    */
   int Count;
   /*!
    */
   int Retries;
   /*!
    */
   int RespawnTime;
   /*!
    */
   float CastDistance;
   /*!
    */
   bool AllowOnTerrain;
   /*!
    */
   bool AllowOnInteriors;
   /*!
    */
   bool AllowOnStatics;
   /*!
    */
   bool AllowUnderWater;
   /*!
    */
   float minSlope;
   /*!
    */
   float maxSlope;
   /*!
    */
   caseString color;
   /*!
    */
   int mat1;
   /*!
    */
   int mat2;
   /*!
    */
   int mat3;
   /*!
    */
   int mat4;
   /// @}

};

class  PathCameraData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

};

class  PlayerData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   bool renderFirstPerson;
   /*!
    */
   float pickupRadius;
   /*!
    */
   float minLookAngle;
   /*!
    */
   float maxLookAngle;
   /*!
    */
   float maxFreelookAngle;
   /*!
    */
   float maxTimeScale;
   /*!
    */
   float maxStepHeight;
   /*!
    */
   float runForce;
   /*!
    */
   float runEnergyDrain;
   /*!
    */
   float minRunEnergy;
   /*!
    */
   float maxForwardSpeed;
   /*!
    */
   float maxBackwardSpeed;
   /*!
    */
   float maxSideSpeed;
   /*!
    */
   float maxUnderwaterForwardSpeed;
   /*!
    */
   float maxUnderwaterBackwardSpeed;
   /*!
    */
   float maxUnderwaterSideSpeed;
   /*!
    */
   float runSurfaceAngle;
   /*!
    */
   float minImpactSpeed;
   /*!
    */
   int recoverDelay;
   /*!
    */
   float recoverRunForceScale;
   /*!
    */
   float jumpForce;
   /*!
    */
   float jumpEnergyDrain;
   /*!
    */
   float minJumpEnergy;
   /*!
    */
   float minJumpSpeed;
   /*!
    */
   float maxJumpSpeed;
   /*!
    */
   float jumpSurfaceAngle;
   /*!
    */
   int jumpDelay;
   /*!
    */
   Point3F boundingBox;
   /*!
    */
   bool ignoreScale;
   /*!
    */
   float boxHeadPercentage;
   /*!
    */
   float boxTorsoPercentage;
   /*!
    */
   int boxHeadLeftPercentage;
   /*!
    */
   int boxHeadRightPercentage;
   /*!
    */
   int boxHeadBackPercentage;
   /*!
    */
   int boxHeadFrontPercentage;
   /*!
    */
   float horizMaxSpeed;
   /*!
    */
   float horizResistSpeed;
   /*!
    */
   float horizResistFactor;
   /*!
    */
   float upMaxSpeed;
   /*!
    */
   float upResistSpeed;
   /*!
    */
   float upResistFactor;
   /*!
    */
   DecalDataPtr DecalData;
   /*!
    */
   float decalOffset;
   /*!
    */
   ParticleEmitterDataPtr footPuffEmitter;
   /*!
    */
   int footPuffNumParts;
   /*!
    */
   float footPuffRadius;
   /*!
    */
   ParticleEmitterDataPtr dustEmitter;
   /*!
    */
   AudioProfilePtr FootSoftSound;
   /*!
    */
   AudioProfilePtr FootHardSound;
   /*!
    */
   AudioProfilePtr FootMetalSound;
   /*!
    */
   AudioProfilePtr FootSnowSound;
   /*!
    */
   AudioProfilePtr FootShallowSound;
   /*!
    */
   AudioProfilePtr FootWadingSound;
   /*!
    */
   AudioProfilePtr FootUnderwaterSound;
   /*!
    */
   AudioProfilePtr FootBubblesSound;
   /*!
    */
   AudioProfilePtr movingBubblesSound;
   /*!
    */
   AudioProfilePtr waterBreathSound;
   /*!
    */
   AudioProfilePtr impactSoftSound;
   /*!
    */
   AudioProfilePtr impactHardSound;
   /*!
    */
   AudioProfilePtr impactMetalSound;
   /*!
    */
   AudioProfilePtr impactSnowSound;
   /*!
    */
   float mediumSplashSoundVelocity;
   /*!
    */
   float hardSplashSoundVelocity;
   /*!
    */
   float exitSplashSoundVelocity;
   /*!
    */
   AudioProfilePtr impactWaterEasy;
   /*!
    */
   AudioProfilePtr impactWaterMedium;
   /*!
    */
   AudioProfilePtr impactWaterHard;
   /*!
    */
   AudioProfilePtr exitingWater;
   /*!
    */
   SplashDataPtr Splash;
   /*!
    */
   float splashVelocity;
   /*!
    */
   float splashAngle;
   /*!
    */
   float splashFreqMod;
   /*!
    */
   float splashVelEpsilon;
   /*!
    */
   float bubbleEmitTime;
   /*!
    */
   ParticleEmitterDataPtr splashEmitter;
   /*!
    */
   float footstepSplashHeight;
   /*!
    */
   float groundImpactMinSpeed;
   /*!
    */
   Point3F groundImpactShakeFreq;
   /*!
    */
   Point3F groundImpactShakeAmp;
   /*!
    */
   float groundImpactShakeDuration;
   /*!
    */
   float groundImpactShakeFalloff;
   /*!
    */
   bool isHorse;
};

class  Player : public ShapeBase {
  public:
   virtual bool setHookLen(Float) {}
   virtual bool setHookPos(Vector) {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  ProjectileData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   ParticleEmitterDataPtr particleEmitter;
   /*!
    */
   ParticleEmitterDataPtr particleWaterEmitter;
   /*!
    */
   filename projectileShapeName;
   /*!
    */
   Point3F scale;
   /*!
    */
   AudioProfilePtr sound;
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr waterExplosion;
   /*!
    */
   ExplosionDataPtr bounceExplosion;
   /*!
    */
   ExplosionDataPtr stickExplosion;
   /*!
    */
   ExplosionDataPtr bloodExplosion;
   /*!
    */
   SplashDataPtr Splash;
   /*!
    */
   DecalDataPtr decals;
   /*!
    */
   bool hasLight;
   /*!
    */
   float lightRadius;
   /*!
    */
   ColorF lightColor;
   /*!
    */
   bool hasWaterLight;
   /*!
    */
   ColorF waterLightColor;
   /*!
    */
   bool isBallistic;
   /*!
    */
   float velInheritFactor;
   /*!
    */
   float muzzleVelocity;
   /*!
    */
   bool isHook;
   /*!
    */
   int lifetime;
   /*!
    */
   int armingDelay;
   /*!
    */
   int fadeDelay;
   /*!
    */
   bool explodeOnDeath;
   /*!
    */
   float bounceAngle;
   /*!
    */
   float bounceElasticity;
   /*!
    */
   float bounceFriction;
   /*!
    */
   float gravityMod;
};

class  Projectile : public GameBase {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   Point3F initialPosition;
   /*!
    */
   Point3F initialVelocity;
   /// @}


   /*! @name Source
   @{ */
   /*!
    */
   int sourceObject;
   /*!
    */
   int sourceSlot;
   /// @}

};

class  StaticShape : public ShapeBase {
  public:
   virtual void setPoweredState() {}
   virtual bool getPoweredState() {}
   virtual void setCollision() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  ScopeAlwaysShape : public StaticShape {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  ShapeBaseImageData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   bool emap;
   /*!
    */
   filename shapeFile;
   /*!
    */
   ProjectileDataPtr Projectile;
   /*!
    */
   bool cloakable;
   /*!
    */
   int mountPoint;
   /*!
    */
   MatrixPosition offset;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   MatrixPosition eyeOffset;
   /*!
    */
   MatrixRotation eyeRotation;
   /*!
    */
   bool correctMuzzleVector;
   /*!
    */
   bool firstPerson;
   /*!
    */
   float mass;
   /*!
    */
   bool usesEnergy;
   /*!
    */
   float minEnergy;
   /*!
    */
   bool accuFire;
   /*!
    */
   enumval lightType;
   /*!
    */
   ColorF lightColor;
   /*!
    */
   int LightTime;
   /*!
    */
   float lightRadius;
   /*!
    */
   DebrisDataPtr casing;
   /*!
    */
   Point3F shellExitDir;
   /*!
    */
   float shellExitVariance;
   /*!
    */
   float shellVelocity;
   /*!
    */
   caseString stateName;
   /*!
    */
   string stateTransitionOnLoaded;
   /*!
    */
   string stateTransitionOnNotLoaded;
   /*!
    */
   string stateTransitionOnAmmo;
   /*!
    */
   string stateTransitionOnNoAmmo;
   /*!
    */
   string stateTransitionOnTarget;
   /*!
    */
   string stateTransitionOnNoTarget;
   /*!
    */
   string stateTransitionOnWet;
   /*!
    */
   string stateTransitionOnNotWet;
   /*!
    */
   string stateTransitionOnTriggerUp;
   /*!
    */
   string stateTransitionOnTriggerDown;
   /*!
    */
   string stateTransitionOnTimeout;
   /*!
    */
   float stateTimeoutValue;
   /*!
    */
   bool stateWaitForTimeout;
   /*!
    */
   bool stateFire;
   /*!
    */
   bool stateEjectShell;
   /*!
    */
   float stateEnergyDrain;
   /*!
    */
   bool stateAllowImageChange;
   /*!
    */
   bool stateDirection;
   /*!
    */
   enumval stateLoadedFlag;
   /*!
    */
   enumval stateSpinThread;
   /*!
    */
   enumval stateRecoil;
   /*!
    */
   string stateSequence;
   /*!
    */
   bool stateSequenceRandomFlash;
   /*!
    */
   AudioProfilePtr stateSound;
   /*!
    */
   caseString stateScript;
   /*!
    */
   ParticleEmitterDataPtr stateEmitter;
   /*!
    */
   float stateEmitterTime;
   /*!
    */
   int stateEmitterNode;
   /*!
    */
   bool stateIgnoreLoadedForReady;
   /*!
    */
   bool computeCRC;
   /*!
    */
   caseString mat1Name;
   /*!
    */
   caseString mat2Name;
   /*!
    */
   caseString mat3Name;
   /*!
    */
   caseString mat4Name;
};

class  ShowTSCtrl : public GuiTSCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;
};

class  StaticShapeData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   bool noIndividualDamage;
   /*!
    */
   int dynamicType;
};

class  TSStatic : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename shapeName;
   /// @}

};

class  GuiCrossHairHud : public GuiBitmapCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool center;
   /*!
    */
   bool wrap;
   /// @}


   /*! @name Damage
   @{ */
   /*!
    */
   ColorF damageFillColor;
   /*!
    */
   ColorF damageFrameColor;
   /*!
    */
   Point2I damageRect;
   /*!
    */
   Point2I damageOffset;
   /*!
    */
   Point2I itemNameOffset;
   /// @}

};

class  GuiHealthBarHud : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name colors
   @{ */
   /*!
    */
   ColorF fillColor;
   /*!
    */
   ColorF frameColor;
   /*!
    */
   ColorF damageFillColor;
   /// @}


   /*! @name Pulse
   @{ */
   /*!
    */
   int pulseRate;
   /*!
    */
   float pulseThreshold;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool showFill;
   /*!
    */
   bool showFrame;
   /*!
    */
   bool displayEnergy;
   /// @}

};

class  GuiShapeNameHud : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name colors
   @{ */
   /*!
    */
   ColorF fillColor;
   /*!
    */
   ColorF frameColor;
   /*!
    */
   ColorF textColor;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool showFill;
   /*!
    */
   bool showFrame;
   /*!
    */
   float verticalOffset;
   /*!
    */
   float distanceFade;
   /// @}

};

class  Explosion : public GameBase {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  ExplosionData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   filename explosionShape;
   /*!
    */
   AudioProfilePtr soundProfile;
   /*!
    */
   bool faceViewer;
   /*!
    */
   ParticleEmitterDataPtr particleEmitter;
   /*!
    */
   int particleDensity;
   /*!
    */
   float particleRadius;
   /*!
    */
   Point3F explosionScale;
   /*!
    */
   float playSpeed;
   /*!
    */
   ParticleEmitterDataPtr emitter;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   float debrisThetaMin;
   /*!
    */
   float debrisThetaMax;
   /*!
    */
   float debrisPhiMin;
   /*!
    */
   float debrisPhiMax;
   /*!
    */
   int debrisNum;
   /*!
    */
   int debrisNumVariance;
   /*!
    */
   float debrisVelocity;
   /*!
    */
   float debrisVelocityVariance;
   /*!
    */
   ExplosionDataPtr subExplosion;
   /*!
    */
   int delayMS;
   /*!
    */
   int delayVariance;
   /*!
    */
   int lifetimeMS;
   /*!
    */
   int lifetimeVariance;
   /*!
    */
   float offset;
   /*!
    */
   float times;
   /*!
    */
   Point3F sizes;
   /*!
    */
   bool shakeCamera;
   /*!
    */
   Point3F camShakeFreq;
   /*!
    */
   Point3F camShakeAmp;
   /*!
    */
   float camShakeDuration;
   /*!
    */
   float camShakeRadius;
   /*!
    */
   float camShakeFalloff;
   /*!
    */
   float lightStartRadius;
   /*!
    */
   float lightEndRadius;
   /*!
    */
   ColorF lightStartColor;
   /*!
    */
   ColorF lightEndColor;
};

class  fxDTSBrickData : public GameBaseData {
  public:

   /*! @name fxDTSBrickData Stuff
   @{ */
   /*!
    */
   filename renderShapeName;
   /*!
    */
   filename collisionShapeName;
   /*!
    */
   filename brickFile;
   /*!
    */
   int topArea;
   /*!
    */
   int bottomArea;
   /*!
    */
   int northArea;
   /*!
    */
   int eastArea;
   /*!
    */
   int southArea;
   /*!
    */
   int westArea;
   /*!
    */
   bool canCoverTop;
   /*!
    */
   bool canCoverBottom;
   /*!
    */
   bool canCoverNorth;
   /*!
    */
   bool canCoverEast;
   /*!
    */
   bool canCoverSouth;
   /*!
    */
   bool canCoverWest;
   /*!
    */
   string category;
   /*!
    */
   string subCategory;
   /*!
    */
   string uiName;
   /*!
    */
   string iconName;
   /*!
    */
   int brickSizeX;
   /*!
    */
   int brickSizeY;
   /*!
    */
   int brickSizeZ;
   /// @}

};

class  fxBrickBatcher : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

};

class  StaticBrickDataEvent {
  public:
};

class  fxFoliageReplicator : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Debugging
   @{ */
   /*!
    */
   bool UseDebugInfo;
   /*!
    */
   float DebugBoxHeight;
   /*!
    */
   bool HideFoliage;
   /*!
    */
   bool ShowPlacementArea;
   /*!
    */
   int PlacementAreaHeight;
   /*!
    */
   ColorF PlacementColour;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   int Seed;
   /*!
    */
   filename FoliageFile;
   /*!
    */
   int FoliageCount;
   /*!
    */
   int FoliageRetries;
   /// @}


   /*! @name Area
   @{ */
   /*!
    */
   int InnerRadiusX;
   /*!
    */
   int InnerRadiusY;
   /*!
    */
   int OuterRadiusX;
   /*!
    */
   int OuterRadiusY;
   /// @}


   /*! @name dimensions
   @{ */
   /*!
    */
   float MinWidth;
   /*!
    */
   float MaxWidth;
   /*!
    */
   float MinHeight;
   /*!
    */
   float MaxHeight;
   /*!
    */
   bool FixAspectRatio;
   /*!
    */
   bool FixSizeToMax;
   /*!
    */
   float OffsetZ;
   /*!
    */
   bool RandomFlip;
   /// @}


   /*! @name Culling
   @{ */
   /*!
    */
   bool UseCulling;
   /*!
    */
   int CullResolution;
   /*!
    */
   float ViewDistance;
   /*!
    */
   float ViewClosest;
   /*!
    */
   float FadeInRegion;
   /*!
    */
   float FadeOutRegion;
   /*!
    */
   float AlphaCutoff;
   /*!
    */
   float GroundAlpha;
   /// @}


   /*! @name Animation
   @{ */
   /*!
    */
   bool SwayOn;
   /*!
    */
   bool SwaySync;
   /*!
    */
   float SwayMagSide;
   /*!
    */
   float SwayMagFront;
   /*!
    */
   float MinSwayTime;
   /*!
    */
   float MaxSwayTime;
   /// @}


   /*! @name Lighting
   @{ */
   /*!
    */
   bool LightOn;
   /*!
    */
   bool LightSync;
   /*!
    */
   float MinLuminance;
   /*!
    */
   float MaxLuminance;
   /*!
    */
   float LightTime;
   /// @}


   /*! @name Restrictions
   @{ */
   /*!
    */
   bool AllowOnTerrain;
   /*!
    */
   bool AllowOnInteriors;
   /*!
    */
   bool AllowOnStatics;
   /*!
    */
   bool AllowOnWater;
   /*!
    */
   bool AllowWaterSurface;
   /*!
    */
   int AllowedTerrainSlope;
   /// @}

};

class  fxGrassReplicator : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

   /*!
    */
   bool UseDebugInfo;
   /*!
    */
   float DebugBoxHeight;
   /*!
    */
   bool HideGrass;
   /*!
    */
   bool ShowPlacementArea;
   /*!
    */
   int PlacementAreaHeight;
   /*!
    */
   ColorF PlacementColour;
   /*!
    */
   int Seed;
   /*!
    */
   filename GrassFile;
   /*!
    */
   int GrassCount;
   /*!
    */
   int GrassRetries;
   /*!
    */
   int InnerRadiusX;
   /*!
    */
   int InnerRadiusY;
   /*!
    */
   int OuterRadiusX;
   /*!
    */
   int OuterRadiusY;
   /*!
    */
   float MinWidth;
   /*!
    */
   float MaxWidth;
   /*!
    */
   float MinHeight;
   /*!
    */
   float MaxHeight;
   /*!
    */
   bool FixAspectRatio;
   /*!
    */
   bool FixSizeToMax;
   /*!
    */
   float OffsetZ;
   /*!
    */
   bool RandomFlip;
   /*!
    */
   bool UseCulling;
   /*!
    */
   int CullResolution;
   /*!
    */
   float ViewDistance;
   /*!
    */
   float ViewClosest;
   /*!
    */
   float FadeInRegion;
   /*!
    */
   float FadeOutRegion;
   /*!
    */
   float AlphaCutoff;
   /*!
    */
   float GroundAlpha;
   /*!
    */
   bool SwayOn;
   /*!
    */
   bool SwaySync;
   /*!
    */
   float SwayMagSide;
   /*!
    */
   float SwayMagFront;
   /*!
    */
   float MinSwayTime;
   /*!
    */
   float MaxSwayTime;
   /*!
    */
   bool LightOn;
   /*!
    */
   bool LightSync;
   /*!
    */
   float MinLuminance;
   /*!
    */
   float MaxLuminance;
   /*!
    */
   float LightTime;
   /*!
    */
   bool UseSunLight;
   /*!
    */
   bool AllowOnTerrain;
   /*!
    */
   bool AllowOnInteriors;
   /*!
    */
   bool AllowOnStatics;
   /*!
    */
   bool AllowOnWater;
   /*!
    */
   bool AllowWaterSurface;
   /*!
    */
   int AllowedTerrainSlope;
   /*!
    */
   ColorF FoilageColourTop;
   /*!
    */
   ColorF FoilageColourBtm;
   /*!
    */
   bool UseColour;
   /*!
    */
   bool IsRandomRot;
   /*!
    */
   bool IsSquareArea;
   /*!
    */
   float RotationAngle;
   /*!
    */
   bool SurfaceExclusionMode;
   /*!
    */
   enumval SurfaceType;
};

class  fxLightData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   bool LightOn;
   /*!
    */
   float radius;
   /*!
    */
   float Brightness;
   /*!
    */
   ColorF Colour;
   /*!
    */
   bool FlareOn;
   /*!
    */
   bool FlareTP;
   /*!
    */
   filename FlareBitmap;
   /*!
    */
   ColorF FlareColour;
   /*!
    */
   bool ConstantSizeOn;
   /*!
    */
   float ConstantSize;
   /*!
    */
   float NearSize;
   /*!
    */
   float FarSize;
   /*!
    */
   float NearDistance;
   /*!
    */
   float FarDistance;
   /*!
    */
   float FadeTime;
   /*!
    */
   int BlendMode;
   /*!
    */
   bool AnimColour;
   /*!
    */
   bool AnimBrightness;
   /*!
    */
   bool AnimRadius;
   /*!
    */
   bool AnimOffsets;
   /*!
    */
   bool AnimRotation;
   /*!
    */
   bool LinkFlare;
   /*!
    */
   bool LinkFlareSize;
   /*!
    */
   ColorF MinColour;
   /*!
    */
   ColorF MaxColour;
   /*!
    */
   float MinBrightness;
   /*!
    */
   float MaxBrightness;
   /*!
    */
   float MinRadius;
   /*!
    */
   float MaxRadius;
   /*!
    */
   Point3F StartOffset;
   /*!
    */
   Point3F EndOffset;
   /*!
    */
   float MinRotation;
   /*!
    */
   float MaxRotation;
   /*!
    */
   bool SingleColourKeys;
   /*!
    */
   string RedKeys;
   /*!
    */
   string GreenKeys;
   /*!
    */
   string BlueKeys;
   /*!
    */
   string BrightnessKeys;
   /*!
    */
   string RadiusKeys;
   /*!
    */
   string OffsetKeys;
   /*!
    */
   string RotationKeys;
   /*!
    */
   float ColourTime;
   /*!
    */
   float BrightnessTime;
   /*!
    */
   float RadiusTime;
   /*!
    */
   float OffsetTime;
   /*!
    */
   float RotationTime;
   /*!
    */
   bool LerpColour;
   /*!
    */
   bool LerpBrightness;
   /*!
    */
   bool LerpRadius;
   /*!
    */
   bool LerpOffset;
   /*!
    */
   bool LerpRotation;
};

class  fxShapeReplicator : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Debugging
   @{ */
   /*!
    */
   bool HideReplications;
   /*!
    */
   bool ShowPlacementArea;
   /*!
    */
   int PlacementAreaHeight;
   /*!
    */
   ColorF PlacementColour;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename shapeFile;
   /// @}


   /*! @name Replications
   @{ */
   /*!
    */
   int Seed;
   /*!
    */
   int ShapeCount;
   /*!
    */
   int ShapeRetries;
   /// @}


   /*! @name Placement Radius
   @{ */
   /*!
    */
   int InnerRadiusX;
   /*!
    */
   int InnerRadiusY;
   /*!
    */
   int OuterRadiusX;
   /*!
    */
   int OuterRadiusY;
   /// @}


   /*! @name Restraints
   @{ */
   /*!
    */
   bool AllowOnTerrain;
   /*!
    */
   bool AllowOnInteriors;
   /*!
    */
   bool AllowOnStatics;
   /*!
    */
   bool AllowOnWater;
   /*!
    */
   bool AllowWaterSurface;
   /*!
    */
   bool AlignToTerrain;
   /*!
    */
   bool Interactions;
   /*!
    */
   int AllowedTerrainSlope;
   /*!
    */
   Point3F TerrainAlignment;
   /// @}


   /*! @name Object Transforms
   @{ */
   /*!
    */
   bool FixShapeAspect;
   /*!
    */
   Point3F ShapeScaleMin;
   /*!
    */
   Point3F ShapeScaleMax;
   /*!
    */
   Point3F ShapeRotateMin;
   /*!
    */
   Point3F ShapeRotateMax;
   /*!
    */
   int OffsetZ;
   /// @}

};

class  fxShapeReplicatedStatic : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename shapeName;
   /// @}

};

class  LightningData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   AudioProfilePtr strikeSound;
   /*!
    */
   AudioProfilePtr thunderSounds;
   /*!
    */
   string strikeTextures;
};

class  LightningStrikeEvent {
  public:
};

class  ParticleEmitterNodeData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   float timeMultiple;
};

class  ParticleEmitterNode : public GameBase {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   ParticleEmitterDataPtr emitter;
   /*!
    */
   float velocity;
};

class  ParticleEmitterData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   int ejectionPeriodMS;
   /*!
    */
   int periodVarianceMS;
   /*!
    */
   float ejectionVelocity;
   /*!
    */
   float velocityVariance;
   /*!
    */
   float ejectionOffset;
   /*!
    */
   float thetaMin;
   /*!
    */
   float thetaMax;
   /*!
    */
   float phiReferenceVel;
   /*!
    */
   float phiVariance;
   /*!
    */
   bool overrideAdvance;
   /*!
    */
   bool orientParticles;
   /*!
    */
   bool orientOnVelocity;
   /*!
    */
   string particles;
   /*!
    */
   int lifetimeMS;
   /*!
    */
   int lifetimeVarianceMS;
   /*!
    */
   bool useEmitterSizes;
   /*!
    */
   bool useEmitterColors;
   /*!
    */
   bool usePlacementForVelocity;
};

class  ParticleData : public SimDataBlock {
  public:
   /*!
    */
   float dragCoefficient;
   /*!
    */
   float windCoefficient;
   /*!
    */
   float gravityCoefficient;
   /*!
    */
   float inheritedVelFactor;
   /*!
    */
   float constantAcceleration;
   /*!
    */
   int lifetimeMS;
   /*!
    */
   int lifetimeVarianceMS;
   /*!
    */
   float spinSpeed;
   /*!
    */
   float spinRandomMin;
   /*!
    */
   float spinRandomMax;
   /*!
    */
   bool useInvAlpha;
   /*!
    */
   bool animateTexture;
   /*!
    */
   int framesPerSec;
   /*!
    */
   filename textureName;
   /*!
    */
   filename animTexName;
   /*!
    */
   ColorF colors;
   /*!
    */
   float sizes;
   /*!
    */
   float times;
};

class  PrecipitationData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   AudioProfilePtr soundProfile;
   /*!
    */
   filename dropTexture;
   /*!
    */
   filename splashTexture;
   /*!
    */
   float dropSize;
   /*!
    */
   float splashSize;
   /*!
    */
   bool useTrueBillboards;
   /*!
    */
   int splashMS;
};

class  SplashData : public GameBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   AudioProfilePtr soundProfile;
   /*!
    */
   Point3F scale;
   /*!
    */
   ParticleEmitterDataPtr emitter;
   /*!
    */
   int delayMS;
   /*!
    */
   int delayVariance;
   /*!
    */
   int lifetimeMS;
   /*!
    */
   int lifetimeVariance;
   /*!
    */
   float width;
   /*!
    */
   int numSegments;
   /*!
    */
   float velocity;
   /*!
    */
   float height;
   /*!
    */
   float acceleration;
   /*!
    */
   float times;
   /*!
    */
   ColorF colors;
   /*!
    */
   filename Texture;
   /*!
    */
   float texWrap;
   /*!
    */
   float texFactor;
   /*!
    */
   float ejectionFreq;
   /*!
    */
   float ejectionAngle;
   /*!
    */
   float ringLifetime;
   /*!
    */
   float startRadius;
   /*!
    */
   ExplosionDataPtr Explosion;
};

class  Splash : public GameBase {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  twSurfaceReference : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

   /*!
    */
   bool ShowPlacementArea;
   /*!
    */
   int PlacementAreaHeight;
   /*!
    */
   ColorF PlacementColour;
   /*!
    */
   enumval SurfaceType;
};

class  volumeLight : public SceneObject {
  public:
   virtual void settailColour(r, g, b, a) {}
   virtual void setfootColour(r, g, b, a) {}
   virtual void setSubdivideV(value) {}
   virtual void setSubdivideU(value) {}
   virtual void setYextent(value) {}
   virtual void setXextent(value) {}
   virtual void setShootDistance(value) {}
   virtual void setlpDistance(value) {}
   virtual void setLTexture(bitmap) {}
   virtual void setEnable(status) {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

   /*!
    */
   bool Enable;
   /*!
    */
   filename Texture;
   /*!
    */
   float lpDistance;
   /*!
    */
   float ShootDistance;
   /*!
    */
   float Xextent;
   /*!
    */
   float Yextent;
   /*!
    */
   int SubdivideU;
   /*!
    */
   int SubdivideV;
   /*!
    */
   ColorF FootColour;
   /*!
    */
   ColorF TailColour;
};

class  RemoteCommandEvent {
  public:
};

class  SimpleMessageEvent {
  public:
};

class  VehicleData : public ShapeBaseData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   float jetForce;
   /*!
    */
   float jetEnergyDrain;
   /*!
    */
   float minJetEnergy;
   /*!
    */
   Point3F massCenter;
   /*!
    */
   Point3F massBox;
   /*!
    */
   float bodyRestitution;
   /*!
    */
   float bodyFriction;
   /*!
    */
   AudioProfilePtr softImpactSound;
   /*!
    */
   AudioProfilePtr hardImpactSound;
   /*!
    */
   float minImpactSpeed;
   /*!
    */
   float softImpactSpeed;
   /*!
    */
   float hardImpactSpeed;
   /*!
    */
   float minRollSpeed;
   /*!
    */
   float maxSteeringAngle;
   /*!
    */
   float maxDrag;
   /*!
    */
   float minDrag;
   /*!
    */
   int integration;
   /*!
    */
   float collisionTol;
   /*!
    */
   float contactTol;
   /*!
    */
   bool cameraRoll;
   /*!
    */
   float cameraLag;
   /*!
    */
   float cameraDecay;
   /*!
    */
   float cameraOffset;
   /*!
    */
   ParticleEmitterDataPtr dustEmitter;
   /*!
    */
   float triggerDustHeight;
   /*!
    */
   float dustHeight;
   /*!
    */
   ParticleEmitterDataPtr damageEmitter;
   /*!
    */
   ParticleEmitterDataPtr splashEmitter;
   /*!
    */
   Point3F damageEmitterOffset;
   /*!
    */
   float damageLevelTolerance;
   /*!
    */
   float numDmgEmitterAreas;
   /*!
    */
   float splashFreqMod;
   /*!
    */
   float splashVelEpsilon;
   /*!
    */
   float exitSplashSoundVelocity;
   /*!
    */
   float softSplashSoundVelocity;
   /*!
    */
   float mediumSplashSoundVelocity;
   /*!
    */
   float hardSplashSoundVelocity;
   /*!
    */
   AudioProfilePtr exitingWater;
   /*!
    */
   AudioProfilePtr impactWaterEasy;
   /*!
    */
   AudioProfilePtr impactWaterMedium;
   /*!
    */
   AudioProfilePtr impactWaterHard;
   /*!
    */
   AudioProfilePtr waterWakeSound;
   /*!
    */
   float collDamageThresholdVel;
   /*!
    */
   float collDamageMultiplier;
};

class  FlyingVehicleData : public VehicleData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   float jetForce;
   /*!
    */
   float jetEnergyDrain;
   /*!
    */
   float minJetEnergy;
   /*!
    */
   Point3F massCenter;
   /*!
    */
   Point3F massBox;
   /*!
    */
   float bodyRestitution;
   /*!
    */
   float bodyFriction;
   /*!
    */
   AudioProfilePtr softImpactSound;
   /*!
    */
   AudioProfilePtr hardImpactSound;
   /*!
    */
   float minImpactSpeed;
   /*!
    */
   float softImpactSpeed;
   /*!
    */
   float hardImpactSpeed;
   /*!
    */
   float minRollSpeed;
   /*!
    */
   float maxSteeringAngle;
   /*!
    */
   float maxDrag;
   /*!
    */
   float minDrag;
   /*!
    */
   int integration;
   /*!
    */
   float collisionTol;
   /*!
    */
   float contactTol;
   /*!
    */
   bool cameraRoll;
   /*!
    */
   float cameraLag;
   /*!
    */
   float cameraDecay;
   /*!
    */
   float cameraOffset;
   /*!
    */
   ParticleEmitterDataPtr dustEmitter;
   /*!
    */
   float triggerDustHeight;
   /*!
    */
   float dustHeight;
   /*!
    */
   ParticleEmitterDataPtr damageEmitter;
   /*!
    */
   ParticleEmitterDataPtr splashEmitter;
   /*!
    */
   Point3F damageEmitterOffset;
   /*!
    */
   float damageLevelTolerance;
   /*!
    */
   float numDmgEmitterAreas;
   /*!
    */
   float splashFreqMod;
   /*!
    */
   float splashVelEpsilon;
   /*!
    */
   float exitSplashSoundVelocity;
   /*!
    */
   float softSplashSoundVelocity;
   /*!
    */
   float mediumSplashSoundVelocity;
   /*!
    */
   float hardSplashSoundVelocity;
   /*!
    */
   AudioProfilePtr exitingWater;
   /*!
    */
   AudioProfilePtr impactWaterEasy;
   /*!
    */
   AudioProfilePtr impactWaterMedium;
   /*!
    */
   AudioProfilePtr impactWaterHard;
   /*!
    */
   AudioProfilePtr waterWakeSound;
   /*!
    */
   float collDamageThresholdVel;
   /*!
    */
   float collDamageMultiplier;
   /*!
    */
   AudioProfilePtr jetSound;
   /*!
    */
   AudioProfilePtr engineSound;
   /*!
    */
   float maneuveringForce;
   /*!
    */
   float horizontalSurfaceForce;
   /*!
    */
   float verticalSurfaceForce;
   /*!
    */
   float autoInputDamping;
   /*!
    */
   float steeringForce;
   /*!
    */
   float steeringRollForce;
   /*!
    */
   float rollForce;
   /*!
    */
   float autoAngularForce;
   /*!
    */
   float rotationalDrag;
   /*!
    */
   float autoLinearForce;
   /*!
    */
   float maxAutoSpeed;
   /*!
    */
   float hoverHeight;
   /*!
    */
   float createHoverHeight;
   /*!
    */
   ParticleEmitterDataPtr forwardJetEmitter;
   /*!
    */
   ParticleEmitterDataPtr backwardJetEmitter;
   /*!
    */
   ParticleEmitterDataPtr downJetEmitter;
   /*!
    */
   ParticleEmitterDataPtr trailEmitter;
   /*!
    */
   float minTrailSpeed;
   /*!
    */
   float vertThrustMultiple;
};

class  GuiSpeedometerHud : public GuiBitmapCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool center;
   /*!
    */
   bool wrap;
   /// @}


   /*! @name Needle
   @{ */
   /*!
    */
   float maxSpeed;
   /*!
    */
   float minAngle;
   /*!
    */
   float maxAngle;
   /*!
    */
   ColorF color;
   /*!
    */
   Point2F center;
   /*!
    */
   float length;
   /*!
    */
   float width;
   /*!
    */
   float tail;
   /// @}

};

class  HoverVehicleData : public VehicleData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   float jetForce;
   /*!
    */
   float jetEnergyDrain;
   /*!
    */
   float minJetEnergy;
   /*!
    */
   Point3F massCenter;
   /*!
    */
   Point3F massBox;
   /*!
    */
   float bodyRestitution;
   /*!
    */
   float bodyFriction;
   /*!
    */
   AudioProfilePtr softImpactSound;
   /*!
    */
   AudioProfilePtr hardImpactSound;
   /*!
    */
   float minImpactSpeed;
   /*!
    */
   float softImpactSpeed;
   /*!
    */
   float hardImpactSpeed;
   /*!
    */
   float minRollSpeed;
   /*!
    */
   float maxSteeringAngle;
   /*!
    */
   float maxDrag;
   /*!
    */
   float minDrag;
   /*!
    */
   int integration;
   /*!
    */
   float collisionTol;
   /*!
    */
   float contactTol;
   /*!
    */
   bool cameraRoll;
   /*!
    */
   float cameraLag;
   /*!
    */
   float cameraDecay;
   /*!
    */
   float cameraOffset;
   /*!
    */
   ParticleEmitterDataPtr dustEmitter;
   /*!
    */
   float triggerDustHeight;
   /*!
    */
   float dustHeight;
   /*!
    */
   ParticleEmitterDataPtr damageEmitter;
   /*!
    */
   ParticleEmitterDataPtr splashEmitter;
   /*!
    */
   Point3F damageEmitterOffset;
   /*!
    */
   float damageLevelTolerance;
   /*!
    */
   float numDmgEmitterAreas;
   /*!
    */
   float splashFreqMod;
   /*!
    */
   float splashVelEpsilon;
   /*!
    */
   float exitSplashSoundVelocity;
   /*!
    */
   float softSplashSoundVelocity;
   /*!
    */
   float mediumSplashSoundVelocity;
   /*!
    */
   float hardSplashSoundVelocity;
   /*!
    */
   AudioProfilePtr exitingWater;
   /*!
    */
   AudioProfilePtr impactWaterEasy;
   /*!
    */
   AudioProfilePtr impactWaterMedium;
   /*!
    */
   AudioProfilePtr impactWaterHard;
   /*!
    */
   AudioProfilePtr waterWakeSound;
   /*!
    */
   float collDamageThresholdVel;
   /*!
    */
   float collDamageMultiplier;
   /*!
    */
   float dragForce;
   /*!
    */
   float vertFactor;
   /*!
    */
   float floatingThrustFactor;
   /*!
    */
   float mainThrustForce;
   /*!
    */
   float reverseThrustForce;
   /*!
    */
   float strafeThrustForce;
   /*!
    */
   float turboFactor;
   /*!
    */
   float stabLenMin;
   /*!
    */
   float stabLenMax;
   /*!
    */
   float stabSpringConstant;
   /*!
    */
   float stabDampingConstant;
   /*!
    */
   float gyroDrag;
   /*!
    */
   float normalForce;
   /*!
    */
   float restorativeForce;
   /*!
    */
   float steeringForce;
   /*!
    */
   float rollForce;
   /*!
    */
   float pitchForce;
   /*!
    */
   AudioProfilePtr jetSound;
   /*!
    */
   AudioProfilePtr engineSound;
   /*!
    */
   AudioProfilePtr floatSound;
   /*!
    */
   ParticleEmitterDataPtr dustTrailEmitter;
   /*!
    */
   Point3F dustTrailOffset;
   /*!
    */
   float triggerTrailHeight;
   /*!
    */
   float dustTrailFreqMod;
   /*!
    */
   float floatingGravMag;
   /*!
    */
   float brakingForce;
   /*!
    */
   float brakingActivationSpeed;
   /*!
    */
   ParticleEmitterDataPtr forwardJetEmitter;
};

class  Vehicle : public ShapeBase {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   bool disableMove;
};

class  HoverVehicle : public Vehicle {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   bool disableMove;
};

class  VehicleBlocker : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

   /*!
    */
   Point3F dimensions;
};

class  WheeledVehicleTire : public SimDataBlock {
  public:
   /*!
    */
   filename shapeFile;
   /*!
    */
   float mass;
   /*!
    */
   float radius;
   /*!
    */
   float staticFriction;
   /*!
    */
   float kineticFriction;
   /*!
    */
   float restitution;
   /*!
    */
   float lateralForce;
   /*!
    */
   float lateralDamping;
   /*!
    */
   float lateralRelaxation;
   /*!
    */
   float longitudinalForce;
   /*!
    */
   float longitudinalDamping;
   /*!
    */
   float logitudinalRelaxation;
};

class  WheeledVehicleSpring : public SimDataBlock {
  public:
   /*!
    */
   float length;
   /*!
    */
   float force;
   /*!
    */
   float damping;
   /*!
    */
   float antiSwayForce;
};

class  WheeledVehicleData : public VehicleData {
  public:
   /*!
    */
   caseString category;
   /*!
    */
   string className;

   /*! @name Render
   @{ */
   /*!
    */
   filename shapeFile;
   /*!
    */
   filename cloakTexture;
   /*!
    */
   bool emap;
   /// @}


   /*! @name Destruction
   
   Parameters related to the destruction effects of this object.
   @{ */
   /*!
    */
   ExplosionDataPtr Explosion;
   /*!
    */
   ExplosionDataPtr underwaterExplosion;
   /*!
    */
   DebrisDataPtr Debris;
   /*!
    */
   bool renderWhenDestroyed;
   /*!
    */
   filename debrisShapeName;
   /// @}


   /*! @name Physics
   @{ */
   /*!
    */
   float mass;
   /*!
    */
   float drag;
   /*!
    */
   float density;
   /// @}


   /*! @name Damage/Energy
   @{ */
   /*!
    */
   float maxEnergy;
   /*!
    */
   float maxDamage;
   /*!
    */
   float disabledLevel;
   /*!
    */
   float destroyedLevel;
   /*!
    */
   float repairRate;
   /*!
    */
   bool inheritEnergyFromMount;
   /*!
    */
   bool isInvincible;
   /// @}


   /*! @name Camera
   @{ */
   /*!
    */
   float cameraMaxDist;
   /*!
    */
   float cameraMinDist;
   /*!
    */
   float cameraDefaultFov;
   /*!
    */
   float cameraMinFov;
   /*!
    */
   float cameraMaxFov;
   /*!
    */
   bool firstPersonOnly;
   /*!
    */
   bool useEyePoint;
   /*!
    */
   bool observeThroughObject;
   /// @}


   /*! @name HUD
   
   @deprecated Likely to be removed soon.
   @{ */
   /*!
    */
   string hudImageName;
   /*!
    */
   string hudImageNameFriendly;
   /*!
    */
   string hudImageNameEnemy;
   /*!
    */
   bool hudRenderCenter;
   /*!
    */
   bool hudRenderModulated;
   /*!
    */
   bool hudRenderAlways;
   /*!
    */
   bool hudRenderDistance;
   /*!
    */
   bool hudRenderName;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool aiAvoidThis;
   /*!
    */
   bool computeCRC;
   /// @}

   /*!
    */
   float jetForce;
   /*!
    */
   float jetEnergyDrain;
   /*!
    */
   float minJetEnergy;
   /*!
    */
   Point3F massCenter;
   /*!
    */
   Point3F massBox;
   /*!
    */
   float bodyRestitution;
   /*!
    */
   float bodyFriction;
   /*!
    */
   AudioProfilePtr softImpactSound;
   /*!
    */
   AudioProfilePtr hardImpactSound;
   /*!
    */
   float minImpactSpeed;
   /*!
    */
   float softImpactSpeed;
   /*!
    */
   float hardImpactSpeed;
   /*!
    */
   float minRollSpeed;
   /*!
    */
   float maxSteeringAngle;
   /*!
    */
   float maxDrag;
   /*!
    */
   float minDrag;
   /*!
    */
   int integration;
   /*!
    */
   float collisionTol;
   /*!
    */
   float contactTol;
   /*!
    */
   bool cameraRoll;
   /*!
    */
   float cameraLag;
   /*!
    */
   float cameraDecay;
   /*!
    */
   float cameraOffset;
   /*!
    */
   ParticleEmitterDataPtr dustEmitter;
   /*!
    */
   float triggerDustHeight;
   /*!
    */
   float dustHeight;
   /*!
    */
   ParticleEmitterDataPtr damageEmitter;
   /*!
    */
   ParticleEmitterDataPtr splashEmitter;
   /*!
    */
   Point3F damageEmitterOffset;
   /*!
    */
   float damageLevelTolerance;
   /*!
    */
   float numDmgEmitterAreas;
   /*!
    */
   float splashFreqMod;
   /*!
    */
   float splashVelEpsilon;
   /*!
    */
   float exitSplashSoundVelocity;
   /*!
    */
   float softSplashSoundVelocity;
   /*!
    */
   float mediumSplashSoundVelocity;
   /*!
    */
   float hardSplashSoundVelocity;
   /*!
    */
   AudioProfilePtr exitingWater;
   /*!
    */
   AudioProfilePtr impactWaterEasy;
   /*!
    */
   AudioProfilePtr impactWaterMedium;
   /*!
    */
   AudioProfilePtr impactWaterHard;
   /*!
    */
   AudioProfilePtr waterWakeSound;
   /*!
    */
   float collDamageThresholdVel;
   /*!
    */
   float collDamageMultiplier;
   /*!
    */
   AudioProfilePtr jetSound;
   /*!
    */
   AudioProfilePtr engineSound;
   /*!
    */
   AudioProfilePtr squealSound;
   /*!
    */
   AudioProfilePtr WheelImpactSound;
   /*!
    */
   ParticleEmitterDataPtr tireEmitter;
   /*!
    */
   float maxWheelSpeed;
   /*!
    */
   float engineTorque;
   /*!
    */
   float engineBrake;
   /*!
    */
   float brakeTorque;
};

class  GuiAviBitmapCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool done;
   /// @}

};

class  GuiBorderButtonCtrl : public GuiButtonBaseCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString text;
   /*!
    */
   int groupNum;
   /*!
    */
   enumval buttonType;
   /// @}

};

class  GuiBubbleTextCtrl : public GuiTextCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
};

class  GuiControlProfile : public SimObject {
  public:
   /*!
    */
   bool tab;
   /*!
    */
   bool canKeyFocus;
   /*!
    */
   bool mouseOverSelected;
   /*!
    */
   bool modal;
   /*!
    */
   bool opaque;
   /*!
    */
   ColorI fillColor;
   /*!
    */
   ColorI fillColorHL;
   /*!
    */
   ColorI fillColorNA;
   /*!
    */
   int border;
   /*!
    */
   int borderThickness;
   /*!
    */
   ColorI borderColor;
   /*!
    */
   ColorI borderColorHL;
   /*!
    */
   ColorI borderColorNA;
   /*!
    */
   string fontType;
   /*!
    */
   int fontSize;
   /*!
    */
   ColorI fontColors;
   /*!
    */
   ColorI fontColor;
   /*!
    */
   ColorI fontColorHL;
   /*!
    */
   ColorI fontColorNA;
   /*!
    */
   ColorI fontColorSEL;
   /*!
    */
   ColorI fontColorLink;
   /*!
    */
   ColorI fontColorLinkHL;
   /*!
    */
   enumval justify;
   /*!
    */
   Point2I textOffset;
   /*!
    */
   bool autoSizeWidth;
   /*!
    */
   bool autoSizeHeight;
   /*!
    */
   bool returnTab;
   /*!
    */
   bool numbersOnly;
   /*!
    */
   ColorI cursorColor;
   /*!
    */
   filename bitmap;
   /*!
    */
   AudioProfilePtr soundButtonDown;
   /*!
    */
   AudioProfilePtr soundButtonOver;
};

class  GuiCursor : public SimObject {
  public:
   /*!
    */
   Point2I hotSpot;
   /*!
    */
   filename bitmapName;
};

class  GuiBackgroundCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  GuiTextEditSliderCtrl : public GuiTextEditCtrl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
   /*!
    */
   string validate;
   /*!
    */
   string escapeCommand;
   /*!
    */
   int historySize;
   /*!
    */
   bool password;
   /*!
    */
   bool tabComplete;
   /*!
    */
   AudioProfilePtr deniedSound;
   /*!
    */
   bool sinkAllKeyEvents;
   /*!
    */
   string format;
   /*!
    */
   Point2F range;
   /*!
    */
   float increment;
};

class  GuiMouseEventCtrl : public GuiControl {
  public:

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   bool lockMouse;
};

class  MirrorSubObject : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

};

class  PathedInteriorData : public GameBaseData {
  public:
   /*!
    */
   AudioProfilePtr StartSound;
   /*!
    */
   AudioProfilePtr SustainSound;
   /*!
    */
   AudioProfilePtr StopSound;
   /*!
    */
   caseString category;
   /*!
    */
   string className;
};

class  NetStringEvent {
  public:
};

class  DecalManager : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

};

class  DecalData : public SimDataBlock {
  public:
   /*!
    */
   float sizeX;
   /*!
    */
   float sizeY;
   /*!
    */
   filename textureName;
};

class  ConnectionMessageEvent {
  public:
};

class  FileDownloadRequestEvent {
  public:
};

class  FileChunkEvent {
  public:
};

class  GhostAlwaysObjectEvent {
  public:
};

class  PathManagerEvent {
  public:
};

class  Marker : public SceneObject {
  public:

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}

   /*!
    */
   int seqNum;
   /*!
    */
   enumval type;
   /*!
    */
   int msToNext;
   /*!
    */
   enumval smoothingType;
   /// @}

};

class  Sun : public NetObject {
  public:

   /*! @name Misc
   @{ */
   /*!
    */
   float azimuth;
   /*!
    */
   float elevation;
   /*!
    */
   ColorF color;
   /*!
    */
   ColorF ambient;
   /// @}

};

class  TSShapeConstructor : public SimDataBlock {
  public:

   /*! @name Media
   @{ */
   /*!
    */
   filename baseShape;
   /// @}


   /*! @name Sequences
   @{ */
   /*!
    */
   filename sequence0;
   /*!
    */
   filename sequence1;
   /*!
    */
   filename sequence2;
   /*!
    */
   filename sequence3;
   /*!
    */
   filename sequence4;
   /*!
    */
   filename sequence5;
   /*!
    */
   filename sequence6;
   /*!
    */
   filename sequence7;
   /*!
    */
   filename sequence8;
   /*!
    */
   filename sequence9;
   /*!
    */
   filename sequence10;
   /*!
    */
   filename sequence11;
   /*!
    */
   filename sequence12;
   /*!
    */
   filename sequence13;
   /*!
    */
   filename sequence14;
   /*!
    */
   filename sequence15;
   /*!
    */
   filename sequence16;
   /*!
    */
   filename sequence17;
   /*!
    */
   filename sequence18;
   /*!
    */
   filename sequence19;
   /*!
    */
   filename sequence20;
   /*!
    */
   filename sequence21;
   /*!
    */
   filename sequence22;
   /*!
    */
   filename sequence23;
   /*!
    */
   filename sequence24;
   /*!
    */
   filename sequence25;
   /*!
    */
   filename sequence26;
   /*!
    */
   filename sequence27;
   /*!
    */
   filename sequence28;
   /*!
    */
   filename sequence29;
   /*!
    */
   filename sequence30;
   /*!
    */
   filename sequence31;
   /*!
    */
   filename sequence32;
   /*!
    */
   filename sequence33;
   /*!
    */
   filename sequence34;
   /*!
    */
   filename sequence35;
   /*!
    */
   filename sequence36;
   /*!
    */
   filename sequence37;
   /*!
    */
   filename sequence38;
   /*!
    */
   filename sequence39;
   /*!
    */
   filename sequence40;
   /*!
    */
   filename sequence41;
   /*!
    */
   filename sequence42;
   /*!
    */
   filename sequence43;
   /*!
    */
   filename sequence44;
   /*!
    */
   filename sequence45;
   /*!
    */
   filename sequence46;
   /*!
    */
   filename sequence47;
   /*!
    */
   filename sequence48;
   /*!
    */
   filename sequence49;
   /*!
    */
   filename sequence50;
   /*!
    */
   filename sequence51;
   /*!
    */
   filename sequence52;
   /*!
    */
   filename sequence53;
   /*!
    */
   filename sequence54;
   /*!
    */
   filename sequence55;
   /*!
    */
   filename sequence56;
   /*!
    */
   filename sequence57;
   /*!
    */
   filename sequence58;
   /*!
    */
   filename sequence59;
   /*!
    */
   filename sequence60;
   /*!
    */
   filename sequence61;
   /*!
    */
   filename sequence62;
   /*!
    */
   filename sequence63;
   /*!
    */
   filename sequence64;
   /*!
    */
   filename sequence65;
   /*!
    */
   filename sequence66;
   /*!
    */
   filename sequence67;
   /*!
    */
   filename sequence68;
   /*!
    */
   filename sequence69;
   /*!
    */
   filename sequence70;
   /*!
    */
   filename sequence71;
   /*!
    */
   filename sequence72;
   /*!
    */
   filename sequence73;
   /*!
    */
   filename sequence74;
   /*!
    */
   filename sequence75;
   /*!
    */
   filename sequence76;
   /*!
    */
   filename sequence77;
   /*!
    */
   filename sequence78;
   /*!
    */
   filename sequence79;
   /*!
    */
   filename sequence80;
   /*!
    */
   filename sequence81;
   /*!
    */
   filename sequence82;
   /*!
    */
   filename sequence83;
   /*!
    */
   filename sequence84;
   /*!
    */
   filename sequence85;
   /*!
    */
   filename sequence86;
   /*!
    */
   filename sequence87;
   /*!
    */
   filename sequence88;
   /*!
    */
   filename sequence89;
   /*!
    */
   filename sequence90;
   /*!
    */
   filename sequence91;
   /*!
    */
   filename sequence92;
   /*!
    */
   filename sequence93;
   /*!
    */
   filename sequence94;
   /*!
    */
   filename sequence95;
   /*!
    */
   filename sequence96;
   /*!
    */
   filename sequence97;
   /*!
    */
   filename sequence98;
   /*!
    */
   filename sequence99;
   /*!
    */
   filename sequence100;
   /*!
    */
   filename sequence101;
   /*!
    */
   filename sequence102;
   /*!
    */
   filename sequence103;
   /*!
    */
   filename sequence104;
   /*!
    */
   filename sequence105;
   /*!
    */
   filename sequence106;
   /*!
    */
   filename sequence107;
   /*!
    */
   filename sequence108;
   /*!
    */
   filename sequence109;
   /*!
    */
   filename sequence110;
   /*!
    */
   filename sequence111;
   /*!
    */
   filename sequence112;
   /*!
    */
   filename sequence113;
   /*!
    */
   filename sequence114;
   /*!
    */
   filename sequence115;
   /*!
    */
   filename sequence116;
   /*!
    */
   filename sequence117;
   /*!
    */
   filename sequence118;
   /*!
    */
   filename sequence119;
   /*!
    */
   filename sequence120;
   /*!
    */
   filename sequence121;
   /*!
    */
   filename sequence122;
   /*!
    */
   filename sequence123;
   /*!
    */
   filename sequence124;
   /*!
    */
   filename sequence125;
   /*!
    */
   filename sequence126;
   /// @}

};

class  AudioEnvironment : public SimDataBlock {
  public:
   /*!
    */
   bool useRoom;
   /*!
    */
   enumval room;
   /*!
    */
   int roomHF;
   /*!
    */
   int reflections;
   /*!
    */
   int reverb;
   /*!
    */
   float roomRolloffFactor;
   /*!
    */
   float decayTime;
   /*!
    */
   float decayHFRatio;
   /*!
    */
   float reflectionsDelay;
   /*!
    */
   float reverbDelay;
   /*!
    */
   int roomVolume;
   /*!
    */
   float effectVolume;
   /*!
    */
   float damping;
   /*!
    */
   float environmentSize;
   /*!
    */
   float environmentDiffusion;
   /*!
    */
   float airAbsorption;
   /*!
    */
   int flags;
};

class  AudioSampleEnvironment : public SimDataBlock {
  public:
   /*!
    */
   int direct;
   /*!
    */
   int directHF;
   /*!
    */
   int room;
   /*!
    */
   float obstruction;
   /*!
    */
   float obstructionLFRatio;
   /*!
    */
   float occlusion;
   /*!
    */
   float occlusionLFRatio;
   /*!
    */
   float occlusionRoomRatio;
   /*!
    */
   float roomRolloff;
   /*!
    */
   float airAbsorption;
   /*!
    */
   int outsideVolumeHF;
   /*!
    */
   int flags;
};

class  AudioDescription : public SimDataBlock {
  public:
   /*!
    */
   float volume;
   /*!
    */
   bool isLooping;
   /*!
    */
   bool isStreaming;
   /*!
    */
   bool is3D;
   /*!
    */
   float referenceDistance;
   /*!
    */
   float maxDistance;
   /*!
    */
   int coneInsideAngle;
   /*!
    */
   int coneOutsideAngle;
   /*!
    */
   float coneOutsideVolume;
   /*!
    */
   Point3F coneVector;
   /*!
    */
   float environmentLevel;
   /*!
    */
   int loopCount;
   /*!
    */
   int minLoopGap;
   /*!
    */
   int maxLoopGap;
   /*!
    */
   int type;
};

class  AudioProfile : public SimDataBlock {
  public:
   /*!
    */
   filename fileName;
   /*!
    */
   AudioDescriptionPtr description;
   /*!
    */
   AudioSampleEnvironmentPtr environment;
   /*!
    */
   bool preload;
};

class  ConsoleLogger : public SimObject {
  public:
   virtual bool attach() {}
   virtual bool detach() {}

   /*! @name Logging
   @{ */
   /*!
    */
   enumval level;
   /// @}

};

class  FileObject : public SimObject {
  public:
   virtual bool openForRead() {}
   virtual bool openForWrite() {}
   virtual bool openForAppend() {}
   virtual bool isEOF() {}
   virtual string readLine() {}
   virtual void writeLine() {}
   virtual void close() {}
};

class  CreatorTree : public GuiArrayCtrl {
  public:
   virtual int addGroup() {}
   virtual int addItem() {}
   virtual bool fileNameMatch() {}
   virtual int getSelected() {}
   virtual bool isGroup() {}
   virtual string getName() {}
   virtual string getValue() {}
   virtual void clear() {}
   virtual int getParent() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  EditManager : public GuiControl {
  public:
   virtual void setBookmark() {}
   virtual void gotoBookmark() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  EditTSCtrl : public GuiTSCtrl {
  public:
   virtual void renderSphere() {}
   virtual void renderCircle() {}
   virtual void renderTriangle() {}
   virtual void renderLine() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;

   /*! @name Mission Area
   @{ */
   /*!
    */
   bool renderMissionArea;
   /*!
    */
   ColorI missionAreaFillColor;
   /*!
    */
   ColorI missionAreaFrameColor;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   ColorI consoleFrameColor;
   /*!
    */
   ColorI consoleFillColor;
   /*!
    */
   int consoleSphereLevel;
   /*!
    */
   int consoleCircleSegments;
   /*!
    */
   int consoleLineWidth;
   /// @}

};

class  GuiTerrPreviewCtrl : public GuiControl {
  public:
   virtual void reset() {}
   virtual void setRoot() {}
   virtual string getRoot() {}
   virtual void setOrigin() {}
   virtual string getOrigin() {}
   virtual string getValue() {}
   virtual void setValue() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  MissionAreaEditor : public GuiBitmapCtrl {
  public:
   virtual void centerWorld() {}
   virtual string getArea() {}
   virtual void setArea() {}
   virtual void updateTerrain() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   filename bitmap;
   /*!
    */
   bool center;
   /*!
    */
   bool wrap;
   /// @}


   /*! @name Mirror
   @{ */
   /*!
    */
   bool enableMirroring;
   /*!
    */
   int mirrorIndex;
   /*!
    */
   ColorI mirrorLineColor;
   /*!
    */
   ColorI mirrorArrowColor;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   ColorI handleFrameColor;
   /*!
    */
   ColorI handleFillColor;
   /*!
    */
   ColorI defaultObjectColor;
   /*!
    */
   ColorI waterObjectColor;
   /*!
    */
   ColorI missionBoundsColor;
   /*!
    */
   ColorI cameraColor;
   /*!
    */
   bool squareBitmap;
   /*!
    */
   bool enableEditing;
   /*!
    */
   bool renderCamera;
   /// @}

};

class  Terraformer : public SimObject {
  public:
   virtual void setTerrainInfo() {}
   virtual void setShift() {}
   virtual int generateSeed() {}
   virtual bool saveGreyscale() {}
   virtual bool loadGreyscale() {}
   virtual bool saveHeightField() {}
   virtual bool setTerrain() {}
   virtual string getCameraPosition() {}
   virtual void setCameraPosition() {}
   virtual bool terrainData() {}
   virtual bool terrainFile() {}
   virtual bool scale() {}
   virtual bool smooth() {}
   virtual bool smoothWater() {}
   virtual bool smoothRidges() {}
   virtual bool filter() {}
   virtual bool blend() {}
   virtual bool turbulence() {}
   virtual void maskFBm() {}
   virtual bool maskHeight() {}
   virtual bool maskSlope() {}
   virtual bool maskWater() {}
   virtual bool mergeMasks() {}
   virtual bool setMaterials() {}
   virtual bool erodeHydraulic() {}
   virtual bool erodeThermal() {}
   virtual bool canyon() {}
   virtual void previewScaled() {}
   virtual void preview() {}
   virtual void clearRegister() {}
   virtual void fBm() {}
   virtual void sinus() {}
   virtual void rigidMultiFractal() {}
};

class  TerrainEditor : public EditTSCtrl {
  public:
   virtual void attachTerrain() {}
   virtual void setBrushType() {}
   virtual void setBrushSize() {}
   virtual string getBrushPos() {}
   virtual void setBrushPos() {}
   virtual void setAction() {}
   virtual string getActionName() {}
   virtual int getNumActions() {}
   virtual string getCurrentAction() {}
   virtual void resetSelWeights() {}
   virtual void undo() {}
   virtual void redo() {}
   virtual void clearSelection() {}
   virtual void processAction() {}
   virtual void buildMaterialMap() {}
   virtual int getNumTextures() {}
   virtual string getTextureName() {}
   virtual void markEmptySquares() {}
   virtual void clearModifiedFlags() {}
   virtual void mirrorTerrain() {}
   virtual void pushBaseMaterialInfo() {}
   virtual void popBaseMaterialInfo() {}
   virtual void setLoneBaseMaterial() {}
   virtual void setTerraformOverlay() {}
   virtual void setTerrainMaterials() {}
   virtual string getTerrainMaterials() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;

   /*! @name Mission Area
   @{ */
   /*!
    */
   bool renderMissionArea;
   /*!
    */
   ColorI missionAreaFillColor;
   /*!
    */
   ColorI missionAreaFrameColor;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   ColorI consoleFrameColor;
   /*!
    */
   ColorI consoleFillColor;
   /*!
    */
   int consoleSphereLevel;
   /*!
    */
   int consoleCircleSegments;
   /*!
    */
   int consoleLineWidth;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool isDirty;
   /*!
    */
   bool isMissionDirty;
   /*!
    */
   bool renderBorder;
   /*!
    */
   float borderHeight;
   /*!
    */
   ColorI borderFillColor;
   /*!
    */
   ColorI borderFrameColor;
   /*!
    */
   bool borderLineMode;
   /*!
    */
   bool selectionHidden;
   /*!
    */
   bool enableSoftBrushes;
   /*!
    */
   bool renderVertexSelection;
   /*!
    */
   bool processUsesBrush;
   /*!
    */
   float adjustHeightVal;
   /*!
    */
   float setHeightVal;
   /*!
    */
   float scaleVal;
   /*!
    */
   float smoothFactor;
   /*!
    */
   int materialGroup;
   /*!
    */
   float softSelectRadius;
   /*!
    */
   string softSelectFilter;
   /*!
    */
   string softSelectDefaultFilter;
   /*!
    */
   float adjustHeightMouseScale;
   /*!
    */
   caseString paintMaterial;
   /// @}

};

class  WorldEditor : public EditTSCtrl {
  public:
   virtual void ignoreObjClass() {}
   virtual void clearIgnoreList() {}
   virtual void undo() {}
   virtual void redo() {}
   virtual void clearSelection() {}
   virtual void selectObject() {}
   virtual void unselectObject() {}
   virtual int getSelectionSize() {}
   virtual int getSelectedObject() {}
   virtual string getSelectionCentroid() {}
   virtual void dropSelection() {}
   virtual void deleteSelection() {}
   virtual void copySelection() {}
   virtual void pasteSelection() {}
   virtual bool canPasteSelection() {}
   virtual void hideSelection() {}
   virtual void lockSelection() {}
   virtual void redirectConsole() {}
   virtual string getMode() {}
   virtual void setMode() {}
   virtual void addUndoState() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;

   /*! @name Mission Area
   @{ */
   /*!
    */
   bool renderMissionArea;
   /*!
    */
   ColorI missionAreaFillColor;
   /*!
    */
   ColorI missionAreaFrameColor;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   ColorI consoleFrameColor;
   /*!
    */
   ColorI consoleFillColor;
   /*!
    */
   int consoleSphereLevel;
   /*!
    */
   int consoleCircleSegments;
   /*!
    */
   int consoleLineWidth;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool isDirty;
   /*!
    */
   bool planarMovement;
   /*!
    */
   int undoLimit;
   /*!
    */
   enumval dropType;
   /*!
    */
   float projectDistance;
   /*!
    */
   bool boundingBoxCollision;
   /*!
    */
   bool renderPlane;
   /*!
    */
   bool renderPlaneHashes;
   /*!
    */
   ColorI gridColor;
   /*!
    */
   float planeDim;
   /*!
    */
   Point3F gridSize;
   /*!
    */
   bool renderPopupBackground;
   /*!
    */
   ColorI popupBackgroundColor;
   /*!
    */
   ColorI popupTextColor;
   /*!
    */
   ColorI objectTextColor;
   /*!
    */
   bool objectsUseBoxCenter;
   /*!
    */
   int axisGizmoMaxScreenLen;
   /*!
    */
   bool axisGizmoActive;
   /*!
    */
   float mouseMoveScale;
   /*!
    */
   float mouseRotateScale;
   /*!
    */
   float mouseScaleScale;
   /*!
    */
   float minScaleFactor;
   /*!
    */
   float maxScaleFactor;
   /*!
    */
   ColorI objSelectColor;
   /*!
    */
   ColorI objMouseOverSelectColor;
   /*!
    */
   ColorI objMouseOverColor;
   /*!
    */
   bool showMousePopupInfo;
   /*!
    */
   ColorI dragRectColor;
   /*!
    */
   bool renderObjText;
   /*!
    */
   bool renderObjHandle;
   /*!
    */
   string objTextFormat;
   /*!
    */
   ColorI faceSelectColor;
   /*!
    */
   bool renderSelectionBox;
   /*!
    */
   ColorI selectionBoxColor;
   /*!
    */
   bool selectionLocked;
   /*!
    */
   bool snapToGrid;
   /*!
    */
   bool snapRotations;
   /*!
    */
   float rotationSnap;
   /*!
    */
   bool toggleIgnoreList;
   /*!
    */
   bool renderNav;
   /*!
    */
   filename selectHandle;
   /*!
    */
   filename defaultHandle;
   /*!
    */
   filename lockedHandle;
   /// @}

};

class  NetConnection : public SimGroup {
  public:
   virtual void transmitPaths() {}
   virtual void clearPaths() {}
   virtual string getAddress() {}
   virtual void setSimulatedNetParams() {}
   virtual int getPing() {}
   virtual int getPacketLoss() {}
   virtual void checkMaxRate() {}
   virtual void connect() {}
   virtual string connectLocal() {}
   virtual int getGhostsActive() {}
};

class  GameConnection : public NetConnection {
  public:
   virtual Script onConnectRequestTimedOut() {}
   virtual Script onConnectRequestRejected() {}
   virtual Script onConnectionError() {}
   virtual Script onConnectionDropped() {}
   virtual Script onConnectionTimedOut() {}
   virtual Script onConnectionAccepted() {}
   virtual Script setLagIcon() {}
   virtual Script initialControlSet() {}
   virtual void setJoinPassword() {}
   virtual void setConnectArgs() {}
   virtual void transmitDataBlocks() {}
   virtual void activateGhosting() {}
   virtual void resetGhosting() {}
   virtual bool setControlObject() {}
   virtual int getControlObject() {}
   virtual bool isAIControlled() {}
   virtual bool play2D() {}
   virtual bool play3D() {}
   virtual bool chaseCam() {}
   virtual void setControlCameraFov() {}
   virtual float getControlCameraFov() {}
   virtual void setBlackOut() {}
   virtual void setMissionCRC() {}
   virtual void delete() {}
   virtual void startRecording() {}
   virtual void stopRecording() {}
   virtual bool playDemo() {}
   virtual bool isDemoPlaying() {}
   virtual bool isDemoRecording() {}
   virtual void transmitStaticBrickData() {}
};

class  AIConnection : public GameConnection {
  public:
   virtual void setMove() {}
   virtual float getMove() {}
   virtual void setFreeLook() {}
   virtual bool getFreeLook() {}
   virtual void setTrigger() {}
   virtual bool getTrigger() {}
   virtual string getAddress() {}
};

class  AIPlayer : public Player {
  public:
   virtual void stop() {}
   virtual void clearAim() {}
   virtual void setMoveSpeed() {}
   virtual void setMoveDestination() {}
   virtual string getMoveDestination() {}
   virtual void setAimLocation() {}
   virtual string getAimLocation() {}
   virtual void setAimObject() {}
   virtual int getAimObject() {}
   virtual void setMoveObject() {}
   virtual int getMoveObject() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  BanList : public SimObject {
  public:
   virtual void addAbsolute() {}
   virtual void add() {}
   virtual void removeBan() {}
   virtual bool isBanned() {}
   virtual void export() {}
};

class  Camera : public ShapeBase {
  public:
   virtual string getPosition() {}
   virtual void setOrbitMode() {}
   virtual void setFlyMode() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  Debris : public GameBase {
  public:
   virtual bool init() {}

   /*! @name Misc
   @{ */
   /*!
    */
   float lifetime;
   /// @}

};

class  DebugView : public GuiTextCtrl {
  public:
   virtual void addLine() {}
   virtual void clearLines() {}
   virtual void setText() {}
   virtual void clearText() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   caseString text;
   /*!
    */
   int maxLength;
};

class  GuiPlayerView : public GuiTSCtrl {
  public:
   virtual void setModel() {}
   virtual void setSeq() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   float cameraZRot;
   /*!
    */
   float forceFOV;
};

class  Item : public ShapeBase {
  public:
   virtual bool isStatic() {}
   virtual bool isRotating() {}
   virtual bool setCollisionTimeout() {}
   virtual string getLastStickyPos() {}
   virtual string getLastStickyNormal() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Item Misc
   @{ */
   /*!
    */
   bool collideable;
   /*!
    */
   bool static;
   /*!
    */
   bool rotate;
   /// @}


   /*! @name Item Properties
   @{ */
   /*!
    */
   int mat1;
   /*!
    */
   int mat2;
   /*!
    */
   int mat3;
   /*!
    */
   int mat4;
   /*!
    */
   caseString name;
   /*!
    */
   int quantity;
   /*!
    */
   int price;
   /*!
    */
   bool randomMaterials;
   /*!
    */
   bool sometimesUnifyMaterials;
   /*!
    */
   bool alwaysUnifyMaterials;
   /*!
    */
   caseString questName;
   /*!
    */
   bool canBuy;
   /*!
    */
   ColorI dyeColor;
   /// @}

};

class  MissionArea : public NetObject {
  public:
   virtual string getArea() {}
   virtual void setArea() {}

   /*! @name dimensions
   @{ */
   /*!
    */
   RectI Area;
   /*!
    */
   float flightCeiling;
   /*!
    */
   float flightCeilingRange;
   /// @}

};

class  PathCamera : public ShapeBase {
  public:
   virtual void setPosition() {}
   virtual void setTarget() {}
   virtual void setState() {}
   virtual void reset() {}
   virtual void pushBack() {}
   virtual void pushFront() {}
   virtual void popFront() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

};

class  PhysicalZone : public SceneObject {
  public:
   virtual void activate() {}
   virtual void deactivate() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   float velocityMod;
   /*!
    */
   float gravityMod;
   /*!
    */
   Point3F appliedForce;
   /*!
    */
   TriggerPolyhedron polyhedron;
   /// @}

};

class  TriggerData : public GameBaseData {
  public:
   virtual void onEnterTrigger() {}
   virtual void onLeaveTrigger() {}
   virtual void onTickTrigger() {}
   /*!
    */
   caseString category;
   /*!
    */
   string className;
   /*!
    */
   int tickPeriodMS;
};

class  Trigger : public GameBase {
  public:
   virtual int getNumObjects() {}
   virtual int getObject() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   TriggerPolyhedron polyhedron;
};

class  GuiClockHud : public GuiControl {
  public:
   virtual void setTime() {}
   virtual float getTime() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool showFill;
   /*!
    */
   bool showFrame;
   /*!
    */
   ColorF fillColor;
   /*!
    */
   ColorF frameColor;
   /*!
    */
   ColorF textColor;
   /// @}

};

class  fxDTSBrick : public SceneObject {
  public:
   virtual int getAngleID() {}
   virtual int getColorID() {}
   virtual int getPrintID() {}
   virtual bool isPearl() {}
   virtual bool isChrome() {}
   virtual bool isBasePlate() {}
   virtual bool isPlanted() {}
   virtual bool isDead() {}
   virtual void setColor() {}
   virtual void setChrome() {}
   virtual void setPearl() {}
   virtual void setPrint() {}
   virtual int plant() {}
   virtual bool hasPathToGround() {}
   virtual int getDataBlock() {}
   virtual void dumpUpList() {}
   virtual void dumpDownList() {}
   virtual bool isExposed() {}
   virtual void killBrick() {}
   virtual void disableCollision() {}
   virtual void enableCollision() {}
   virtual void disableRendering() {}
   virtual void enableRendering() {}
   virtual void disableRayCasting() {}
   virtual void enableRayCasting() {}
   virtual int getExposedAreaTop() {}
   virtual int getExposedAreaBottom() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name fxDTSBrick Stuff
   @{ */
   /*!
    */
   GameBaseDataPtr dataBlock;
   /*!
    */
   int angleID;
   /*!
    */
   int printID0;
   /*!
    */
   int printID1;
   /*!
    */
   int printID2;
   /*!
    */
   int printID3;
   /*!
    */
   int printID4;
   /*!
    */
   int printID5;
   /*!
    */
   int sizeX;
   /*!
    */
   int sizeY;
   /*!
    */
   int sizeZ;
   /*!
    */
   int colorID;
   /*!
    */
   bool isPearl;
   /*!
    */
   bool isChrome;
   /*!
    */
   bool isBasePlate;
   /*!
    */
   bool isPlanted;
   /// @}

};

class  fxLight : public GameBase {
  public:
   virtual void setEnable() {}
   virtual void reset() {}
   virtual void attachToObject() {}
   virtual void detachFromObject() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   bool Enable;
   /*!
    */
   float IconSize;
};

class  fxSunLight : public SceneObject {
  public:
   virtual void setEnable() {}
   virtual void setFlareBitmaps() {}
   virtual void setSunAzimuth() {}
   virtual void setSunElevation() {}
   virtual void setFlareTP() {}
   virtual void setFlareColour() {}
   virtual void setFlareBrightness() {}
   virtual void setFlareSize() {}
   virtual void setFadeTime() {}
   virtual void setBlendMode() {}
   virtual void setUseColour() {}
   virtual void setUseBrightness() {}
   virtual void setUseRotation() {}
   virtual void setUseSize() {}
   virtual void setUseAzimuth() {}
   virtual void setUseElevation() {}
   virtual void setLerpColour() {}
   virtual void setLerpBrightness() {}
   virtual void setLerpRotation() {}
   virtual void setLerpSize() {}
   virtual void setLerpAzimuth() {}
   virtual void setLerpElevation() {}
   virtual void setLinkFlareSize() {}
   virtual void setSingleColourKeys() {}
   virtual void setMinColour() {}
   virtual void setMaxColour() {}
   virtual void setMinBrightness() {}
   virtual void setMaxBrightness() {}
   virtual void setMinRotation() {}
   virtual void setMaxRotation() {}
   virtual void setMinSize() {}
   virtual void setMaxSize() {}
   virtual void setMinAzimuth() {}
   virtual void setMaxAzimuth() {}
   virtual void setMinElevation() {}
   virtual void setMaxElevation() {}
   virtual void setRedKeys() {}
   virtual void setGreenKeys() {}
   virtual void setBlueKeys() {}
   virtual void setBrightnessKeys() {}
   virtual void setRotationKeys() {}
   virtual void setSizeKeys() {}
   virtual void setAzimuthKeys() {}
   virtual void setElevationKeys() {}
   virtual void setColourTime() {}
   virtual void setBrightnessTime() {}
   virtual void setRotationTime() {}
   virtual void setSizeTime() {}
   virtual void setAzimuthTime() {}
   virtual void setElevationTime() {}
   virtual void reset() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Debugging
   @{ */
   /*!
    */
   bool Enable;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename LocalFlareBitmap;
   /*!
    */
   filename RemoteFlareBitmap;
   /// @}


   /*! @name Sun Orbit
   @{ */
   /*!
    */
   float SunAzimuth;
   /*!
    */
   float SunElevation;
   /*!
    */
   bool LockToRealSun;
   /// @}


   /*! @name Lens Flare
   @{ */
   /*!
    */
   bool FlareTP;
   /*!
    */
   ColorF Colour;
   /*!
    */
   float Brightness;
   /*!
    */
   float FlareSize;
   /*!
    */
   float FadeTime;
   /*!
    */
   int BlendMode;
   /// @}


   /*! @name Animation Options
   @{ */
   /*!
    */
   bool AnimColour;
   /*!
    */
   bool AnimBrightness;
   /*!
    */
   bool AnimRotation;
   /*!
    */
   bool AnimSize;
   /*!
    */
   bool AnimAzimuth;
   /*!
    */
   bool AnimElevation;
   /*!
    */
   bool LerpColour;
   /*!
    */
   bool LerpBrightness;
   /*!
    */
   bool LerpRotation;
   /*!
    */
   bool LerpSize;
   /*!
    */
   bool LerpAzimuth;
   /*!
    */
   bool LerpElevation;
   /*!
    */
   bool LinkFlareSize;
   /*!
    */
   bool SingleColourKeys;
   /// @}


   /*! @name Animation Extents
   @{ */
   /*!
    */
   ColorF MinColour;
   /*!
    */
   ColorF MaxColour;
   /*!
    */
   float MinBrightness;
   /*!
    */
   float MaxBrightness;
   /*!
    */
   float MinRotation;
   /*!
    */
   float MaxRotation;
   /*!
    */
   float minSize;
   /*!
    */
   float MaxSize;
   /*!
    */
   float MinAzimuth;
   /*!
    */
   float MaxAzimuth;
   /*!
    */
   float MinElevation;
   /*!
    */
   float MaxElevation;
   /// @}


   /*! @name Animation Keys
   @{ */
   /*!
    */
   string RedKeys;
   /*!
    */
   string GreenKeys;
   /*!
    */
   string BlueKeys;
   /*!
    */
   string BrightnessKeys;
   /*!
    */
   string RotationKeys;
   /*!
    */
   string SizeKeys;
   /*!
    */
   string AzimuthKeys;
   /*!
    */
   string ElevationKeys;
   /// @}


   /*! @name Animation Times
   @{ */
   /*!
    */
   float ColourTime;
   /*!
    */
   float BrightnessTime;
   /*!
    */
   float RotationTime;
   /*!
    */
   float SizeTime;
   /*!
    */
   float AzimuthTime;
   /*!
    */
   float ElevationTime;
   /// @}

};

class  Lightning : public GameBase {
  public:
   virtual void warningFlashes() {}
   virtual void strikeRandomPoint() {}
   virtual void strikeObject() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Strikes
   @{ */
   /*!
    */
   int strikesPerMinute;
   /*!
    */
   float strikeWidth;
   /*!
    */
   float strikeRadius;
   /// @}


   /*! @name colors
   @{ */
   /*!
    */
   ColorF color;
   /*!
    */
   ColorF fadeColor;
   /// @}


   /*! @name Bolts
   @{ */
   /*!
    */
   float chanceToHitTarget;
   /*!
    */
   float boltStartRadius;
   /*!
    */
   bool useFog;
   /// @}

};

class  Precipitation : public GameBase {
  public:
   virtual void setPercentange() {}
   virtual void modifyStorm() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}


   /*! @name Movement
   @{ */
   /*!
    */
   float minSpeed;
   /*!
    */
   float maxSpeed;
   /*!
    */
   float minMass;
   /*!
    */
   float maxMass;
   /// @}


   /*! @name turbulence
   @{ */
   /*!
    */
   float maxTurbulence;
   /*!
    */
   float turbulenceSpeed;
   /*!
    */
   bool rotateWithCamVel;
   /*!
    */
   bool useTurbulence;
   /// @}

   /*!
    */
   int numDrops;
   /*!
    */
   float boxWidth;
   /*!
    */
   float boxHeight;
   /*!
    */
   bool doCollision;
};

class  HTTPObject : public TCPObject {
  public:
   virtual void get() {}
   virtual void post() {}
};

class  SimpleNetObject : public NetObject {
  public:
   virtual void setMessage() {}
};

class  FlyingVehicle : public Vehicle {
  public:
   virtual void useCreateHeight() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   bool disableMove;
};

class  WheeledVehicle : public Vehicle {
  public:
   virtual bool setWheelSteering() {}
   virtual bool setWheelPowered() {}
   virtual bool setWheelTire() {}
   virtual bool setWheelSpring() {}
   virtual int getWheelCount() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   bool disableMove;
};

class  GuiBitmapButtonCtrl : public GuiButtonCtrl {
  public:
   virtual void setBitmap() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString text;
   /*!
    */
   int groupNum;
   /*!
    */
   enumval buttonType;
   /// @}

   /*!
    */
   filename bitmap;
};

class  DbgFileView : public GuiArrayCtrl {
  public:
   virtual void setCurrentLine() {}
   virtual string getCurrentLine() {}
   virtual bool open() {}
   virtual void clearBreakPositions() {}
   virtual void setBreakPosition() {}
   virtual void setBreak() {}
   virtual void removeBreak() {}
   virtual bool findString() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

};

class  GuiFilterCtrl : public GuiControl {
  public:
   virtual string getValue() {}
   virtual void setValue() {}
   virtual void identity() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   int controlPoints;
   /*!
    */
   floatList filter;
};

class  GuiFrameSetCtrl : public GuiControl {
  public:
   virtual void frameBorder() {}
   virtual void frameMovable() {}
   virtual void frameMinExtent() {}
   virtual void addColumn() {}
   virtual void addRow() {}
   virtual void removeColumn() {}
   virtual void removeRow() {}
   virtual int getColumnCount() {}
   virtual int getRowCount() {}
   virtual int getColumnOffset() {}
   virtual int getRowOffset() {}
   virtual void setColumnOffset() {}
   virtual void setRowOffset() {}

   /*! @name Parent
   @{ */
   /*!
    */
   GuiProfile profile;
   /*!
    */
   enumval horizSizing;
   /*!
    */
   enumval vertSizing;
   /*!
    */
   Point2I position;
   /*!
    */
   Point2I extent;
   /*!
    */
   Point2I minExtent;
   /*!
    */
   bool visible;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated modal;
   /*!
   @deprecated This member is deprecated, which means that its value is always undefined.
    */
   deprecated setFirstResponder;
   /*!
    */
   string variable;
   /*!
    */
   string command;
   /*!
    */
   string altCommand;
   /*!
    */
   string accelerator;
   /// @}

   /*!
    */
   intList columns;
   /*!
    */
   intList rows;
   /*!
    */
   int borderWidth;
   /*!
    */
   ColorI borderColor;
   /*!
    */
   enumval borderEnable;
   /*!
    */
   enumval borderMovable;
   /*!
    */
   bool autoBalance;
   /*!
    */
   int fudgeFactor;
};

class  MessageVector : public SimObject {
  public:
   virtual void clear() {}
   virtual void pushBackLine() {}
   virtual bool popBackLine() {}
   virtual void pushFrontLine() {}
   virtual bool popFrontLine() {}
   virtual bool insertLine() {}
   virtual bool deleteLine() {}
   virtual void dump() {}
   virtual int getNumLines() {}
   virtual string getLineTextByTag() {}
   virtual int getLineIndexByTag() {}
   virtual string getLineText() {}
   virtual int getLineTag() {}
};

class  InteriorInstance : public SceneObject {
  public:
   virtual void setAlarmMode() {}
   virtual void activateLight() {}
   virtual void deactivateLight() {}
   virtual void echoTriggerableLights() {}
   virtual void magicButton() {}
   virtual void setSkinBase() {}
   virtual int getNumDetailLevels() {}
   virtual void setDetailLevel() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename interiorFile;
   /// @}


   /*! @name Audio
   @{ */
   /*!
    */
   AudioProfilePtr AudioProfile;
   /*!
    */
   AudioEnvironmentPtr AudioEnvironment;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   bool showTerrainInside;
   /*!
    */
   bool noRelight;
   /// @}

};

class  PathedInterior : public GameBase {
  public:
   virtual void setPathPosition() {}
   virtual void setTargetPosition() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   caseString nameTag;
   /*!
    */
   GameBaseDataPtr dataBlock;
   /// @}

   /*!
    */
   string interiorResource;
   /*!
    */
   int interiorIndex;
   /*!
    */
   MatrixPosition basePosition;
   /*!
    */
   MatrixRotation baseRotation;
   /*!
    */
   Point3F baseScale;
};

class  ActionMap : public SimObject {
  public:
   virtual Script blockBind() {}
   virtual Script copyBind() {}
   virtual void bind() {}
   virtual void bindCmd() {}
   virtual void unbind() {}
   virtual void save() {}
   virtual void push() {}
   virtual void pop() {}
   virtual string getBinding() {}
   virtual string getCommand() {}
   virtual bool isInverted() {}
   virtual float getScale() {}
   virtual string getDeadZone() {}
};

class  Path : public SimGroup {
  public:
   virtual int getPathId() {}
   /*!
    */
   bool isLooping;
};

class  Sky : public SceneObject {
  public:
   virtual void stormClouds() {}
   virtual void stormFog() {}
   virtual void realFog() {}
   virtual string getWindVelocity() {}
   virtual void setWindVelocity() {}
   virtual void stormCloudsShow() {}
   virtual void stormFogShow() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename materialList;
   /// @}


   /*! @name Clouds
   @{ */
   /*!
    */
   string cloudText;
   /*!
    */
   float cloudHeightPer;
   /*!
    */
   float cloudSpeed1;
   /*!
    */
   float cloudSpeed2;
   /*!
    */
   float cloudSpeed3;
   /// @}


   /*! @name Visibility
   @{ */
   /*!
    */
   float visibleDistance;
   /// @}


   /*! @name Fog
   @{ */
   /*!
    */
   float fogDistance;
   /*!
    */
   ColorF fogColor;
   /*!
    */
   bool fogStorm1;
   /*!
    */
   bool fogStorm2;
   /*!
    */
   bool fogStorm3;
   /*!
    */
   Point3F fogVolume1;
   /*!
    */
   Point3F fogVolume2;
   /*!
    */
   Point3F fogVolume3;
   /*!
    */
   ColorF fogVolumeColor1;
   /*!
    */
   ColorF fogVolumeColor2;
   /*!
    */
   ColorF fogVolumeColor3;
   /// @}


   /*! @name Wind
   @{ */
   /*!
    */
   Point3F windVelocity;
   /*!
    */
   bool windEffectPrecipitation;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   ColorF SkySolidColor;
   /*!
    */
   bool useSkyTextures;
   /*!
    */
   bool renderBottomTexture;
   /*!
    */
   bool noRenderBans;
   /*!
    */
   bool useDayNightCycle;
   /*!
    */
   int timeScale;
   /// @}

};

class  TerrainBlock : public SceneObject {
  public:
   virtual bool save() {}
   virtual void setTextureScript() {}
   virtual void setHeightfieldScript() {}
   virtual string getTextureScript() {}
   virtual string getHeightfieldScript() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename detailTexture;
   /*!
    */
   filename terrainFile;
   /*!
    */
   filename bumpTexture;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   int squareSize;
   /*!
    */
   intList emptySquares;
   /*!
    */
   float bumpScale;
   /*!
    */
   float bumpOffset;
   /*!
    */
   int zeroBumpScale;
   /// @}

};

class  WaterBlock : public SceneObject {
  public:
   virtual void toggleWireFrame() {}

   /*! @name Transform
   @{ */
   /*!
    */
   MatrixPosition position;
   /*!
    */
   MatrixRotation rotation;
   /*!
    */
   Point3F scale;
   /// @}


   /*! @name Debugging
   @{ */
   /*!
    */
   bool UseDepthMask;
   /// @}


   /*! @name Media
   @{ */
   /*!
    */
   filename surfaceTexture;
   /*!
    */
   filename ShoreTexture;
   /*!
    */
   filename envMapOverTexture;
   /*!
    */
   filename envMapUnderTexture;
   /*!
    */
   filename submergeTexture;
   /*!
    */
   filename specularMaskTex;
   /// @}


   /*! @name Fluid
   @{ */
   /*!
    */
   enumval liquidType;
   /*!
    */
   float density;
   /*!
    */
   float viscosity;
   /// @}


   /*! @name Surface
   @{ */
   /*!
    */
   float waveMagnitude;
   /*!
    */
   float surfaceOpacity;
   /*!
    */
   float envMapIntensity;
   /*!
    */
   float TessSurface;
   /*!
    */
   float TessShore;
   /*!
    */
   float SurfaceParallax;
   /// @}


   /*! @name Movement
   @{ */
   /*!
    */
   float FlowAngle;
   /*!
    */
   float FlowRate;
   /*!
    */
   float DistortGridScale;
   /*!
    */
   float DistortMag;
   /*!
    */
   float DistortTime;
   /// @}


   /*! @name Depth Fx
   @{ */
   /*!
    */
   float ShoreDepth;
   /*!
    */
   float DepthGradient;
   /*!
    */
   float MinAlpha;
   /*!
    */
   float MaxAlpha;
   /// @}


   /*! @name Misc
   @{ */
   /*!
    */
   AudioEnvironmentPtr AudioEnvironment;
   /*!
    */
   bool removeWetEdges;
   /*!
    */
   ColorF specularColor;
   /*!
    */
   float specularPower;
   /// @}

};


```
