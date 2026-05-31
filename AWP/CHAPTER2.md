# **Chapter 2: Introduction to AngularJS**

## **Table of Contents**

2.1 Basics of AngularJS  
2.2 Features  
2.3 Advantages and Disadvantages  
2.4 Application Structure  
2.5 MVC with AngularJS  
2.6 Basics of Routes and Navigation  
2.7 Expression  
2.8 Controller  
2.9 Scope  
2.10 Services  

---

## **2.1 Basics of AngularJS**

=> **AngularJS** is an open-source JavaScript framework used to develop dynamic web applications and single page applications.

=> AngularJS extends HTML by using special attributes called **directives**.

=> It is mainly used for client-side development, form handling, data binding, validation, routing and dynamic page updates.

### **Why AngularJS is used**

1. To create dynamic web applications.
2. To reduce manual DOM manipulation.
3. To bind data between model and view.
4. To create single page applications.
5. To organize code using MVC architecture.

### **Adding AngularJS**

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
```

### **Simple AngularJS Example**

```html
<!DOCTYPE html>
<html ng-app="">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body>
  <h3>AngularJS Basic Example</h3>

  Enter Name:
  <input type="text" ng-model="name">

  <p>Hello {{name}}</p>
</body>
</html>
```

### **Explanation**

=> `ng-app` initializes AngularJS application.

=> `ng-model="name"` binds input value with the model variable `name`.

=> `{{name}}` displays the value of model variable.

### **Important AngularJS Terms**

| Term | Meaning |
|---|---|
| Directive | Special AngularJS attribute such as `ng-app`, `ng-model` |
| Model | Application data |
| View | HTML page shown to user |
| Controller | JavaScript function that controls data and logic |
| Scope | Object that connects controller and view |
| Service | Reusable object/function for common logic |

## **2.2 Features**

=> AngularJS provides many features that make web application development easier.

### **1. Two-way Data Binding**

=> Two-way data binding automatically synchronizes data between model and view.

```html
<div ng-app="">
  <input ng-model="city">
  <p>City: {{city}}</p>
</div>
```

=> When user changes input, the displayed value changes automatically.

### **2. MVC Architecture**

=> AngularJS supports Model View Controller architecture.

=> This separates application data, user interface and logic.

### **3. Directives**

=> Directives extend HTML functionality.

```html
<p ng-bind="message"></p>
<button ng-click="count = count + 1">Click</button>
<li ng-repeat="s in students">{{s}}</li>
```

### **4. Dependency Injection**

=> AngularJS automatically provides required services to controllers.

```js
app.controller("MyCtrl", function($scope, $http) {
  // $scope and $http are injected by AngularJS
});
```

### **5. Services**

=> Services are reusable objects used to share logic.

=> Examples: `$http`, `$timeout`, `$interval`, `$location`.

### **6. Filters**

=> Filters format data before displaying it.

```html
<p>{{"angular js" | uppercase}}</p>
<p>{{250 | currency}}</p>
```

### **7. Routing**

=> Routing is used to create single page applications by loading different views without full page reload.

### **8. Form Validation**

=> AngularJS provides built-in validation states like `$valid`, `$invalid`, `$dirty`, `$touched`.

```html
<form name="f" ng-app="">
  <input name="email" type="email" ng-model="email" required>
  <span ng-show="f.email.$invalid">Invalid Email</span>
</form>
```

## **2.3 Advantages and Disadvantages**

### **Advantages of AngularJS**

1. **Easy data binding**

=> Two-way data binding reduces manual DOM update code.

2. **MVC support**

=> MVC makes application code organized and maintainable.

3. **Less DOM manipulation**

=> AngularJS updates DOM automatically based on model changes.

4. **Reusable components**

=> Directives and services can be reused.

5. **Form validation**

=> AngularJS provides validation states and validation directives.

6. **Single Page Application support**

=> Routing helps create SPA navigation.

7. **Dependency injection**

=> Makes code easier to test and maintain.

### **Disadvantages of AngularJS**

1. **Learning curve**

=> Concepts like scope, services, directives and dependency injection require practice.

2. **Performance issue in large apps**

=> Too many watchers can slow down the application.

3. **JavaScript dependency**

=> If JavaScript is disabled, AngularJS application will not work.

4. **SEO issue in older SPA**

=> Single page applications may need extra SEO handling.

5. **Not ideal for very complex modern apps**

=> Newer frameworks are often preferred for large modern applications.

### **Comparison Table**

| Advantages | Disadvantages |
|---|---|
| Two-way binding | Learning curve |
| MVC support | Performance issue in large apps |
| Reusable services/directives | Depends on JavaScript |
| Built-in validation | SEO needs extra work |
| SPA support | Older framework |

## **2.4 Application Structure**

=> AngularJS application is commonly divided into modules, controllers, views, services and routes.

### **Basic Structure**

```text
angular-app/
  index.html
  app.js
  controllers/
    studentController.js
  services/
    studentService.js
  views/
    home.html
    about.html
```

### **Parts of AngularJS Application**

| Part | Purpose |
|---|---|
| `index.html` | Main HTML file |
| Module | Main container of app |
| Controller | Handles view logic |
| Service | Reusable business logic |
| View | HTML template |
| Route | Defines navigation |

### **Simple Application Structure Example**

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="StudentCtrl">
  <h3>{{title}}</h3>
  <p>Name: {{student.name}}</p>
  <p>Branch: {{student.branch}}</p>

  <script>
  var app = angular.module("studentApp", []);

  app.controller("StudentCtrl", function($scope) {
    $scope.title = "Student Application";
    $scope.student = {
      name: "Aman",
      branch: "CE"
    };
  });
  </script>
</body>
</html>
```

### **Explanation**

=> `studentApp` is the module.

=> `StudentCtrl` is the controller.

=> `$scope.student` is the model data.

=> HTML page is the view.

## **2.5 MVC with AngularJS**

=> **MVC** stands for **Model View Controller**.

=> It separates an application into three parts.

| Part | Meaning | AngularJS Example |
|---|---|---|
| Model | Stores data | `$scope.student` |
| View | Displays UI | HTML page |
| Controller | Handles logic | `StudentCtrl` |

### **MVC Flow**

```text
User interacts with View
        |
Controller handles logic
        |
Model data changes
        |
View updates automatically
```

### **AngularJS MVC Example**

```html
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="MyCtrl">
  <h3>{{heading}}</h3>

  Name: <input ng-model="student.name"><br>
  Semester: <input ng-model="student.sem"><br>

  <p>Student Name: {{student.name}}</p>
  <p>Semester: {{student.sem}}</p>

  <button ng-click="show()">Show Message</button>
  <p>{{message}}</p>

  <script>
  var app = angular.module("myApp", []);

  app.controller("MyCtrl", function($scope) {
    $scope.heading = "MVC with AngularJS";

    $scope.student = {
      name: "Aman",
      sem: 6
    };

    $scope.show = function() {
      $scope.message = "Welcome " + $scope.student.name;
    };
  });
  </script>
</body>
</html>
```

### **Explanation**

=> `student` object is the model.

=> HTML controls and paragraphs are the view.

=> `MyCtrl` is the controller.

=> `ng-model` provides two-way binding between model and view.

### **Benefits of MVC**

1. Code becomes organized.
2. Maintenance becomes easier.
3. View and logic are separated.
4. Testing becomes easier.
5. Same model can be used by multiple views.

## **2.6 Basics of Routes and Navigation**

=> Routing is used to navigate between different views without refreshing the full page.

=> AngularJS uses `ngRoute` module for routing.

### **Requirements**

1. AngularJS library.
2. `angular-route.js`.
3. Module dependency `ngRoute`.
4. `$routeProvider` configuration.
5. `ng-view` directive.

### **Routing Example**

```html
<!DOCTYPE html>
<html ng-app="routeApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular-route.js"></script>
</head>
<body>
  <h2>AngularJS Routing</h2>

  <a href="#!/">Home</a> |
  <a href="#!/about">About</a> |
  <a href="#!/contact">Contact</a>

  <hr>
  <div ng-view></div>

  <script>
  var app = angular.module("routeApp", ["ngRoute"]);

  app.config(function($routeProvider) {
    $routeProvider
      .when("/", {
        template: "<h3>Home Page</h3><p>Welcome to home page.</p>"
      })
      .when("/about", {
        template: "<h3>About Page</h3><p>This is about page.</p>"
      })
      .when("/contact", {
        template: "<h3>Contact Page</h3><p>Email: test@example.com</p>"
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

=> `ngRoute` enables routing.

=> `$routeProvider.when()` defines route paths.

=> `ng-view` displays selected route template.

=> `otherwise()` redirects invalid routes to default page.

### **Advantages of Routing**

1. Creates single page application.
2. Avoids full page reload.
3. Improves user experience.
4. Keeps navigation organized.

## **2.7 Expression**

=> AngularJS expressions are used to bind data to HTML.

=> They are written inside double curly braces `{{ }}`.

```html
<p>{{10 + 20}}</p>
<p>{{firstName + " " + lastName}}</p>
```

### **Expression Example**

```html
<!DOCTYPE html>
<html ng-app="">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-init="firstName='Aman'; lastName='Patel'; marks=80">
  <p>Full Name: {{firstName + " " + lastName}}</p>
  <p>Marks: {{marks}}</p>
  <p>Result: {{marks >= 35 ? "Pass" : "Fail"}}</p>
</body>
</html>
```

### **AngularJS Expressions vs JavaScript Expressions**

| AngularJS Expression | JavaScript Expression |
|---|---|
| Written in `{{ }}` | Written in JS code |
| Evaluated against Angular scope | Evaluated in JS scope |
| Used mainly for binding | Used for full logic |
| Handles undefined safely | May throw error |
| Does not support loops directly | Supports loops and conditions |

### **Important Points**

=> Expressions should be simple.

=> Complex logic should be written in controller.

=> Expressions can use numbers, strings, objects and arrays.

## **2.8 Controller**

=> Controller is a JavaScript function that controls data and behavior of a view.

=> It is connected to HTML using the `ng-controller` directive.

### **Uses of Controller**

1. Initializes model data.
2. Defines functions for view.
3. Handles user events.
4. Connects model and view.
5. Keeps view logic organized.

### **Controller Example**

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="StudentCtrl">
  <h3>{{title}}</h3>

  Name: <input ng-model="student.name"><br>
  Branch: <input ng-model="student.branch"><br>

  <button ng-click="display()">Display</button>
  <p>{{message}}</p>

  <script>
  var app = angular.module("studentApp", []);

  app.controller("StudentCtrl", function($scope) {
    $scope.title = "Controller Example";

    $scope.student = {
      name: "Aman",
      branch: "CE"
    };

    $scope.display = function() {
      $scope.message =
        "Name: " + $scope.student.name + ", Branch: " + $scope.student.branch;
    };
  });
  </script>
</body>
</html>
```

### **Explanation**

=> `StudentCtrl` controls the HTML section.

=> `$scope.title`, `$scope.student` and `$scope.message` are available in view.

=> `display()` function executes when button is clicked.

## **2.9 Scope**

=> **Scope** is an object that connects controller and view in AngularJS.

=> `$scope` stores variables and functions that can be used in the HTML view.

### **Scope Example**

```html
<!DOCTYPE html>
<html ng-app="app">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="MyCtrl">
  <h3>{{appName}}</h3>
  <p>{{message}}</p>
  <button ng-click="changeMessage()">Change</button>

  <script>
  var app = angular.module("app", []);

  app.controller("MyCtrl", function($scope) {
    $scope.appName = "Scope Example";
    $scope.message = "Old Message";

    $scope.changeMessage = function() {
      $scope.message = "New Message";
    };
  });
  </script>
</body>
</html>
```

### **Types of Scope**

1. **`$scope`**

=> Local scope for a controller.

2. **`$rootScope`**

=> Top-level scope available throughout the application.

### **`$rootScope` Example**

```html
<div ng-app="app" ng-controller="Ctrl">
  <h3>{{appTitle}}</h3>
  <p>{{message}}</p>
</div>

<script>
var app = angular.module("app", []);

app.run(function($rootScope) {
  $rootScope.appTitle = "AWP Application";
});

app.controller("Ctrl", function($scope) {
  $scope.message = "Controller Scope Message";
});
</script>
```

### **Important Points**

=> `$scope` is used for controller-specific data.

=> `$rootScope` is used for application-wide data.

=> Too much use of `$rootScope` should be avoided because it makes code harder to maintain.

## **2.10 Services**

=> Service is a reusable object or function used to share data and logic across the application.

=> Services are injected into controllers using dependency injection.

### **Common AngularJS Services**

| Service | Use |
|---|---|
| `$http` | Sends HTTP/AJAX requests |
| `$timeout` | Executes code after delay |
| `$interval` | Executes code repeatedly |
| `$location` | Works with browser URL |
| `$rootScope` | Stores application-level data |
| `$filter` | Applies filters in JavaScript |

### **`$timeout` Service Example**

```html
<!DOCTYPE html>
<html ng-app="app">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="Ctrl">
  <p>{{message}}</p>

  <script>
  var app = angular.module("app", []);

  app.controller("Ctrl", function($scope, $timeout) {
    $scope.message = "Please wait...";

    $timeout(function() {
      $scope.message = "Message changed after 2 seconds";
    }, 2000);
  });
  </script>
</body>
</html>
```

### **`$http` Service Example**

```html
<!DOCTYPE html>
<html ng-app="app">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="StudentCtrl">
  <table border="1">
    <tr>
      <th>Roll No</th>
      <th>Name</th>
      <th>Branch</th>
    </tr>
    <tr ng-repeat="s in students">
      <td>{{s.rollno}}</td>
      <td>{{s.name}}</td>
      <td>{{s.branch}}</td>
    </tr>
  </table>

  <script>
  var app = angular.module("app", []);

  app.controller("StudentCtrl", function($scope, $http) {
    $http.get("students.json").then(function(response) {
      $scope.students = response.data;
    }, function(error) {
      alert("Unable to load student data");
    });
  });
  </script>
</body>
</html>
```

### **Custom Service Example**

```html
<div ng-app="app" ng-controller="CalcCtrl">
  <p>Square: {{result}}</p>
</div>

<script>
var app = angular.module("app", []);

app.service("MathService", function() {
  this.square = function(n) {
    return n * n;
  };
});

app.controller("CalcCtrl", function($scope, MathService) {
  $scope.result = MathService.square(5);
});
</script>
```

### **Advantages of Services**

1. Code reusability.
2. Separation of business logic.
3. Easy sharing of data between controllers.
4. Cleaner controllers.
5. Easier testing and maintenance.

## **Exam Short Questions**

1. Define AngularJS.
2. List features of AngularJS.
3. State advantages of AngularJS.
4. Write disadvantages of AngularJS.
5. What is two-way data binding?
6. Define MVC.
7. Explain MVC with AngularJS.
8. What is AngularJS module?
9. Explain application structure of AngularJS.
10. What is routing in AngularJS?
11. What is `ngRoute`?
12. What is `ng-view`?
13. Define AngularJS expression.
14. Differentiate AngularJS expression and JavaScript expression.
15. What is controller?
16. What is `$scope`?
17. What is `$rootScope`?
18. What are AngularJS services?
19. Explain `$http` service.
20. Explain `$timeout` service.
