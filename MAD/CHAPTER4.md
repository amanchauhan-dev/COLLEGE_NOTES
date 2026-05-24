# **4 Storing the Data Persistently**

## **4.1 Storage Data Folder**

=> **Core concept**: `The application data folder is used to store application-specific data.`

=> The application data folder is a special hidden folder that your app can use to store application-specific data, such as configuration files.

=> The application data folder is automatically created when you attempt to create a file in it.

=> Use this folder to store any files that the user shouldn't directly interact with.

=> This folder is only accessible by your application and its contents are hidden from the user and from other Drive apps.

=> The application data folder is deleted when a user uninstalls your app from their MyDrive.

=> Users can also delete your app's data folder manually.

### **4.1.1 Application Data Folder Scope**

=> Before you can access the application data folder, you must request access to the https://www.googleapis.com/auth/drive.appdata scope.

### **4.1.2 Creating File in App Data Folder**

=> To create a file in the application data folder, specify appDataFolder in the parents property of the file.

=> Use the files.create method to upload the file to the folder.

### **4.1.3 Search for Files in App Data Folder**

=> To search for files in the application data folder, set the spaces field to appDataFolder and use the files.list method.

## **4.2 Using Internal Storage**

=> **Core concept**: `Android read write data to internal file.`

=> Android data can be saved in internal storage (ROM), external storage (SD card), shared preferences or SQLite database.

=> Android is based on Linux, and the android file system is Linux based also.

=> Android studio provides an android device monitor tool for you to monitor and transfer files between the android device and your PC.

=> All android app internal data files are saved in the /data/data/<your app package name> folder.

=> **Example**: `my app data internal file is saved in /data/data/com.dev2qa.example folder.`

=> There are files and cache sub folders under the package name folder.

Types of internal storage folders

1. **Files folder**: android.content.Context's getFilesDir() method can return this folder, which is used to save general files.
2. **Cache folder**: android.content.Context's getCacheDir() method can return this folder, which is used to save cached files.

=> **Important explanation point**: `When device internal storage space is low, cache files will be removed by android OS automatically to make internal storage space bigger.`

=> Generally, you need to delete the unused cache files in code timely, and total cache file size is better not more than 1 MB.

## **4.3 Using External Storage**

=> Android data can be saved in internal storage (ROM), external storage (SD card), shared preferences or SQLite database.

=> Android external storage can be used to write and save data, read configuration files etc.

=> External storage such as SD card can also store application data, and there is no security enforced upon files you save to the external storage.

Types of External Storage

1. **Primary External Storage**: In-built shared storage which is accessible by the user by plugging in a USB cable and mounting it as a drive on a host computer (Example: Nexus 5 32 GB).
2. **Secondary External Storage**: Removable storage like an SD Card.

=> All applications can read and write files placed on the external storage and the user can remove them.

=> We need to check if the SD card is available and if we can write to it before allowing operations like saving.

=> Firstly, we need to make sure that the application has permission to read and write data to the users SD card by adding permissions in the AndroidManifest.xml.

=> External storage may be tied up by the user having mounted it as a USB storage device, so we need to check if it is available and is not read-only.

=> getExternalStorageState() is a static method of Environment to determine if external storage is presently available or not.

Types of External Storage Methods

1. `Environment.getExternalStorageState()`: returns path to internal SD mount point like "/mnt/sdcard".
2. `getExternalFilesDir()`: It returns the path to files folder inside Android/data/data/application_package/ on the SD card.

=> The getExternalFilesDir() folder is used to store any required files for your app like images downloaded from web or cache files.

=> Once the app is uninstalled, any data stored in this folder is gone too.

## **4.4 Shared Preferences**

=> **Core concept**: `Shared preferences allow you to read and write small amounts of primitive data as key/value pairs to a file on the device storage.`

=> The SharedPreference class provides APIs for getting a handle to a preference file and for reading, writing, and managing this data.

=> The shared preferences file itself is managed by the Android framework and is accessible to (shared with) all the components of your app.

=> **Important explanation point**: `That data is not, however, shared with or accessible to any other apps.`

=> The data you save to shared preferences is different from the data in the saved activity state.

=> The data in the activity instance state is retained across activity instances in the same user session.

=> Shared preferences persist across user sessions, even if your app is killed and restarted or if the device is rebooted.

=> Use shared preferences only when you need to save a small amount of simple key/value pairs.

=> To manage larger amounts of persistent app data, use other methods such as SQL databases.

### **4.4.1 Creating Private and Shared Preferences**

=> Individual activities can have their own private preferences.

=> These preferences are for the specific Activity only and are not shared with other activities within the application.

=> The activity gets only one group of private preferences.

=> You can access shared preferences by name from any activity in the application.

=> There is no limit to the number of different shared preferences you can create.

=> **Example**: `You can have some shared preferences called UserNetworkPreferences and another called AppDisplayPreferences.`

=> How you organize shared preferences is up to you, the developer.

=> It is recommended to declare your preference name as a variable (in a base class or header) so that you can reuse the name across multiple activities.

## **4.5 SQLite**

=> **Definition**: `SQLite is a software library that provides a relational database management system.`

=> The 'lite' in SQLite means lightweight in terms of setup, database administration, and required resource.

=> A SQLite database is a good storage solution when you have structured data that you need to store persistently and access, search, and change frequently.

=> SQLite is self-contained, meaning it requires minimal support from the operating system or external library.

=> This makes SQLite usable in any environments, especially in embedded devices like iPhones, Android phones, game consoles, handheld media players, etc.

=> SQLite is developed using ANSI-C, with the source code available as a big sqlite3.c and its header file sqlite3.h.

=> If you want to develop an application that uses SQLite, you just need to drop these files into your project and compile it with your code.

=> SQLite databases are very lightweight, unlike other database systems, there is no configuration or installation required to start working on an SQLite database.

=> When you use a SQLite database, all interactions with the database are through an instance of the SQLiteOpenHelper class which executes your requests and manages your database for you.

=> The Android SQLite Database requires very little memory (around 250kb), which is available on all android devices.

=> Every device has an inbuilt support for SQLite database, which is automatically managed on android right from its creation, execution to querying up process.

=> SQLite is an open-source database, available on every android database, and it supports standard relational database features like SQL syntax, transactions & SQL statements.

=> Most of the SQL commands don't run on the lighter version of SQL database (SQLite), so it is important to ensure that a feature or command is available in SQLite before executing it.

Advantages of SQLite

1. It's a light weight database.
2. Requires very little memory.
3. An Automatically managed database.

Types of Datatypes supported by SQLite

1. Text (like string) - for storing data type store.
2. Integer (like int) - for storing integer primary key.
3. Real (like double) - for storing long.

=> Unlike other database management systems, there is no CREATE DATABASE command in SQLite.

=> The simplest way to create a new SQLiteDatabase instance for your application is to use the openOrCreateDatabase() method of your application Context.

## **4.6 Content Provider**

=> **Definition**: `A content provider manages access to a central repository of data.`

=> A provider is part of an Android application, which often provides its own UI for working with the data.

=> Content providers are primarily intended to be used by other applications, which access the provider using a provider client object.

=> Together, providers and provider clients offer a consistent, standard interface to data that also handles inter-process communication and secure data access.

=> A content provider presents data to external applications as one or more tables that are similar to the tables found in a relational database.

=> A row represents an instance of some type of data the provider collects, and each column in the row represents an individual piece of data collected for an instance.

=> Typically you work with content providers in one of two scenarios: you may want to implement code to access an existing content provider or implement one in another.

=> A content provider coordinates access to the data storage layer in your application for a number of different APIs and components.

Types of components the content provider handles

1. Sharing access to your application data with other applications.
2. Sending data to a widget.
3. Returning custom search suggestions for your application through the search framework using SearchRecentSuggestionsProvider.
4. Synchronizing application data with your server using an implementation of AbstractThreadedSyncAdapter.
5. Loading data in your UI using a CursorLoader.

### **4.6.1 Content Provider Classes**

=> A content provider in Android shares data between applications, with each application usually running in its own process.

=> By default, applications can't access the data and files of other applications.

=> You can make preferences and files available across application boundaries with the correct permissions and if each application knows the context and path.

=> This solution applies only to related applications that already know details about one another.

=> In contrast, with a content provider you can publish and expose a particular data type for other applications to query, add, update, and delete.

=> With content providers, applications don't need to have any prior knowledge of paths, resources, or who provides the content.

=> The canonical content provider in Android is the contacts list, which provides names, addresses, and phone numbers.

=> You can access this data from any application by using the correct URI and series of methods provided by the Activity and ContentResolver classes to retrieve and store data.

### **4.6.2 Deleting Database Records**

=> The data modification clauses in SQLite are INSERT, UPDATE, and DELETE statements.

=> It is used for inserting new rows, updating existing values, or deleting rows from the database.

=> You can remove records from the database using the remove() method, which takes a few arguments.

=> Passing null to the WHERE clause deletes all records within the table.

=> Most of the time, though, we want to delete individual records by their unique identifiers.

=> You need not use the primary key (id) to delete records; the WHERE clause is entirely up to you.

## **4.7 Handling Database in Android**

=> In the same way that you retrieve data from a provider, you also use the interaction between a provider client and the provider's ContentProvider to modify data.

=> You call a method of ContentResolver with arguments that are passed to the corresponding method of ContentProvider.

=> The provider and provider client automatically handle security and inter-process communication.

### **4.7.1 Inserting Data**

=> To insert data into a provider, you call the ContentResolver.insert() method.

=> This method inserts a new row into the provider and returns a content URI for that row.

=> The data for the new row goes into a single ContentValues object, which is similar in form to a one-row cursor.

=> The columns in this object don't need to have the same data type, and if you don't want to specify a value at all, you can set a column to null using ContentValues.putNull().

=> You generally don't add the _ID column to the ContentValues because this column is maintained automatically.

=> The provider assigns a unique value of _ID to every row that is added, which providers usually use as the table's primary key.

=> The content URI returned identifies the newly-added row with a specific format containing the <id_value> for the new row.

=> Most providers can detect this form of content URI automatically and then perform the requested operation on that particular row.

=> To get the value of _ID from the returned Uri, call ContentUris.parseId().

### **4.7.2 Updating Data**

=> To update a row, you use a ContentValues object with the updated values just as you do with an insertion.

=> You specify selection criteria just as you do with a query to identify the rows to update.

=> You should also sanitize user input when you call ContentResolver.update().

### **4.7.3 Deleting data**

=> Deleting rows is similar to retrieving row data: you specify selection criteria for the rows you want to delete.

=> The client method returns the number of deleted rows.

=> You should also sanitize user input when you call ContentResolver.delete().
