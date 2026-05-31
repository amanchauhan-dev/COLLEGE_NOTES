# Summer 2026 - Advanced Web Programming Predicted Paper Solutions

## Q.1 (a) Describe CSS Selectors with examples. Difference between class and ID selectors. [03]

=> **CSS selector** is used to select one or more HTML elements and apply style rules to them.

### Common CSS selectors

| Selector | Example | Explanation |
|---|---|---|
| Element selector | `p { color: blue; }` | Selects all `<p>` elements |
| Class selector | `.box { padding: 10px; }` | Selects all elements having `class="box"` |
| ID selector | `#header { background: gray; }` | Selects the element having `id="header"` |
| Universal selector | `* { margin: 0; }` | Selects all elements |
| Attribute selector | `input[type="text"] { border: 1px solid black; }` | Selects elements using attribute |
| Group selector | `h1, p { color: green; }` | Applies same style to multiple selectors |

```html
<style>
p { color: blue; }
.highlight { background: yellow; }
#mainTitle { color: red; }
</style>

<h1 id="mainTitle">AWP</h1>
<p class="highlight">CSS Selector Example</p>
```

### Class selector vs ID selector

| Class selector | ID selector |
|---|---|
| Written with dot `.` | Written with hash `#` |
| Can be used by many elements | Should be unique on a page |
| Example: `.box` | Example: `#header` |
| Used for reusable styling | Used for one specific element |

## Q.1 (b) Explain asynchronous programming in JavaScript. What is AJAX? Role of `XMLHttpRequest`. [04]

=> **Asynchronous programming** allows JavaScript to start a task and continue executing the next statements without waiting for that task to complete.

=> It is useful for slow operations such as API calls, file loading, timers and server communication.

```js
console.log("Start");

setTimeout(function() {
  console.log("This runs after 2 seconds");
}, 2000);

console.log("End");
```

=> Output will be `Start`, `End`, then `This runs after 2 seconds`.

### AJAX

=> **AJAX** stands for **Asynchronous JavaScript and XML**.

=> It is used to send and receive data from a server without refreshing the whole web page.

### Role of `XMLHttpRequest`

=> `XMLHttpRequest` is a browser object used to make AJAX requests.

=> It can send HTTP requests such as GET and POST and receive server response asynchronously.

```js
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    document.getElementById("result").innerHTML = this.responseText;
  }
};
xhttp.open("GET", "data.txt", true);
xhttp.send();
```

=> `readyState === 4` means request is completed and `status === 200` means request is successful.

## Q.1 (c) What is DOM? Explain DOM Tree and DOM methods with example. [07]

=> **DOM** stands for **Document Object Model**.

=> It represents an HTML document as a tree of objects. JavaScript uses DOM to access, modify, add or delete HTML elements dynamically.

### DOM tree structure

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

=> In DOM tree, every tag is a node. The `document` object is the root object. Elements, attributes and text are represented as nodes.

### Common DOM methods

| Method | Use |
|---|---|
| `getElementById()` | Selects element by id |
| `getElementsByClassName()` | Selects elements by class |
| `getElementsByTagName()` | Selects elements by tag name |
| `querySelector()` | Selects first matching CSS selector |
| `querySelectorAll()` | Selects all matching CSS selectors |
| `createElement()` | Creates a new HTML element |
| `appendChild()` | Adds child element |

### Example

```html
<!DOCTYPE html>
<html>
<body>
  <h2 id="title">Old Heading</h2>
  <p class="msg">Old paragraph</p>
  <button onclick="changeData()">Change</button>

  <script>
  function changeData() {
    document.getElementById("title").innerHTML = "New Heading";
    document.querySelector(".msg").style.color = "blue";

    let p = document.createElement("p");
    p.innerHTML = "New paragraph added using DOM";
    document.body.appendChild(p);
  }
  </script>
</body>
</html>
```

=> In this example, heading content is changed, paragraph style is modified and a new paragraph is added dynamically.

## Q.2 (a) What is AngularJS? Features and advantages over plain JavaScript. [03]

=> **AngularJS** is an open-source JavaScript framework used to build dynamic web applications and single page applications.

### Features

1. **Two-way data binding**: Keeps model and view synchronized.
2. **MVC architecture**: Separates data, view and logic.
3. **Directives**: Extends HTML using attributes like `ng-model`, `ng-repeat`.
4. **Services**: Provides reusable logic such as `$http`, `$timeout`.
5. **Dependency injection**: Supplies required services automatically.

### Advantages over plain JavaScript

=> AngularJS reduces manual DOM manipulation, provides ready-made validation, supports routing and organizes code better than plain JavaScript.

## Q.2 (b) Explain MVC Architecture in AngularJS with example. [04]

=> **MVC** stands for **Model View Controller**.

1. **Model** stores application data.
2. **View** displays data to the user.
3. **Controller** connects model and view and contains application logic.

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<body ng-controller="StudentCtrl">
  <h3>{{title}}</h3>
  Name: <input ng-model="student.name">
  <p>Welcome {{student.name}}</p>

  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <script>
  var app = angular.module("studentApp", []);
  app.controller("StudentCtrl", function($scope) {
    $scope.title = "Student Application";
    $scope.student = { name: "Aman" };
  });
  </script>
</body>
</html>
```

=> Here `student` object is the model, HTML is the view and `StudentCtrl` is the controller.

## Q.2 (c) Bootstrap student form with AngularJS display and email validation. [07]

```html
<!DOCTYPE html>
<html ng-app="studentApp">
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>
<body ng-controller="StudentCtrl" class="p-4">
<div class="container">
  <h3>Student Form</h3>

  <input class="form-control mb-2" ng-model="student.enroll" placeholder="Enrollment No.">
  <input class="form-control mb-2" ng-model="student.name" placeholder="Name">
  <input class="form-control mb-2" ng-model="student.sem" placeholder="Semester">
  <input class="form-control mb-2" ng-model="student.branch" placeholder="Branch">
  <input class="form-control mb-2" ng-model="student.mobile" placeholder="Mobile Number">
  <input class="form-control mb-2" id="email" ng-model="student.email" placeholder="Email">
  <textarea class="form-control mb-2" ng-model="student.address" placeholder="Address"></textarea>

  <button class="btn btn-primary" ng-click="validateEmail()">Submit</button>
  <p class="text-danger mt-2">{{error}}</p>

  <h3 class="mt-4">Student Details</h3>
  <table class="table table-bordered">
    <tr><th>Enrollment</th><td>{{student.enroll}}</td></tr>
    <tr><th>Name</th><td>{{student.name}}</td></tr>
    <tr><th>Semester</th><td>{{student.sem}}</td></tr>
    <tr><th>Branch</th><td>{{student.branch}}</td></tr>
    <tr><th>Mobile</th><td>{{student.mobile}}</td></tr>
    <tr><th>Email</th><td>{{student.email}}</td></tr>
    <tr><th>Address</th><td>{{student.address}}</td></tr>
  </table>
</div>

<script>
var app = angular.module("studentApp", []);
app.controller("StudentCtrl", function($scope) {
  $scope.student = {};
  $scope.validateEmail = function() {
    var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!pattern.test($scope.student.email || "")) {
      $scope.error = "Invalid email address";
    } else {
      $scope.error = "Email is valid";
    }
  };
});
</script>
</body>
</html>
```

=> Bootstrap provides form styling, `ng-model` stores input data and AngularJS expressions display data on the page. JavaScript regular expression validates email format.

## Q.2 (c OR) Read Customer data from `Customers.php` using `$http`. [07]

```html
<!DOCTYPE html>
<html ng-app="customerApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <style>
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #333; padding: 8px; }
    th { background: #e5e5e5; }
    tr:nth-child(even) { background: #f7f7f7; }
  </style>
</head>
<body ng-controller="CustomerCtrl">
  <h3>Customer Details</h3>
  <table>
    <tr>
      <th>ID</th><th>Name</th><th>City</th><th>Email</th><th>Mobile</th>
    </tr>
    <tr ng-repeat="c in customers">
      <td>{{c.id}}</td>
      <td>{{c.name}}</td>
      <td>{{c.city}}</td>
      <td>{{c.email}}</td>
      <td>{{c.mobile}}</td>
    </tr>
  </table>

  <script>
  var app = angular.module("customerApp", []);
  app.controller("CustomerCtrl", function($scope, $http) {
    $http.get("Customers.php").then(function(response) {
      $scope.customers = response.data;
    }, function(error) {
      alert("Unable to load customer data");
    });
  });
  </script>
</body>
</html>
```

=> `$http.get()` sends an asynchronous request to `Customers.php`. The JSON response is stored in `$scope.customers` and displayed using `ng-repeat`.

## Q.3 (a) Define Directive in AngularJS. Explain `ng-hide`, `ng-show`, `ng-click`, `ng-repeat`. [03]

=> **Directive** is a special AngularJS attribute used to extend HTML behavior.

| Directive | Use | Example |
|---|---|---|
| `ng-hide` | Hides element when expression is true | `<p ng-hide="flag">Hidden</p>` |
| `ng-show` | Shows element when expression is true | `<p ng-show="flag">Shown</p>` |
| `ng-click` | Executes expression on click | `<button ng-click="count=count+1">Click</button>` |
| `ng-repeat` | Repeats HTML for each item | `<li ng-repeat="s in students">{{s}}</li>` |

```html
<div ng-app="" ng-init="show=true; students=['Aman','Ravi']; count=0">
  <button ng-click="show=!show">Toggle</button>
  <p ng-show="show">Visible text</p>
  <p ng-hide="show">Hidden text is now visible</p>
  <button ng-click="count=count+1">Count {{count}}</button>
  <ul><li ng-repeat="s in students">{{s}}</li></ul>
</div>
```

## Q.3 (b) Explain AngularJS Form Validation and field states. [04]

=> AngularJS provides built-in form validation using directives like `required`, `type="email"`, `ng-minlength` and `ng-maxlength`.

### Form field states

| State | Meaning |
|---|---|
| `$pristine` | Field/form has not been changed by user |
| `$dirty` | Field/form has been changed by user |
| `$valid` | Field/form satisfies all validation rules |
| `$invalid` | Field/form fails one or more validation rules |
| `$touched` | Field has lost focus after user visited it |
| `$untouched` | Field has not lost focus yet |

```html
<form name="myForm" ng-app="">
  <input name="email" type="email" ng-model="email" required>

  <p ng-show="myForm.email.$touched && myForm.email.$invalid">
    Please enter a valid email.
  </p>
  <p>Valid: {{myForm.email.$valid}}</p>
  <p>Dirty: {{myForm.email.$dirty}}</p>
</form>
```

=> These states help display validation messages only when required.

## Q.3 (c) Explain AngularJS Routing with example using `ng-route`. [07]

=> Routing is used in AngularJS to create **Single Page Applications**. It loads different views in the same page without full page refresh.

### Main parts

1. `ngRoute` module provides routing support.
2. `$routeProvider` defines route configuration.
3. `ng-view` displays selected route template.
4. Links use `#!` route paths.

```html
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular-route.js"></script>
</head>
<body>
  <a href="#!/">Home</a>
  <a href="#!/about">About</a>

  <div ng-view></div>

  <script>
  var app = angular.module("myApp", ["ngRoute"]);

  app.config(function($routeProvider) {
    $routeProvider
      .when("/", {
        template: "<h2>Home Page</h2><p>Welcome to home page.</p>"
      })
      .when("/about", {
        template: "<h2>About Page</h2><p>This is about page.</p>"
      })
      .otherwise({
        redirectTo: "/"
      });
  });
  </script>
</body>
</html>
```

=> When user clicks Home or About, AngularJS changes only the view inside `ng-view`.

## Q.3 (a OR) Node JS code to print current directory files. [03]

```js
const fs = require("fs");

fs.readdir(".", function(err, files) {
  if (err) {
    console.log("Error:", err.message);
    return;
  }

  files.forEach(function(file) {
    console.log(file);
  });
});
```

=> `fs.readdir()` reads all file and folder names from the given directory.

## Q.3 (b OR) What is NPM? Install, upgrade and uninstall modules. [04]

=> **NPM** stands for **Node Package Manager**.

=> It is used to install, update, remove and manage reusable Node JS packages.

```bash
npm init -y
npm install express
npm install nodemon --save-dev
npm update express
npm uninstall express
npm list
```

### Explanation

1. `npm init -y` creates `package.json`.
2. `npm install express` installs Express package.
3. `--save-dev` installs package as development dependency.
4. `npm update` upgrades package.
5. `npm uninstall` removes package.

## Q.3 (c OR) Read query string values from URL in Node JS. [07]

```js
const http = require("http");
const url = require("url");

http.createServer(function(req, res) {
  const parsedUrl = url.parse(req.url, true);
  const query = parsedUrl.query;

  res.writeHead(200, {"Content-Type": "text/html"});
  res.write("<h3>Query String Values</h3>");
  res.write("Name: " + query.Name + "<br>");
  res.write("Mobile: " + query.Mobile);
  res.end();
}).listen(8081, function() {
  console.log("Server running at http://localhost:8081");
});
```

=> Open `http://localhost:8081?Name=GTU&Mobile=9876543210`.

=> `url.parse(req.url, true)` converts query string into an object so values can be accessed using `query.Name` and `query.Mobile`.

## Q.4 (a) Explain Callbacks in Node JS. What is error-first callback? [03]

=> **Callback** is a function passed as an argument to another function and executed later after an operation completes.

```js
function greet(name, callback) {
  callback("Hello " + name);
}

greet("GTU", function(message) {
  console.log(message);
});
```

=> **Error-first callback** is a Node JS convention where the first callback parameter is `err` and second parameter is result/data.

```js
const fs = require("fs");
fs.readFile("data.txt", "utf8", function(err, data) {
  if (err) {
    console.log("Error:", err.message);
    return;
  }
  console.log(data);
});
```

## Q.4 (b) Explain EventEmitter class and any three methods. [04]

=> `EventEmitter` is a class from Node JS `events` module. It is used to create and handle custom events.

### Important methods

| Method | Explanation |
|---|---|
| `on()` | Registers an event listener |
| `emit()` | Triggers an event |
| `once()` | Registers listener that runs only once |
| `removeListener()` | Removes a listener |

```js
const EventEmitter = require("events");
const event = new EventEmitter();

function orderHandler(id) {
  console.log("Order received:", id);
}

event.on("order", orderHandler);
event.once("start", function() {
  console.log("Application started");
});

event.emit("start");
event.emit("start");
event.emit("order", 101);

event.removeListener("order", orderHandler);
```

=> `start` event runs only once because `once()` is used. `order` event runs when `emit("order")` is called.

## Q.4 (c) File System methods and Node JS file operation application. [07]

=> Node JS `fs` module is used to perform file and directory operations.

### Common `fs` methods

| Method | Use |
|---|---|
| `fs.writeFile()` | Creates a file or replaces file content |
| `fs.appendFile()` | Adds data at the end of a file |
| `fs.readFile()` | Reads file content |
| `fs.unlink()` | Deletes a file |
| `fs.rename()` | Renames file |
| `fs.mkdir()` | Creates directory |
| `fs.readdir()` | Reads directory content |

### Program

```js
const fs = require("fs");

// 1. Create and write data into a file
fs.writeFile("student.txt", "Name: Aman\nBranch: CE", function(err) {
  if (err) throw err;
  console.log("File created and data written");

  // 2. Read content from file
  fs.readFile("student.txt", "utf8", function(err, data) {
    if (err) throw err;
    console.log("File content:\n" + data);

    // 3. Write more data into file
    fs.appendFile("student.txt", "\nSemester: 6", function(err) {
      if (err) throw err;
      console.log("Data appended");

      // 4. Delete file
      fs.unlink("student.txt", function(err) {
        if (err) throw err;
        console.log("File deleted");
      });
    });
  });
});
```

=> This program performs create, read, write/append and delete operations using asynchronous `fs` methods.

## Q.4 (a OR) Explain error handling in Node JS with example. [03]

=> Error handling is used to manage runtime errors and prevent application crash.

### Ways to handle errors

1. `try...catch` for synchronous code.
2. Error-first callbacks for asynchronous code.
3. `.catch()` for promises.

```js
try {
  let result = JSON.parse("{invalid json}");
  console.log(result);
} catch (err) {
  console.log("Invalid JSON:", err.message);
}
```

```js
const fs = require("fs");
fs.readFile("missing.txt", "utf8", function(err, data) {
  if (err) {
    console.log("File error:", err.message);
    return;
  }
  console.log(data);
});
```

## Q.4 (b OR) Timers in Node JS. [04]

=> Timer functions are global functions used to schedule code execution.

### `setTimeout()`

=> Executes code once after a specified delay.

```js
setTimeout(function() {
  console.log("Executed after 2 seconds");
}, 2000);
```

### `setInterval()`

=> Executes code repeatedly after a fixed interval.

```js
let count = 0;
let id = setInterval(function() {
  count++;
  console.log("Count:", count);
  if (count === 3) clearInterval(id);
}, 1000);
```

### `setImmediate()`

=> Executes code after the current event loop phase.

```js
setImmediate(function() {
  console.log("Runs immediately after current operation");
});
```

## Q.4 (c OR) Explain Streams in Node JS and demonstrate piping. [07]

=> **Stream** is used to process data in chunks instead of loading full data into memory.

=> Streams are useful for large files, network communication and real-time data processing.

### Types of streams

| Type | Explanation |
|---|---|
| Readable | Used to read data, example `fs.createReadStream()` |
| Writable | Used to write data, example `fs.createWriteStream()` |
| Duplex | Can read and write both |
| Transform | Modifies data while reading/writing |

### Readable stream and piping example

```js
const fs = require("fs");

const readStream = fs.createReadStream("input.txt", "utf8");
const writeStream = fs.createWriteStream("output.txt");

readStream.on("data", function(chunk) {
  console.log("Chunk received:");
  console.log(chunk);
});

readStream.on("end", function() {
  console.log("Reading completed");
});

readStream.on("error", function(err) {
  console.log("Error:", err.message);
});

readStream.pipe(writeStream);
```

=> `pipe()` sends data from readable stream directly to writable stream. It is memory efficient because data is handled chunk by chunk.

## Q.5 (a) What is MongoDB? Advantages and basic features. [03]

=> **MongoDB** is a NoSQL document-oriented database. It stores data in BSON format, which is similar to JSON.

### Advantages

1. Flexible schema.
2. Fast read/write performance.
3. Supports nested documents.
4. Easy horizontal scaling.
5. Good for modern web applications.

### Basic features

1. **Collection** stores documents.
2. **Document** stores data as key-value pairs.
3. **Indexing** improves search performance.
4. **Replication** improves availability.
5. **Sharding** distributes data across servers.

## Q.5 (b) NoSQL vs Relational database and MongoDB data models. [04]

### NoSQL vs Relational database

| NoSQL Database | Relational Database |
|---|---|
| Stores data as documents, key-value, graph or column | Stores data in tables |
| Flexible schema | Fixed schema |
| Good for unstructured/semi-structured data | Good for structured data |
| Horizontally scalable | Usually vertically scalable |
| Example: MongoDB | Example: MySQL |

### MongoDB data models

1. **Embedded data model**

=> Related data is stored inside the same document.

```js
{
  name: "Aman",
  address: { city: "Ahmedabad", pincode: 380001 }
}
```

=> It is useful when related data is commonly read together.

2. **Referenced data model**

=> Related data is stored in separate collections and connected using ids.

```js
// students
{ _id: 1, name: "Aman", branchId: 10 }

// branches
{ _id: 10, name: "CE" }
```

=> It reduces duplication and is useful for large or shared related data.

## Q.5 (c) Node JS MongoDB operations on `GTU.Students`. [07]

```js
const { MongoClient } = require("mongodb");

async function main() {
  const client = new MongoClient("mongodb://127.0.0.1:27017");

  try {
    await client.connect();
    const db = client.db("GTU");
    const students = db.collection("Students");

    // 1. Insert multiple student documents
    await students.insertMany([
      {
        enrollmentNo: "101",
        name: "Aman",
        age: 21,
        branch: "CE",
        course: "AWP"
      },
      {
        enrollmentNo: "102",
        name: "Ravi",
        age: 22,
        branch: "IT",
        course: "MAD"
      },
      {
        enrollmentNo: "103",
        name: "Neha",
        age: 20,
        branch: "CE",
        course: "CNS"
      }
    ]);
    console.log("Students inserted");

    // 2. Find all students belonging to CE branch
    const ceStudents = await students.find({ branch: "CE" }).toArray();
    console.log("CE Students:", ceStudents);

    // 3. Update course of a specific student
    const updatedStudent = await students.findOneAndUpdate(
      { enrollmentNo: "103" },
      { $set: { course: "AWP" } },
      { returnDocument: "after" }
    );
    console.log("Updated student:", updatedStudent);

    // 4. Delete a student record
    await students.deleteOne({ enrollmentNo: "102" });
    console.log("Student deleted");
  } catch (err) {
    console.log("Error:", err.message);
  } finally {
    await client.close();
  }
}

main();
```

=> `insertMany()` inserts multiple documents, `find()` retrieves matching documents, `findOneAndUpdate()` updates one matched document and `deleteOne()` removes one matched document.

## Q.5 (a OR) Explain MongoDB data types with examples. [03]

=> MongoDB supports many data types to store different kinds of values.

| Data type | Example |
|---|---|
| String | `{ name: "Aman" }` |
| Number | `{ age: 21 }` |
| Boolean | `{ active: true }` |
| Array | `{ subjects: ["AWP", "MAD"] }` |
| Object/Document | `{ address: { city: "Surat" } }` |
| Date | `{ createdAt: new Date() }` |
| ObjectId | `{ _id: ObjectId("...") }` |
| Null | `{ middleName: null }` |

=> BSON data types allow MongoDB to store nested and flexible records.

## Q.5 (b OR) Explain Sort, Find and Query with conditions using Node JS and MongoDB. [04]

=> MongoDB provides methods to search, filter and arrange documents.

### Find

```js
const result = await employees.find({}).toArray();
```

=> `find({})` returns all documents from collection.

### Query with conditions

```js
const highSalary = await employees.find({ salary: { $gt: 50000 } }).toArray();
const ceEmployees = await employees.find({ department: "CE" }).toArray();
```

=> Conditions use operators such as `$gt`, `$lt`, `$gte`, `$lte`, `$eq`, `$ne`.

### Sort

```js
const sorted = await employees.find({}).sort({ salary: -1 }).toArray();
```

=> `1` means ascending order and `-1` means descending order.

## Q.5 (c OR) CRUD operations on Employee collection using MongoDB. [07]

```js
const { MongoClient } = require("mongodb");

async function main() {
  const client = new MongoClient("mongodb://127.0.0.1:27017");

  try {
    await client.connect();
    const db = client.db("Company");
    const employees = db.collection("Employee");

    // 1. insertOne() - insert a new employee
    await employees.insertOne({
      emp_id: 1,
      name: "Raj",
      department: "IT",
      salary: 45000
    });
    console.log("Employee inserted");

    // 2. find() - display all employees
    const allEmployees = await employees.find({}).toArray();
    console.log("All employees:", allEmployees);

    // 3. findOneAndUpdate() - update salary
    const updated = await employees.findOneAndUpdate(
      { emp_id: 1 },
      { $set: { salary: 55000 } },
      { returnDocument: "after" }
    );
    console.log("Updated employee:", updated);

    // 4. deleteMany() - delete all employees from department
    await employees.deleteMany({ department: "IT" });
    console.log("Employees deleted from IT department");
  } catch (err) {
    console.log("Error:", err.message);
  } finally {
    await client.close();
  }
}

main();
```

=> This program covers all CRUD operations: create using `insertOne()`, read using `find()`, update using `findOneAndUpdate()` and delete using `deleteMany()`.
