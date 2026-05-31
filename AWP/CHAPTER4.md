# **Chapter 4: Introduction to Node.js**

## **Table of Contents**

4.1 Introduction to Node.js  
4.2 Setup Node.js Environment  
4.3 Package Manager  
4.3.1 `package.json`  
4.3.2 Local and Global Packages  
4.4 Features of Node.js  
4.5 Console Object  
4.6 Concept of Callbacks  
4.7 Important Definitions  
4.8 Exam Short Questions  

---

## **4.1 Introduction to Node.js**

=> **Node.js** is an open-source, cross-platform JavaScript runtime environment.

=> It allows JavaScript code to run outside the browser.

=> Node.js is mainly used to develop server-side applications, REST APIs, real-time applications, command-line tools and backend services.

=> Node.js is built on the **Google Chrome V8 JavaScript engine**.

### **Definition**

=> Node.js is a JavaScript runtime environment that executes JavaScript code on the server side using the V8 engine.

### **Why Node.js is Used**

1. To create fast and scalable server-side applications.
2. To build REST APIs.
3. To develop real-time applications such as chat apps.
4. To handle many client requests efficiently.
5. To use JavaScript for both frontend and backend.
6. To create command-line tools.

### **Simple Node.js Program**

```js
console.log("Welcome to Node.js");
```

### **Running the Program**

```bash
node app.js
```

### **Output**

```text
Welcome to Node.js
```

### **Important Point for Exam**

=> Node.js is not a programming language and not a framework. It is a runtime environment for executing JavaScript outside the browser.

### **Node.js Architecture**

```text
Client Request
      |
      v
Node.js Application
      |
      v
Event Queue -> Event Loop -> Worker Threads / System Operations
      |
      v
Callback Response
```

=> Node.js uses an event-driven and non-blocking architecture.

=> It can handle multiple requests without creating a separate thread for every request.

### **Node.js vs Browser JavaScript**

| Browser JavaScript | Node.js |
|---|---|
| Runs inside web browser | Runs outside browser |
| Used for client-side scripting | Used for server-side scripting |
| Can access DOM | Cannot directly access DOM |
| Limited file system access | Can access file system using modules |
| Uses browser APIs | Uses Node.js APIs |

---

## **4.2 Setup Node.js Environment**

=> To write and run Node.js programs, Node.js must be installed on the system.

=> Node.js installation usually includes **Node runtime** and **npm**.

=> `npm` stands for **Node Package Manager**.

### **Steps to Setup Node.js**

1. Download Node.js from the official Node.js website.
2. Install the LTS version.
3. Open terminal or command prompt.
4. Check Node.js version.
5. Check npm version.
6. Create a JavaScript file.
7. Run the file using `node` command.

### **Check Node.js Version**

```bash
node -v
```

### **Check npm Version**

```bash
npm -v
```

### **Create First Program**

=> Create a file named `app.js`.

```js
console.log("My first Node.js program");
```

### **Run Program**

```bash
node app.js
```

### **Output**

```text
My first Node.js program
```

### **Node.js REPL**

=> **REPL** stands for **Read Eval Print Loop**.

=> It is an interactive shell where JavaScript code can be written and executed immediately.

### **Start REPL**

```bash
node
```

### **REPL Example**

```js
> 10 + 20
30
> "Node" + "JS"
'NodeJS'
```

### **Meaning of REPL**

| Term | Meaning |
|---|---|
| Read | Reads user input |
| Eval | Evaluates the input |
| Print | Prints the result |
| Loop | Repeats the process |

### **Creating a Simple HTTP Server**

```js
const http = require("http");

const server = http.createServer(function(req, res) {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Hello from Node.js server");
});

server.listen(3000, function() {
  console.log("Server running at http://localhost:3000");
});
```

### **Run Server**

```bash
node server.js
```

### **Explanation**

=> `require("http")` imports the built-in HTTP module.

=> `createServer()` creates a web server.

=> `req` represents client request.

=> `res` represents server response.

=> `listen(3000)` starts server on port number `3000`.

### **Common Setup Problems**

| Problem | Solution |
|---|---|
| `node` command not found | Reinstall Node.js or set PATH |
| `npm` command not found | Install Node.js with npm |
| Port already in use | Use another port number |
| File not found | Run command from correct folder |

---

## **4.3 Package Manager**

=> **Package manager** is a tool used to install, update, remove and manage reusable libraries or packages.

=> In Node.js, the most common package manager is **npm**.

=> npm is installed automatically with Node.js.

### **Definition**

=> npm is the default package manager for Node.js that helps developers install and manage external packages and project dependencies.

### **Why Package Manager is Used**

1. To install third-party libraries.
2. To manage project dependencies.
3. To share reusable code.
4. To run project scripts.
5. To maintain version information of packages.
6. To remove or update packages easily.

### **Important npm Commands**

| Command | Use |
|---|---|
| `npm init` | Creates `package.json` file |
| `npm init -y` | Creates `package.json` with default values |
| `npm install package-name` | Installs package locally |
| `npm install -g package-name` | Installs package globally |
| `npm uninstall package-name` | Removes package |
| `npm update package-name` | Updates package |
| `npm list` | Lists installed packages |
| `npm -v` | Shows npm version |
| `npm run script-name` | Runs script from `package.json` |

### **Example: Initialize Project**

```bash
mkdir node-demo
cd node-demo
npm init -y
```

=> This creates a `package.json` file.

### **Example: Install Package**

```bash
npm install express
```

=> This installs Express package in the current project.

### **Using Installed Package**

```js
const express = require("express");

const app = express();

app.get("/", function(req, res) {
  res.send("Express package is working");
});

app.listen(3000, function() {
  console.log("Server started on port 3000");
});
```

### **Important Files and Folders**

| Name | Meaning |
|---|---|
| `package.json` | Stores project metadata, dependencies and scripts |
| `package-lock.json` | Stores exact installed package versions |
| `node_modules` | Folder containing installed packages |

### **Important Point**

=> `node_modules` folder can become large. It is usually not manually edited.

---

## **4.3.1 `package.json`**

=> `package.json` is an important file in a Node.js project.

=> It stores project information such as name, version, description, scripts and dependencies.

### **Sample `package.json`**

```json
{
  "name": "student-api",
  "version": "1.0.0",
  "description": "Simple Node.js project",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

### **Explanation**

| Field | Meaning |
|---|---|
| `name` | Project name |
| `version` | Project version |
| `description` | Short project description |
| `main` | Entry point file |
| `scripts` | Commands that can be run using npm |
| `dependencies` | Packages required by the project |

### **Running Script**

```bash
npm start
```

=> `npm start` runs the command defined inside the `start` script.

### **Why `package.json` is Important**

1. It identifies the project.
2. It stores dependency list.
3. It defines scripts.
4. It helps recreate the project environment.
5. It is required before publishing a package.

---

## **4.3.2 Local and Global Packages**

=> npm packages can be installed locally or globally.

### **Local Package**

=> Local package is installed inside the current project.

```bash
npm install express
```

=> It is stored in the `node_modules` folder of the project.

### **Global Package**

=> Global package is installed at system level and can be used from anywhere in terminal.

```bash
npm install -g nodemon
```

### **Difference Between Local and Global Packages**

| Local Package | Global Package |
|---|---|
| Installed in current project | Installed system-wide |
| Used by project code | Used as command-line tool |
| Saved in project dependencies | Not usually saved in project dependencies |
| Example: `express` | Example: `nodemon` |

### **Development Dependency**

=> Development dependency is required only during development, not in production.

```bash
npm install nodemon --save-dev
```

### **Dependency vs Dev Dependency**

| Dependency | Dev Dependency |
|---|---|
| Required to run application | Required during development |
| Stored in `dependencies` | Stored in `devDependencies` |
| Example: `express` | Example: `nodemon`, testing tools |

---

## **4.4 Features of Node.js**

=> Node.js provides many features that make it useful for server-side development.

### **1. Asynchronous and Non-blocking**

=> Node.js does not wait for slow operations such as file reading or database query to complete.

=> It continues executing other tasks and handles the result later using callback, promise or async/await.

```js
const fs = require("fs");

fs.readFile("data.txt", "utf8", function(err, data) {
  if (err) {
    console.log("Error:", err);
    return;
  }

  console.log(data);
});

console.log("This line runs before file reading completes");
```

### **2. Event-driven Architecture**

=> Node.js works using events.

=> When an event occurs, the related callback function is executed.

```js
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("greet", function(name) {
  console.log("Hello " + name);
});

emitter.emit("greet", "Aman");
```

### **3. Single-threaded Event Loop**

=> Node.js uses a single main thread with an event loop.

=> The event loop helps Node.js handle many requests efficiently.

=> Time-consuming tasks are handled asynchronously.

### **4. Fast Execution**

=> Node.js uses the V8 JavaScript engine.

=> V8 compiles JavaScript into machine code, so execution is fast.

### **5. Cross-platform**

=> Node.js can run on Windows, Linux and macOS.

### **6. npm Ecosystem**

=> npm provides many open-source packages.

=> Developers can use existing packages instead of writing everything from scratch.

### **7. Scalable**

=> Node.js is suitable for applications with many simultaneous users, especially I/O-heavy applications.

### **8. Same Language for Frontend and Backend**

=> Developers can use JavaScript for both client-side and server-side development.

### **9. Built-in Modules**

=> Node.js provides built-in modules such as `http`, `fs`, `path`, `url`, `events` and `os`.

```js
const os = require("os");

console.log("Platform:", os.platform());
console.log("Free Memory:", os.freemem());
```

### **Features Summary**

| Feature | Explanation |
|---|---|
| Asynchronous | Executes slow tasks without blocking main flow |
| Event-driven | Uses events and callbacks |
| Fast | Uses V8 engine |
| Scalable | Handles many requests efficiently |
| Cross-platform | Runs on different operating systems |
| npm support | Provides many packages |
| Built-in modules | Provides ready modules for common tasks |

### **Advantages of Node.js**

1. Fast performance.
2. Handles many concurrent requests.
3. Good for real-time applications.
4. Large package ecosystem.
5. Uses JavaScript on server side.
6. Suitable for APIs and microservices.

### **Limitations of Node.js**

1. Not ideal for heavy CPU-intensive tasks.
2. Callback-based code can become complex if not managed properly.
3. Error handling must be done carefully.
4. Too many external packages can create security risks.

### **Best Use Cases of Node.js**

1. REST APIs.
2. Chat applications.
3. Streaming applications.
4. Real-time dashboards.
5. Command-line tools.
6. Single page application backend.

---

## **4.5 Console Object**

=> **Console object** in Node.js is used to print messages, errors, warnings and debugging information.

=> It is a global object, so it can be used without importing any module.

### **Definition**

=> Console object provides methods to display output on the terminal and helps in debugging Node.js programs.

### **Common Console Methods**

| Method | Use |
|---|---|
| `console.log()` | Prints normal output |
| `console.error()` | Prints error message |
| `console.warn()` | Prints warning message |
| `console.table()` | Prints data in table format |
| `console.time()` | Starts timer |
| `console.timeEnd()` | Ends timer and prints time |
| `console.clear()` | Clears console |
| `console.count()` | Counts number of times label is called |

### **`console.log()` Example**

```js
let name = "Aman";
let marks = 85;

console.log("Name:", name);
console.log("Marks:", marks);
```

### **Output**

```text
Name: Aman
Marks: 85
```

### **`console.error()` and `console.warn()` Example**

```js
console.warn("Warning: Low disk space");
console.error("Error: File not found");
```

### **`console.table()` Example**

```js
const students = [
  { rollno: 1, name: "Aman", branch: "CE" },
  { rollno: 2, name: "Riya", branch: "IT" }
];

console.table(students);
```

### **`console.time()` and `console.timeEnd()` Example**

```js
console.time("loopTime");

for (let i = 0; i < 100000; i++) {
  // loop for time measurement
}

console.timeEnd("loopTime");
```

### **`console.count()` Example**

```js
console.count("Login");
console.count("Login");
console.count("Logout");
console.count("Login");
```

### **Output**

```text
Login: 1
Login: 2
Logout: 1
Login: 3
```

### **Difference Between `console.log()` and `console.error()`**

| `console.log()` | `console.error()` |
|---|---|
| Used for normal messages | Used for error messages |
| Writes to standard output | Writes to standard error |
| Useful for general debugging | Useful for error debugging |

### **Important Exam Point**

=> Console object is mainly used during development and debugging. It should not be used as the only logging method in large production applications.

---

## **4.6 Concept of Callbacks**

=> **Callback** is a function passed as an argument to another function.

=> The callback function is executed after the completion of a task.

=> Callbacks are commonly used in asynchronous programming.

### **Definition**

=> Callback is a function that is passed to another function and is called later when an operation is completed.

### **Why Callbacks are Used**

1. To handle asynchronous operations.
2. To execute code after a task completes.
3. To avoid blocking program execution.
4. To handle file system, database and network operations.
5. To define custom behavior after a function finishes.

### **Simple Callback Example**

```js
function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

function sayBye() {
  console.log("Goodbye");
}

greet("Aman", sayBye);
```

### **Output**

```text
Hello Aman
Goodbye
```

### **Explanation**

=> `sayBye` is passed as a callback to `greet`.

=> After printing greeting message, `greet()` calls `callback()`.

### **Asynchronous Callback Example**

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

### **Explanation**

=> `setTimeout()` is asynchronous.

=> Node.js does not wait for 2 seconds before running the next line.

=> The callback runs after timer completes.

### **File Reading Callback Example**

```js
const fs = require("fs");

fs.readFile("student.txt", "utf8", function(err, data) {
  if (err) {
    console.log("Error reading file");
    return;
  }

  console.log("File Data:", data);
});

console.log("Reading file...");
```

### **Explanation**

=> `fs.readFile()` reads file asynchronously.

=> The callback receives `err` and `data`.

=> If error occurs, `err` contains error information.

=> If file is read successfully, `data` contains file content.

### **Error-first Callback**

=> Node.js commonly uses **error-first callback** pattern.

=> In this pattern, the first parameter of callback is error and the second parameter is result/data.

### **Syntax**

```js
function(err, data) {
  if (err) {
    // handle error
    return;
  }

  // use data
}
```

### **Example of Error-first Callback**

```js
const fs = require("fs");

fs.readFile("data.txt", "utf8", function(err, data) {
  if (err) {
    console.error("File error:", err.message);
    return;
  }

  console.log(data);
});
```

### **Synchronous vs Asynchronous Callback Behavior**

| Synchronous Code | Asynchronous Callback |
|---|---|
| Executes line by line | Executes later after task completes |
| Blocks next operation until complete | Does not block next operation |
| Simpler but slower for I/O tasks | Better for file, network and database tasks |

### **Callback Hell**

=> Callback hell means deeply nested callbacks that make code difficult to read and maintain.

### **Example of Callback Hell**

```js
loginUser("aman", function(user) {
  getProfile(user.id, function(profile) {
    getOrders(profile.id, function(orders) {
      console.log(orders);
    });
  });
});
```

### **Problems of Callback Hell**

1. Code becomes difficult to read.
2. Error handling becomes complex.
3. Maintenance becomes difficult.
4. Debugging becomes harder.

### **How to Avoid Callback Hell**

1. Use named functions.
2. Use Promises.
3. Use `async` and `await`.
4. Keep functions small.
5. Handle errors clearly.

### **Callback Hell Improved with Named Functions**

```js
function showOrders(orders) {
  console.log(orders);
}

function loadOrders(profile) {
  getOrders(profile.id, showOrders);
}

function loadProfile(user) {
  getProfile(user.id, loadOrders);
}

loginUser("aman", loadProfile);
```

### **Advantages of Callbacks**

1. Useful for asynchronous programming.
2. Helps execute code after task completion.
3. Prevents blocking for I/O operations.
4. Makes event handling possible.

### **Disadvantages of Callbacks**

1. Nested callbacks reduce readability.
2. Error handling can become difficult.
3. Callback hell may occur.
4. Program flow can be harder to understand.

### **Important Exam Point**

=> Callbacks are important in Node.js because Node.js uses asynchronous and event-driven programming. Many built-in functions such as `fs.readFile()` use callbacks.

---

## **4.7 Important Definitions**

### **Node.js**

=> Node.js is a JavaScript runtime environment used to execute JavaScript outside the browser.

### **V8 Engine**

=> V8 is Google Chrome's JavaScript engine that compiles JavaScript into machine code.

### **Runtime Environment**

=> Runtime environment provides the tools and libraries required to execute a program.

### **npm**

=> npm is the default package manager for Node.js.

### **Package**

=> Package is reusable code or library that can be installed in a Node.js project.

### **Dependency**

=> Dependency is a package required by an application to run properly.

### **`package.json`**

=> `package.json` is a file that stores project metadata, scripts and dependencies.

### **REPL**

=> REPL stands for Read Eval Print Loop and provides an interactive Node.js shell.

### **Module**

=> Module is a reusable block of code that can be imported into another file.

### **Callback**

=> Callback is a function passed as an argument to another function and executed later.

### **Error-first Callback**

=> Error-first callback is a Node.js callback pattern where the first parameter represents error and the second parameter represents result.

### **Callback Hell**

=> Callback hell is a situation where many nested callbacks make code difficult to read and maintain.

### **Console Object**

=> Console object provides methods such as `log()`, `error()`, `warn()` and `table()` to print output on terminal.

### **Event-driven**

=> Event-driven means program flow is controlled by events such as request, click, timer or file completion.

### **Non-blocking I/O**

=> Non-blocking I/O means Node.js does not wait for slow input/output operations to finish before executing the next code.

### **Exam-Oriented Important Points**

1. Node.js runs JavaScript outside the browser.
2. Node.js uses the V8 JavaScript engine.
3. Node.js is event-driven and non-blocking.
4. npm is used to manage packages.
5. `package.json` stores dependencies and scripts.
6. Local packages are installed inside the project.
7. Global packages are installed system-wide.
8. Console object is used for output and debugging.
9. Callback is a function passed to another function.
10. Node.js commonly uses error-first callback pattern.

---

## **4.8 Exam Short Questions**

1. Define Node.js.
2. Why is Node.js used?
3. Is Node.js a programming language? Explain.
4. What is V8 engine?
5. List features of Node.js.
6. Explain asynchronous and non-blocking nature of Node.js.
7. What is event-driven architecture?
8. Write steps to install and setup Node.js.
9. Write command to check Node.js version.
10. Write command to run a Node.js file.
11. What is REPL?
12. Explain REPL with example.
13. Create a simple HTTP server in Node.js.
14. What is npm?
15. Why is package manager used?
16. Write any five npm commands.
17. What is `package.json`?
18. State uses of `package.json`.
19. Differentiate local and global packages.
20. What is dependency?
21. What is dev dependency?
22. Differentiate dependency and dev dependency.
23. What is `node_modules`?
24. What is console object?
25. List methods of console object.
26. Explain `console.log()` with example.
27. Explain `console.table()` with example.
28. Differentiate `console.log()` and `console.error()`.
29. Define callback.
30. Why are callbacks used in Node.js?
31. Explain callback with example.
32. Explain asynchronous callback using `setTimeout()`.
33. What is error-first callback?
34. Explain `fs.readFile()` callback.
35. What is callback hell?
36. How can callback hell be avoided?
37. State advantages of callbacks.
38. State disadvantages of callbacks.
