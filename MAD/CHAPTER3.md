**3 User Interface**

**3.1 Android Graphics Interface**

=> Definition: Android graphical interfaces are usually implemented as XML files, although they could also be dynamically created from Java code.

=> Core concept: An Android UI is conceptually similar to a common HTML web page.

=> In a manner similar to a web page interaction, when the Android user touches the screen, the controller interprets the input and determines what specific portion of the screen and gestures were involved.

=> Based on this information, it tells the model about the interaction in such a way that the appropriate callback listener or lifecycle state could be called into action.

=> Unlike a Web application which refreshes its pages after explicit requests from the user, an asynchronous Android background service could quietly notify the controller about some change of state, such as reaching a given coordinate on a map.

=> This process can in turn trigger a change of the view's state entirely without user intervention.

**3.2 Layouts in Android**

=> Definition: Layouts are invisible structured containers used for holding other Views and nested layouts.

=> A typical layout defines the visual structure for an android user interface and can be created either at run time using View or ViewGroup objects, or declared using a simple XML file like main_layout.xml located in the res/layout folder.

=> A layout may contain any type of widgets such as buttons, labels, textboxes, and so on.

=> Once your layout has been created, you can securely load the layout resource from your application code within your Activity.onCreate() callback implementation.

**Android Layout types**

=> There are a number of Layouts provided by Android which you will use in almost all Android applications to provide different views, looks, and feels.

Types

1. Linear Layout: A view group that aligns all children in a single direction, either vertically or horizontally.
2. Relative Layout: A view group that displays child views in relative positions.
3. Table Layout: A view that groups views into specific rows and columns.
4. Absolute Layout: A layout that enables you to specify the exact location of its children.
5. Frame Layout: A placeholder on the screen that you can use to display a single view.
6. List View: A view group that accurately displays a list of scrollable items.
7. Grid View: A view group that displays items in a two-dimensional, scrollable grid.

**3.3 Android User Interface**

=> Core concept: Android is a widely used OS made for smart phones and tablets, functioning as an open-source project led by Google and released under the Apache License.

=> Android has a very large community that actively extends its features and creates apps that cover almost all aspects.

=> All android applications, known as apps, are securely built on the Android UI framework.

=> The app interface is the very first thing a user sees and interacts with.

=> From the user perspective, this framework keeps the overall experience highly consistent for every app installed on our smartphones or tablets.

=> From the developer perspective, this framework provides essential basic blocks that can be used to build complex and consistent user interfaces or APIs.

Types of areas in the Android UI interface

1. Home screen: The landing area when we power our phone on, which is highly customizable and themed using widgets.
2. All apps: The interface where the actively installed apps are displayed.
3. Recent screen: The screen that displays the list of last used apps.

=> Since its birth, Android has drastically changed a lot in terms of its core features and interfaces.

=> At the beginning, apps in Android did not have a consistent interface or well-defined rules, causing every app to have a different approach, navigation structure, and button position which led to user confusion.

**3.3.1 Editable Text View**

=> The EditText editable text field automatically places the cursor in the text field and quickly displays the on-screen keyboard.

=> You will change attributes of the text entry field so that the keyboard smartly suggests spelling corrections while you type, and automatically starts each new sentence with capital letters.

=> Example: android:inputType="textCapSentences" safely sets the keyboard to capital letters at the beginning of sentences.

=> Example: android:inputType="textAutoCorrect" configures the keyboard to automatically show spelling corrections as you enter characters.

=> Example: android:inputType="textMultiLine" correctly enables the Return key on the keyboard to end lines and create new blank lines without closing the keyboard.

=> Example: android:inputType="textPassword" strictly sets the characters the user enters into dots to conceal the entered password.

**3.3.2 Radio and Toggle Buttons**

=> Definition: Radio buttons are input controls that are highly useful for selecting only one option from a set of options.

=> You should use radio buttons if you actively want the user to see all available options side-by-side.

=> A basic Button is often utilized to perform some sort of action, such as submitting a form or confirming a selection, and can cleanly contain a text or image label.

=> A CheckBox is a simple button with two states, checked or unchecked, often used to turn a feature on or off or to pick multiple items from a list.

=> A ToggleButton is functionally similar to a CheckBox, but you use it to visually show the state, functioning exactly like a power on/off button.

=> A RadioButton efficiently provides the selection of a single item.

=> Grouping RadioButton controls together in a dedicated container called a RadioGroup actively enables the developer to strictly enforce that only one RadioButton is selected at a time.

**3.3.3 Creating Radio Button**

=> To create each radio button option, you must securely create a RadioButton in your layout.

=> Because radio buttons are mutually exclusive, you must safely group them together inside a RadioGroup container.

=> By cleanly grouping them together, the system successfully ensures that only one radio button can be selected at a time.

**3.3.4 Spinners**

=> Definition: Spinners dynamically provide a quick way to select one value from a set of options.

=> You can create a spinner like any view and specifically utilize the android:entries attribute to cleanly specify the set of options.

=> Developers can accurately specify the string array of options inside an XML file stored in res/values/planets_array.xml.

**3.4 Event Handling**

=> Core concept: Input Events are utilized to precisely capture events, such as button clicks and edittext touches, from the View objects defined in the user interface when the user interacts with them.

=> To securely handle input events in android, the active views must have an event listener in place.

=> The primary View class, from which all UI components are deeply derived, contains a wide range of event listener interfaces where each contains an abstract declaration for a callback method.

=> To respond to an event of a particular type, the view must actively register an appropriate event listener and implement the corresponding callback method.

=> Example: If a button is to correctly respond to a click event, it must register the View.onClickListener event listener and securely implement the corresponding onClick() callback method.

=> In an active application, when a button click event is detected, the Android framework will automatically call the onClick() method of that particular view.

=> Generally, to handle input events we rely on Event Listeners and Event Handling in android applications to listen for user interactions and to safely extend a View class to build a custom component.

**Android Event Listeners**

=> Definition: An Android Event Listener is a defined interface in the View class that contains a single call-back method.

=> These methods will be instantly called by the Android framework when the specific View which is registered with the listener is triggered by user interaction within the UI.

=> There are many more specific event listeners natively available as a part of the View class to use in our android applications.

**3.5 Android Toolbox of Standard View**

=> Android securely supplies a toolbox of standard Views to effectively help you create simple interfaces.

=> By cleanly using these controls, and modifying or extending them as necessary, you can smartly simplify your development and provide structural consistency between applications.

Types of standard toolbox controls

1. TextView: A standard read-only text label that natively supports multiline display, string formatting, and automatic word wrapping.
2. EditText: An editable text entry box that comfortably accepts multiline entry and word wrapping.
3. ListView: A View Group that logically creates and manages a group of Views used to display the items in a list, often displaying the string value of an array of objects.
4. Spinner: A composite control displaying a TextView and an associated ListView that seamlessly lets you select an item from a list to display in the textbox.
5. Button: A standard interactive push-button.
6. CheckBox: A strictly two-state button represented securely with a checked or unchecked box.
7. RadioButton: Two-state grouped buttons that present the user with multiple binary options of which absolutely only one can be selected at a time.

**3.6 Menus in Android**

=> Core concept: Menus seamlessly offer a way to expose application functions without sacrificing valuable screen space.

=> Each activity can accurately specify its own activity menu that is instantly displayed when the device's menu button is pressed.

=> Android also seamlessly supports context menus that can be explicitly assigned to any View within an Activity.

=> A View's context menu is instantly triggered when a user holds the middle D-pad button, depresses the trackball, or longpresses the touch screen for around 3 seconds when the View has focus.

=> Activity and context menus robustly support submenus, checkboxes, radio buttons, shortcut keys, and icons.

=> To drastically improve the usability of application menus, Android intelligently features a three-stage menu system optimized precisely for small screens.

Types of Menu System Stages

1. The Icon Menu: This compact menu instantly appears along the bottom of the screen when the Menu button is pressed, displaying the icons and text for up to six Menu Items. This menu does not display checkboxes, radio buttons, or shortcut keys.
2. The Expanded Menu: Triggered strictly when a user selects the More Menu Item from the icon menu. It actively displays a scrollable list of only the Menu Items that weren't visible in the icon menu, showing full text, shortcut keys, and checkboxes/radio buttons as appropriate.
3. Submenus: The traditional expanding hierarchical tree can be incredibly awkward to navigate on mobile devices, so Android displays each submenu clearly in a floating window Dialog box.

**3.7 Android Layout Classes**

=> Definition: Layout Managers, more generally called layouts, are vital extensions of the ViewGroup class specifically designed to control the exact position of child controls on a screen.

=> Layouts can be safely nested together, comfortably letting you create arbitrarily complex interfaces using a smart combination of Layout Managers.

=> The standard Android SDK securely includes some simple layouts to logically help you construct your UI, leaving it up to you to carefully select the right combination to make your interface easy to understand.

Types of Layout Classes

1. FrameLayout: The simplest of the Layout Managers, which simply pins each child view securely to the top left corner.
2. LinearLayout: Adds each child View logically in a straight line, either entirely vertically or horizontally. It also cleverly allows you to specify a weight for each child that controls the relative size of each within the available space.
3. RelativeLayout: Using this layout, you can freely define the exact positions of each of the child Views strictly relative to each other and the active screen boundaries.
4. TableLayout: Lets you logically lay out Views securely using a grid of rows and columns, which can dynamically span multiple rows and columns.
5. AbsoluteLayout: In this layout, each child View's exact position is strictly defined in absolute coordinates.

=> Limitation: Defining a layout in absolute terms using AbsoluteLayout explicitly means that your layout absolutely cannot dynamically adjust to different screen resolutions and orientations.

**Working with Layouts**

=> Much as web designers dynamically use HTML, user interface designers can securely use XML to clearly define Android application screen elements and layouts.

=> A layout XML resource fundamentally is where many different resources neatly come together to efficiently form the core definition of an Android application screen.

=> Layout resource files are cleanly included in the /res/layout/ directory and are actively compiled into the application package strictly at build time.

=> Standard Layout files might deeply include many interface controls and thoroughly define the layout for an entire screen or precisely describe controls used in other layouts.
