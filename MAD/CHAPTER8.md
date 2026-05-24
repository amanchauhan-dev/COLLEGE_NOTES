# **8 Publishing and Distributing Android Application**

## **8.1 Signing the Android Application**

=> **Core concept**: `The Android platform requires every application file to be digitally signed in order to run on a device or emulator.`

=> **Important explanation point**: `Without a signature, an application simply won't run.`

=> The signing requirement is entirely transparent to most developers until it is time to publish an application for others to use.

=> When you are publishing an application for distribution, the application needs to be signed with a nondebug signature.

=> Fortunately, the applications can be self-signed, meaning a certificate authority isn't required.

=> This keeps the complexity and cost down considerably compared to the signing process required for other mobile platforms.

=> The Export Android Application wizard simplifies the process of creating and signing a release build of your application package.

Steps

1. Open the application in Android Studio.

2. Generate a signed .apk file from Android Studio.

3. Fill the details and press Next.

4. Choose the Variant and version according to choice and requirement, and then press Finish.

=> Having selected a signing certificate, the next step is to select an output destination for your package.

=> The wizard will then compile, sign, and zip-align the package.

## **8.2 Publishing Android App**

=> **Definition**: `Publishing an application involves digitally signing it and uploading it to the appropriate platforms.`

=> There are various possibilities in which the application can be released, such as on Google Play, Websites or directly to the Users.

=> Google Play uses application package names as unique identifiers and will not allow you to upload a duplicate package name.

=> To release an app on Google Play, you need to follow specific simple steps.

Steps

1. Add some promotional material like screen shots, videos and interesting features of the app.

2. Configure options with information such as language, country, type, category, etc.

=> Publish the release version: Once the application is ready to be released, we can click on the Publish button on the console.

=> In a few minutes, the application would be available throughout the world to download.

### **8.2.1 Process of Publishing an Android Application**

=> The steps of the publishing process are summarized systematically.

Processes with sequential order

1. Select an appropriate AppStore.

2. Read and understand the policies and agreements of the selected AppStore.

3. Quality test.

4. Determine the content rating for the Android application.

5. Determine the country or countries to distribute.

6. Confirm the overall size, platform and the screen compatibility ranges.

7. Decide the revenue model.

8. Decide how to bill or collect the revenue (e.g., In-App or using Google Pay).

9. Set the price or prices.

10. Localization.

11. Prepare promotional graphics, videos and screencasts.

12. Build and upload the release version.

13. Plan for Beta release.

14. Complete AppStore listing.

15. Support users after launch.

## **8.3 Distribution of Android App**

=> Android applications are distributed as Android package files (.APK).

=> Google Play is a robust platform that supports us to release, sell and distribute applications throughout the world.

=> Another way to get great distribution is to partner with device manufacturers and mobile operators, who often select applications to pre-load onto devices prior to purchase.

=> Look for special developer programs that can help you foster partnerships and other distribution relationships with manufacturers, carriers, and the like.

=> Various third-party sites also offer distribution channels.

=> These sites have different agreement types and different payment models, so you should research them carefully before using them.

## **8.4 App Characteristics**

### **8.4.1 Performance of App**

=> The performance of an app plays an important role in getting a 5-star rating in all marketplaces like playstore, app store or windows store.

=> If an application takes more than 10 seconds to load then it will not be used by users.

=> If an application takes too long a time to process data then it will not be used by users.

=> If an application takes too long a time to switch between screens then it will not be used by users.

=> The performance of an app is an important factor which decides the success of the app.

=> Understand your target device: Most developers classify devices based on operating system, but forget about the configuration of devices.

=> Always classify devices based on a specification sheet and try developing apps based on low specification mobiles which will automatically run in all mobiles.

=> Understand your tools: Try to understand the tools that are used to develop the mobile app, as this helps to make important architectural designs.

=> **Example**: `Understanding about phone gap helps to develop an app for multiple platforms.`

=> Understand core concepts of the language used to build the app: Understanding the core programming language used to develop an app will help to avoid performance issues.

=> **Example**: `An extra string comparison in jscript will surely reduce the performance.`

=> Understand the library: Try to understand the library used in tools.

=> If you simply call third-party methods for simple operations then it will increase battery usage and reduce the performance, so always use standard codes for simple tasks.

### **8.4.2 Modifiability of App**

=> Modifiability helps to release multiple versions of an app more easily.

=> Modifiability is achieved by developing as multiple units instead of a single unit.

=> If any bugs arise after launch then it is easy to modify the unit instead of changing everything in the code.

=> Modifiability is minimizing the technical risks and cost impact of changes in software.

=> In order to achieve modifiability as a system quality, software architects need to envision and incorporate modifiability support in the system's design cycle.

=> The architectural design supports the modifiability requirements of a system.

=> The modifiability quality of a system can be expressed in terms of cohesion and coupling.

=> Coupling measures the mutual association strength between the system's software components.

=> Cohesion is a measure for the number of internal relationships between the responsibilities of a software component.

### **8.4.3 Availability of App**

=> Availability refers to continuous working of the application in both offline and online modes.

=> Today mobile users are travelling across multiple cell sites which frequently disturb the wireless internet connectivity to mobile.

=> This interruption should not affect the mobile app.

=> It is possible to achieve high availability by effectively managing offline data.

=> High availability can be provided by giving an effective synchronization mechanism.

### **8.4.4 Security of App**

=> Mobile apps should satisfy stringent requirements for data security and privacy.

=> This is no longer the exclusive domain of the enterprise, as organizations of every size and function are subject to mounting ethical and legal pressure to control and protect the information under their purview.

=> Fiduciary responsibility and internal and external policies exist to govern what organizations must do in this regard, from data storage to disaster recovery, encryption to secure updating.

=> By definition, internet access and mobile devices carry inherent security risks, including but not limited to the apps that run on them.

## **8.5 Short Questions and Answers**

=> **Question**: `List out at least four versions of Android.`

=> **Answer**: `Android alpha (1.0), Cupcake (1.5), Eclair (2.0 - 2.1), Gingerbread (2.3 - 2.3.7), Android beta (1.1), Doughnut (1.6), Froyo (2.2 - 2.2.3), Honeycomb (3.0 - 3.2.6), Ice Cream Sandwich (4.0 - 4.0.4), Jelly Bean (4.1 - 4.3.1), KitKat (4.4 - 4.4 w),.`

=> **Question**: `Each application can have zero or more activities. True or False? Justify in short.`

=> **Answer**: `True, an Android application can contain zero or more activities.`

=> When your application has more than one activity, you may need to navigate from one activity to another.

## **8.6 Multiple Choice Questions**

=> **Question 1**: `Android applications must be signed ____.`

=> **Answer**: `before they are installed.`

=> **Question 2**: `The emulated device for android ____.`

=> **Answer**: `runs the same code base as the actual device, all the way down to the machine layer.`

=> **Question 3**: `The ____ file specifies the layout of your screen.`

=> **Answer**: `layout file.`

=> **Question 4**: `What runs in the background and doesn't have any UI components?.`

=> **Answer**: `Services.`

=> **Question 5**: `What is AAPT?.`

=> **Answer**: `Android Asset Packaging Tool.`

=> **Question 6**: `What is contained within the manifest xml file?.`

=> **Answer**: `The permissions the app requires.`
