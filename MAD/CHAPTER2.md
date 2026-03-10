**2 Activities and Fragments**

**2.1 Activity Lifecycle**

=> Definition: An application comprises one or more activities, and the user's experience of an activity is governed by a set of states known as the lifecycle.

=> The lifecycle efficiently manages system resources and user progress, preventing the app from crashing during interruptions like phone calls or screen rotations between landscape and portrait orientations.

=> To securely navigate transitions between stages of the activity lifecycle, the Activity class provides a core set of six distinct callbacks.

Processes with sequential order

1. onCreate(): This callback must be implemented and fires when the system first creates your activity to initialize essential components, such as creating views and binding data.
2. onStart(): As onCreate() exits, the activity enters the Started state, becomes visible to the user, and makes final preparations for coming to the foreground to become interactive.
3. onResume(): The system invokes this callback just before the activity starts interacting with the user, placing the activity at the top of the activity stack to capture all user input.
4. onPause(): This occurs when the activity loses focus and enters a Paused state, meaning it is partially visible but the user is actively leaving the activity.
5. onStop(): The system calls this when the activity is no longer visible to the user because it is being destroyed, a new activity is starting, or an existing one is resuming.
6. onDestroy(): This is the final callback an activity receives before it is destroyed, implemented to ensure that all of an activity's resources are completely released.

=> Important explanation point: Inside the onCreate() method, developers must strictly call setContentView() to define the layout for the activity's user interface.

=> Important explanation point: An activity in the Paused state may dynamically continue to update the UI if the user expects it to, such as a media player playing or a navigation map updating.

=> Important explanation point: Developers should never use the onPause() callback to save application or user data, make network calls, or execute database transactions.

=> Depending on what happens after the activity enters the Paused state, the subsequent callback is either onStop() or onResume().

=> The callback following onStop() is either onRestart() if the activity is coming back to interact with the user, or onDestroy() if the activity is completely terminating.

**2.2 Fragments in Android**

=> Core concept: The Fragment class in Android is utilized to build dynamic User Interfaces and should be strictly used within an Activity.

=> A fragment functionally represents a behavior or a distinct portion of the user interface within a FragmentActivity.

=> A fragment acts as a modular section of an activity, which possesses its own lifecycle, receives its own input events, and can be added or removed while the activity is running.

=> A fragment must always be securely hosted in an activity, and its lifecycle is directly affected by the host activity's lifecycle.

=> Important explanation point: When the host activity is paused or destroyed, all active fragments contained within it are simultaneously paused or destroyed.

=> While an activity is actively running in the resumed state, developers can manipulate each fragment independently, such as adding or removing them.

=> The back stack safely allows the user to reverse a fragment transaction and navigate backwards by simply pressing the Back button.

=> You can natively insert a fragment into your activity layout by declaring it as a <fragment> element in the layout file, or programmatically by adding it to an existing ViewGroup from your application code.

**2.2.1 Importance of Fragments**

Advantages

1. Reusing View and Logic Components: Fragments effectively enable the re-use of parts of the screen, including views and event logic, across many disparate activities.
2. Tablet Support: Fragments logically enable device-specific activities to reuse shared elements, allowing a tablet version to have a substantially different layout from the phone version.
3. Screen Orientation: Fragments actively enable applications to provide substantially different layouts for portrait and landscape versions while cleanly reusing shared elements.

**2.2.2 Purpose of Fragments**

=> Definition: The main purpose of a Fragment is to reliably support a more dynamic UI on varying screen sizes like tablets and smartphones, making the reuse of UI components significantly easier.

=> To logically create a Fragment, developers have to subclass the Fragment class and heavily provide a public no-argument constructor to reinstantiate the Fragment class when a state restore is needed.

=> A Fragment can transparently exist without its own UI, acting as an invisible worker for the parent Activity.

**2.2.3 Communication between Fragments and Activity**

Steps

1. Execute the Fragment.getActivity() method to successfully return the FragmentActivity object to which the Fragment belongs.
2. Use the FragmentActivity.getSupportFragmentManager() method to natively return an android.support.v4.app.FragmentManager instance.
3. Execute the FragmentManager.findFragmentById() method to securely retrieve the desired Fragment object with the specified ID.
4. Call the Fragment.getView().findViewById() method to accurately get the view controls housed inside that specific Fragment.
5. Safely change the view control's property and programmatically add an event listener as needed.

**2.3 Life Cycle of Fragment**

=> Definition: An Android Fragment is defined as a part of an activity and is often referred to as a sub-activity.

=> There can be multiple fragments active inside one activity, allowing fragments to smartly represent multiple screens within a single Activity container.

=> The Android fragment lifecycle is deeply affected by the activity lifecycle because fragments are tightly embedded inside the host activity.

Processes with sequential order

1. onAttach(Activity): This method is called exactly once when the fragment is securely attached to the activity.
2. onCreate(Bundle): This method is explicitly used to initialize the fragment.
3. onCreateView(LayoutInflater, ViewGroup, Bundle): This dynamically creates and returns the specific view hierarchy for the fragment.
4. onActivityCreated(Bundle): This is invoked immediately after the completion of the host activity's onCreate() method.
5. onViewStateRestored(Bundle): This provides essential information to the fragment that all the saved states of the fragment view hierarchy have been perfectly restored.
6. onStart(): This smoothly transitions the fragment to be visible to the user.
7. onResume(): This natively makes the fragment interactive to user input.
8. onPause(): This is called precisely when the fragment is no longer interactive.
9. onStop(): This is safely called when the fragment is no longer visible.
10. onDestroyView(): This allows the fragment to efficiently clean up resources associated with its view.
11. onDestroy(): This allows the fragment to do the final clean up of its fragment state.
12. onDetach(): This is called immediately prior to the fragment no longer being securely associated with its host activity.

**2.4 Replacing Fragment**

=> The standard procedure to replace a fragment is remarkably similar to adding one, but it strictly requires utilizing the replace() method instead of the add() method.

=> When fragment transactions like replacing or removing are performed, it is highly appropriate to allow the user to navigate backward and seamlessly "undo" the change.

=> To safely allow the user to navigate backward through fragment transactions, you must explicitly call addToBackStack() before committing the FragmentTransaction.

=> Important explanation point: When you dynamically remove or replace a fragment and thoughtfully add the transaction to the back stack, the removed fragment is merely stopped rather than completely destroyed.

=> If the transaction is intelligently added to the back stack, navigating back will successfully restore and restart the fragment.

=> If you explicitly do not add the transaction to the back stack, the fragment is permanently destroyed when it is removed or replaced.

=> The addToBackStack() method cleanly accepts an optional string parameter that carefully specifies a unique name for the transaction, used primarily for advanced FragmentManager operations.

**2.5 Intent**

=> Definition: An Intent is a specialized messaging object utilized to request an action from another app component, such as activities, services, broadcast receivers, and content providers.

=> Intent application components securely allow an Android application to connect with completely other Android applications.

=> Intents act as highly asynchronous messages which seamlessly allow application components to request targeted functionality from other Android components.

=> An intent can reliably contain extensive data packaged via a Bundle, which can then be read and used by the receiving component.

=> In Android architecture, the active reuse of other application components is a highly important concept known as a task.

=> A task allows your application to successfully trigger another component in the Android system, even if that specific component is not part of your application, and safely return the generated data back to your application.

Types

1. Starting an activity: By passing an Intent object to the startActivity() method, developers can cleanly perform required actions using a new or existing Activity.
2. Starting a service: By passing an Intent object to the startService() method, developers can effortlessly send required instructions to an active or new Service.
3. Delivering a broadcast: By passing an Intent object to the sendBroadcast() method, developers cleanly deliver a specific message to other active app broadcast receivers.

**2.6 Intent to Start Another Activity**

=> Core concept: An Intent acts as an object that fundamentally provides a runtime binding between completely separate components, most commonly between two different activities.

=> The Intent programmatically represents an application's strict intent to actively perform a task, with one of the most common tasks being the initiation of another activity.

=> The constructor of the Intent object requires exactly two parameters: a Context and a Class.

=> The Context parameter is intentionally used first because the Activity class is inherently a subclass of the Context package.

=> The Class parameter specifically identifies the exact app component to which the Android system must efficiently deliver the Intent.

=> The putExtra() method logically adds values to the intent in the format of key-value pairs, which are widely known as extras.

=> It is strongly considered good practice to meticulously define keys for intent extras by using your app's package name as a prefix, ensuring that the keys logically remain unique during cross-app interactions.

=> The startActivity() method safely starts an operational instance of the target activity strictly specified by the fully configured Intent.

**2.7 Implicit and Explicit Intent**

Types

1. Implicit Intent: This cleverly does not name a specific component but instead firmly declares a general action to perform. The background system dynamically searches for an appropriate component, and if multiple components are compatible, it displays a dialog so the user can accurately pick which app to use.
2. Explicit Intent: This forcefully specifies the targeted component by explicitly defining the fully-qualified class name, acting as the most common method to securely start a component located within the very same app.

=> Example: If an app wants to quickly trigger a phone call using an implicit intent, it logically only has to specify the corresponding standardized action named ACTION_DIAL.

=> Example: An explicit intent is initialized by clearly defining the targeted context and the explicit class name parameter, such as `new Intent(myContext, AnotherActivity.class)`.

**2.8 Android Virtual Device (AVD)**

=> Definition: An Android Virtual Device (AVD) acts as a highly specialized configuration that completely defines the characteristics of an Android phone, tablet, Wear OS, Android TV, or Automotive OS device.

=> The AVD safely works in tandem with the Android emulator to successfully provide a virtual device-specific environment in which developers can cleanly install and reliably run Android apps.

=> Key components: An active AVD dynamically contains a strictly defined hardware profile, a specific system image, an allocated storage area, a visual skin, and other configured properties.

=> The avdmanager smoothly operates as a command-line tool securely provided in the Android SDK Tools package that powerfully allows you to actively create and cleanly manage AVDs directly from the command line.

=> If developers are securely using the Android Studio IDE, they smartly do not need to use the command line tool and can instead effortlessly create and manage AVDs visually from within the IDE interface.

**2.9 Mapping Application to Process**

=> Core concept: Android applications are robustly written primarily in the standard Java programming language.

=> During active development, the software developer transparently creates the required Android specific configuration files and meticulously writes the application logic strictly in Java.

=> The ADT (Android Developer Tools) or Android Studio IDE tools quietly transparently convert these compiled application files safely into a complete Android application.

=> When developers forcefully trigger a deployment from their IDE, the entire targeted application is securely compiled, cleanly packaged, efficiently deployed, and successfully started.

Processes with sequential order

1. The provided Java source files are cleanly converted into Java class files natively by the Java compiler.
2. The specialized Android SDK tool called dx securely converts the Java class files into a highly optimized .dex (Dalvik Executable) file.
3. During this conversion phase, completely redundant information logically optimized so the resulting .dex file actively remains much smaller in size compared to the original class files.
4. The generated .dex file and all physical resources of the Android project (e.g., images and XML files) are packed firmly into an .apk (Android package) file strictly utilizing the aapt (Android Asset Packaging Tool) program.
5. The tightly created .apk file safely contains all necessary runtime data and is finally deployed over to a targeted Android device accurately via the adb tool.

Types of Android SDK Features

1. Requires absolutely no licensing, has zero required distributions or development fees, and securely avoids complex release approval processes.
2. Grants developers transparent and full multimedia hardware control.
3. Delivers deep APIs specifically designed for elegantly using sensor hardware including the accelerometer and the compass.
4. Exposes highly optimized APIs exclusively for building advanced location based services.
5. Deeply handles advanced native Android Inter-Process Communication (IPC).
6. Provides secure and flexible shared data storage.
7. Cleanly executes transparent background applications and processes.
8. Safely enables robust dynamic home screen widgets and useful live folders.
9. Completely implements an optimized HTML5 WebKit-based web browser directly natively.
10. Directly supports hardware GSM, EDGE, and 3G networks smoothly for fast telephony and reliable data transfer.
11. Generously includes advanced development tools logically aimed to seamlessly help safely compile and highly effectively debug any mobile app.
12. Offers an integrated visually responsive Android emulator actively showing exactly how an app will visually look and strictly behave identically on a real Android hardware device.
