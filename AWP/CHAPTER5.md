# **Chapter 5: Node.js in Details**

## **Table of Contents**

5.1 Events and Event Loop  
5.1.1 Introduction to Events  
5.1.2 Concept of Event Loop  
5.2 Timers  
5.3 Error Handling  
5.4 Buffers, Streams and File System  
5.4.1 Buffer  
5.4.2 Stream  
5.4.3 File System  
5.5 Networking with Node.js  
5.6 Web Module  
5.7 Debugging  
5.8 Express in Node.js  
5.9 Node.js REST API  
5.10 Sessions and Cookies  
5.10.1 Sessions  
5.10.2 Cookies  
5.11 Design Patterns  
5.12 Caching and Scalability  
5.13 Important Definitions  
5.14 Exam Short Questions  

---

## **5.1 Events and Event Loop**

=> Node.js is based on **event-driven architecture**.

=> In Node.js, many operations such as file reading, network request, timer completion and server request are handled as events.

=> Node.js does not wait for one operation to finish before starting another operation.

=> It uses the **event loop** to manage asynchronous operations.

### **Definition**

=> Event-driven programming is a programming style where the flow of program is controlled by events and callback functions.

### **Why Events are Important in Node.js**

1. Node.js handles many requests using events.
2. Events make asynchronous programming possible.
3. Events avoid blocking of main execution.
4. Events are useful in servers, streams, timers and network programming.
5. Events help Node.js build scalable applications.

### **Event-driven Flow**

```text
Event Occurs
     |
     v
Event Listener Detects Event
     |
     v
Callback Function Executes
     |
     v
Response / Output Generated
```

---

## **5.1.1 Introduction to Events**

=> An **event** is an action or occurrence detected by a program.

=> Examples of events are client request, file read completion, button click, timer completion and data received from network.

=> Node.js provides the built-in `events` module to create and handle custom events.

### **Important Terms**

| Term | Meaning |
|---|---|
| Event | Action or occurrence |
| EventEmitter | Class used to create and handle events |
| Listener | Function executed when event occurs |
| `on()` | Registers event listener |
| `emit()` | Triggers an event |

### **Basic Event Example**

```js
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("greet", function() {
  console.log("Hello from event");
});

emitter.emit("greet");
```

### **Output**

```text
Hello from event
```

### **Explanation**

=> `require("events")` imports the events module.

=> `new EventEmitter()` creates an event emitter object.

=> `on("greet", callback)` registers a listener for `greet` event.

=> `emit("greet")` triggers the event.

### **Event with Argument**

```js
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("login", function(username) {
  console.log(username + " logged in successfully");
});

emitter.emit("login", "Aman");
```

### **Output**

```text
Aman logged in successfully
```

### **Multiple Event Listeners**

```js
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("order", function() {
  console.log("Order received");
});

emitter.on("order", function() {
  console.log("Sending confirmation email");
});

emitter.emit("order");
```

### **Important EventEmitter Methods**

| Method | Use |
|---|---|
| `on()` | Adds event listener |
| `emit()` | Emits or triggers event |
| `once()` | Adds listener that runs only once |
| `removeListener()` | Removes specific listener |
| `removeAllListeners()` | Removes all listeners |
| `listenerCount()` | Counts listeners for event |

### **`once()` Example**

```js
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.once("connect", function() {
  console.log("Connected only once");
});

emitter.emit("connect");
emitter.emit("connect");
```

=> Output is printed only one time because `once()` runs listener only once.

---

## **5.1.2 Concept of Event Loop**

=> **Event loop** is the mechanism that allows Node.js to perform non-blocking asynchronous operations.

=> Node.js runs JavaScript code on a single main thread, but it can handle many operations with the help of event loop and system-level background work.

### **Definition**

=> Event loop is a continuous process in Node.js that checks pending callbacks and executes them when the main call stack is empty.

### **Simple Event Loop Flow**

```text
Call Stack
    |
    v
Node APIs / Background Operations
    |
    v
Callback Queue
    |
    v
Event Loop
    |
    v
Callback Execution
```

### **How Event Loop Works**

1. JavaScript code starts executing in call stack.
2. Asynchronous task is sent to Node.js APIs or background system.
3. Main thread continues executing next statements.
4. After async task completes, its callback goes to callback queue.
5. Event loop checks if call stack is empty.
6. If call stack is empty, callback is moved to call stack and executed.

### **Event Loop Example**

```js
console.log("Start");

setTimeout(function() {
  console.log("Timer callback");
}, 0);

console.log("End");
```

### **Output**

```text
Start
End
Timer callback
```

### **Explanation**

=> Even though timer is `0`, callback runs after synchronous code finishes.

=> This happens because callback waits in queue until call stack becomes empty.

### **Blocking vs Non-blocking**

| Blocking | Non-blocking |
|---|---|
| Waits until task completes | Does not wait for task completion |
| Slower for I/O operations | Faster for many I/O operations |
| Example: `fs.readFileSync()` | Example: `fs.readFile()` |

### **Blocking Example**

```js
const fs = require("fs");

console.log("Start");

const data = fs.readFileSync("data.txt", "utf8");
console.log(data);

console.log("End");
```

### **Non-blocking Example**

```js
const fs = require("fs");

console.log("Start");

fs.readFile("data.txt", "utf8", function(err, data) {
  if (err) {
    console.log(err.message);
    return;
  }

  console.log(data);
});

console.log("End");
```

### **Important Exam Point**

=> Event loop is the main reason Node.js can handle many concurrent requests efficiently using a single-threaded model.

---

## **5.2 Timers**

=> Timers are used to execute code after a delay or repeatedly after a fixed interval.

=> Node.js provides timer functions globally, so no module import is required.

### **Common Timer Functions**

| Function | Use |
|---|---|
| `setTimeout()` | Executes code once after delay |
| `setInterval()` | Executes code repeatedly after interval |
| `setImmediate()` | Executes code after current event loop phase |
| `clearTimeout()` | Cancels timeout |
| `clearInterval()` | Cancels interval |
| `clearImmediate()` | Cancels immediate callback |

### **`setTimeout()` Example**

```js
console.log("Start");

setTimeout(function() {
  console.log("Runs after 2 seconds");
}, 2000);

console.log("End");
```

### **`setInterval()` Example**

```js
let count = 1;

const timer = setInterval(function() {
  console.log("Count:", count);
  count++;

  if (count > 5) {
    clearInterval(timer);
  }
}, 1000);
```

### **`setImmediate()` Example**

```js
console.log("Before immediate");

setImmediate(function() {
  console.log("Immediate callback executed");
});

console.log("After immediate");
```

### **Difference Between Timer Functions**

| Function | Execution |
|---|---|
| `setTimeout()` | Runs once after specified delay |
| `setInterval()` | Runs repeatedly after specified delay |
| `setImmediate()` | Runs after current operation completes |

### **Important Points**

1. Timer delay is written in milliseconds.
2. `1000` milliseconds means 1 second.
3. Timer callbacks are asynchronous.
4. `clearTimeout()` and `clearInterval()` are used to stop timers.

---

## **5.3 Error Handling**

=> Error handling is the process of detecting, managing and responding to errors in a program.

=> Proper error handling prevents application crashes and helps debugging.

### **Types of Errors**

| Error Type | Meaning |
|---|---|
| Syntax error | Error in code syntax |
| Runtime error | Error while program is running |
| Logical error | Program runs but gives wrong output |
| Operational error | Error due to file, network, database or input issue |

### **Syntax Error Example**

```js
console.log("Hello"
```

=> Missing closing bracket causes syntax error.

### **Runtime Error Example**

```js
let user = null;
console.log(user.name);
```

=> `user.name` causes error because `user` is `null`.

### **Using `try...catch`**

```js
try {
  let result = 10 / x;
  console.log(result);
} catch (err) {
  console.log("Error:", err.message);
}
```

### **Using `finally`**

```js
try {
  console.log("Opening file");
  throw new Error("File not found");
} catch (err) {
  console.log("Error:", err.message);
} finally {
  console.log("Cleanup code executed");
}
```

### **Error-first Callback Pattern**

=> Node.js commonly uses error-first callback pattern.

=> First callback parameter is error.

=> Second callback parameter is result/data.

```js
const fs = require("fs");

fs.readFile("data.txt", "utf8", function(err, data) {
  if (err) {
    console.error("Unable to read file:", err.message);
    return;
  }

  console.log(data);
});
```

### **Throwing Custom Error**

```js
function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero is not allowed");
  }

  return a / b;
}

try {
  console.log(divide(10, 0));
} catch (err) {
  console.log(err.message);
}
```

### **Error Handling in Express**

```js
app.get("/user", function(req, res, next) {
  try {
    throw new Error("User not found");
  } catch (err) {
    next(err);
  }
});

app.use(function(err, req, res, next) {
  res.status(500).send(err.message);
});
```

### **Best Practices**

1. Always check `err` in callbacks.
2. Use meaningful error messages.
3. Use `try...catch` for synchronous code.
4. Use Express error middleware for Express applications.
5. Do not expose sensitive error details to users.

---

## **5.4 Buffers, Streams and File System**

=> Node.js provides powerful features to work with binary data, streams and files.

=> These features are useful for file upload, file reading, video/audio streaming and network data handling.

---

## **5.4.1 Buffer**

=> **Buffer** is a temporary memory area used to store binary data.

=> JavaScript strings are Unicode-based, but files, images, videos and network packets often use binary data.

=> Node.js uses Buffer to handle such binary data.

### **Definition**

=> Buffer is a built-in Node.js object used to store and manipulate binary data.

### **Creating Buffer**

```js
const buf = Buffer.from("Node.js");

console.log(buf);
console.log(buf.toString());
```

### **Output**

```text
<Buffer 4e 6f 64 65 2e 6a 73>
Node.js
```

### **Allocate Buffer**

```js
const buf = Buffer.alloc(10);

buf.write("Hello");

console.log(buf.toString());
```

### **Common Buffer Methods**

| Method | Use |
|---|---|
| `Buffer.from()` | Creates buffer from string/array |
| `Buffer.alloc()` | Creates buffer of fixed size |
| `write()` | Writes data into buffer |
| `toString()` | Converts buffer to string |
| `length` | Returns buffer size |

### **Important Points**

1. Buffer stores raw binary data.
2. Buffer is useful for files, streams and network data.
3. Buffer size is fixed after creation.
4. Buffer is available globally in Node.js.

---

## **5.4.2 Stream**

=> **Stream** is used to read or write data piece by piece.

=> Streams are useful when working with large files because the full file is not loaded into memory at once.

### **Definition**

=> Stream is a Node.js object that allows continuous reading or writing of data in chunks.

### **Types of Streams**

| Stream Type | Meaning | Example |
|---|---|---|
| Readable | Used to read data | `fs.createReadStream()` |
| Writable | Used to write data | `fs.createWriteStream()` |
| Duplex | Can read and write both | TCP socket |
| Transform | Modifies data while reading/writing | Compression stream |

### **Read Stream Example**

```js
const fs = require("fs");

const readStream = fs.createReadStream("input.txt", "utf8");

readStream.on("data", function(chunk) {
  console.log("New chunk:");
  console.log(chunk);
});

readStream.on("end", function() {
  console.log("File reading completed");
});
```

### **Write Stream Example**

```js
const fs = require("fs");

const writeStream = fs.createWriteStream("output.txt");

writeStream.write("First line\n");
writeStream.write("Second line\n");
writeStream.end();
```

### **Pipe Example**

=> `pipe()` sends data from readable stream to writable stream.

```js
const fs = require("fs");

const readStream = fs.createReadStream("input.txt");
const writeStream = fs.createWriteStream("copy.txt");

readStream.pipe(writeStream);
```

### **Advantages of Streams**

1. Efficient for large files.
2. Saves memory.
3. Processes data faster.
4. Useful for video/audio streaming.
5. Supports piping from one stream to another.

---

## **5.4.3 File System**

=> Node.js provides the built-in `fs` module to work with files and directories.

=> `fs` stands for **File System**.

### **Import File System Module**

```js
const fs = require("fs");
```

### **Read File Asynchronously**

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

### **Write File**

```js
const fs = require("fs");

fs.writeFile("data.txt", "Hello Node.js", function(err) {
  if (err) {
    console.log(err.message);
    return;
  }

  console.log("File written successfully");
});
```

### **Append File**

```js
const fs = require("fs");

fs.appendFile("data.txt", "\nNew line added", function(err) {
  if (err) {
    console.log(err.message);
    return;
  }

  console.log("Data appended");
});
```

### **Delete File**

```js
const fs = require("fs");

fs.unlink("data.txt", function(err) {
  if (err) {
    console.log(err.message);
    return;
  }

  console.log("File deleted");
});
```

### **Common `fs` Methods**

| Method | Use |
|---|---|
| `readFile()` | Reads file asynchronously |
| `readFileSync()` | Reads file synchronously |
| `writeFile()` | Writes data to file |
| `appendFile()` | Adds data at end of file |
| `unlink()` | Deletes file |
| `mkdir()` | Creates directory |
| `rmdir()` | Removes directory |
| `stat()` | Gives file information |
| `createReadStream()` | Creates readable stream |
| `createWriteStream()` | Creates writable stream |

### **Async vs Sync File Methods**

| Async Method | Sync Method |
|---|---|
| Does not block execution | Blocks execution |
| Uses callback/promise | Returns result directly |
| Better for server apps | Useful for simple scripts |
| Example: `readFile()` | Example: `readFileSync()` |

---

## **5.5 Networking with Node.js**

=> Node.js can create network applications using built-in modules.

=> It supports HTTP servers, TCP servers, UDP sockets and client-server communication.

### **Important Networking Modules**

| Module | Use |
|---|---|
| `http` | Creates HTTP server/client |
| `https` | Creates secure HTTP server/client |
| `net` | Creates TCP server/client |
| `dgram` | Creates UDP socket |
| `dns` | Performs DNS lookup |
| `url` | Parses URL |

### **TCP Server Example**

```js
const net = require("net");

const server = net.createServer(function(socket) {
  socket.write("Welcome to TCP server\n");

  socket.on("data", function(data) {
    console.log("Client:", data.toString());
  });
});

server.listen(4000, function() {
  console.log("TCP server running on port 4000");
});
```

### **DNS Lookup Example**

```js
const dns = require("dns");

dns.lookup("google.com", function(err, address) {
  if (err) {
    console.log(err.message);
    return;
  }

  console.log("IP Address:", address);
});
```

### **URL Parsing Example**

```js
const url = require("url");

const address = "http://localhost:3000/student?id=101&name=Aman";
const result = url.parse(address, true);

console.log(result.pathname);
console.log(result.query.id);
console.log(result.query.name);
```

### **Important Points**

1. Networking modules are built into Node.js.
2. `http` is used for web server development.
3. `net` is used for TCP communication.
4. `dns` is used for domain name lookup.
5. Node.js is suitable for real-time network applications.

---

## **5.6 Web Module**

=> In Node.js, the built-in `http` module is used to create web servers.

=> It can handle HTTP requests and send HTTP responses.

### **Definition**

=> Web module in Node.js refers to the built-in `http` module used to create server-side web applications.

### **Simple Web Server**

```js
const http = require("http");

const server = http.createServer(function(req, res) {
  res.writeHead(200, { "Content-Type": "text/html" });
  res.write("<h1>Welcome to Node.js Web Server</h1>");
  res.end();
});

server.listen(3000, function() {
  console.log("Server running at http://localhost:3000");
});
```

### **Handling Routes Manually**

```js
const http = require("http");

const server = http.createServer(function(req, res) {
  res.writeHead(200, { "Content-Type": "text/html" });

  if (req.url === "/") {
    res.end("<h1>Home Page</h1>");
  } else if (req.url === "/about") {
    res.end("<h1>About Page</h1>");
  } else {
    res.writeHead(404, { "Content-Type": "text/html" });
    res.end("<h1>404 Page Not Found</h1>");
  }
});

server.listen(3000);
```

### **Request and Response Objects**

| Object | Meaning |
|---|---|
| `req` | Represents client request |
| `res` | Represents server response |

### **Common Response Methods**

| Method | Use |
|---|---|
| `res.writeHead()` | Sends status code and headers |
| `res.write()` | Writes response body |
| `res.end()` | Ends response |
| `res.setHeader()` | Sets response header |

### **HTTP Status Codes**

| Code | Meaning |
|---|---|
| `200` | OK |
| `201` | Created |
| `400` | Bad Request |
| `401` | Unauthorized |
| `404` | Not Found |
| `500` | Internal Server Error |

---

## **5.7 Debugging**

=> Debugging is the process of finding and fixing errors in a program.

=> Node.js applications can be debugged using console methods, Node inspector and editor tools.

### **Common Debugging Techniques**

1. Use `console.log()` to check values.
2. Use `console.error()` for errors.
3. Use Node.js inspector.
4. Use breakpoints in editor.
5. Read stack trace carefully.
6. Test functions separately.

### **Debug using Console**

```js
function add(a, b) {
  console.log("a:", a);
  console.log("b:", b);
  return a + b;
}

console.log(add(10, 20));
```

### **Node Inspector Command**

```bash
node --inspect app.js
```

### **Debug with Break at Start**

```bash
node --inspect-brk app.js
```

=> `--inspect-brk` starts debugger and pauses execution at the first line.

### **Using `debugger` Statement**

```js
let x = 10;
let y = 20;

debugger;

let sum = x + y;
console.log(sum);
```

### **Stack Trace**

=> Stack trace shows where an error occurred in the program.

```js
function first() {
  second();
}

function second() {
  throw new Error("Something went wrong");
}

first();
```

### **Good Debugging Practices**

1. Reproduce the error.
2. Read the error message.
3. Check line number.
4. Use small test cases.
5. Avoid random changes.
6. Remove unnecessary console logs after debugging.

---

## **5.8 Express in Node.js**

=> **Express.js** is a lightweight web framework for Node.js.

=> It simplifies routing, middleware, request handling and API development.

### **Definition**

=> Express is a Node.js framework used to build web applications and REST APIs easily.

### **Install Express**

```bash
npm install express
```

### **Simple Express Server**

```js
const express = require("express");

const app = express();

app.get("/", function(req, res) {
  res.send("Welcome to Express");
});

app.listen(3000, function() {
  console.log("Server running on port 3000");
});
```

### **Express Routing**

```js
app.get("/", function(req, res) {
  res.send("Home Page");
});

app.get("/about", function(req, res) {
  res.send("About Page");
});

app.post("/students", function(req, res) {
  res.send("Student created");
});
```

### **HTTP Methods in Express**

| Method | Use |
|---|---|
| `GET` | Read data |
| `POST` | Create data |
| `PUT` | Update full data |
| `PATCH` | Update partial data |
| `DELETE` | Delete data |

### **Middleware**

=> Middleware is a function that has access to request object, response object and `next()` function.

=> Middleware can modify request, send response or pass control to next middleware.

### **Middleware Example**

```js
app.use(function(req, res, next) {
  console.log(req.method, req.url);
  next();
});
```

### **JSON Body Middleware**

```js
app.use(express.json());
```

=> `express.json()` parses JSON request body.

### **Route Parameter**

```js
app.get("/students/:id", function(req, res) {
  res.send("Student ID: " + req.params.id);
});
```

### **Query Parameter**

```js
app.get("/search", function(req, res) {
  res.send("Search text: " + req.query.q);
});
```

### **Advantages of Express**

1. Simple and lightweight.
2. Easy routing.
3. Middleware support.
4. Useful for REST APIs.
5. Large community support.
6. Reduces manual HTTP server code.

---

## **5.9 Node.js REST API**

=> **REST API** is an application programming interface based on REST principles.

=> REST APIs use HTTP methods to perform operations on resources.

### **Definition**

=> REST API is a web service that allows client and server to communicate using HTTP methods such as GET, POST, PUT and DELETE.

### **REST Resource Example**

=> In a student application, `students` is a resource.

| Operation | HTTP Method | URL |
|---|---|---|
| Get all students | `GET` | `/students` |
| Get one student | `GET` | `/students/:id` |
| Add student | `POST` | `/students` |
| Update student | `PUT` | `/students/:id` |
| Delete student | `DELETE` | `/students/:id` |

### **Simple REST API Example**

```js
const express = require("express");

const app = express();
app.use(express.json());

let students = [
  { id: 1, name: "Aman", branch: "CE" },
  { id: 2, name: "Riya", branch: "IT" }
];

app.get("/students", function(req, res) {
  res.json(students);
});

app.get("/students/:id", function(req, res) {
  const id = Number(req.params.id);
  const student = students.find(function(s) {
    return s.id === id;
  });

  if (!student) {
    res.status(404).json({ message: "Student not found" });
    return;
  }

  res.json(student);
});

app.post("/students", function(req, res) {
  const student = {
    id: students.length + 1,
    name: req.body.name,
    branch: req.body.branch
  };

  students.push(student);
  res.status(201).json(student);
});

app.put("/students/:id", function(req, res) {
  const id = Number(req.params.id);
  const student = students.find(function(s) {
    return s.id === id;
  });

  if (!student) {
    res.status(404).json({ message: "Student not found" });
    return;
  }

  student.name = req.body.name;
  student.branch = req.body.branch;

  res.json(student);
});

app.delete("/students/:id", function(req, res) {
  const id = Number(req.params.id);
  students = students.filter(function(s) {
    return s.id !== id;
  });

  res.json({ message: "Student deleted" });
});

app.listen(3000, function() {
  console.log("REST API running on port 3000");
});
```

### **Testing REST API**

| Request | Purpose |
|---|---|
| `GET /students` | Get all records |
| `GET /students/1` | Get one record |
| `POST /students` | Add new record |
| `PUT /students/1` | Update record |
| `DELETE /students/1` | Delete record |

### **Important REST Principles**

1. Use proper HTTP methods.
2. Use meaningful resource URLs.
3. Use JSON for request and response.
4. Use proper status codes.
5. Keep server stateless.

### **Advantages of REST API**

1. Platform independent.
2. Easy to test.
3. Uses standard HTTP methods.
4. Supports JSON data.
5. Suitable for web and mobile apps.

---

## **5.10 Sessions and Cookies**

=> Sessions and cookies are used to store user-related data in web applications.

=> They are commonly used for login systems, user preferences and shopping carts.

### **Difference Between Session and Cookie**

| Cookie | Session |
|---|---|
| Stored on client browser | Stored on server |
| Less secure for sensitive data | More secure than cookies |
| Has size limitation | Can store more data |
| Sent with every request | Identified using session ID |
| Can persist after browser closes | Usually expires after logout or timeout |

---

## **5.10.1 Sessions**

=> **Session** stores user information on server side.

=> Browser stores only a session ID in cookie.

### **Install Session Package**

```bash
npm install express-session
```

### **Session Example**

```js
const express = require("express");
const session = require("express-session");

const app = express();

app.use(session({
  secret: "mysecret",
  resave: false,
  saveUninitialized: true
}));

app.get("/login", function(req, res) {
  req.session.username = "Aman";
  res.send("Session created");
});

app.get("/profile", function(req, res) {
  if (req.session.username) {
    res.send("Welcome " + req.session.username);
  } else {
    res.send("Please login first");
  }
});

app.get("/logout", function(req, res) {
  req.session.destroy();
  res.send("Logged out");
});

app.listen(3000);
```

### **Advantages of Sessions**

1. Stores sensitive data on server.
2. Useful for authentication.
3. Can store user state.
4. More secure than storing everything in cookies.

---

## **5.10.2 Cookies**

=> **Cookie** is small data stored in the client browser.

=> Cookies are sent to server with each request.

### **Install Cookie Parser**

```bash
npm install cookie-parser
```

### **Cookie Example**

```js
const express = require("express");
const cookieParser = require("cookie-parser");

const app = express();

app.use(cookieParser());

app.get("/set-cookie", function(req, res) {
  res.cookie("username", "Aman", { maxAge: 60000 });
  res.send("Cookie set");
});

app.get("/get-cookie", function(req, res) {
  res.send("Username: " + req.cookies.username);
});

app.get("/clear-cookie", function(req, res) {
  res.clearCookie("username");
  res.send("Cookie cleared");
});

app.listen(3000);
```

### **Uses of Cookies**

1. Remember user preferences.
2. Store session ID.
3. Track user activity.
4. Store small non-sensitive data.

### **Cookie Security Points**

1. Do not store passwords in cookies.
2. Use `httpOnly` for security.
3. Use `secure` cookie for HTTPS.
4. Set proper expiry time.

---

## **5.11 Design Patterns**

=> **Design pattern** is a reusable solution to a common software design problem.

=> In Node.js, design patterns help organize application code.

### **Common Node.js Design Patterns**

| Pattern | Use |
|---|---|
| Module pattern | Splits code into reusable modules |
| Middleware pattern | Processes request step by step |
| Singleton pattern | Creates only one object instance |
| Factory pattern | Creates objects without exposing creation logic |
| MVC pattern | Separates model, view and controller |

### **Module Pattern Example**

### **File: `math.js`**

```js
function add(a, b) {
  return a + b;
}

function sub(a, b) {
  return a - b;
}

module.exports = {
  add: add,
  sub: sub
};
```

### **File: `app.js`**

```js
const math = require("./math");

console.log(math.add(10, 5));
console.log(math.sub(10, 5));
```

### **Middleware Pattern Example**

```js
app.use(function(req, res, next) {
  console.log("Request received");
  next();
});

app.use(function(req, res, next) {
  console.log("Authentication checked");
  next();
});
```

### **MVC Pattern**

=> MVC stands for **Model View Controller**.

| Part | Meaning |
|---|---|
| Model | Handles data and database logic |
| View | Handles user interface |
| Controller | Handles request and response logic |

### **MVC Folder Structure**

```text
project/
  models/
    studentModel.js
  controllers/
    studentController.js
  routes/
    studentRoutes.js
  views/
    index.ejs
  app.js
```

### **Advantages of Design Patterns**

1. Makes code organized.
2. Improves reusability.
3. Reduces duplication.
4. Helps maintain large applications.
5. Makes code easier to test.

---

## **5.12 Caching and Scalability**

=> **Caching** means storing frequently used data temporarily so it can be accessed faster.

=> **Scalability** means the ability of an application to handle increased users, requests or data.

### **Caching Definition**

=> Caching is a technique of storing frequently accessed data in fast storage to reduce repeated processing or database access.

### **Scalability Definition**

=> Scalability is the ability of a system to grow and handle more load without major performance loss.

### **Why Caching is Used**

1. To improve response time.
2. To reduce database load.
3. To reduce repeated calculations.
4. To improve application performance.
5. To handle more users efficiently.

### **Simple In-memory Cache Example**

```js
const cache = {};

function getStudent(id) {
  if (cache[id]) {
    console.log("Data from cache");
    return cache[id];
  }

  console.log("Data from database");
  const student = { id: id, name: "Aman", branch: "CE" };
  cache[id] = student;

  return student;
}

console.log(getStudent(1));
console.log(getStudent(1));
```

### **Types of Caching**

| Type | Meaning |
|---|---|
| Browser caching | Browser stores static resources |
| Server-side caching | Server stores frequently used data |
| Database query caching | Stores result of database queries |
| CDN caching | CDN stores static files near users |
| In-memory caching | Stores data in memory using tools like Redis |

### **Scalability Techniques in Node.js**

1. Use non-blocking I/O.
2. Use clustering.
3. Use load balancing.
4. Use caching.
5. Optimize database queries.
6. Use message queues for heavy background work.
7. Serve static files using CDN.
8. Avoid CPU-heavy work on main thread.

### **Vertical vs Horizontal Scaling**

| Vertical Scaling | Horizontal Scaling |
|---|---|
| Increase power of one server | Add more servers |
| Example: more RAM, CPU | Example: multiple app servers |
| Simple but limited | More scalable |
| Single server can be failure point | Better fault tolerance |

### **Cluster Module**

=> Node.js runs on a single main thread, but `cluster` module can create multiple worker processes.

=> This helps use multiple CPU cores.

### **Simple Cluster Example**

```js
const cluster = require("cluster");
const http = require("http");
const os = require("os");

if (cluster.isMaster) {
  const cpuCount = os.cpus().length;

  for (let i = 0; i < cpuCount; i++) {
    cluster.fork();
  }
} else {
  http.createServer(function(req, res) {
    res.end("Handled by process " + process.pid);
  }).listen(3000);
}
```

### **Important Performance Points**

1. Do not block event loop.
2. Use streams for large files.
3. Cache repeated data.
4. Use pagination for large API responses.
5. Use compression for responses.
6. Use proper error handling and logging.

---

## **5.13 Important Definitions**

### **Event**

=> Event is an action or occurrence such as request, file completion or timer completion.

### **EventEmitter**

=> EventEmitter is a Node.js class used to create, emit and listen to events.

### **Event Loop**

=> Event loop is a mechanism that executes asynchronous callbacks when the call stack is empty.

### **Timer**

=> Timer is used to execute code after delay or repeatedly at fixed intervals.

### **Buffer**

=> Buffer is a Node.js object used to store binary data.

### **Stream**

=> Stream is an object used to read or write data in chunks.

### **File System Module**

=> File System module is a built-in Node.js module used to work with files and directories.

### **Express**

=> Express is a lightweight Node.js framework used to build web applications and REST APIs.

### **REST API**

=> REST API is an API that uses HTTP methods to perform operations on resources.

### **Session**

=> Session stores user data on server side.

### **Cookie**

=> Cookie stores small data on client browser.

### **Design Pattern**

=> Design pattern is a reusable solution for a common software design problem.

### **Caching**

=> Caching stores frequently used data temporarily for faster access.

### **Scalability**

=> Scalability is the ability of an application to handle increased load.

### **Exam-Oriented Important Points**

1. Node.js uses events and event loop for asynchronous execution.
2. `EventEmitter` is used to create custom events.
3. `setTimeout()` runs code once after delay.
4. `setInterval()` runs code repeatedly.
5. `fs` module is used for file handling.
6. Buffer stores binary data.
7. Stream processes data in chunks.
8. Express simplifies web server and API development.
9. REST API uses HTTP methods such as GET, POST, PUT and DELETE.
10. Session stores data on server, cookie stores data on client.
11. Caching improves performance.
12. Scalability helps application handle more users.

---

## **5.14 Exam Short Questions**

1. Define event in Node.js.
2. What is EventEmitter?
3. Explain `on()` and `emit()` methods.
4. Write a program to create custom event.
5. What is event loop?
6. Explain event loop with diagram.
7. Differentiate blocking and non-blocking code.
8. Explain `setTimeout()` with example.
9. Explain `setInterval()` with example.
10. What is error handling?
11. Explain error-first callback pattern.
12. Explain `try...catch` in Node.js.
13. What is Buffer?
14. Write code to create Buffer.
15. What is Stream?
16. List types of streams.
17. Explain `pipe()` method.
18. What is File System module?
19. Explain `readFile()` with example.
20. Explain `writeFile()` with example.
21. List networking modules in Node.js.
22. Create simple HTTP server in Node.js.
23. What is request object?
24. What is response object?
25. What is debugging?
26. Write command to start Node.js inspector.
27. What is Express.js?
28. List advantages of Express.js.
29. Explain middleware in Express.
30. Explain route parameter and query parameter.
31. Define REST API.
32. List HTTP methods used in REST API.
33. Write REST API endpoints for student resource.
34. Differentiate session and cookie.
35. What is session?
36. What is cookie?
37. State cookie security points.
38. What is design pattern?
39. Explain module pattern.
40. Explain MVC pattern.
41. What is caching?
42. Why is caching used?
43. What is scalability?
44. Differentiate vertical and horizontal scaling.
45. List scalability techniques in Node.js.
