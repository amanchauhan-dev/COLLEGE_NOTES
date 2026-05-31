# **Chapter 6: Database Programming with Node.js and MongoDB**

## **Table of Contents**

6.1 Basics of MongoDB  
6.1.1 NoSQL Database  
6.1.2 MongoDB Features  
6.1.3 MongoDB Data Model  
6.2 MongoDB Data Types  
6.3 MongoDB Installation  
6.4 Database Commands  
6.5 Connect Node.js with MongoDB  
6.6 Operations on Data using Node.js  
6.6.1 Insert Operation  
6.6.2 Find Operation  
6.6.3 Update Operation  
6.6.4 Delete Operation  
6.6.5 Sort, Limit and Query Conditions  
6.7 Complete CRUD Example  
6.8 Important Definitions  
6.9 Exam Short Questions  

---

## **6.1 Basics of MongoDB**

=> **MongoDB** is an open-source NoSQL database.

=> It stores data in document format instead of table format.

=> MongoDB documents are stored in **BSON** format, which is a binary form of JSON.

=> MongoDB is commonly used with Node.js in modern web applications.

### **Definition**

=> MongoDB is a NoSQL document-oriented database that stores data in flexible JSON-like documents.

### **Example MongoDB Document**

```json
{
  "rollno": 101,
  "name": "Aman",
  "branch": "CE",
  "age": 21,
  "skills": ["JavaScript", "Node.js", "MongoDB"]
}
```

### **Important MongoDB Terms**

| MongoDB Term | Relational Database Term | Meaning |
|---|---|---|
| Database | Database | Container for collections |
| Collection | Table | Group of documents |
| Document | Row / Record | Single data record |
| Field | Column | Name-value pair inside document |
| `_id` | Primary key | Unique identifier of document |

### **MongoDB Structure**

```text
Database
  |
  v
Collection
  |
  v
Document
  |
  v
Fields
```

### **Example Structure**

```text
GTU Database
  |
  v
Students Collection
  |
  v
{ rollno: 101, name: "Aman", branch: "CE" }
```

### **Why MongoDB is Used**

1. It stores flexible documents.
2. It is suitable for modern web applications.
3. It supports fast read and write operations.
4. It can store nested data.
5. It supports horizontal scaling.
6. It works well with JavaScript and Node.js.

---

## **6.1.1 NoSQL Database**

=> **NoSQL** means **Not Only SQL**.

=> NoSQL databases store data in formats other than traditional relational tables.

=> NoSQL databases are useful when data structure is flexible, large or frequently changing.

### **Types of NoSQL Databases**

| Type | Description | Example |
|---|---|---|
| Document database | Stores data as documents | MongoDB |
| Key-value database | Stores data as key-value pairs | Redis |
| Column database | Stores data in column families | Cassandra |
| Graph database | Stores data as nodes and edges | Neo4j |

### **NoSQL vs Relational Database**

| NoSQL Database | Relational Database |
|---|---|
| Stores data in flexible format | Stores data in tables |
| Schema is flexible | Schema is fixed |
| Good for nested and changing data | Good for structured data |
| Uses collections and documents | Uses tables and rows |
| Horizontal scaling is easier | Vertical scaling is common |
| Example: MongoDB | Example: MySQL |

### **Important Exam Point**

=> MongoDB is a NoSQL document database. It stores records as documents in collections, while relational databases store records as rows in tables.

---

## **6.1.2 MongoDB Features**

=> MongoDB provides many features that make it useful for application development.

### **1. Document-oriented**

=> Data is stored as documents.

=> Documents are similar to JSON objects.

### **2. Flexible Schema**

=> Different documents in the same collection can have different fields.

```json
{ "name": "Aman", "branch": "CE" }
{ "name": "Riya", "branch": "IT", "city": "Surat" }
```

### **3. High Performance**

=> MongoDB provides fast read and write operations for many applications.

### **4. Indexing**

=> Indexes improve search performance.

```js
db.students.createIndex({ rollno: 1 })
```

### **5. Replication**

=> Replication stores copies of data on multiple servers.

=> It improves availability and fault tolerance.

### **6. Sharding**

=> Sharding distributes data across multiple servers.

=> It supports horizontal scaling.

### **7. Aggregation**

=> Aggregation is used for data processing, grouping and calculations.

### **8. JavaScript Friendly**

=> MongoDB documents are JSON-like, so they work naturally with JavaScript and Node.js.

### **Features Summary**

| Feature | Explanation |
|---|---|
| Document storage | Stores data in BSON documents |
| Flexible schema | Fields can vary between documents |
| Indexing | Improves query speed |
| Replication | Provides backup and high availability |
| Sharding | Supports horizontal scaling |
| Aggregation | Performs data analysis |

---

## **6.1.3 MongoDB Data Model**

=> MongoDB commonly uses two data models:

1. Embedded data model.
2. Referenced data model.

### **Embedded Data Model**

=> In embedded model, related data is stored inside the same document.

```json
{
  "name": "Aman",
  "branch": "CE",
  "address": {
    "city": "Ahmedabad",
    "state": "Gujarat"
  }
}
```

### **Advantages of Embedded Model**

1. Data is available in a single document.
2. Read operation is faster.
3. Useful for one-to-few relationships.
4. Reduces need for joins.

### **Referenced Data Model**

=> In referenced model, related data is stored in separate collections and linked using an ID.

### **Students Collection**

```json
{
  "_id": 1,
  "name": "Aman",
  "branch": "CE"
}
```

### **Marks Collection**

```json
{
  "studentId": 1,
  "subject": "AWP",
  "marks": 85
}
```

### **Advantages of Referenced Model**

1. Avoids duplicate data.
2. Useful for large related data.
3. Better for many-to-many relationships.
4. Keeps documents smaller.

### **Embedded vs Referenced Data Model**

| Embedded Model | Referenced Model |
|---|---|
| Related data stored in same document | Related data stored in separate documents |
| Faster read | More normalized |
| Can duplicate data | Reduces duplication |
| Good for small related data | Good for large or shared data |

---

## **6.2 MongoDB Data Types**

=> MongoDB supports many data types because it stores data in BSON format.

### **Common MongoDB Data Types**

| Data Type | Example | Use |
|---|---|---|
| String | `"Aman"` | Text data |
| Number / Double | `85.5` | Decimal values |
| Integer | `21` | Whole numbers |
| Boolean | `true` | True or false |
| Array | `["CE", "IT"]` | List of values |
| Object / Document | `{ city: "Surat" }` | Nested data |
| ObjectId | `ObjectId("...")` | Unique document ID |
| Date | `new Date()` | Date and time |
| Null | `null` | Empty value |

### **Document with Different Data Types**

```js
db.students.insertOne({
  name: "Aman",
  age: 21,
  marks: 85.5,
  isActive: true,
  skills: ["Node.js", "MongoDB"],
  address: {
    city: "Ahmedabad",
    state: "Gujarat"
  },
  admissionDate: new Date()
});
```

### **ObjectId**

=> MongoDB automatically creates `_id` field if it is not provided.

=> `_id` is usually an ObjectId and uniquely identifies a document.

```json
{
  "_id": ObjectId("65c1a8f2b9d22a12a1234567"),
  "name": "Aman"
}
```

### **Important Points**

1. MongoDB data is stored in BSON format.
2. BSON supports more data types than JSON.
3. `_id` field is unique for every document.
4. Array and nested object make MongoDB flexible.

---

## **6.3 MongoDB Installation**

=> MongoDB can be installed locally or used as a cloud database through MongoDB Atlas.

### **Local Installation Steps**

1. Download MongoDB Community Server.
2. Install MongoDB on the system.
3. Add MongoDB `bin` folder to PATH if required.
4. Start MongoDB server.
5. Open MongoDB shell or MongoDB Compass.
6. Create database and collections.

### **Check MongoDB Version**

```bash
mongod --version
```

### **Start MongoDB Server**

```bash
mongod
```

### **Open MongoDB Shell**

```bash
mongosh
```

### **MongoDB Compass**

=> MongoDB Compass is a graphical user interface for MongoDB.

=> It helps view databases, collections and documents without writing commands.

### **MongoDB Atlas**

=> MongoDB Atlas is a cloud-based MongoDB service.

=> It is useful when we do not want to install MongoDB locally.

### **Default Local Connection URL**

```text
mongodb://127.0.0.1:27017
```

### **Important Exam Point**

=> For Node.js programs, install the MongoDB driver using npm:

```bash
npm install mongodb
```

---

## **6.4 Database Commands**

=> MongoDB commands are used to create databases, collections and perform CRUD operations.

### **Show Databases**

```js
show dbs
```

### **Create or Switch Database**

```js
use GTU
```

=> MongoDB creates the database when data is inserted.

### **Show Current Database**

```js
db
```

### **Create Collection**

```js
db.createCollection("students")
```

### **Show Collections**

```js
show collections
```

### **Insert One Document**

```js
db.students.insertOne({
  rollno: 101,
  name: "Aman",
  branch: "CE",
  age: 21
});
```

### **Insert Many Documents**

```js
db.students.insertMany([
  { rollno: 102, name: "Riya", branch: "IT", age: 20 },
  { rollno: 103, name: "Neha", branch: "CE", age: 22 }
]);
```

### **Find Documents**

```js
db.students.find()
```

### **Find with Condition**

```js
db.students.find({ branch: "CE" })
```

### **Pretty Output**

```js
db.students.find().pretty()
```

### **Update One Document**

```js
db.students.updateOne(
  { rollno: 101 },
  { $set: { age: 22 } }
);
```

### **Update Many Documents**

```js
db.students.updateMany(
  { branch: "CE" },
  { $set: { course: "AWP" } }
);
```

### **Delete One Document**

```js
db.students.deleteOne({ rollno: 101 })
```

### **Delete Many Documents**

```js
db.students.deleteMany({ branch: "IT" })
```

### **Drop Collection**

```js
db.students.drop()
```

### **Drop Database**

```js
db.dropDatabase()
```

### **Comparison Operators**

| Operator | Meaning | Example |
|---|---|---|
| `$eq` | Equal to | `{ age: { $eq: 21 } }` |
| `$ne` | Not equal to | `{ branch: { $ne: "CE" } }` |
| `$gt` | Greater than | `{ age: { $gt: 20 } }` |
| `$gte` | Greater than or equal | `{ age: { $gte: 20 } }` |
| `$lt` | Less than | `{ age: { $lt: 25 } }` |
| `$lte` | Less than or equal | `{ age: { $lte: 25 } }` |
| `$in` | Matches values in array | `{ branch: { $in: ["CE", "IT"] } }` |

### **Logical Operators**

| Operator | Meaning |
|---|---|
| `$and` | Both conditions true |
| `$or` | Any one condition true |
| `$not` | Negates condition |
| `$nor` | None of conditions true |

### **Query Examples**

```js
db.students.find({ age: { $gte: 20 } })
```

```js
db.students.find({
  $and: [
    { branch: "CE" },
    { age: { $gte: 20 } }
  ]
})
```

---

## **6.5 Connect Node.js with MongoDB**

=> Node.js connects with MongoDB using the official `mongodb` driver.

=> The common sequence is:

1. Install MongoDB driver.
2. Import `MongoClient`.
3. Create connection URL.
4. Connect to MongoDB server.
5. Select database.
6. Select collection.
7. Perform operation.
8. Close connection.

### **Install MongoDB Driver**

```bash
npm install mongodb
```

### **Basic Connection Example**

```js
const { MongoClient } = require("mongodb");

const url = "mongodb://127.0.0.1:27017";
const client = new MongoClient(url);

async function connectDB() {
  try {
    await client.connect();
    console.log("Connected to MongoDB");

    const db = client.db("GTU");
    const collection = db.collection("students");

    console.log("Database and collection selected");
  } catch (err) {
    console.log("Connection error:", err.message);
  } finally {
    await client.close();
  }
}

connectDB();
```

### **Explanation**

=> `MongoClient` is used to connect Node.js with MongoDB.

=> `mongodb://127.0.0.1:27017` is local MongoDB URL.

=> `client.connect()` connects to MongoDB server.

=> `client.db("GTU")` selects `GTU` database.

=> `db.collection("students")` selects `students` collection.

=> `client.close()` closes database connection.

### **Connection Using Promise**

```js
const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://127.0.0.1:27017");

client.connect()
  .then(function() {
    console.log("Connected");
    return client.close();
  })
  .catch(function(err) {
    console.log(err.message);
  });
```

### **Important Connection Points**

1. MongoDB server must be running.
2. Use `npm install mongodb` before running code.
3. Always handle connection errors.
4. Close connection after operation in small scripts.
5. In Express apps, connection is usually reused.

---

## **6.6 Operations on Data using Node.js**

=> CRUD operations are most important for Node.js and MongoDB exam questions.

=> CRUD means:

| Letter | Operation | MongoDB Method |
|---|---|---|
| C | Create | `insertOne()`, `insertMany()` |
| R | Read | `find()`, `findOne()` |
| U | Update | `updateOne()`, `updateMany()` |
| D | Delete | `deleteOne()`, `deleteMany()` |

---

## **6.6.1 Insert Operation**

=> Insert operation adds new documents into a MongoDB collection.

### **Insert One Document**

```js
const { MongoClient } = require("mongodb");

async function insertStudent() {
  const client = new MongoClient("mongodb://127.0.0.1:27017");

  try {
    await client.connect();

    const db = client.db("GTU");
    const students = db.collection("students");

    const result = await students.insertOne({
      rollno: 101,
      name: "Aman",
      branch: "CE",
      age: 21
    });

    console.log("Inserted ID:", result.insertedId);
  } catch (err) {
    console.log(err.message);
  } finally {
    await client.close();
  }
}

insertStudent();
```

### **Insert Many Documents**

```js
const result = await students.insertMany([
  { rollno: 102, name: "Riya", branch: "IT", age: 20 },
  { rollno: 103, name: "Neha", branch: "CE", age: 22 }
]);

console.log("Inserted Count:", result.insertedCount);
```

### **Important Points**

1. `insertOne()` inserts one document.
2. `insertMany()` inserts multiple documents.
3. MongoDB creates `_id` automatically if not provided.
4. Insert result contains inserted ID or inserted count.

---

## **6.6.2 Find Operation**

=> Find operation retrieves documents from a MongoDB collection.

### **Find All Documents**

```js
const cursor = students.find();
const result = await cursor.toArray();

console.log(result);
```

### **Find One Document**

```js
const student = await students.findOne({ rollno: 101 });

console.log(student);
```

### **Find with Condition**

```js
const result = await students.find({ branch: "CE" }).toArray();

console.log(result);
```

### **Find with Comparison Operator**

```js
const result = await students.find({
  age: { $gte: 20 }
}).toArray();

console.log(result);
```

### **Find with Projection**

=> Projection is used to select specific fields.

```js
const result = await students.find(
  { branch: "CE" },
  { projection: { _id: 0, name: 1, branch: 1 } }
).toArray();

console.log(result);
```

### **Important Points**

1. `find()` returns a cursor.
2. Use `toArray()` to convert cursor into array.
3. `findOne()` returns one matching document.
4. Projection controls which fields are shown.

---

## **6.6.3 Update Operation**

=> Update operation modifies existing documents in a MongoDB collection.

### **Update One Document**

```js
const result = await students.updateOne(
  { rollno: 101 },
  { $set: { age: 22, course: "AWP" } }
);

console.log("Modified Count:", result.modifiedCount);
```

### **Update Many Documents**

```js
const result = await students.updateMany(
  { branch: "CE" },
  { $set: { course: "Advanced Web Programming" } }
);

console.log("Modified Count:", result.modifiedCount);
```

### **Increment Field**

```js
await students.updateOne(
  { rollno: 101 },
  { $inc: { age: 1 } }
);
```

### **Update Operators**

| Operator | Use |
|---|---|
| `$set` | Sets or updates field value |
| `$inc` | Increments numeric value |
| `$unset` | Removes field |
| `$push` | Adds value to array |
| `$pull` | Removes value from array |

### **Important Points**

1. `updateOne()` updates first matching document.
2. `updateMany()` updates all matching documents.
3. `$set` is commonly used for updating fields.
4. Always provide correct filter condition.

---

## **6.6.4 Delete Operation**

=> Delete operation removes documents from a MongoDB collection.

### **Delete One Document**

```js
const result = await students.deleteOne({ rollno: 101 });

console.log("Deleted Count:", result.deletedCount);
```

### **Delete Many Documents**

```js
const result = await students.deleteMany({ branch: "IT" });

console.log("Deleted Count:", result.deletedCount);
```

### **Delete with Condition**

```js
await students.deleteMany({
  age: { $lt: 18 }
});
```

### **Important Points**

1. `deleteOne()` deletes first matching document.
2. `deleteMany()` deletes all matching documents.
3. Empty filter in `deleteMany({})` can delete all documents.
4. Use delete operations carefully.

---

## **6.6.5 Sort, Limit and Query Conditions**

=> MongoDB provides methods to arrange, limit and filter documents.

### **Sort Ascending**

```js
const result = await students.find().sort({ name: 1 }).toArray();
```

=> `1` means ascending order.

### **Sort Descending**

```js
const result = await students.find().sort({ age: -1 }).toArray();
```

=> `-1` means descending order.

### **Limit Result**

```js
const result = await students.find().limit(5).toArray();
```

### **Skip Records**

```js
const result = await students.find().skip(5).limit(5).toArray();
```

### **Query with `$and`**

```js
const result = await students.find({
  $and: [
    { branch: "CE" },
    { age: { $gte: 20 } }
  ]
}).toArray();
```

### **Query with `$or`**

```js
const result = await students.find({
  $or: [
    { branch: "CE" },
    { branch: "IT" }
  ]
}).toArray();
```

### **Common Query Methods**

| Method | Use |
|---|---|
| `sort()` | Sorts documents |
| `limit()` | Limits number of documents |
| `skip()` | Skips documents |
| `countDocuments()` | Counts matching documents |

### **Count Documents**

```js
const count = await students.countDocuments({ branch: "CE" });

console.log("Total CE Students:", count);
```

---

## **6.7 Complete CRUD Example**

=> This example is important for 7-mark practical questions.

=> It performs insert, find, update and delete operations on `GTU` database and `students` collection.

```js
const { MongoClient } = require("mongodb");

const url = "mongodb://127.0.0.1:27017";
const client = new MongoClient(url);

async function main() {
  try {
    await client.connect();
    console.log("Connected to MongoDB");

    const db = client.db("GTU");
    const students = db.collection("students");

    // Insert
    await students.insertOne({
      enrollmentNo: "2160001",
      name: "Aman",
      age: 21,
      branch: "CE",
      course: "AWP"
    });
    console.log("Student inserted");

    // Find
    const allStudents = await students.find().toArray();
    console.log("All Students:", allStudents);

    // Query with condition
    const ceStudents = await students.find({ branch: "CE" }).toArray();
    console.log("CE Students:", ceStudents);

    // Update
    await students.updateOne(
      { enrollmentNo: "2160001" },
      { $set: { age: 22 } }
    );
    console.log("Student updated");

    // Delete
    await students.deleteOne({ enrollmentNo: "2160001" });
    console.log("Student deleted");
  } catch (err) {
    console.log("Error:", err.message);
  } finally {
    await client.close();
    console.log("Connection closed");
  }
}

main();
```

### **Employee CRUD Example**

=> This example is useful for questions asking Employee collection operations.

```js
const { MongoClient } = require("mongodb");

async function employeeCRUD() {
  const client = new MongoClient("mongodb://127.0.0.1:27017");

  try {
    await client.connect();

    const db = client.db("Company");
    const employees = db.collection("Employee");

    await employees.insertMany([
      { emp_id: 1, name: "Raj", department: "Sales", salary: 25000 },
      { emp_id: 2, name: "Neha", department: "IT", salary: 40000 }
    ]);

    const highSalary = await employees.find({
      salary: { $gte: 30000 }
    }).toArray();
    console.log(highSalary);

    await employees.updateOne(
      { emp_id: 1 },
      { $set: { salary: 30000 } }
    );

    await employees.deleteOne({ emp_id: 2 });

    console.log("Employee CRUD completed");
  } catch (err) {
    console.log(err.message);
  } finally {
    await client.close();
  }
}

employeeCRUD();
```

### **Steps to Write Node.js MongoDB CRUD in Exam**

1. Import `MongoClient`.
2. Create connection URL.
3. Create client object.
4. Use `async` function.
5. Connect using `await client.connect()`.
6. Select database using `client.db()`.
7. Select collection using `db.collection()`.
8. Perform CRUD method.
9. Handle errors using `try...catch`.
10. Close connection using `finally`.

### **Common Mistakes**

1. Forgetting `npm install mongodb`.
2. MongoDB server not running.
3. Not using `await` with async operations.
4. Forgetting `toArray()` after `find()`.
5. Not closing connection in scripts.
6. Using wrong database or collection name.

---

## **6.8 Important Definitions**

### **MongoDB**

=> MongoDB is a NoSQL document-oriented database that stores data in BSON documents.

### **NoSQL**

=> NoSQL is a non-relational database approach used to store flexible, large or changing data.

### **BSON**

=> BSON is Binary JSON format used internally by MongoDB to store documents.

### **Database**

=> Database is a container for collections.

### **Collection**

=> Collection is a group of MongoDB documents.

### **Document**

=> Document is a single record in MongoDB stored as field-value pairs.

### **Field**

=> Field is a key-value pair inside a MongoDB document.

### **ObjectId**

=> ObjectId is a unique identifier automatically generated for MongoDB documents.

### **CRUD**

=> CRUD stands for Create, Read, Update and Delete.

### **MongoClient**

=> MongoClient is a class provided by MongoDB driver to connect Node.js with MongoDB.

### **Embedded Model**

=> Embedded model stores related data inside the same document.

### **Referenced Model**

=> Referenced model stores related data in separate collections and links it using ID.

### **Replication**

=> Replication stores copies of data on multiple MongoDB servers for high availability.

### **Sharding**

=> Sharding distributes data across multiple servers for horizontal scaling.

### **Index**

=> Index is a data structure that improves query search performance.

### **Exam-Oriented Important Points**

1. MongoDB is a NoSQL document database.
2. MongoDB stores data in BSON format.
3. Database contains collections and collection contains documents.
4. `_id` uniquely identifies each document.
5. `insertOne()` and `insertMany()` insert documents.
6. `find()` and `findOne()` retrieve documents.
7. `updateOne()` and `updateMany()` update documents.
8. `deleteOne()` and `deleteMany()` delete documents.
9. Node.js connects with MongoDB using `mongodb` driver.
10. `MongoClient` is used for database connection.
11. Always use `try...catch...finally` for database code.
12. `find()` returns cursor, so `toArray()` is commonly used.

---

## **6.9 Exam Short Questions with Answers**

### **Q1. Define MongoDB.**

=> MongoDB is an open-source NoSQL document-oriented database.

=> It stores data in BSON documents, which are similar to JSON objects.

=> It is commonly used with Node.js for modern web applications.

### **Q2. What is NoSQL database?**

=> NoSQL database is a non-relational database used to store flexible and large data.

=> It does not require fixed table-based schema like relational databases.

=> Types include document, key-value, column and graph databases.

### **Q3. List features of MongoDB.**

=> Important features of MongoDB are:

1. Document-oriented storage.
2. Flexible schema.
3. Indexing.
4. Replication.
5. Sharding.
6. Aggregation.
7. High performance.

### **Q4. Differentiate NoSQL and relational database.**

| NoSQL Database | Relational Database |
|---|---|
| Stores data as documents/key-value etc. | Stores data in tables |
| Flexible schema | Fixed schema |
| Example: MongoDB | Example: MySQL |
| Good for nested/changing data | Good for structured data |

### **Q5. What is BSON?**

=> BSON stands for Binary JSON.

=> MongoDB stores documents internally in BSON format.

=> BSON supports extra data types such as ObjectId, Date and binary data.

### **Q6. What is collection?**

=> Collection is a group of MongoDB documents.

=> It is similar to a table in relational database.

=> Example: `students` collection stores multiple student documents.

### **Q7. What is document?**

=> Document is a single record in MongoDB.

=> It stores data as field-value pairs.

```json
{ "rollno": 101, "name": "Aman", "branch": "CE" }
```

### **Q8. What is `_id` in MongoDB?**

=> `_id` is the unique identifier of a MongoDB document.

=> MongoDB automatically creates `_id` if not provided.

=> It works like a primary key in relational database.

### **Q9. Explain MongoDB database structure.**

```text
Database
  |
  Collection
  |
  Document
  |
  Field-value pairs
```

=> Example: `GTU` database contains `students` collection, and collection contains student documents.

### **Q10. Explain embedded data model.**

=> Embedded data model stores related data inside the same document.

```json
{
  "name": "Aman",
  "address": { "city": "Surat", "state": "Gujarat" }
}
```

=> It gives faster read because related data is available in one document.

### **Q11. Explain referenced data model.**

=> Referenced model stores related data in separate collections.

=> Documents are linked using an ID such as `studentId`.

=> It is useful when related data is large, shared or many-to-many.

### **Q12. Differentiate embedded and referenced model.**

| Embedded Model | Referenced Model |
|---|---|
| Related data in same document | Related data in separate documents |
| Faster read | Reduces duplication |
| Good for small related data | Good for large/shared data |

### **Q13. List MongoDB data types.**

=> MongoDB data types include:

1. String.
2. Number / Integer / Double.
3. Boolean.
4. Array.
5. Object / Document.
6. ObjectId.
7. Date.
8. Null.

### **Q14. Explain ObjectId.**

=> ObjectId is a unique value used in MongoDB `_id` field.

=> It is automatically generated when a document is inserted.

=> It helps identify each document uniquely in a collection.

### **Q15. Write steps to install MongoDB.**

1. Download MongoDB Community Server.
2. Install MongoDB.
3. Add MongoDB `bin` folder to PATH if required.
4. Start server using `mongod`.
5. Open shell using `mongosh`.
6. Use Compass for GUI if needed.

### **Q16. What is MongoDB Compass?**

=> MongoDB Compass is a graphical user interface for MongoDB.

=> It helps view databases, collections and documents visually.

=> It can run queries, create indexes and inspect schema without command line.

### **Q17. What is MongoDB Atlas?**

=> MongoDB Atlas is a cloud database service for MongoDB.

=> It allows creating MongoDB database without local installation.

=> It provides cloud hosting, backup, monitoring and scaling.

### **Q18. Write command to show databases.**

```js
show dbs
```

=> This command lists available MongoDB databases.

=> A database appears after it contains data.

### **Q19. Write command to create or switch database.**

```js
use GTU
```

=> This command switches to `GTU` database.

=> If database does not exist, MongoDB creates it when data is inserted.

### **Q20. Write command to create collection.**

```js
db.createCollection("students")
```

=> This creates a collection named `students`.

=> MongoDB can also create collection automatically during first insert.

### **Q21. Write command to insert one document.**

```js
db.students.insertOne({
  rollno: 101,
  name: "Aman",
  branch: "CE"
});
```

=> `insertOne()` inserts one document into collection.

### **Q22. Write command to find documents.**

```js
db.students.find()
```

=> This displays all documents from `students` collection.

```js
db.students.find({ branch: "CE" })
```

=> This finds documents matching condition.

### **Q23. Write command to update one document.**

```js
db.students.updateOne(
  { rollno: 101 },
  { $set: { branch: "IT" } }
);
```

=> `updateOne()` updates first matching document.

### **Q24. Write command to delete one document.**

```js
db.students.deleteOne({ rollno: 101 })
```

=> `deleteOne()` deletes first document matching the condition.

=> Delete commands should be used carefully.

### **Q25. List MongoDB comparison operators.**

=> Important comparison operators are:

1. `$eq` equal to.
2. `$ne` not equal to.
3. `$gt` greater than.
4. `$gte` greater than or equal.
5. `$lt` less than.
6. `$lte` less than or equal.
7. `$in` match values in array.

### **Q26. Explain `$and` and `$or` operators.**

=> `$and` returns documents where all conditions are true.

=> `$or` returns documents where at least one condition is true.

```js
db.students.find({ $and: [{ branch: "CE" }, { age: { $gte: 20 } }] })
```

### **Q27. How to connect Node.js with MongoDB?**

=> Node.js connects with MongoDB using the `mongodb` driver.

=> Steps are install driver, import `MongoClient`, create client, connect, select database, select collection and perform operations.

=> Connection URL for local server is usually `mongodb://127.0.0.1:27017`.

### **Q28. What is MongoClient?**

=> `MongoClient` is a class provided by MongoDB Node.js driver.

=> It is used to connect Node.js application with MongoDB server.

=> It provides methods to connect, select database and close connection.

### **Q29. Write npm command to install MongoDB driver.**

```bash
npm install mongodb
```

=> This installs official MongoDB driver for Node.js.

=> After installation, `MongoClient` can be imported from `mongodb`.

### **Q30. Write Node.js code to connect MongoDB.**

```js
const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://127.0.0.1:27017");

async function main() {
  await client.connect();
  console.log("Connected");
  await client.close();
}

main();
```

=> This connects Node.js with local MongoDB server.

### **Q31. Explain `insertOne()` with example.**

=> `insertOne()` inserts one document into a collection.

```js
await students.insertOne({
  rollno: 101,
  name: "Aman",
  branch: "CE"
});
```

=> MongoDB automatically adds `_id` if it is missing.

### **Q32. Explain `insertMany()` with example.**

=> `insertMany()` inserts multiple documents at once.

```js
await students.insertMany([
  { rollno: 102, name: "Riya" },
  { rollno: 103, name: "Neha" }
]);
```

=> It is useful for bulk insert operations.

### **Q33. Explain `find()` and `findOne()`.**

=> `find()` returns all matching documents as a cursor.

=> `findOne()` returns only the first matching document.

```js
await students.find({ branch: "CE" }).toArray();
await students.findOne({ rollno: 101 });
```

### **Q34. Why is `toArray()` used?**

=> `find()` returns a cursor, not a direct array.

=> `toArray()` converts cursor result into an array of documents.

=> It is commonly used to print or process query results in Node.js.

### **Q35. Explain `updateOne()` with example.**

=> `updateOne()` updates first document matching the filter.

```js
await students.updateOne(
  { rollno: 101 },
  { $set: { age: 22 } }
);
```

=> `$set` updates or adds field value.

### **Q36. Explain `deleteOne()` with example.**

=> `deleteOne()` deletes first document matching the condition.

```js
await students.deleteOne({ rollno: 101 });
```

=> It returns result containing `deletedCount`.

### **Q37. Explain sort and limit operations.**

=> `sort()` arranges documents in ascending or descending order.

=> `limit()` restricts number of returned documents.

```js
await students.find().sort({ name: 1 }).limit(5).toArray();
```

=> `1` means ascending and `-1` means descending.

### **Q38. Write CRUD operations on Student collection using Node.js and MongoDB.**

```js
await students.insertOne({ rollno: 101, name: "Aman", branch: "CE" });
const data = await students.find().toArray();
await students.updateOne({ rollno: 101 }, { $set: { branch: "IT" } });
await students.deleteOne({ rollno: 101 });
```

=> These statements perform create, read, update and delete operations on `students`.

### **Q39. Write CRUD operations on Employee collection using Node.js and MongoDB.**

```js
await employees.insertOne({ emp_id: 1, name: "Raj", salary: 25000 });
const data = await employees.find({ salary: { $gte: 20000 } }).toArray();
await employees.updateOne({ emp_id: 1 }, { $set: { salary: 30000 } });
await employees.deleteOne({ emp_id: 1 });
```

=> These operations insert, read, update and delete employee documents.

### **Q40. State common mistakes in Node.js MongoDB programming.**

=> Common mistakes are:

1. MongoDB server not running.
2. Forgetting `npm install mongodb`.
3. Not using `await`.
4. Forgetting `toArray()` after `find()`.
5. Wrong database or collection name.
6. Not closing connection in small scripts.
