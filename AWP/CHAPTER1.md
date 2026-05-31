# **Chapter 1: Refreshing JavaScript and CSS**

## **Table of Contents**

### **Part I: CSS and Bootstrap**

1.1 Introduction to CSS  
1.1.1 Benefits of CSS  
1.2 CSS Syntax and Structure  
1.3 Location of Styles  
1.3.1 Inline Style Sheet  
1.3.2 Document Level Style Sheet  
1.3.3 External Stylesheet  
1.4 Selectors  
1.4.1 Simple Selector Form  
1.4.2 Class Selectors  
1.4.3 Generic Selectors  
1.4.4 ID Selectors  
1.4.5 Universal Selectors  
1.4.6 Attribute Selector  
1.4.7 Contextual Selector  
1.5 Background  
1.6 Color and Color Properties  
1.6.1 Color Groups  
1.6.2 Color Properties  
1.7 Manipulating Texts and Fonts  
1.7.1 Font Families  
1.7.2 Font Sizes  
1.7.3 Font Variants  
1.7.4 Font Styles  
1.7.5 Font Weights  
1.7.6 Font Shorthands  
1.7.7 Text Decoration  
1.7.8 Alignment of Text  
1.8 Lists  
1.9 Responsive Design  
1.9.1 Setting Viewports  
1.9.2 Media Queries  
1.10 Bootstrap Introduction  
1.10.1 Grid System  
1.10.2 Typography  
1.10.3 Tables  
1.10.4 Images  
1.10.5 Button  
1.10.6 Form  

### **Part II: JavaScript**

1.11 JavaScript Syntax  
1.12 JavaScript Inbuilt Objects  
1.12.1 Math Objects  
1.12.2 Number Objects  
1.12.3 Date Objects  
1.12.4 Boolean Objects  
1.12.5 String Objects  
1.12.6 Object Creation and Modification  
1.13 DOM  
1.13.1 Definition of DOM  
1.13.2 DOM Tree  
1.13.3 Using DOM Methods  
1.13.3.1 Accessing Elements using DOM  
1.13.3.2 Modifying Elements using DOM  
1.14 Event Handling  
1.14.1 Handling Events from the Body Elements  
1.15 Error Handling  
1.16 Validators  
1.17 Asynchronous Programming  
1.17.1 Introduction to AJAX  
1.17.2 Architecture  
1.17.3 XMLHttpRequest Object  

---

# **Part I: CSS and Bootstrap**

## **1.1 Introduction to CSS**

=> **CSS** stands for **Cascading Style Sheets**.

=> CSS is used to design and format HTML documents. HTML defines the structure of a webpage, while CSS controls how that webpage looks.

=> CSS can control colors, fonts, spacing, borders, backgrounds, layouts, animations and responsive behavior.

### **Example**

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h1 {
      color: blue;
      text-align: center;
    }

    p {
      font-size: 18px;
      color: green;
    }
  </style>
</head>
<body>
  <h1>Advanced Web Programming</h1>
  <p>CSS is used to style HTML pages.</p>
</body>
</html>
```

=> In this example, CSS changes the heading color, heading alignment, paragraph size and paragraph color.

## **1.1.1 Benefits of CSS**

1. **Separation of content and design**

=> HTML content and page design are kept separate, making code cleaner.

2. **Reusability**

=> One CSS file can be used for many HTML pages.

3. **Easy maintenance**

=> A small change in one stylesheet can update the design of the entire website.

4. **Faster page loading**

=> External CSS files can be cached by browsers.

5. **Responsive design**

=> CSS media queries help create layouts for mobile, tablet and desktop screens.

6. **Consistency**

=> Same design can be applied across all pages.

## **1.2 CSS Syntax and Structure**

=> CSS rule contains a **selector** and a **declaration block**.

```css
selector {
  property: value;
}
```

### **Example**

```css
p {
  color: red;
  font-size: 18px;
}
```

=> `p` is the selector.  
=> `color` and `font-size` are properties.  
=> `red` and `18px` are values.

### **Complete Example**

```html
<style>
  .box {
    background-color: lightgray;
    padding: 15px;
    border: 1px solid black;
  }
</style>

<div class="box">CSS Syntax Example</div>
```

## **1.3 Location of Styles**

=> CSS can be added to HTML in three ways:

1. Inline CSS.
2. Internal or document-level CSS.
3. External CSS.

| Type | Location | Best use |
|---|---|---|
| Inline CSS | Inside HTML tag | Small quick changes |
| Internal CSS | Inside `<style>` tag | Single page styling |
| External CSS | Separate `.css` file | Large websites |

## **1.3.1 Inline Style Sheet**

=> Inline CSS is written directly inside an HTML element using the `style` attribute.

```html
<p style="color: red; font-size: 20px;">This is inline CSS.</p>
```

### **Advantages**

1. Quick to apply.
2. Useful for testing.
3. Has high priority.

### **Disadvantages**

1. Difficult to maintain.
2. Repetition increases.
3. Not suitable for large websites.

## **1.3.2 Document Level Style Sheet**

=> Document-level or internal CSS is written inside the `<style>` tag in the `<head>` section.

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h2 {
      color: purple;
    }

    p {
      line-height: 1.6;
    }
  </style>
</head>
<body>
  <h2>Internal CSS</h2>
  <p>This paragraph is styled using internal CSS.</p>
</body>
</html>
```

=> Internal CSS is useful when only one page needs a specific design.

## **1.3.3 External Stylesheet**

=> External CSS is written in a separate `.css` file and linked with the HTML file.

### **HTML file**

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>External CSS</h1>
  <p>This page uses an external stylesheet.</p>
</body>
</html>
```

### **style.css**

```css
h1 {
  color: navy;
}

p {
  color: #333;
  font-size: 18px;
}
```

=> External CSS is preferred for large projects because it is reusable and easy to maintain.

## **1.4 Selectors**

=> CSS selector selects the HTML element on which CSS rules are applied.

### **Common Selectors**

| Selector | Example | Meaning |
|---|---|---|
| Element | `p` | Selects all paragraphs |
| Class | `.box` | Selects elements with class `box` |
| ID | `#header` | Selects element with id `header` |
| Universal | `*` | Selects all elements |
| Attribute | `input[type="text"]` | Selects elements by attribute |
| Contextual | `div p` | Selects `p` inside `div` |

## **1.4.1 Simple Selector Form**

=> Simple selector selects elements by tag name.

```css
h1 {
  color: blue;
}

p {
  font-size: 18px;
}
```

```html
<h1>Heading</h1>
<p>Paragraph text</p>
```

=> All `<h1>` elements become blue and all `<p>` elements get font size `18px`.

## **1.4.2 Class Selectors**

=> Class selector selects elements using the `class` attribute.

=> It starts with a dot `.`.

```css
.important {
  color: red;
  font-weight: bold;
}
```

```html
<p class="important">This is important text.</p>
<h3 class="important">Important heading</h3>
```

=> Same class can be used on multiple elements.

## **1.4.3 Generic Selectors**

=> Generic class selector can be applied to any HTML element.

```css
.center {
  text-align: center;
}

.warning {
  color: darkred;
  background-color: lightyellow;
}
```

```html
<h2 class="center">Centered Heading</h2>
<p class="warning">This is a warning message.</p>
```

=> Generic selectors are useful for reusable styles.

## **1.4.4 ID Selectors**

=> ID selector selects one unique element using `id`.

=> It starts with `#`.

```css
#mainTitle {
  color: green;
  text-transform: uppercase;
}
```

```html
<h1 id="mainTitle">Main Heading</h1>
```

### **Class selector vs ID selector**

| Class selector | ID selector |
|---|---|
| Starts with `.` | Starts with `#` |
| Can be used many times | Should be unique |
| Used for reusable style | Used for one specific element |

## **1.4.5 Universal Selectors**

=> Universal selector selects all HTML elements.

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

=> It is commonly used to reset default browser spacing.

## **1.4.6 Attribute Selector**

=> Attribute selector selects elements based on attribute or attribute value.

```css
input[type="text"] {
  border: 1px solid blue;
}

input[type="email"] {
  border: 1px solid green;
}

a[target="_blank"] {
  color: red;
}
```

```html
<input type="text" placeholder="Name">
<input type="email" placeholder="Email">
<a href="https://example.com" target="_blank">Open</a>
```

## **1.4.7 Contextual Selector**

=> Contextual selector selects elements based on their position or relationship with other elements.

```css
div p {
  color: blue;
}

ul li {
  margin-bottom: 5px;
}
```

```html
<div>
  <p>This paragraph is inside div.</p>
</div>

<p>This paragraph is outside div.</p>
```

=> Only paragraph inside `div` becomes blue.

## **1.5 Background**

=> CSS background properties are used to control background color and images.

### **Important background properties**

| Property | Use |
|---|---|
| `background-color` | Sets background color |
| `background-image` | Sets background image |
| `background-repeat` | Controls image repetition |
| `background-position` | Sets image position |
| `background-size` | Sets image size |
| `background` | Shorthand property |

```css
.banner {
  background-color: #e8f0ff;
  background-image: url("banner.jpg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  padding: 60px;
}
```

```html
<div class="banner">
  <h1>Welcome</h1>
</div>
```

## **1.6 Color and Color Properties**

=> CSS colors can be applied to text, background, borders and shadows.

```css
p {
  color: red;
  background-color: lightyellow;
  border: 1px solid black;
}
```

## **1.6.1 Color Groups**

=> CSS supports different ways to define colors.

| Color type | Example |
|---|---|
| Color name | `red`, `blue`, `green` |
| Hex code | `#ff0000`, `#00ff00` |
| RGB | `rgb(255, 0, 0)` |
| RGBA | `rgba(255, 0, 0, 0.5)` |
| HSL | `hsl(120, 100%, 50%)` |

```css
.name-color { color: red; }
.hex-color { color: #0066cc; }
.rgb-color { color: rgb(0, 150, 100); }
.rgba-color { background-color: rgba(255, 0, 0, 0.2); }
```

## **1.6.2 Color Properties**

| Property | Use |
|---|---|
| `color` | Text color |
| `background-color` | Background color |
| `border-color` | Border color |
| `outline-color` | Outline color |

```css
.card {
  color: #222;
  background-color: #f5f5f5;
  border: 2px solid #0080ff;
}
```

## **1.7 Manipulating Texts and Fonts**

=> CSS text and font properties control how text appears on a webpage.

## **1.7.1 Font Families**

=> `font-family` specifies the font of text.

```css
body {
  font-family: Arial, Helvetica, sans-serif;
}
```

=> Multiple fonts are written as fallback options.

## **1.7.2 Font Sizes**

=> `font-size` controls text size.

```css
h1 {
  font-size: 32px;
}

p {
  font-size: 1rem;
}
```

### **Common units**

| Unit | Meaning |
|---|---|
| `px` | Fixed pixels |
| `%` | Relative to parent |
| `em` | Relative to parent font size |
| `rem` | Relative to root font size |

## **1.7.3 Font Variants**

=> `font-variant` is used to display text in small caps.

```css
.small-caps {
  font-variant: small-caps;
}
```

```html
<p class="small-caps">advanced web programming</p>
```

## **1.7.4 Font Styles**

=> `font-style` controls normal, italic or oblique text.

```css
.italic {
  font-style: italic;
}
```

## **1.7.5 Font Weights**

=> `font-weight` controls text thickness.

```css
.normal {
  font-weight: normal;
}

.bold {
  font-weight: bold;
}

.heavy {
  font-weight: 700;
}
```

## **1.7.6 Font Shorthands**

=> `font` shorthand can set multiple font properties in one line.

```css
p {
  font: italic small-caps bold 18px Arial, sans-serif;
}
```

=> Order generally includes style, variant, weight, size and family.

## **1.7.7 Text Decoration**

=> `text-decoration` adds or removes underline, overline and line-through.

```css
a {
  text-decoration: none;
}

.deleted {
  text-decoration: line-through;
}

.important {
  text-decoration: underline;
}
```

## **1.7.8 Alignment of Text**

=> `text-align` controls horizontal alignment of text.

```css
.left { text-align: left; }
.center { text-align: center; }
.right { text-align: right; }
.justify { text-align: justify; }
```

```html
<p class="center">This text is center aligned.</p>
```

## **1.8 Lists**

=> CSS can style ordered and unordered lists.

### **Important list properties**

| Property | Use |
|---|---|
| `list-style-type` | Type of bullet/number |
| `list-style-position` | Position of marker |
| `list-style-image` | Custom bullet image |
| `list-style` | Shorthand |

```css
ul {
  list-style-type: square;
}

ol {
  list-style-type: upper-roman;
}

.menu {
  list-style: none;
  padding: 0;
}
```

```html
<ul>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<ol>
  <li>AngularJS</li>
  <li>Node JS</li>
</ol>
```

## **1.9 Responsive Design**

=> **Responsive design** makes a webpage adjust automatically on different devices such as desktop, tablet and mobile.

### **Need of responsive design**

1. Same website works on different screen sizes.
2. Improves user experience.
3. Reduces need for separate mobile website.
4. Important for modern web development.

```css
.container {
  width: 80%;
  margin: auto;
}

@media (max-width: 600px) {
  .container {
    width: 100%;
  }
}
```

## **1.9.1 Setting Viewports**

=> Viewport is the visible area of a webpage on a device.

=> The viewport meta tag is required for responsive design on mobile devices.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

=> `width=device-width` sets page width equal to device width.  
=> `initial-scale=1.0` sets initial zoom level.

## **1.9.2 Media Queries**

=> Media query applies CSS based on device width, height or other conditions.

```css
body {
  background-color: white;
}

@media (max-width: 768px) {
  body {
    background-color: lightgray;
  }

  h1 {
    font-size: 24px;
  }
}
```

### **Responsive layout example**

```html
<style>
.row {
  display: flex;
  gap: 10px;
}

.col {
  flex: 1;
  background: lightblue;
  padding: 20px;
}

@media (max-width: 600px) {
  .row {
    flex-direction: column;
  }
}
</style>

<div class="row">
  <div class="col">Column 1</div>
  <div class="col">Column 2</div>
</div>
```

## **1.10 Bootstrap Introduction**

=> **Bootstrap** is a popular front-end framework used to create responsive and mobile-first websites quickly.

=> It provides ready-made CSS classes for layout, forms, buttons, tables, images, navigation and components.

### **Adding Bootstrap**

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

## **1.10.1 Grid System**

=> Bootstrap grid system divides a row into 12 columns.

=> It uses `.container`, `.row` and `.col-*` classes.

```html
<div class="container">
  <div class="row">
    <div class="col-md-6 bg-light">Column 1</div>
    <div class="col-md-6 bg-secondary text-white">Column 2</div>
  </div>
</div>
```

=> `col-md-6` means each column takes 6 out of 12 columns on medium and larger screens.

## **1.10.2 Typography**

=> Bootstrap provides typography classes for headings, paragraphs and text formatting.

```html
<h1 class="display-4">Bootstrap Heading</h1>
<p class="lead">This is a lead paragraph.</p>
<p class="text-center text-primary">Centered blue text</p>
<p class="fw-bold">Bold text</p>
```

## **1.10.3 Tables**

=> Bootstrap table classes improve table design.

```html
<table class="table table-bordered table-striped">
  <tr>
    <th>Roll No</th>
    <th>Name</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Aman</td>
  </tr>
</table>
```

| Class | Use |
|---|---|
| `table` | Basic Bootstrap table |
| `table-bordered` | Adds borders |
| `table-striped` | Adds alternate row color |
| `table-hover` | Adds hover effect |

## **1.10.4 Images**

=> Bootstrap provides classes for responsive and styled images.

```html
<img src="photo.jpg" class="img-fluid" alt="Responsive image">
<img src="photo.jpg" class="rounded" alt="Rounded image">
<img src="photo.jpg" class="img-thumbnail" alt="Thumbnail image">
```

=> `img-fluid` makes image responsive by setting maximum width to 100%.

## **1.10.5 Button**

=> Bootstrap provides predefined button classes.

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-outline-dark">Outline</button>
```

| Class | Meaning |
|---|---|
| `btn` | Basic button class |
| `btn-primary` | Blue button |
| `btn-success` | Green button |
| `btn-danger` | Red button |
| `btn-outline-*` | Outline button |

## **1.10.6 Form**

=> Bootstrap form classes make forms clean and responsive.

```html
<form>
  <div class="mb-3">
    <label class="form-label">Name</label>
    <input type="text" class="form-control" placeholder="Enter name">
  </div>

  <div class="mb-3">
    <label class="form-label">Email</label>
    <input type="email" class="form-control" placeholder="Enter email">
  </div>

  <button class="btn btn-primary">Submit</button>
</form>
```

=> `form-control` styles input fields and `mb-3` adds bottom margin.

# **Part II: JavaScript**

## **1.11 JavaScript Syntax**

=> JavaScript is a scripting language used to make web pages dynamic and interactive.

=> JavaScript can be written inside `<script>` tag or in an external `.js` file.

```html
<script>
  let name = "Aman";
  let age = 21;

  document.write("Name: " + name + "<br>");
  document.write("Age: " + age);
</script>
```

### **Variables**

```js
var a = 10;
let b = 20;
const pi = 3.14;
```

=> `var` is older function-scoped variable.  
=> `let` is block-scoped variable.  
=> `const` is block-scoped constant.

### **Conditional statement**

```js
let marks = 75;

if (marks >= 35) {
  console.log("Pass");
} else {
  console.log("Fail");
}
```

### **Loop**

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

### **Function**

```js
function add(a, b) {
  return a + b;
}

console.log(add(10, 20));
```

## **1.12 JavaScript Inbuilt Objects**

=> JavaScript provides built-in objects for common operations such as math, date, string, number and boolean handling.

## **1.12.1 Math Objects**

=> `Math` object provides mathematical functions and constants.

```js
console.log(Math.PI);
console.log(Math.sqrt(25));
console.log(Math.pow(2, 3));
console.log(Math.round(4.6));
console.log(Math.floor(4.9));
console.log(Math.ceil(4.1));
console.log(Math.random());
```

| Method | Use |
|---|---|
| `Math.sqrt()` | Square root |
| `Math.pow()` | Power |
| `Math.round()` | Round value |
| `Math.floor()` | Lower integer |
| `Math.ceil()` | Higher integer |
| `Math.random()` | Random number |

## **1.12.2 Number Objects**

=> Number object is used to work with numeric values.

```js
let x = 123.456;

console.log(x.toFixed(2));
console.log(x.toPrecision(4));
console.log(Number.isInteger(x));
console.log(parseInt("100"));
console.log(parseFloat("10.50"));
```

=> `toFixed(2)` displays number with 2 decimal places.

## **1.12.3 Date Objects**

=> Date object is used to work with date and time.

```js
let d = new Date();

console.log(d);
console.log(d.getFullYear());
console.log(d.getMonth() + 1);
console.log(d.getDate());
console.log(d.getHours());
console.log(d.getMinutes());
```

### **Creating specific date**

```js
let examDate = new Date("2026-05-31");
console.log(examDate);
```

## **1.12.4 Boolean Objects**

=> Boolean represents true or false values.

```js
let isValid = true;
let isLoggedIn = false;

console.log(isValid);
console.log(Boolean(10));
console.log(Boolean(""));
```

=> `Boolean(10)` returns true.  
=> `Boolean("")` returns false.

## **1.12.5 String Objects**

=> String object provides methods to work with text.

```js
let str = "Advanced Web Programming";

console.log(str.length);
console.log(str.toUpperCase());
console.log(str.toLowerCase());
console.log(str.indexOf("Web"));
console.log(str.includes("Programming"));
console.log(str.substring(0, 8));
console.log(str.replace("Web", "Internet"));
```

| Method | Use |
|---|---|
| `length` | Returns string length |
| `toUpperCase()` | Converts to uppercase |
| `toLowerCase()` | Converts to lowercase |
| `indexOf()` | Finds position |
| `includes()` | Checks text exists |
| `substring()` | Extracts part |
| `replace()` | Replaces text |

## **1.12.6 Object Creation and Modification**

=> Object stores data in key-value pairs.

### **Object literal**

```js
let student = {
  rollno: 1,
  name: "Aman",
  branch: "CE"
};

console.log(student.name);
```

### **Modifying object**

```js
student.name = "Aman Patel";
student.semester = 6;
delete student.branch;

console.log(student);
```

### **Constructor function**

```js
function Student(rollno, name) {
  this.rollno = rollno;
  this.name = name;
}

let s1 = new Student(1, "Aman");
console.log(s1.name);
```

## **1.13 DOM**

=> DOM is used by JavaScript to access and modify HTML documents.

## **1.13.1 Definition of DOM**

=> **DOM** stands for **Document Object Model**.

=> It represents an HTML page as a tree of objects.

=> JavaScript can use DOM to change content, attributes, styles and structure of a webpage.

## **1.13.2 DOM Tree**

```text
document
  |
  html
  |-- head
  |   |-- title
  |
  |-- body
      |-- h1
      |-- p
      |-- button
```

=> Each HTML element is called a node in DOM tree.

## **1.13.3 Using DOM Methods**

=> DOM methods allow JavaScript to access and modify elements.

## **1.13.3.1 Accessing Elements using DOM**

| Method | Use |
|---|---|
| `getElementById()` | Selects element by id |
| `getElementsByClassName()` | Selects elements by class |
| `getElementsByTagName()` | Selects elements by tag |
| `querySelector()` | Selects first matching CSS selector |
| `querySelectorAll()` | Selects all matching CSS selectors |

```html
<h2 id="title">DOM Example</h2>
<p class="msg">Paragraph 1</p>
<p class="msg">Paragraph 2</p>

<script>
let title = document.getElementById("title");
let messages = document.getElementsByClassName("msg");

console.log(title.innerHTML);
console.log(messages[0].innerHTML);
</script>
```

## **1.13.3.2 Modifying Elements using DOM**

=> DOM can modify text, style, attribute and structure.

```html
<h2 id="title">Old Title</h2>
<p id="para">Old paragraph</p>
<button onclick="changeData()">Change</button>

<script>
function changeData() {
  document.getElementById("title").innerHTML = "New Title";
  document.getElementById("para").style.color = "blue";
  document.getElementById("para").setAttribute("class", "highlight");
}
</script>
```

### **Adding new element**

```html
<div id="box"></div>

<script>
let p = document.createElement("p");
p.innerHTML = "New paragraph added using DOM";
document.getElementById("box").appendChild(p);
</script>
```

## **1.14 Event Handling**

=> Event is an action that happens in browser, such as click, keypress, mouseover, submit or page load.

=> Event handling means writing code that executes when an event occurs.

```html
<button onclick="showMessage()">Click Me</button>
<p id="msg"></p>

<script>
function showMessage() {
  document.getElementById("msg").innerHTML = "Button clicked";
}
</script>
```

### **Common events**

| Event | Use |
|---|---|
| `onclick` | Mouse click |
| `onmouseover` | Mouse pointer over element |
| `onmouseout` | Mouse pointer leaves element |
| `onchange` | Input value changes |
| `onsubmit` | Form submitted |
| `onload` | Page loaded |

## **1.14.1 Handling Events from the Body Elements**

=> Body events are triggered by actions on the page body.

```html
<body onload="pageLoaded()" onkeydown="keyPressed(event)">
  <h2>Body Event Example</h2>

  <script>
  function pageLoaded() {
    alert("Page loaded successfully");
  }

  function keyPressed(event) {
    console.log("Key pressed: " + event.key);
  }
  </script>
</body>
```

=> `onload` executes when page loads.  
=> `onkeydown` executes when a keyboard key is pressed.

## **1.15 Error Handling**

=> Error handling is used to detect and handle errors in JavaScript.

=> JavaScript uses `try`, `catch`, `finally` and `throw`.

```js
try {
  let age = -5;

  if (age < 0) {
    throw new Error("Age cannot be negative");
  }

  console.log(age);
} catch (err) {
  console.log("Error: " + err.message);
} finally {
  console.log("Validation completed");
}
```

### **Explanation**

1. `try` contains code that may produce error.
2. `catch` handles the error.
3. `finally` always executes.
4. `throw` creates custom error.

## **1.16 Validators**

=> Validators check whether user input is valid before processing it.

=> Validation can be done using HTML attributes and JavaScript.

### **Email validation example**

```html
<input type="text" id="email" placeholder="Enter email">
<button onclick="validateEmail()">Validate</button>
<p id="msg"></p>

<script>
function validateEmail() {
  let email = document.getElementById("email").value;
  let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (pattern.test(email)) {
    document.getElementById("msg").innerHTML = "Valid email";
  } else {
    document.getElementById("msg").innerHTML = "Invalid email";
  }
}
</script>
```

### **Password validation example**

```html
<input type="password" id="pwd" placeholder="Password">
<button onclick="validatePassword()">Check</button>
<p id="result"></p>

<script>
function validatePassword() {
  let pwd = document.getElementById("pwd").value;
  let pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;

  if (pattern.test(pwd)) {
    document.getElementById("result").innerHTML = "Valid password";
  } else {
    document.getElementById("result").innerHTML =
      "Password must contain uppercase, lowercase, digit and minimum 8 characters";
  }
}
</script>
```

=> Validation improves data correctness and user experience.

## **1.17 Asynchronous Programming**

=> **Asynchronous programming** allows JavaScript to start a task and continue executing other statements without waiting for that task to finish.

=> It is useful for timers, API calls, file loading and server communication.

```js
console.log("Start");

setTimeout(function() {
  console.log("This runs after 2 seconds");
}, 2000);

console.log("End");
```

### **Output**

```text
Start
End
This runs after 2 seconds
```

=> JavaScript does not wait for `setTimeout()`.

## **1.17.1 Introduction to AJAX**

=> **AJAX** stands for **Asynchronous JavaScript and XML**.

=> AJAX is used to send and receive data from server without refreshing the whole page.

### **Uses of AJAX**

1. Loading search suggestions.
2. Submitting forms without page reload.
3. Fetching table data from server.
4. Updating part of webpage dynamically.

## **1.17.2 Architecture**

### **AJAX architecture flow**

```text
User Action
    |
JavaScript Function
    |
XMLHttpRequest Object
    |
Server
    |
Response Data
    |
DOM Update
```

### **Explanation**

1. User performs action such as button click.
2. JavaScript creates request.
3. `XMLHttpRequest` sends request to server.
4. Server sends response.
5. JavaScript updates webpage using DOM.

## **1.17.3 XMLHttpRequest Object**

=> `XMLHttpRequest` is a browser object used to send AJAX requests.

### **Important methods and properties**

| Method/Property | Use |
|---|---|
| `open()` | Initializes request |
| `send()` | Sends request |
| `onreadystatechange` | Handles state change |
| `readyState` | Request state |
| `status` | HTTP status code |
| `responseText` | Server response text |

### **AJAX GET example**

```html
<button onclick="loadData()">Load Data</button>
<div id="result"></div>

<script>
function loadData() {
  let xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      document.getElementById("result").innerHTML = this.responseText;
    }
  };

  xhttp.open("GET", "data.txt", true);
  xhttp.send();
}
</script>
```

=> `readyState === 4` means request completed.  
=> `status === 200` means request successful.

### **AJAX POST example**

```html
<button onclick="sendData()">Send Data</button>
<p id="msg"></p>

<script>
function sendData() {
  let xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      document.getElementById("msg").innerHTML = this.responseText;
    }
  };

  xhttp.open("POST", "save.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("name=Aman&branch=CE");
}
</script>
```

=> POST request sends data to the server in request body.

## **Exam Short Questions**

1. Define CSS.
2. List benefits of CSS.
3. Explain inline, internal and external CSS.
4. What is CSS selector?
5. Differentiate class selector and ID selector.
6. Explain attribute selector with example.
7. What is responsive design?
8. What is viewport meta tag?
9. Explain media query.
10. What is Bootstrap?
11. Explain Bootstrap grid system.
12. Define JavaScript.
13. List JavaScript inbuilt objects.
14. Explain Math object.
15. Explain String object.
16. What is DOM?
17. Draw DOM tree.
18. List DOM methods.
19. Explain event handling.
20. Explain JavaScript error handling.
21. What is AJAX?
22. Explain `XMLHttpRequest`.
23. Write email validation using JavaScript.
24. Explain asynchronous programming.
