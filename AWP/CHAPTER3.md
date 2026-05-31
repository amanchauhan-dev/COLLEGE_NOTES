# **Chapter 3: AngularJS in Details**

## **Table of Contents**

3.1 Directives  
3.1.1 Built-in Directives  
3.1.2 Custom Directives  
3.2 Modules  
3.3 Routes  
3.4 AngularJS Forms and Validations  
3.5 Data Binding  
3.6 Creating Single Page Website using AngularJS  
3.7 Important Definitions  
3.8 Exam Short Questions  

---

## **3.1 Directives**

=> **Directive** is a special marker or attribute in AngularJS that extends HTML functionality.

=> Directives tell AngularJS to attach special behavior to HTML elements.

=> AngularJS directives usually start with the prefix `ng-`.

### **Simple Definition**

=> A directive is an AngularJS instruction written inside HTML to bind data, repeat elements, handle events, validate forms, show or hide elements, and control DOM behavior.

### **Why Directives are Used**

1. To initialize an AngularJS application.
2. To bind HTML controls with model data.
3. To repeat HTML elements dynamically.
4. To show, hide, enable or disable elements.
5. To handle events such as click, change and submit.
6. To validate forms.
7. To create reusable custom HTML components.

### **Basic Example**

```html
<!DOCTYPE html>
<html ng-app="">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body>
  Enter Name:
  <input type="text" ng-model="name">

  <h3>Hello {{name}}</h3>
</body>
</html>
```

### **Explanation**

=> `ng-app` starts the AngularJS application.

=> `ng-model="name"` binds textbox value with the model variable `name`.

=> `{{name}}` displays the value of `name`.

### **Important Point for Exam**

=> Directives are one of the most important features of AngularJS because they allow developers to write dynamic behavior directly inside HTML without manual DOM manipulation.

## **3.1.1 Built-in Directives**

=> AngularJS provides many predefined directives for common tasks.

| Directive | Use |
|---|---|
| `ng-app` | Initializes AngularJS application |
| `ng-init` | Initializes application data |
| `ng-model` | Binds input field with model data |
| `ng-bind` | Binds data to HTML element |
| `ng-repeat` | Repeats HTML element for each item in collection |
| `ng-click` | Executes expression on click event |
| `ng-show` | Shows element when condition is true |
| `ng-hide` | Hides element when condition is true |
| `ng-if` | Adds or removes element based on condition |
| `ng-class` | Applies CSS class dynamically |
| `ng-style` | Applies CSS style dynamically |
| `ng-submit` | Executes expression on form submission |
| `ng-disabled` | Disables element based on condition |
| `ng-options` | Generates options for select list |
| `ng-view` | Displays routed view in SPA |

### **1. `ng-app` Directive**

=> `ng-app` defines the root element of an AngularJS application.

=> It tells AngularJS from where the application should start.

```html
<html ng-app="studentApp">
```

### **Example**

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body>
  <p>AngularJS application starts from this page.</p>

  <script>
  var app = angular.module("studentApp", []);
  </script>
</body>
</html>
```

### **2. `ng-init` Directive**

=> `ng-init` initializes data for an AngularJS application.

=> It is useful for small examples, but in real applications data is usually initialized in a controller.

```html
<div ng-app="" ng-init="student='Aman'; marks=85">
  <p>Name: {{student}}</p>
  <p>Marks: {{marks}}</p>
</div>
```

### **3. `ng-model` Directive**

=> `ng-model` binds form controls such as textbox, checkbox, radio button and select list with AngularJS model data.

=> It is used for two-way data binding.

```html
<div ng-app="">
  <input type="text" ng-model="city">
  <p>Selected City: {{city}}</p>
</div>
```

### **4. `ng-bind` Directive**

=> `ng-bind` binds AngularJS expression value to an HTML element.

=> It is an alternative to interpolation `{{ }}`.

```html
<div ng-app="" ng-init="subject='Advanced Web Programming'">
  <p ng-bind="subject"></p>
</div>
```

### **Difference Between `ng-bind` and `{{ }}`**

| `ng-bind` | `{{ }}` |
|---|---|
| Written as an attribute | Written inside HTML content |
| Avoids display of raw expression before AngularJS loads | Raw expression may appear for a moment |
| Useful for cleaner output | Easy and commonly used |

### **5. `ng-repeat` Directive**

=> `ng-repeat` repeats an HTML element for every item in an array or object.

=> It is commonly used to display lists and tables.

```html
<!DOCTYPE html>
<html ng-app="app">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="StudentCtrl">
  <h3>Student List</h3>

  <ul>
    <li ng-repeat="s in students">
      {{s.rollno}} - {{s.name}} - {{s.branch}}
    </li>
  </ul>

  <script>
  var app = angular.module("app", []);

  app.controller("StudentCtrl", function($scope) {
    $scope.students = [
      { rollno: 1, name: "Aman", branch: "CE" },
      { rollno: 2, name: "Riya", branch: "IT" },
      { rollno: 3, name: "Neha", branch: "CE" }
    ];
  });
  </script>
</body>
</html>
```

### **6. `ng-click` Directive**

=> `ng-click` executes an AngularJS expression or function when an element is clicked.

```html
<div ng-app="app" ng-controller="CounterCtrl">
  <button ng-click="count = count + 1">Click</button>
  <p>Total Clicks: {{count}}</p>
</div>

<script>
var app = angular.module("app", []);

app.controller("CounterCtrl", function($scope) {
  $scope.count = 0;
});
</script>
```

### **7. `ng-show`, `ng-hide` and `ng-if`**

=> These directives are used to control visibility of HTML elements.

| Directive | Meaning |
|---|---|
| `ng-show` | Shows element if condition is true |
| `ng-hide` | Hides element if condition is true |
| `ng-if` | Adds or removes element from DOM based on condition |

```html
<div ng-app="">
  <input type="checkbox" ng-model="showDetails"> Show Details

  <p ng-show="showDetails">This paragraph is visible using ng-show.</p>
  <p ng-if="showDetails">This paragraph is created using ng-if.</p>
</div>
```

### **Difference Between `ng-show` and `ng-if`**

| `ng-show` | `ng-if` |
|---|---|
| Element remains in DOM | Element is added or removed from DOM |
| Uses CSS display property | Creates or destroys the element |
| Faster for frequent show/hide | Better when element is not always needed |

### **8. `ng-class` Directive**

=> `ng-class` applies CSS class dynamically based on a condition.

```html
<!DOCTYPE html>
<html ng-app="">
<head>
  <style>
    .pass { color: green; font-weight: bold; }
    .fail { color: red; font-weight: bold; }
  </style>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-init="marks=72">
  <p ng-class="marks >= 35 ? 'pass' : 'fail'">
    Result: {{marks >= 35 ? 'Pass' : 'Fail'}}
  </p>
</body>
</html>
```

### **9. `ng-options` Directive**

=> `ng-options` is used to create dropdown options from an array.

```html
<div ng-app="app" ng-controller="CityCtrl">
  <select ng-model="selectedCity" ng-options="city for city in cities">
  </select>

  <p>Selected City: {{selectedCity}}</p>
</div>

<script>
var app = angular.module("app", []);

app.controller("CityCtrl", function($scope) {
  $scope.cities = ["Ahmedabad", "Surat", "Rajkot", "Vadodara"];
});
</script>
```

## **3.1.2 Custom Directives**

=> A **custom directive** is a user-defined directive created by a developer.

=> It is used to create reusable HTML components and custom behavior.

### **Syntax**

```js
app.directive("directiveName", function() {
  return {
    template: "HTML content"
  };
});
```

### **Important Naming Rule**

=> In JavaScript, directive name is written in camelCase.

=> In HTML, directive name is written using hyphen-separated form.

| JavaScript Name | HTML Name |
|---|---|
| `studentCard` | `student-card` |
| `myHeader` | `my-header` |

### **Custom Directive Example**

```html
<!DOCTYPE html>
<html ng-app="app">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body>
  <student-card></student-card>

  <script>
  var app = angular.module("app", []);

  app.directive("studentCard", function() {
    return {
      template: "<h3>Student Name: Aman</h3><p>Branch: Computer Engineering</p>"
    };
  });
  </script>
</body>
</html>
```

### **Directive Restriction**

=> The `restrict` property defines how a directive can be used.

| Restrict Value | Meaning | Example |
|---|---|---|
| `E` | Element directive | `<student-card></student-card>` |
| `A` | Attribute directive | `<div student-card></div>` |
| `C` | Class directive | `<div class="student-card"></div>` |
| `M` | Comment directive | `<!-- directive: student-card -->` |

### **Custom Directive with Restrict**

```html
<div student-info></div>

<script>
var app = angular.module("app", []);

app.directive("studentInfo", function() {
  return {
    restrict: "A",
    template: "<b>Student information loaded using attribute directive.</b>"
  };
});
</script>
```

### **Advantages of Custom Directives**

1. Makes code reusable.
2. Reduces repeated HTML.
3. Creates custom HTML tags.
4. Keeps page structure clean.
5. Helps in component-based development.

---

## **3.2 Modules**

=> **Module** is a container for different parts of an AngularJS application.

=> It contains controllers, services, filters, directives and configuration.

=> Every AngularJS application should have at least one module.

### **Definition**

=> AngularJS module is a collection of application components that organizes code into a single application unit.

### **Syntax**

```js
var app = angular.module("appName", []);
```

=> `"appName"` is the module name.

=> `[]` is the dependency array.

=> If the application depends on other modules, their names are written inside this array.

### **Simple Module Example**

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="StudentCtrl">
  <h3>{{title}}</h3>
  <p>Name: {{studentName}}</p>

  <script>
  var app = angular.module("studentApp", []);

  app.controller("StudentCtrl", function($scope) {
    $scope.title = "Student Application";
    $scope.studentName = "Aman";
  });
  </script>
</body>
</html>
```

### **Explanation**

=> `studentApp` is the module name.

=> `ng-app="studentApp"` connects the HTML page with the module.

=> `StudentCtrl` is registered inside the module.

=> `$scope` stores data used by the view.

### **Creating and Retrieving a Module**

```js
// Creates a new module
var app = angular.module("myApp", []);

// Retrieves an existing module
var sameApp = angular.module("myApp");
```

=> While creating a module, dependency array `[]` is required.

=> While retrieving an existing module, dependency array is not written.

### **Module with Dependency**

```js
var app = angular.module("myApp", ["ngRoute"]);
```

=> Here `myApp` depends on the `ngRoute` module for routing.

### **Parts of a Module**

| Part | Purpose |
|---|---|
| Controller | Handles data and logic for view |
| Service | Provides reusable logic or data |
| Directive | Adds custom behavior to HTML |
| Filter | Formats data before displaying |
| Config block | Configures routes and providers |
| Run block | Runs code after module is loaded |

### **Controller Inside Module**

```js
app.controller("HomeCtrl", function($scope) {
  $scope.message = "Welcome to AngularJS";
});
```

### **Service Inside Module**

```js
app.service("StudentService", function() {
  this.getName = function() {
    return "Aman";
  };
});
```

### **Using Service in Controller**

```js
app.controller("StudentCtrl", function($scope, StudentService) {
  $scope.name = StudentService.getName();
});
```

### **Config Block**

=> `config()` is used to configure providers before the application starts.

=> Routing is commonly written inside the config block.

```js
app.config(function($routeProvider) {
  $routeProvider.when("/", {
    templateUrl: "home.html",
    controller: "HomeCtrl"
  });
});
```

### **Run Block**

=> `run()` executes after the injector is created and the application starts.

```js
app.run(function($rootScope) {
  $rootScope.appTitle = "Student Portal";
});
```

### **Advantages of Modules**

1. Organizes application code.
2. Supports separation of concerns.
3. Makes application easier to maintain.
4. Supports dependency injection.
5. Allows reusable components.
6. Makes testing easier.

### **Important Exam Point**

=> Module is the starting point of an AngularJS application. Without a module, controllers, routes, services and directives cannot be organized properly in a large application.

---

## **3.3 Routes**

=> **Routing** is used to create single page applications in AngularJS.

=> Routing loads different views inside the same page without refreshing the entire page.

=> AngularJS routing is commonly implemented using the `ngRoute` module.

### **Definition**

=> Route is a mapping between a URL path and a view/template that should be displayed for that path.

### **Why Routing is Used**

1. To create single page applications.
2. To navigate between pages without full page reload.
3. To load different views dynamically.
4. To maintain browser history.
5. To make application faster and smoother.

### **Important Routing Terms**

| Term | Meaning |
|---|---|
| `ngRoute` | AngularJS module used for routing |
| `$routeProvider` | Service used to define routes |
| `ng-view` | Placeholder where routed template is displayed |
| `templateUrl` | Path of HTML template |
| `controller` | Controller used for a route |
| `$routeParams` | Service used to read route parameters |
| `otherwise()` | Defines default route |

### **Required Scripts**

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular-route.min.js"></script>
```

### **Basic Route Example**

```html
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular-route.min.js"></script>
</head>
<body>
  <a href="#!/">Home</a>
  <a href="#!/about">About</a>
  <a href="#!/contact">Contact</a>

  <hr>
  <div ng-view></div>

  <script>
  var app = angular.module("myApp", ["ngRoute"]);

  app.config(function($routeProvider) {
    $routeProvider
      .when("/", {
        template: "<h3>Home Page</h3><p>Welcome to home page.</p>"
      })
      .when("/about", {
        template: "<h3>About Page</h3><p>This is about page.</p>"
      })
      .when("/contact", {
        template: "<h3>Contact Page</h3><p>Email: info@example.com</p>"
      })
      .otherwise({
        redirectTo: "/"
      });
  });
  </script>
</body>
</html>
```

### **Explanation**

=> `ngRoute` is added as module dependency.

=> `$routeProvider.when()` defines routes.

=> `ng-view` displays the selected route content.

=> `href="#!/about"` changes route without full page reload.

=> `otherwise()` redirects invalid routes.

### **Routing with Template and Controller**

```js
var app = angular.module("myApp", ["ngRoute"]);

app.config(function($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "views/home.html",
      controller: "HomeCtrl"
    })
    .when("/students", {
      templateUrl: "views/students.html",
      controller: "StudentCtrl"
    })
    .otherwise({
      redirectTo: "/"
    });
});

app.controller("HomeCtrl", function($scope) {
  $scope.message = "Welcome to Student Portal";
});

app.controller("StudentCtrl", function($scope) {
  $scope.students = ["Aman", "Riya", "Neha"];
});
```

### **Route Parameter Example**

=> Route parameters are used to pass values in the URL.

```js
app.config(function($routeProvider) {
  $routeProvider.when("/student/:id", {
    template: "<h3>Student ID: {{id}}</h3>",
    controller: "StudentDetailCtrl"
  });
});

app.controller("StudentDetailCtrl", function($scope, $routeParams) {
  $scope.id = $routeParams.id;
});
```

### **HTML Link**

```html
<a href="#!/student/101">View Student 101</a>
```

### **Advantages of Routing**

1. Creates SPA behavior.
2. Reduces page reload.
3. Improves user experience.
4. Maintains browser navigation.
5. Separates application into multiple views.

### **Limitations of Routing**

1. Requires JavaScript to work.
2. Initial setup is more complex than normal links.
3. Search engine optimization may need extra configuration.
4. Wrong route configuration can show blank view.

---

## **3.4 AngularJS Forms and Validations**

=> AngularJS provides built-in support for form handling and validation.

=> It tracks the state of forms and input controls.

=> It can check whether form data is valid, invalid, touched, untouched, changed or unchanged.

### **Definition**

=> AngularJS form validation is the process of checking user input using built-in validation directives and form states before submitting data.

### **Common Form Directives**

| Directive | Use |
|---|---|
| `ng-model` | Binds form input with model |
| `ng-submit` | Handles form submission |
| `ng-required` | Makes field required dynamically |
| `ng-minlength` | Sets minimum length |
| `ng-maxlength` | Sets maximum length |
| `ng-pattern` | Validates value using regular expression |
| `ng-disabled` | Disables button/control |
| `ng-change` | Executes expression when value changes |

### **HTML5 Validation Attributes Used in AngularJS**

| Attribute | Use |
|---|---|
| `required` | Field must not be empty |
| `type="email"` | Checks email format |
| `type="number"` | Allows number input |
| `min` | Minimum numeric value |
| `max` | Maximum numeric value |
| `pattern` | Regular expression validation |

### **Form States**

| State | Meaning |
|---|---|
| `$valid` | Form/control has valid data |
| `$invalid` | Form/control has invalid data |
| `$pristine` | User has not changed the value |
| `$dirty` | User has changed the value |
| `$touched` | User has focused and left the field |
| `$untouched` | User has not left the field |
| `$submitted` | Form has been submitted |

### **Validation CSS Classes**

=> AngularJS automatically adds CSS classes to form controls.

| Class | Meaning |
|---|---|
| `ng-valid` | Input is valid |
| `ng-invalid` | Input is invalid |
| `ng-pristine` | Input is not modified |
| `ng-dirty` | Input is modified |
| `ng-touched` | Input is touched |
| `ng-untouched` | Input is not touched |

### **Simple Form Validation Example**

```html
<!DOCTYPE html>
<html ng-app="app">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <style>
    input.ng-invalid.ng-touched {
      border: 2px solid red;
    }

    input.ng-valid.ng-touched {
      border: 2px solid green;
    }

    .error {
      color: red;
    }
  </style>
</head>
<body ng-controller="RegisterCtrl">
  <h3>Registration Form</h3>

  <form name="regForm" ng-submit="submitForm()" novalidate>
    <p>
      Name:
      <input type="text" name="name" ng-model="user.name" required>
      <span class="error" ng-show="regForm.name.$touched && regForm.name.$invalid">
        Name is required
      </span>
    </p>

    <p>
      Email:
      <input type="email" name="email" ng-model="user.email" required>
      <span class="error" ng-show="regForm.email.$touched && regForm.email.$invalid">
        Enter valid email
      </span>
    </p>

    <p>
      Password:
      <input type="password" name="password" ng-model="user.password" ng-minlength="6" required>
      <span class="error" ng-show="regForm.password.$touched && regForm.password.$error.required">
        Password is required
      </span>
      <span class="error" ng-show="regForm.password.$error.minlength">
        Minimum 6 characters required
      </span>
    </p>

    <button type="submit" ng-disabled="regForm.$invalid">Register</button>
  </form>

  <p>{{message}}</p>

  <script>
  var app = angular.module("app", []);

  app.controller("RegisterCtrl", function($scope) {
    $scope.user = {};

    $scope.submitForm = function() {
      if ($scope.regForm.$valid) {
        $scope.message = "Registration successful for " + $scope.user.name;
      }
    };
  });
  </script>
</body>
</html>
```

### **Explanation**

=> `novalidate` disables browser default validation and allows AngularJS validation to work clearly.

=> `name="regForm"` gives a name to the form object.

=> `regForm.name.$invalid` checks whether name input is invalid.

=> `regForm.email.$touched` checks whether user has visited the email field.

=> `ng-disabled="regForm.$invalid"` disables submit button until the form is valid.

### **Validation Using Pattern**

```html
<form name="mobileForm" ng-app="">
  Mobile:
  <input type="text"
         name="mobile"
         ng-model="mobile"
         ng-pattern="/^[0-9]{10}$/"
         required>

  <span ng-show="mobileForm.mobile.$error.pattern">
    Enter 10 digit mobile number
  </span>
</form>
```

### **Advantages of AngularJS Form Validation**

1. Reduces manual JavaScript validation code.
2. Provides built-in form states.
3. Supports real-time validation.
4. Easy to display custom error messages.
5. Can disable submit button until form is valid.
6. Works well with two-way data binding.

### **Important Exam Point**

=> For form validation questions, always mention `ng-model`, form states like `$valid` and `$invalid`, validation directives, error messages, and `novalidate`.

---

## **3.5 Data Binding**

=> **Data binding** is the process of connecting application data with the HTML view.

=> In AngularJS, data binding automatically synchronizes data between model and view.

### **Definition**

=> Data binding is a technique in which changes in model data are automatically reflected in the view, and user changes in the view can update the model.

### **Types of Data Binding**

| Type | Meaning | Example |
|---|---|---|
| One-way data binding | Data flows from model to view | `{{message}}`, `ng-bind` |
| Two-way data binding | Data flows between model and view | `ng-model` |

### **One-way Data Binding**

=> One-way data binding displays model data in the view.

=> If model changes, view is updated.

```html
<div ng-app="app" ng-controller="MsgCtrl">
  <h3>{{message}}</h3>
  <p ng-bind="subject"></p>
</div>

<script>
var app = angular.module("app", []);

app.controller("MsgCtrl", function($scope) {
  $scope.message = "Welcome to AngularJS";
  $scope.subject = "Advanced Web Programming";
});
</script>
```

### **Two-way Data Binding**

=> Two-way data binding means model and view update each other automatically.

=> When user changes input value, the model changes.

=> When model changes, the view also changes.

```html
<!DOCTYPE html>
<html ng-app="">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body>
  Name:
  <input type="text" ng-model="name">

  <p>Hello {{name}}</p>
</body>
</html>
```

### **Data Binding with Object**

```html
<div ng-app="app" ng-controller="StudentCtrl">
  <input type="text" ng-model="student.name">
  <input type="text" ng-model="student.branch">

  <p>Name: {{student.name}}</p>
  <p>Branch: {{student.branch}}</p>
</div>

<script>
var app = angular.module("app", []);

app.controller("StudentCtrl", function($scope) {
  $scope.student = {
    name: "Aman",
    branch: "CE"
  };
});
</script>
```

### **Data Binding with Table**

```html
<div ng-app="app" ng-controller="StudentCtrl">
  Search:
  <input type="text" ng-model="searchText">

  <table border="1">
    <tr>
      <th>Roll No</th>
      <th>Name</th>
      <th>Branch</th>
    </tr>
    <tr ng-repeat="s in students | filter:searchText">
      <td>{{s.rollno}}</td>
      <td>{{s.name}}</td>
      <td>{{s.branch}}</td>
    </tr>
  </table>
</div>

<script>
var app = angular.module("app", []);

app.controller("StudentCtrl", function($scope) {
  $scope.students = [
    { rollno: 1, name: "Aman", branch: "CE" },
    { rollno: 2, name: "Riya", branch: "IT" },
    { rollno: 3, name: "Neha", branch: "CE" }
  ];
});
</script>
```

### **How Data Binding Works**

=> AngularJS maintains a scope object.

=> View reads values from the scope.

=> Directives like `ng-model` update the scope.

=> AngularJS digest cycle checks for changes and updates the view.

### **Advantages of Data Binding**

1. Reduces DOM manipulation code.
2. Saves development time.
3. Keeps model and view synchronized.
4. Makes form handling easier.
5. Improves readability of code.

### **Limitations of Data Binding**

1. Too many bindings can reduce performance in very large applications.
2. Debugging may be difficult for beginners.
3. Application depends on JavaScript.

### **One-way vs Two-way Data Binding**

| One-way Data Binding | Two-way Data Binding |
|---|---|
| Data flows from model to view | Data flows both ways |
| Used for displaying data | Used for forms and inputs |
| Example: `{{title}}` | Example: `ng-model="name"` |
| Simple and fast | More dynamic and interactive |

---

## **3.6 Creating Single Page Website using AngularJS**

=> A **Single Page Application (SPA)** is a web application that loads a single HTML page and dynamically updates content without reloading the full page.

=> AngularJS is useful for creating SPA because it provides routing, templates, controllers, services and data binding.

### **Definition**

=> Single Page Website or Single Page Application is an application where different views are loaded into the same main page according to route changes.

### **Features of SPA**

1. Only one main HTML page is loaded.
2. Different content is loaded dynamically.
3. Page does not reload completely during navigation.
4. Routing is used for navigation.
5. User experience is faster and smoother.
6. Backend APIs can be used to load data.

### **Normal Website vs Single Page Website**

| Normal Website | Single Page Website |
|---|---|
| Every page request reloads full page | Main page loads once |
| Navigation is slower | Navigation is faster |
| Server sends complete HTML pages | Client loads views dynamically |
| Simple to build | Needs routing and JavaScript |
| Good for static sites | Good for dynamic applications |

### **Steps to Create SPA in AngularJS**

1. Create main `index.html` file.
2. Add AngularJS and AngularJS route library.
3. Create AngularJS module with `ngRoute` dependency.
4. Define routes using `$routeProvider`.
5. Add navigation links using hash route.
6. Add `<div ng-view></div>` as route placeholder.
7. Create HTML templates for different views.
8. Create controllers for views.
9. Run the application using a local server.

### **SPA Project Structure**

```text
student-spa/
  index.html
  app.js
  views/
    home.html
    students.html
    about.html
```

### **File 1: `index.html`**

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<head>
  <title>Student SPA</title>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular-route.min.js"></script>
  <script src="app.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    nav a {
      margin-right: 15px;
      text-decoration: none;
      color: blue;
    }

    table {
      border-collapse: collapse;
      width: 60%;
    }

    th, td {
      border: 1px solid black;
      padding: 8px;
    }
  </style>
</head>
<body>
  <h2>Student Portal</h2>

  <nav>
    <a href="#!/">Home</a>
    <a href="#!/students">Students</a>
    <a href="#!/about">About</a>
  </nav>

  <hr>

  <div ng-view></div>
</body>
</html>
```

### **File 2: `app.js`**

```js
var app = angular.module("studentApp", ["ngRoute"]);

app.config(function($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "views/home.html",
      controller: "HomeCtrl"
    })
    .when("/students", {
      templateUrl: "views/students.html",
      controller: "StudentCtrl"
    })
    .when("/about", {
      templateUrl: "views/about.html",
      controller: "AboutCtrl"
    })
    .otherwise({
      redirectTo: "/"
    });
});

app.controller("HomeCtrl", function($scope) {
  $scope.message = "Welcome to Student Portal";
});

app.controller("StudentCtrl", function($scope) {
  $scope.students = [
    { rollno: 1, name: "Aman", branch: "CE" },
    { rollno: 2, name: "Riya", branch: "IT" },
    { rollno: 3, name: "Neha", branch: "CE" }
  ];
});

app.controller("AboutCtrl", function($scope) {
  $scope.info = "This SPA is created using AngularJS routing.";
});
```

### **File 3: `views/home.html`**

```html
<h3>Home</h3>
<p>{{message}}</p>
```

### **File 4: `views/students.html`**

```html
<h3>Students</h3>

Search:
<input type="text" ng-model="searchText">

<br><br>

<table>
  <tr>
    <th>Roll No</th>
    <th>Name</th>
    <th>Branch</th>
  </tr>
  <tr ng-repeat="s in students | filter:searchText">
    <td>{{s.rollno}}</td>
    <td>{{s.name}}</td>
    <td>{{s.branch}}</td>
  </tr>
</table>
```

### **File 5: `views/about.html`**

```html
<h3>About</h3>
<p>{{info}}</p>
```

### **Explanation of SPA Example**

=> `index.html` is the main page.

=> `ng-view` is the placeholder where route templates are loaded.

=> `app.js` defines module, routes and controllers.

=> `views/home.html`, `views/students.html` and `views/about.html` are partial views.

=> Navigation links use `#!` route format.

=> When user clicks Students, AngularJS loads `students.html` without refreshing the whole page.

### **Important Notes for Practical Exam**

1. Always include `angular-route.min.js` for routing.
2. Add `"ngRoute"` in module dependency array.
3. Use `$routeProvider` inside `app.config()`.
4. Use `<div ng-view></div>` in `index.html`.
5. Use `templateUrl` for external view files.
6. Use a local server because `templateUrl` may not work properly by directly opening file in browser.

### **Advantages of SPA**

1. Fast navigation.
2. Better user experience.
3. Less server load after first page load.
4. Reusable templates and controllers.
5. Suitable for dashboard and web applications.

### **Disadvantages of SPA**

1. Initial load can be heavier.
2. Depends on JavaScript.
3. SEO requires extra care.
4. Browser history and routing need proper configuration.
5. Security must be handled carefully because client-side code is visible.

---

## **3.7 Important Definitions**

### **Directive**

=> Directive is a special AngularJS attribute or element used to extend HTML and attach dynamic behavior.

### **Module**

=> Module is a container for controllers, services, directives, filters and configuration of an AngularJS application.

### **Routing**

=> Routing is a technique used to load different views inside a single page based on URL path.

### **`ngRoute`**

=> `ngRoute` is an AngularJS module that provides routing functionality.

### **`ng-view`**

=> `ng-view` is a directive that works as a placeholder for routed templates.

### **`$routeProvider`**

=> `$routeProvider` is used to define route configuration in AngularJS.

### **Form Validation**

=> Form validation is the process of checking whether user input satisfies required rules before submission.

### **Data Binding**

=> Data binding connects model data with the HTML view and keeps them synchronized.

### **One-way Binding**

=> One-way binding displays model data in the view.

### **Two-way Binding**

=> Two-way binding updates model and view automatically when either side changes.

### **Single Page Application**

=> SPA is a web application that loads one main page and dynamically changes content without full page reload.

### **Exam-Oriented Important Points**

1. AngularJS directives extend HTML.
2. `ng-model` is used for two-way data binding.
3. `ng-repeat` is used to display arrays and lists.
4. AngularJS module is created using `angular.module()`.
5. Routing requires `ngRoute` module.
6. `ng-view` displays routed templates.
7. `$routeProvider.when()` defines route paths.
8. AngularJS forms provide states such as `$valid`, `$invalid`, `$dirty` and `$touched`.
9. `novalidate` is used to disable browser validation.
10. SPA improves navigation by avoiding full page reload.

---

## **3.8 Exam Short Questions with Answers**

### **Q1. Define directive in AngularJS.**

=> Directive is a special AngularJS marker or attribute used to extend HTML behavior.

=> Directives usually start with `ng-`, such as `ng-app`, `ng-model` and `ng-repeat`.

=> They are used for data binding, event handling, validation, repetition and DOM control.

### **Q2. List any five built-in AngularJS directives.**

=> Built-in AngularJS directives include:

1. `ng-app`
2. `ng-model`
3. `ng-bind`
4. `ng-repeat`
5. `ng-click`
6. `ng-show`
7. `ng-if`

=> These directives add dynamic behavior to HTML.

### **Q3. Explain `ng-app` directive.**

=> `ng-app` initializes an AngularJS application.

=> It defines the root element where AngularJS starts working.

```html
<html ng-app="studentApp">
```

=> If a module name is given, AngularJS loads that module.

### **Q4. Explain `ng-model` directive with example.**

=> `ng-model` binds form input with AngularJS model data.

=> It supports two-way data binding.

```html
<input ng-model="name">
<p>Hello {{name}}</p>
```

=> When user types in input, `name` is updated automatically.

### **Q5. Explain `ng-repeat` directive with example.**

=> `ng-repeat` repeats an HTML element for every item in a collection.

```html
<li ng-repeat="s in students">{{s.name}}</li>
```

=> It is commonly used to display arrays, lists and table rows dynamically.

### **Q6. Differentiate `ng-show` and `ng-if`.**

| `ng-show` | `ng-if` |
|---|---|
| Shows/hides element using CSS | Adds/removes element from DOM |
| Element remains in DOM | Element is destroyed when false |
| Faster for frequent toggling | Better for conditional creation |

### **Q7. What is custom directive?**

=> Custom directive is a user-defined directive created by developer.

=> It is used to create reusable HTML components or custom behavior.

=> Example: `student-card` directive can display common student information in many places.

### **Q8. Write syntax for creating custom directive.**

```js
app.directive("studentCard", function() {
  return {
    template: "<h3>Student Card</h3>"
  };
});
```

=> In JavaScript directive name is camelCase, while in HTML it is used as `student-card`.

### **Q9. What is module in AngularJS?**

=> Module is a container for AngularJS application components.

=> It contains controllers, services, filters, directives and configuration.

=> It helps organize code in a clean and maintainable way.

### **Q10. Write syntax of AngularJS module.**

```js
var app = angular.module("myApp", []);
```

=> `myApp` is module name.

=> `[]` is dependency array. Dependencies like `"ngRoute"` are added inside this array.

### **Q11. What is dependency array in module?**

=> Dependency array lists other AngularJS modules required by the application.

```js
var app = angular.module("myApp", ["ngRoute"]);
```

=> Here `ngRoute` is required for routing.

=> Empty array `[]` means module has no dependency.

### **Q12. What is config block?**

=> `config()` block is used to configure AngularJS application before it starts.

=> It is commonly used for route configuration.

```js
app.config(function($routeProvider) {
  // route configuration
});
```

### **Q13. What is run block?**

=> `run()` block executes after AngularJS application starts.

=> It is used for initialization code required after module loading.

```js
app.run(function($rootScope) {
  $rootScope.appTitle = "Student Portal";
});
```

### **Q14. Define routing in AngularJS.**

=> Routing is a technique used to load different views in the same page based on URL.

=> It is used to create single page applications.

=> AngularJS routing uses `ngRoute`, `$routeProvider` and `ng-view`.

### **Q15. What is `ngRoute`?**

=> `ngRoute` is an AngularJS module that provides routing support.

=> It allows an application to map URLs with templates and controllers.

=> It must be included in module dependencies before using routes.

### **Q16. What is `$routeProvider`?**

=> `$routeProvider` is used to define routes in AngularJS.

=> It maps a URL path with template and controller.

```js
$routeProvider.when("/home", {
  templateUrl: "home.html",
  controller: "HomeCtrl"
});
```

### **Q17. What is `ng-view`?**

=> `ng-view` is a placeholder directive where routed templates are displayed.

```html
<div ng-view></div>
```

=> When route changes, AngularJS loads the selected view inside `ng-view`.

### **Q18. Write steps to implement routing in AngularJS.**

1. Add AngularJS and `angular-route.min.js`.
2. Create module with `["ngRoute"]`.
3. Configure routes using `$routeProvider`.
4. Add navigation links using `#!`.
5. Add `<div ng-view></div>` in main page.
6. Create templates and controllers.

### **Q19. What is route parameter?**

=> Route parameter is a value passed through URL route.

```js
$routeProvider.when("/student/:id", {
  templateUrl: "student.html"
});
```

=> It can be accessed using `$routeParams.id`.

### **Q20. Define AngularJS form validation.**

=> AngularJS form validation checks user input before submission.

=> It uses directives like `required`, `ng-minlength`, `ng-pattern` and validation states.

=> It helps display error messages and disable invalid form submission.

### **Q21. List AngularJS form states.**

=> Important form states are:

1. `$valid`
2. `$invalid`
3. `$pristine`
4. `$dirty`
5. `$touched`
6. `$untouched`
7. `$submitted`

=> These states help check input status.

### **Q22. What is `$valid` and `$invalid`?**

=> `$valid` is true when form or input satisfies all validation rules.

=> `$invalid` is true when form or input fails any validation rule.

=> They are commonly used to enable or disable submit button.

### **Q23. What is `$dirty` and `$pristine`?**

=> `$pristine` means user has not changed the input value.

=> `$dirty` means user has changed the input value.

=> These states are useful for showing validation messages only after user interaction.

### **Q24. Why is `novalidate` used?**

=> `novalidate` disables browser default HTML validation.

=> It allows AngularJS validation messages and states to work clearly.

```html
<form name="regForm" novalidate>
```

=> It is commonly used in AngularJS forms.

### **Q25. Explain validation using `ng-pattern`.**

=> `ng-pattern` validates input using a regular expression.

```html
<input name="mobile" ng-model="mobile" ng-pattern="/^[0-9]{10}$/">
```

=> This example accepts only 10-digit mobile number.

### **Q26. Define data binding.**

=> Data binding connects application data with HTML view.

=> In AngularJS, it automatically synchronizes model and view.

=> It reduces manual DOM update code.

### **Q27. Differentiate one-way and two-way data binding.**

| One-way Binding | Two-way Binding |
|---|---|
| Data flows from model to view | Data flows both ways |
| Used for display | Used for input forms |
| Example: `{{title}}` | Example: `ng-model="name"` |

### **Q28. Explain two-way data binding with example.**

=> Two-way binding updates model when view changes and updates view when model changes.

```html
<input ng-model="city">
<p>{{city}}</p>
```

=> When user types city name, paragraph updates automatically.

### **Q29. What is SPA?**

=> SPA stands for **Single Page Application**.

=> It loads one main HTML page and dynamically changes content without full page reload.

=> AngularJS creates SPA using routing, templates, controllers and `ng-view`.

### **Q30. State advantages of SPA.**

=> Advantages of SPA are:

1. Fast navigation.
2. Better user experience.
3. Less full-page reload.
4. Reusable templates.
5. Suitable for dashboards and dynamic applications.

### **Q31. State disadvantages of SPA.**

=> Disadvantages of SPA are:

1. Depends on JavaScript.
2. Initial loading can be heavy.
3. SEO requires extra care.
4. Routing must be configured properly.
5. Security needs careful handling.

### **Q32. Write file structure for AngularJS SPA.**

```text
student-spa/
  index.html
  app.js
  views/
    home.html
    students.html
    about.html
```

=> `index.html` is main page, `app.js` contains routes and controllers, and `views` stores templates.

### **Q33. Explain how `templateUrl` is used.**

=> `templateUrl` specifies the path of external HTML template for a route.

```js
$routeProvider.when("/about", {
  templateUrl: "views/about.html"
});
```

=> AngularJS loads this template inside `ng-view`.

### **Q34. Explain use of controller in route.**

=> Controller in route handles data and logic for that specific view.

```js
.when("/students", {
  templateUrl: "students.html",
  controller: "StudentCtrl"
})
```

=> When route opens, `StudentCtrl` supplies data to `students.html`.

### **Q35. Write a short note on AngularJS forms.**

=> AngularJS forms provide two-way binding and built-in validation.

=> They track input states such as `$valid`, `$invalid`, `$dirty` and `$touched`.

=> They help display custom error messages and prevent invalid form submission.
