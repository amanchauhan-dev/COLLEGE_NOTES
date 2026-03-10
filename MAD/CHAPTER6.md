**6 Graphics and Animation**

**6.1 Working with Graphics**

=> Core concept: Graphics are created by the developer and added to the application.

=> They can be created from results from various operations such as querying, identifying, geoprocessing, geocoding, or routing.

=> Graphics can also be created from external data sources.

=> Important explanation point: If you want to persist the data in a map or scene, then you must use features.

=> Graphics can also be created dynamically by the developer as a result of a map click or touch.

=> The Android SDK provides a huge set of APIs that allows you to create 2-D and 3-D graphics.

=> Android supports 2D graphics via its own library in the packages `android.graphics.drawable` and `android.view.animation`.

=> Limitation: Take note that Android strictly does not support the JDK's AWT and Swing packages.

=> The `android.graphics.drawable` and `android.view.animation` packages are exactly where you will find the common classes used for drawing and animating in two-dimensions.

**6.1.1 Uses of Graphics**

Types of common uses for graphics

1. Display text on top of a map or scene.
2. Highlight a section of the map or scene by overlaying a polygon graphic.
3. Display results from spatial analysis, such as buffer polygons created around features.
4. Display a route between two locations.
5. Display geometry drawn interactively by the app user.
6. Animate data items that change quickly, such as moving objects.

**6.2 Using Drawable Object**

=> Android provides a set of View widgets that provide general functionality for a wide array of user interfaces.

=> You can also extend these widgets to modify the way they look or behave.

=> Custom 2D rendering can be done using the various drawing methods contained in the Canvas class.

=> You can create Drawable objects for things such as textured buttons or frame-by-frame animations.

=> Definition: A drawable resource is a general concept for a graphic that can be drawn to the screen.

=> Important explanation point: When you need to display static images in your app, you can use the Drawable class and its subclasses to draw shapes and images.

=> Drawables are used to define shapes, colors, borders, and gradients, which can then be applied to views within an Activity.

=> Every Drawable is stored as individual files in one of the `res/drawable` folders.

Types of ways to define and instantiate a drawable

1. Using an image saved in your project resources.
2. Using an XML file that defines the Drawable properties.
3. Using the normal class constructors.

**6.3 Using the Shape Drawable Object**

=> Core concept: A drawable object is a primitive shape.

=> When you want to dynamically draw some two-dimensional graphics, a Shape Drawable object will probably suit your needs.

=> With a Shape Drawable, you can programmatically draw primitive shapes and style them in any way imaginable.

=> A Shape Drawable is an extension of Drawable, so you can use one wherever a Drawable is expected, perhaps for the background of a view set with `setBackgroundDrawable()`.

=> You can also draw your shape as its own custom View to be added to your layout however you please.

=> Because the Shape Drawable has its own `draw()` method, you can create a subclass of View that draws the Shape Drawable during the `onDraw()` method.

=> A Shape Drawable takes a Shape object and manages its presence on the screen.

=> If no shape is given, then the Shape Drawable will default to a rectangle shape.

=> Shape Drawables are XML files which allow you to define a geometric object with colors, borders, and gradients.

=> Advantage: The advantage of using XML shape Drawables is that they automatically adjust to the correct size.

**6.4 Hardware Acceleration**

=> Android 3.0 (API level 11) introduced a new rendering pipeline to allow applications to benefit from hardware-accelerated 2-D graphics.

=> You can use hardware acceleration if you have complex computations like scaling, rotating, or translation of images.

=> Hardware Acceleration is used to improve the performance and aesthetics of your activities and views.

=> Important explanation point: All the SDK Views, layouts, and effects support hardware acceleration.

=> Android gives you the option to enable or disable hardware acceleration at multiple levels.

Types of levels to control hardware acceleration

1. Application level: In your Android manifest file, add the attribute `android:hardwareAccelerated="true"` to the `<application>` tag to enable hardware acceleration for your entire application.
2. Activity level: If your application does not behave properly with hardware acceleration turned on globally, you can control it for individual activities as well by using the `android:hardwareAccelerated="false"` attribute for the `<activity>` element.
3. Window level: If you need even more fine-grained control, you can enable hardware acceleration for a given window with the following code: `getWindow().setFlags(WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED, WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);`.
4. View level: You can disable hardware acceleration for an individual view at runtime with the following code: `myView.setLayerType(View.LAYER_TYPE_SOFTWARE, null);`.

**6.5 Working with Animation**

=> Animations can add visual cues that notify users about what's going on in your app.

=> They are especially useful when the UI changes state, such as when new content loads or new actions become available.

=> Animations also add a polished look to your app, which gives it a higher quality look and feel.

Types of Animation

1. Property animation: Property animators were introduced in Android 3.0 (API level 11). It is a powerful framework that can be used to animate almost any property on a target object. Property animators are extremely useful and are used extensively for animating fragments.
2. View animations: Animations that can be applied for views to rotate, move and stretch.
3. Frame animations: Frame-by-frame animations produce a sequence of Drawables, each of which is displayed for a specified duration.

**6.5.1 Clock for Animated Graphics**

=> The methods (functions) provided by the android class SystemClock are used to create animated graphics.

=> The class consists of core timekeeping facilities.

=> To use the methods, we have to import the class by adding the header statement, `import android.os.SystemClock;`.

Types of clocks used to keep time

1. `currentTimeMillis()`: Gives the current time and date expressed in milliseconds since the epoch. This clock can be set by the user or the phone network.
2. `uptimeMillis()`: Gives the active time lapse in milliseconds since the system was booted. This clock stops when the process is in a blocked or a sleep state such as waiting for an I/O event or executing `Thread.sleep()`.
3. `elapsedRealtime()`: Counts the time in milliseconds since the system was booted, including the time when the process is blocked or in a sleep state.

**6.5.2 Controlling Timing Events**

=> There are several ways to control the timing events in an animation process.

Types of methods to control timing events

1. `Thread.sleep(millis)` and `Object.wait(millis)`: Standard blocking functions that can be used to generate desired time delays. When these functions are executed, the `uptimeMillis()` clock stops. The thread can be woken up by the function `Thread.interrupt()`.
2. `SystemClock.sleep(millis)`: A utility function very similar to `Thread.sleep(millis)`, except that it ignores `InterruptedException`.
3. Handler class: We can use the Handler class to schedule asynchronous callbacks at an absolute or relative time. A handler object uses the `uptimeMillis()` clock to keep time and requires an event loop to wait for an event to happen.
4. AlarmManager class: We can use the AlarmManager class to access the system alarm services such as triggering one-time or recurring events when the thread is in a blocked state.

**6.6 Alarms in Android**

=> Core concept: In Android, alarms give you a way to schedule your application to run at some point in the future.

=> Alarms can be used for a wide range of applications, from notifying a user of an appointment to something more sophisticated, such as having an application start, checking for software updates, and then shutting down.

=> Alarms (based on the AlarmManager class) give you a way to perform time-based operations outside the lifetime of your application.

=> Example: You could use an alarm to initiate a long-running operation, such as starting a service once a day to download a weather forecast.

=> An alarm works by registering an Intent with the alarm; at the scheduled time, the alarm broadcasts the Intent.

=> Android automatically starts the targeted application, even if the Android handset is asleep.

=> Android manages all alarms somewhat as it manages the NotificationManager via an AlarmManager class.

=> Characteristics: They let you fire Intents at set times and/or intervals.

=> Characteristics: You can use them in conjunction with broadcast receivers to start services and perform other operations.

=> Characteristics: They operate outside of your application, so you can use them to trigger events or actions even when your app is not running, and even if the device itself is asleep.

=> Characteristics: They help you to minimize your app's resource requirements. You can schedule operations without relying on timers or continuously running background services.

**6.7 Download Manager**

=> Definition: The download manager is a system service that handles long-running HTTP downloads.

=> Clients may request that a URI be downloaded to a particular destination file.

=> The download manager was introduced in Android 2.3 (API level 9).

Advantages of the Android Download Manager

1. It optimizes the handling of long-running downloads in the background.
2. It flawlessly handles HTTP connections, monitors connectivity changes and reboots, and ensures each download completes successfully.
3. The download manager will effectively conduct the download in the background, taking care of HTTP interactions and retrying downloads after failures across connectivity changes and system reboots.

=> Important explanation point: If you want to download over a cellular network, you cannot use Retrofit or Volley, because both recommend using DownloadManager instead.

=> Apps that request downloads through this API should register a broadcast receiver for `ACTION_NOTIFICATION_CLICKED` to appropriately handle when the user clicks on a running download in a notification or from the downloads UI.

=> The application must securely have the `Manifest.permission.INTERNET` permission to use this class.

**6.8 Multiple Choice Questions**

=> Question 1: Resource manager is used for? Answer: It provides access to non-code embedded resources such as strings, color settings and user interface layouts.

=> Question 2: What is a correct statement about an XML layout file? Answer: A file that contains a single activity widget.

=> Question 3: Which is the most popular software used for creating 2D animation for use in web pages? Answer: Flash.

=> Question 4: What is the purpose of the image switcher? Answer: The image switcher enables images to be displayed with animation, and it allows you to add some transitions on the images.
