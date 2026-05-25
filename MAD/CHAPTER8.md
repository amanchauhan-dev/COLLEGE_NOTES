# **8 Publishing and Distributing Android Application**

## **8.1 Signing the Android Application**

=> **Definition**: `Signing is the process of digitally attaching a certificate to an Android application package.`

=> Every Android application must be signed before it can be installed on a device or emulator.

### Why signing is required

1. Identifies the author of the application.
2. Ensures application integrity.
3. Allows Android to verify app updates.
4. Helps protect apps from unauthorized modification.
5. Required for Play Store publishing.

### Types of signing

1. **Debug signing**

=> Used during development and testing.

=> Android Studio automatically signs debug builds using a debug key.

2. **Release signing**

=> Used when publishing app to users.

=> Developer signs the app using a private keystore.

### Steps to generate signed APK/AAB in Android Studio

1. Open project in Android Studio.
2. Click **Build -> Generate Signed Bundle / APK**.
3. Select **Android App Bundle** or **APK**.
4. Create a new keystore or select existing keystore.
5. Enter key alias, password and certificate details.
6. Select release build variant.
7. Click **Finish**.

=> Android Studio creates a signed release build that can be uploaded or distributed.

## **8.2 APK and AAB**

### APK

=> **APK** stands for **Android Package Kit**.

=> It is the package file used to install Android applications directly on devices.

### AAB

=> **AAB** stands for **Android App Bundle**.

=> It is a publishing format used by Google Play to generate optimized APKs for different devices.

### Difference

| APK | AAB |
|---|---|
| Installed directly on device. | Uploaded to Play Store. |
| Contains all resources for all devices. | Play Store generates optimized APKs. |
| Useful for manual distribution. | Preferred for Play Store publishing. |

## **8.3 Versioning in Android Application**

=> Versioning identifies different releases of an Android application.

### Important fields

1. **versionCode**

=> Internal integer used by Android and Play Store to compare versions.

=> It must be increased for every new release.

2. **versionName**

=> User-visible version string such as `1.0`, `1.1`, `2.0`.

### Example

```gradle
android {
    defaultConfig {
        versionCode 3
        versionName "1.2"
    }
}
```

### Uses

1. Supports app updates.
2. Helps track releases.
3. Required when uploading a new version to Play Store.
4. Allows users to identify installed app version.

## **8.4 Publishing Android App**

=> **Definition**: `Publishing is the process of preparing, signing and making an Android application available to users.`

=> Android apps can be published through Google Play Store, company website, third-party app stores or direct APK sharing.

### Steps to publish Android app on Play Store

1. **Complete development**

=> Finish coding, UI design and required features.

2. **Test application**

=> Test on emulator and real devices with different screen sizes and Android versions.

3. **Set app details**

=> Set app icon, app name, package name, versionCode and versionName.

4. **Prepare release build**

=> Remove debug logs, test code and unused files.

5. **Generate signed APK/AAB**

=> Use Android Studio to generate a signed release build.

6. **Create Play Console account**

=> Register as Google Play developer.

7. **Create app listing**

=> Add app title, short description, full description, screenshots, app icon and feature graphic.

8. **Set category and tags**

=> Choose app category such as Education, Tools, Games, Business, etc.

9. **Complete content rating**

=> Fill content rating questionnaire.

10. **Add privacy policy and data safety**

=> Explain what user data the app collects and how it is used.

11. **Set pricing and distribution**

=> Select free/paid app and target countries.

12. **Upload release build**

=> Upload signed APK/AAB to Play Console.

13. **Submit for review**

=> Google reviews the app. After approval, it becomes available to users.

## **8.5 Deploying APK Files**

=> Deploying APK means installing or distributing an Android package file on a device.

### Ways to deploy APK

1. Install through Android Studio.
2. Install using ADB.
3. Share APK file directly.
4. Upload APK to website.
5. Upload APK/AAB to Play Store.

### ADB command

```text
adb install app-release.apk
```

### Important points

1. APK must be signed before installation.
2. Device may require "Install unknown apps" permission for manual APK install.
3. Release APK should be tested before distribution.
4. Play Store distribution requires app listing and policy compliance.

## **8.6 Distribution of Android App**

=> Distribution means delivering the app to users.

### Distribution methods

1. **Google Play Store**

=> Most common and trusted distribution platform.

2. **Website download**

=> Developer can host APK on a website.

3. **Third-party app stores**

=> Apps may be distributed through other stores.

4. **Enterprise distribution**

=> Companies distribute private apps to employees.

5. **Pre-installation**

=> App may be preloaded by device manufacturers or mobile operators.

### Advantages of Google Play Store

1. Large user base.
2. Automatic updates.
3. User reviews and ratings.
4. Payment and in-app purchase support.
5. Security scanning through Play Protect.

## **8.7 App Characteristics**

=> Good Android applications should be performant, modifiable, available and secure.

### **8.7.1 Performance**

=> Performance means how fast and smoothly the application works.

### Important points

1. App should start quickly.
2. UI should not freeze.
3. Heavy tasks should not run on main thread.
4. Images should be optimized.
5. Battery and memory usage should be controlled.

### Ways to improve performance

1. Use background threads for heavy work.
2. Avoid memory leaks.
3. Use efficient layouts.
4. Cache data where needed.
5. Test on low-end devices.

### **8.7.2 Modifiability**

=> Modifiability means the app can be changed, fixed or extended easily.

### Important points

1. Divide app into modules.
2. Keep code reusable.
3. Use proper naming and structure.
4. Reduce tight coupling.
5. Keep related logic together.

=> Modifiability helps in bug fixing and releasing new versions.

### **8.7.3 Availability**

=> Availability means the app should remain usable when needed.

### Important points

1. App should handle network failure.
2. Offline data should be available where possible.
3. App should recover from crashes.
4. Synchronization should be used when network returns.
5. Server errors should be handled gracefully.

### **8.7.4 Security**

=> Security means protecting user data and app functionality from unauthorized access.

### Important points

1. Request only required permissions.
2. Store sensitive data securely.
3. Use HTTPS for network communication.
4. Validate user input.
5. Avoid hardcoding passwords or API keys.
6. Sign release builds properly.
7. Keep dependencies updated.

## **8.8 Why Android Apps Have Less Chance of Device Corruption**

=> Android apps are less likely to corrupt the device because Android provides a controlled and secure execution environment.

### Reasons

1. **Application sandboxing**

=> Each app runs in its own sandbox and cannot directly access other apps' private data.

2. **Linux kernel security**

=> Android uses Linux permissions, process isolation and user IDs.

3. **Permission model**

=> Apps must request permission before using protected features like camera, contacts and location.

4. **Managed runtime**

=> Dalvik/ART manages app execution and memory safety.

5. **Application signing**

=> Apps must be digitally signed before installation.

6. **Play Protect**

=> Play Store apps are scanned for harmful behavior.

=> Because of these protections, normal apps cannot freely modify system files or damage the operating system.

## **8.9 Important Manifest Entries for Publishing**

### Permissions

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.CAMERA" />
```

### App version and SDK in Gradle

```gradle
android {
    defaultConfig {
        applicationId "com.example.myapp"
        minSdk 23
        targetSdk 35
        versionCode 1
        versionName "1.0"
    }
}
```

### Launcher activity

```xml
<activity
    android:name=".MainActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

## **8.10 Exam Short Questions**

=> **Question**: `Android applications must be signed when?`

=> **Answer**: Android applications must be signed before they are installed or published.

=> **Question**: `What is APK?`

=> **Answer**: APK is Android Package Kit, the installable package file of an Android app.

=> **Question**: `What is AAB?`

=> **Answer**: AAB is Android App Bundle, the preferred Play Store publishing format.

=> **Question**: `What is AAPT?`

=> **Answer**: AAPT stands for Android Asset Packaging Tool. It packages resources into the app build.

=> **Question**: `What is contained within AndroidManifest.xml?`

=> **Answer**: It contains app components, permissions, package information, launcher activity and application metadata.

=> **Question**: `Each application can have zero or more activities. True or False?`

=> **Answer**: True. An Android app may have zero or more activities depending on its purpose.

=> **Question**: `List four Android versions.`

=> **Answer**: Cupcake, Donut, Eclair, Froyo, Gingerbread, Honeycomb, Ice Cream Sandwich, Jelly Bean, KitKat, Lollipop.
