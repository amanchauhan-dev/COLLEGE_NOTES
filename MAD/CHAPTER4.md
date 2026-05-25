# **4 Storing Data Persistently**

## **4.1 Data Storage in Android**

=> **Definition**: `Data storage means saving application data so it can be used later.`

=> Android provides multiple storage options depending on data size, privacy and structure.

### Android storage options

1. SharedPreferences.
2. Internal Storage.
3. External Storage.
4. SQLite Database.
5. Content Provider.
6. Network or cloud storage.

### Choosing correct storage

| Requirement | Suitable storage |
|---|---|
| Small settings | SharedPreferences |
| Private app files | Internal Storage |
| Public media/files | External Storage |
| Structured records | SQLite |
| Share data with apps | Content Provider |
| Sync across devices | Network/Cloud |

## **4.2 Internal Storage**

=> **Internal Storage** stores private files inside app-specific storage.

=> Other apps cannot access these files.

=> Files are deleted when the app is uninstalled.

### Important methods

1. `openFileOutput()`
2. `openFileInput()`
3. `getFilesDir()`
4. `getCacheDir()`

### Write file example

```java
String data = "Hello Android";

FileOutputStream fos = openFileOutput("data.txt", MODE_PRIVATE);
fos.write(data.getBytes());
fos.close();
```

### Read file example

```java
FileInputStream fis = openFileInput("data.txt");
BufferedReader reader = new BufferedReader(new InputStreamReader(fis));

String line = reader.readLine();
reader.close();
```

## **4.3 External Storage**

=> **External Storage** stores files in shared or app-specific external storage.

=> It is useful for images, videos, documents and downloaded files.

### Types

1. **Primary external storage**

=> Built-in shared storage.

2. **Secondary external storage**

=> Removable storage such as SD card.

### Important methods

1. `Environment.getExternalStorageState()`
2. `getExternalFilesDir()`
3. `getExternalCacheDir()`

### Write to app-specific external storage

```java
File file = new File(getExternalFilesDir(null), "data.txt");

FileOutputStream fos = new FileOutputStream(file);
fos.write("Hello External Storage".getBytes());
fos.close();
```

### Check storage state

```java
String state = Environment.getExternalStorageState();

if (Environment.MEDIA_MOUNTED.equals(state)) {
    // External storage is available for read and write.
}
```

### Note

=> On newer Android versions, public shared storage access is restricted. App-specific external files usually do not need storage permission.

## **4.4 SharedPreferences**

=> **Definition**: `SharedPreferences are used to store small amounts of primitive data as key-value pairs.`

### Suitable for

1. Login status.
2. Username.
3. App theme.
4. Language preference.
5. Small settings.

### Supported data types

1. String
2. int
3. boolean
4. float
5. long
6. Set<String>

### Write data

```java
SharedPreferences preferences =
        getSharedPreferences("MyPrefs", MODE_PRIVATE);

SharedPreferences.Editor editor = preferences.edit();
editor.putString("username", "Aman");
editor.putBoolean("isLogin", true);
editor.apply();
```

### Read data

```java
SharedPreferences preferences =
        getSharedPreferences("MyPrefs", MODE_PRIVATE);

String username = preferences.getString("username", "");
boolean isLogin = preferences.getBoolean("isLogin", false);
```

### Difference from Activity state

=> Activity state is temporary for current session.

=> SharedPreferences persist even after app restart or phone reboot.

## **4.5 SQLite Database**

=> **Definition**: `SQLite is a lightweight relational database used to store structured data persistently in Android.`

=> SQLite is built into Android and does not require a separate server.

### Features

1. Lightweight database.
2. Requires little memory.
3. Supports SQL.
4. Stores data persistently.
5. Useful for structured records.
6. Automatically managed inside Android app.

### SQLite data types

1. `TEXT`
2. `INTEGER`
3. `REAL`
4. `BLOB`
5. `NULL`

### Common operations

1. Create table.
2. Insert data.
3. Read/query data.
4. Update data.
5. Delete data.

## **4.6 SQLiteOpenHelper**

=> `SQLiteOpenHelper` is used to create and manage SQLite database in Android.

### Important methods

1. `onCreate(SQLiteDatabase db)`

=> Called when database is created first time.

2. `onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion)`

=> Called when database version changes.

3. `getWritableDatabase()`

=> Opens database for read/write operations.

4. `getReadableDatabase()`

=> Opens database for reading.

## **4.7 SQLite Example: Student Database**

### DBHelper.java

```java
public class DBHelper extends SQLiteOpenHelper {
    private static final String DB_NAME = "StudentDB";
    private static final int DB_VERSION = 1;
    private static final String TABLE_NAME = "student";

    public DBHelper(Context context) {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String query = "CREATE TABLE " + TABLE_NAME + "("
                + "enrollment TEXT PRIMARY KEY,"
                + "name TEXT,"
                + "branch TEXT)";
        db.execSQL(query);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    public boolean insertStudent(String enrollment, String name, String branch) {
        SQLiteDatabase db = getWritableDatabase();

        ContentValues values = new ContentValues();
        values.put("enrollment", enrollment);
        values.put("name", name);
        values.put("branch", branch);

        long result = db.insert(TABLE_NAME, null, values);
        return result != -1;
    }
}
```

### Use in Activity

```java
DBHelper dbHelper = new DBHelper(this);

boolean inserted = dbHelper.insertStudent(
        "22012301001",
        "Aman",
        "Computer");

if (inserted) {
    Toast.makeText(this, "Student inserted", Toast.LENGTH_SHORT).show();
}
```

## **4.8 Query, Update and Delete in SQLite**

### Read data

```java
SQLiteDatabase db = dbHelper.getReadableDatabase();

Cursor cursor = db.rawQuery("SELECT * FROM student", null);

while (cursor.moveToNext()) {
    String enrollment = cursor.getString(0);
    String name = cursor.getString(1);
    String branch = cursor.getString(2);
}

cursor.close();
```

### Update data

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();

ContentValues values = new ContentValues();
values.put("branch", "IT");

db.update(
        "student",
        values,
        "enrollment=?",
        new String[]{"22012301001"});
```

### Delete data

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();

db.delete(
        "student",
        "enrollment=?",
        new String[]{"22012301001"});
```

## **4.9 Content Provider**

=> **Definition**: `A Content Provider manages access to a central repository of data and allows data sharing between applications.`

=> By default, one app cannot directly access another app's private data. Content Provider provides a secure standard interface.

### Features

1. Shares data between apps.
2. Uses content URI.
3. Works with `ContentResolver`.
4. Supports query, insert, update and delete.
5. Handles inter-process communication.

### Common built-in Content Providers

1. Contacts Provider.
2. MediaStore Provider.
3. Calendar Provider.
4. Call Log Provider.
5. Settings Provider.
6. User Dictionary Provider.

### Content URI example

```text
content://contacts/people
```

## **4.10 Access Content Provider Example**

### Read contacts

```java
Cursor cursor = getContentResolver().query(
        ContactsContract.Contacts.CONTENT_URI,
        null,
        null,
        null,
        null);

while (cursor != null && cursor.moveToNext()) {
    String name = cursor.getString(
            cursor.getColumnIndexOrThrow(
                    ContactsContract.Contacts.DISPLAY_NAME));
}

if (cursor != null) {
    cursor.close();
}
```

### Required permission

```xml
<uses-permission android:name="android.permission.READ_CONTACTS" />
```

## **4.11 ContentResolver Operations**

### Insert

```java
ContentValues values = new ContentValues();
values.put("name", "Aman");

Uri uri = getContentResolver().insert(CONTENT_URI, values);
```

### Query

```java
Cursor cursor = getContentResolver().query(
        CONTENT_URI,
        null,
        null,
        null,
        null);
```

### Update

```java
ContentValues values = new ContentValues();
values.put("name", "New Name");

getContentResolver().update(
        CONTENT_URI,
        values,
        "id=?",
        new String[]{"1"});
```

### Delete

```java
getContentResolver().delete(
        CONTENT_URI,
        "id=?",
        new String[]{"1"});
```

## **4.12 Data Storage Comparison**

| Storage | Best for | Shared with other apps |
|---|---|---|
| SharedPreferences | Small key-value settings | No |
| Internal Storage | Private files | No |
| External Storage | Media/documents | Yes, depending on location |
| SQLite | Structured records | No |
| Content Provider | Shared structured data | Yes |

## **4.13 Exam Short Questions**

=> **Question**: `What is SharedPreferences?`

=> **Answer**: SharedPreferences store small key-value data persistently.

=> **Question**: `What is SQLite?`

=> **Answer**: SQLite is a lightweight relational database built into Android.

=> **Question**: `What is ContentProvider?`

=> **Answer**: ContentProvider shares data between applications using a standard secure interface.

=> **Question**: `Which storage is best for login status?`

=> **Answer**: SharedPreferences.

=> **Question**: `Which class manages SQLite database creation?`

=> **Answer**: SQLiteOpenHelper.
