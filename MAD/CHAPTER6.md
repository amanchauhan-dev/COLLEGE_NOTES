# **6 Graphics, Animation, Alarm and Download Manager**

## **6.1 Working with Graphics**

=> **Definition**: `Graphics in Android means drawing and displaying visual elements such as shapes, images, text, icons, custom views and animations on the screen.`

=> Android does not use Java AWT or Swing for graphics. It provides its own graphics APIs.

### Important packages

1. `android.graphics`: Provides classes like Canvas, Paint, Bitmap, Color and Path.
2. `android.graphics.drawable`: Provides Drawable classes for images, shapes and animation drawables.
3. `android.view`: Provides View and custom drawing support using `onDraw()`.
4. `android.view.animation`: Provides view animation classes.
5. `android.animation`: Provides property animation classes.

### Common uses of graphics

1. Display static images and icons.
2. Draw shapes like line, circle, rectangle and oval.
3. Create custom UI components.
4. Draw charts, games and diagrams.
5. Animate views and objects.
6. Apply visual effects such as rotation, scaling and translation.

## **6.2 Canvas and Paint**

=> **Canvas** is a drawing surface used to draw 2D graphics.

=> **Paint** defines how drawing should appear, such as color, stroke width, text size and style.

### Common Canvas methods

1. `drawLine()` - draws a line.
2. `drawCircle()` - draws a circle.
3. `drawRect()` - draws a rectangle.
4. `drawText()` - draws text.
5. `drawBitmap()` - draws an image.
6. `drawPath()` - draws a custom path.

### Example: Custom View using Canvas

```java
public class DrawingView extends View {
    private Paint paint;

    public DrawingView(Context context) {
        super(context);
        paint = new Paint();
        paint.setColor(Color.BLUE);
        paint.setStrokeWidth(6);
        paint.setTextSize(40);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);

        canvas.drawLine(50, 50, 300, 50, paint);
        canvas.drawRect(50, 100, 300, 250, paint);
        canvas.drawCircle(180, 400, 80, paint);
        canvas.drawText("Android Graphics", 50, 550, paint);
    }
}
```

Use in Activity:

```java
setContentView(new DrawingView(this));
```

## **6.3 Drawable Object**

=> **Definition**: `A Drawable is a graphic resource that can be drawn to the screen.`

=> Drawables are commonly stored in the `res/drawable` folder.

### Uses of Drawables

1. Set image in `ImageView`.
2. Set background for Button, TextView or layout.
3. Create custom shapes using XML.
4. Create frame-by-frame animation.
5. Define different UI states such as pressed, focused and selected.

### Types of Drawable

1. **BitmapDrawable**: Displays image files such as PNG or JPG.
2. **ShapeDrawable**: Draws simple shapes such as rectangle, oval, line or ring.
3. **LayerDrawable**: Combines multiple drawables in layers.
4. **StateListDrawable**: Changes drawable according to view state.
5. **AnimationDrawable**: Shows frame-by-frame animation.

### Example: Use image drawable

```xml
<ImageView
    android:layout_width="100dp"
    android:layout_height="100dp"
    android:src="@drawable/logo" />
```

## **6.4 ShapeDrawable**

=> **Definition**: `ShapeDrawable is used to draw simple geometric shapes such as rectangle, oval, line and ring.`

=> ShapeDrawable is useful for creating button backgrounds, borders, circles and rounded rectangles without using image files.

### Features

1. Defines shape type.
2. Defines solid color.
3. Defines stroke or border.
4. Defines corner radius.
5. Defines gradient and padding.

### Example: Rounded button background

Create `res/drawable/button_bg.xml`:

```xml
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">

    <solid android:color="#2196F3" />

    <stroke
        android:width="2dp"
        android:color="#0D47A1" />

    <corners android:radius="8dp" />

    <padding
        android:left="12dp"
        android:right="12dp"
        android:top="8dp"
        android:bottom="8dp" />
</shape>
```

Use in layout:

```xml
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:background="@drawable/button_bg"
    android:text="Submit" />
```

## **6.5 Ways to Draw 2D Graphics in Android**

### 1. Using XML Drawable

=> XML drawable is best for simple shapes and backgrounds.

```xml
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval">
    <solid android:color="#4CAF50" />
</shape>
```

### 2. Using Canvas and Paint

=> Canvas and Paint are used for custom drawing in a View.

```java
canvas.drawCircle(200, 200, 100, paint);
```

### 3. Using Bitmap

=> Bitmap is used to draw and manipulate images.

```java
Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.logo);
canvas.drawBitmap(bitmap, 50, 50, paint);
```

### 4. Using ShapeDrawable Programmatically

```java
ShapeDrawable shape = new ShapeDrawable(new OvalShape());
shape.getPaint().setColor(Color.RED);
shape.setBounds(50, 50, 250, 250);
shape.draw(canvas);
```

## **6.6 Hardware Acceleration**

=> **Definition**: `Hardware acceleration means using device hardware, mainly GPU, to render graphics faster.`

=> Android introduced hardware-accelerated 2D rendering from Android 3.0/API level 11.

### Significance

1. Improves UI rendering speed.
2. Makes animations smoother.
3. Reduces CPU load.
4. Improves scaling, rotation and translation effects.
5. Helps apps with complex graphics.

### Enable at application level

```xml
<application
    android:hardwareAccelerated="true">
</application>
```

### Enable or disable at activity level

```xml
<activity
    android:name=".MainActivity"
    android:hardwareAccelerated="true" />
```

### Enable at window level

```java
getWindow().setFlags(
        WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED,
        WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);
```

### Disable for a specific View

```java
myView.setLayerType(View.LAYER_TYPE_SOFTWARE, null);
```

## **6.7 Animation in Android**

=> **Definition**: `Animation is the process of creating motion or visual changes in UI elements over time.`

=> Animation improves user experience by making screen changes smooth and giving visual feedback.

### Types of Animation

1. **View Animation**

=> Used for simple effects on views such as rotate, scale, translate and alpha.

2. **Property Animation**

=> Animates actual properties of objects such as `alpha`, `translationX`, `rotation`, `scaleX`.

3. **Frame Animation**

=> Displays a sequence of drawable images one after another.

### Example: View animation

Create `res/anim/fade_in.xml`:

```xml
<alpha xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="1000"
    android:fromAlpha="0.0"
    android:toAlpha="1.0" />
```

Use in Activity:

```java
Animation animation = AnimationUtils.loadAnimation(this, R.anim.fade_in);
textView.startAnimation(animation);
```

### Example: Property animation

```java
ObjectAnimator animator =
        ObjectAnimator.ofFloat(textView, "translationX", 0f, 300f);
animator.setDuration(1000);
animator.start();
```

### Example: Frame animation

Create `res/drawable/frame_animation.xml`:

```xml
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="false">
    <item android:drawable="@drawable/frame1" android:duration="100" />
    <item android:drawable="@drawable/frame2" android:duration="100" />
</animation-list>
```

## **6.8 Clock and Timing Events**

=> Android provides time-related classes to schedule animation and delayed tasks.

### SystemClock methods

1. `currentTimeMillis()`: Returns current wall-clock time in milliseconds.
2. `uptimeMillis()`: Returns time since boot, excluding deep sleep.
3. `elapsedRealtime()`: Returns time since boot, including sleep time.

### Methods to control timing

1. `Thread.sleep(millis)`: Pauses the current thread.
2. `SystemClock.sleep(millis)`: Sleeps without throwing `InterruptedException`.
3. `Handler.postDelayed()`: Runs code after a delay on a thread's message queue.
4. `AlarmManager`: Schedules work at a specific time outside app lifetime.

### Handler example

```java
new Handler(Looper.getMainLooper()).postDelayed(() -> {
    textView.setText("Task completed");
}, 2000);
```

## **6.9 Alarms in Android**

=> **Definition**: `AlarmManager is used to schedule an operation at a specific time or after a time interval.`

=> Alarms work outside the lifetime of the app. At the scheduled time, Android fires a `PendingIntent`.

### Uses

1. Reminder application.
2. Alarm clock.
3. Scheduled notification.
4. Periodic background work.

### Important classes

1. `AlarmManager`: System service used to schedule alarms.
2. `PendingIntent`: Intent executed in future.
3. `BroadcastReceiver`: Receives alarm event.

### Example: Set one alarm after 10 seconds

```java
AlarmManager alarmManager =
        (AlarmManager) getSystemService(ALARM_SERVICE);

Intent intent = new Intent(this, AlarmReceiver.class);
PendingIntent pendingIntent = PendingIntent.getBroadcast(
        this, 1, intent, PendingIntent.FLAG_IMMUTABLE);

long triggerTime = System.currentTimeMillis() + 10000;

alarmManager.set(
        AlarmManager.RTC_WAKEUP,
        triggerTime,
        pendingIntent);
```

### AlarmReceiver.java

```java
public class AlarmReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context, "Alarm triggered", Toast.LENGTH_LONG).show();
    }
}
```

### Manifest

```xml
<receiver android:name=".AlarmReceiver" />
```

## **6.10 Download Manager**

=> **Definition**: `DownloadManager is a system service that handles long-running HTTP downloads in the background.`

=> It automatically manages network changes, retries, notifications and downloaded files.

### Advantages

1. Downloads files in background.
2. Shows download progress in notification.
3. Handles network failure and retry.
4. Continues download even if app is not in foreground.
5. Reduces need to write manual networking code for file downloads.

### Required permission

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

### Example

```java
DownloadManager.Request request = new DownloadManager.Request(
        Uri.parse("https://example.com/file.pdf"));

request.setTitle("Downloading file");
request.setDescription("Please wait");
request.setNotificationVisibility(
        DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
request.setDestinationInExternalPublicDir(
        Environment.DIRECTORY_DOWNLOADS, "file.pdf");

DownloadManager manager =
        (DownloadManager) getSystemService(DOWNLOAD_SERVICE);
manager.enqueue(request);
```

## **6.11 Exam Short Questions**

=> **Question**: `Resource manager is used for?`

=> **Answer**: Resource manager provides access to non-code resources such as strings, colors, images and layouts.

=> **Question**: `What is Canvas?`

=> **Answer**: Canvas is a 2D drawing surface used to draw lines, circles, rectangles, text and images.

=> **Question**: `What is ShapeDrawable?`

=> **Answer**: ShapeDrawable is used to draw simple shapes like rectangle, oval, line and ring using XML or code.

=> **Question**: `What is the purpose of ImageSwitcher?`

=> **Answer**: ImageSwitcher displays images with animation and transition effects.

=> **Question**: `Why use hardware acceleration?`

=> **Answer**: It uses GPU for faster and smoother UI rendering.
