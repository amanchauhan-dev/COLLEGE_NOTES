# **3 User Interface**

## **3.1 Android User Interface**

=> **Definition**: `Android User Interface is the visual part of an application through which the user interacts with the app.`

=> Android UI is built using **View** and **ViewGroup** objects.

### Ways to create UI

1. **XML layout**

=> UI is declared in XML files inside `res/layout`.

2. **Programmatically**

=> UI is created using Java/Kotlin code.

### XML UI example

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="20dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello Android"
        android:textSize="20sp" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click" />
</LinearLayout>
```

### Dynamic UI example

```java
LinearLayout layout = new LinearLayout(this);
layout.setOrientation(LinearLayout.VERTICAL);

TextView textView = new TextView(this);
textView.setText("Dynamic UI");

Button button = new Button(this);
button.setText("Click");

layout.addView(textView);
layout.addView(button);
setContentView(layout);
```

## **3.2 View and ViewGroup**

=> **View** is the basic UI component that occupies a rectangular area on screen.

=> **ViewGroup** is a container that holds and arranges Views or other ViewGroups.

### Examples of View

1. TextView
2. EditText
3. Button
4. ImageView
5. CheckBox
6. RadioButton
7. Spinner

### Examples of ViewGroup

1. LinearLayout
2. RelativeLayout
3. FrameLayout
4. TableLayout
5. ScrollView
6. RecyclerView

### Difference

| View | ViewGroup |
|---|---|
| Basic UI element. | Container for UI elements. |
| Handles drawing and input. | Arranges child views. |
| Example: Button. | Example: LinearLayout. |

## **3.3 Layouts in Android**

=> **Definition**: `Layouts are ViewGroups used to define the structure and position of UI controls on the screen.`

=> Layout XML files are stored in `res/layout`.

### Load layout in Activity

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
}
```

## **3.4 LinearLayout**

=> **LinearLayout** arranges child views in a single direction: vertical or horizontal.

### Features

1. Simple and easy to use.
2. Supports `android:orientation`.
3. Supports `layout_weight` to divide available space.

### Example

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Username" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Login" />
</LinearLayout>
```

## **3.5 RelativeLayout**

=> **RelativeLayout** positions child views relative to parent or relative to other views.

### Common attributes

1. `layout_centerHorizontal`
2. `layout_centerInParent`
3. `layout_below`
4. `layout_above`
5. `layout_alignParentTop`
6. `layout_alignParentBottom`

### Example

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/txtTitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerHorizontal="true"
        android:text="Login" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@id/txtTitle"
        android:layout_centerHorizontal="true"
        android:text="Submit" />
</RelativeLayout>
```

## **3.6 TableLayout**

=> **TableLayout** arranges views in rows and columns using `TableRow`.

=> It is useful for forms and calculator-like screens.

### Example

```xml
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:stretchColumns="1">

    <TableRow>
        <TextView android:text="Name" />
        <EditText android:hint="Enter name" />
    </TableRow>

    <TableRow>
        <TextView android:text="Password" />
        <EditText android:inputType="textPassword" />
    </TableRow>
</TableLayout>
```

## **3.7 FrameLayout, GridLayout and ScrollView**

### FrameLayout

=> FrameLayout is a simple layout that stacks child views on top of each other.

=> It is commonly used as a fragment container.

```xml
<FrameLayout
    android:id="@+id/container"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

### GridLayout

=> GridLayout arranges child views in rows and columns.

```xml
<GridLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:columnCount="2">

    <Button android:text="1" />
    <Button android:text="2" />
</GridLayout>
```

### ScrollView

=> ScrollView allows vertical scrolling when content is larger than the screen.

=> It can contain only one direct child.

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
    </LinearLayout>
</ScrollView>
```

## **3.8 Standard UI Components**

### TextView

=> Displays read-only text.

```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello"
    android:textSize="18sp" />
```

### EditText

=> Allows user to enter text.

```xml
<EditText
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Enter name"
    android:inputType="text" />
```

### Button

=> Performs an action when clicked.

```xml
<Button
    android:id="@+id/btnSubmit"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Submit" />
```

### ImageView

=> Displays an image.

```xml
<ImageView
    android:layout_width="100dp"
    android:layout_height="100dp"
    android:src="@mipmap/ic_launcher" />
```

## **3.9 EditText Input Types**

=> `android:inputType` controls keyboard type and input behavior.

### Common input types

1. `text`
2. `textPassword`
3. `number`
4. `phone`
5. `textEmailAddress`
6. `textMultiLine`

### Example

```xml
<EditText
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="Password"
    android:inputType="textPassword" />
```

## **3.10 RadioButton and RadioGroup**

=> RadioButton is used when the user must select only one option from a group.

=> RadioGroup ensures that only one RadioButton is selected at a time.

### Example

```xml
<RadioGroup
    android:id="@+id/radioGroup"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content">

    <RadioButton
        android:id="@+id/rbMale"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Male" />

    <RadioButton
        android:id="@+id/rbFemale"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Female" />
</RadioGroup>
```

```java
RadioGroup group = findViewById(R.id.radioGroup);

group.setOnCheckedChangeListener((radioGroup, checkedId) -> {
    RadioButton rb = findViewById(checkedId);
    Toast.makeText(this, rb.getText(), Toast.LENGTH_SHORT).show();
});
```

## **3.11 CheckBox and ToggleButton**

### CheckBox

=> CheckBox allows the user to select one or more options.

```xml
<CheckBox
    android:id="@+id/chkJava"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Java" />
```

```java
if (chkJava.isChecked()) {
    textView.setText("Java selected");
}
```

### ToggleButton

=> ToggleButton has two states: ON and OFF.

```xml
<ToggleButton
    android:id="@+id/toggle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:textOn="ON"
    android:textOff="OFF" />
```

## **3.12 Spinner**

=> **Spinner** provides a drop-down list to select one value from multiple options.

### Example

```xml
<Spinner
    android:id="@+id/spinner"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

```java
String[] branches = {"Computer", "IT", "EC", "Mechanical"};

Spinner spinner = findViewById(R.id.spinner);

ArrayAdapter<String> adapter = new ArrayAdapter<>(
        this,
        android.R.layout.simple_spinner_item,
        branches);

adapter.setDropDownViewResource(
        android.R.layout.simple_spinner_dropdown_item);

spinner.setAdapter(adapter);
```

## **3.13 AdapterView, ListView and GridView**

=> **AdapterView** displays data provided by an Adapter.

=> Adapter acts as a bridge between data source and UI.

### Common AdapterView classes

1. ListView
2. GridView
3. Spinner

### ListView example

```xml
<ListView
    android:id="@+id/listView"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

```java
String[] cities = {"Ahmedabad", "Surat", "Rajkot"};

ArrayAdapter<String> adapter = new ArrayAdapter<>(
        this,
        android.R.layout.simple_list_item_1,
        cities);

ListView listView = findViewById(R.id.listView);
listView.setAdapter(adapter);

listView.setOnItemClickListener((parent, view, position, id) -> {
    Toast.makeText(this, cities[position], Toast.LENGTH_SHORT).show();
});
```

### GridView example

```xml
<GridView
    android:id="@+id/gridView"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:numColumns="2" />
```

## **3.14 RecyclerView**

=> RecyclerView is a modern, flexible and efficient list component.

=> It recycles item views and improves performance for large data sets.

### Main parts

1. RecyclerView
2. Adapter
3. ViewHolder
4. LayoutManager

### Basic usage

```java
RecyclerView recyclerView = findViewById(R.id.recyclerView);
recyclerView.setLayoutManager(new LinearLayoutManager(this));
recyclerView.setAdapter(new MyAdapter(dataList));
```

### Advantages over ListView

1. Better performance.
2. Built-in ViewHolder pattern.
3. Supports list, grid and horizontal layouts.
4. Supports animations.

## **3.15 Event Handling**

=> Event handling means responding to user actions such as click, long click, touch and item selection.

### Common event listeners

1. `View.OnClickListener`
2. `View.OnLongClickListener`
3. `View.OnTouchListener`
4. `AdapterView.OnItemClickListener`

### Button click example

```java
Button btn = findViewById(R.id.btnSubmit);

btn.setOnClickListener(v -> {
    Toast.makeText(this, "Button clicked", Toast.LENGTH_SHORT).show();
});
```

### XML onClick example

```xml
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:onClick="showMessage"
    android:text="Click" />
```

```java
public void showMessage(View view) {
    Toast.makeText(this, "Clicked", Toast.LENGTH_SHORT).show();
}
```

## **3.16 Toast**

=> Toast is a small popup message shown for a short time.

### Example

```java
Toast.makeText(this, "Saved successfully", Toast.LENGTH_SHORT).show();
```

## **3.17 Menus in Android**

=> Menus provide app actions without occupying permanent screen space.

### Types of menus

1. Options menu.
2. Context menu.
3. Popup menu.

### Options menu XML

Create `res/menu/main_menu.xml`:

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/action_settings"
        android:title="Settings" />
</menu>
```

### Use in Activity

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.main_menu, menu);
    return true;
}

@Override
public boolean onOptionsItemSelected(MenuItem item) {
    if (item.getItemId() == R.id.action_settings) {
        Toast.makeText(this, "Settings", Toast.LENGTH_SHORT).show();
        return true;
    }
    return super.onOptionsItemSelected(item);
}
```

## **3.18 Styles and Themes**

=> **Style** is a collection of attributes applied to a View.

=> **Theme** is a style applied to an Activity or whole application.

### Style example

```xml
<style name="MyTextStyle">
    <item name="android:textColor">#000000</item>
    <item name="android:textSize">20sp</item>
    <item name="android:textStyle">bold</item>
</style>
```

### Apply style

```xml
<TextView
    style="@style/MyTextStyle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello" />
```

### Theme example

```xml
<application
    android:theme="@style/AppTheme">
</application>
```

## **3.19 Exam Short Questions**

=> **Question**: `What is View?`

=> **Answer**: View is the basic UI component that draws itself and handles user interaction.

=> **Question**: `What is ViewGroup?`

=> **Answer**: ViewGroup is a container that holds and arranges child views.

=> **Question**: `What is LinearLayout?`

=> **Answer**: LinearLayout arranges child views in one direction, vertical or horizontal.

=> **Question**: `What is Spinner?`

=> **Answer**: Spinner is a drop-down control used to select one value from multiple options.

=> **Question**: `What is Toast?`

=> **Answer**: Toast is a small message displayed for a short time.
