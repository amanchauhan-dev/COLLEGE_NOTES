# **7 Audio, Video and Camera Use**

## **7.1 Media Player**

=> Media player is a part of the Android multimedia framework that plays audio or video from the resource directory and gallery.

=> It also streams music or video from a URL.

=> By using media player class audio or video files from application (raw) resources can be accessed.

=> Standalone files in file system or from a data stream arriving over a network connection can play audio or video files.

=> It provides multiple playback options such as play, pause, forward, backward, etc.

### **7.1.1 User Media Player**

=> The media player class primarily handles the playback of audio and video within an android application.

=> You can play the media stored in application resources, local files, Content Providers or streamed from a network URL using the media player.

=> Media player's management of audio and video are handled in the form of state machines.

=> To play a media resource, you need to create an instance of MediaPlayer class, then initialize it with media source and prepare it for playback.

Processes with sequential order

1. Initialize the media player with media to play.

2. Prepare the media player for the playback.

3. Start the playback.

4. Pause or stop the playback prior to its completing.

5. The playback is completed.

## **7.2 Recording and Playing Sound**

=> The audio track and audio record classes let you record audio directly from the audio output hardware.

=> The audio record class is used to record audio directly from the hardware buffers.

=> The audio track class is used to directly play the raw audio into the hardware buffers.

### **7.2.1 Media Formats**

=> Depending on the codecs used, Android phones can support and play several audio file types.

Types of Supported Audio Formats

1. AAC LC.

2. HE-AACv1 (AAC+).

3. HE-AACv2 (enhanced AAC+).

4. AAC ELD (enhanced low delay AAC).

5. AMR-NB.

6. AMR-WB.

7. FLAC.

8. MP3.

9. MIDI.

10. Vorbis.

11. PCM/WAVE.

=> Depending on the codec used to compress the video container format, it may still not play on your Android phone even though it generally is supported.

=> To watch your videos still, you can convert the video into another format or choose an Android compatible conversion right away.

=> The codecs supported by Android phones are H.263, H.264, MPEG-4, and V8.

Types of Supported Video Container Formats

1. 3GP.

2. MKV.

3. MP4.

4. TS.

5. WEBM.

### **7.2.2 Playing Audio**

=> To play local audio in the supported formats, you first should put the local audio file into the res/raw folder.

=> We can use the MediaPlayer in order to playback any local files.

=> On call to start() method, the music will start playing from the beginning.

=> If this method is called again after the pause() method, the music would start playing from where it left off and not from the beginning.

=> To play back audio from a local file path, you simply initialize a Uri, set the data source, prepare, and start the playback.

### **7.2.3 Playing Video**

=> In Android, VideoView is used to display a video file.

=> It can load images from various sources (such as content providers or resources) taking care of computing its measurement from the video so that it can be used for any layout manager, providing display options such as scaling and tinting.

=> MediaController is a class which is used to provide the controls for the video playback.

=> If a video is simply played using the VideoView class then the user will not be given any control over the playback of the video which will run until the end of the video is reached.

=> This issue can be addressed by attaching an instance of the MediaController class to the VideoView instance.

=> The MediaController will then provide a set of controls allowing the user to manage the playback (such as seeking backwards/forwards and pausing in the video timeline).

## **7.3 Creating a SoundPool**

=> The SoundPool helps developers to make a collection of samples, to load them into memory, not only from a resource of the application APK, but also from a folder in the file system.

=> Creating a SoundPool preloads the audio tracks used by your application and optimizes their require management.

=> You can create a SoundPool class to manage audio when your application requires low audio latency or will be playing multiple audio streams simultaneously (such as a game with multiple sound effects).

=> You can setup SoundPool to make a sound in specific stream type.

=> AudioManager allows you to adjust the volume on the different audio streams.

=> Using STREAM_MUSIC the sound will be produced through one audio device (phone speaker, earphone, bluetooth speaker or something else) connected to the phone.

=> Using STREAM_RING the sound will be produced through all audio device connected to the phone, though this behavior might be differed for each devices.

Types of Audio Streams Supported

1. AudioManager.STREAM_ALARM.

2. AudioManager.STREAM_DTMF.

3. AudioManager.STREAM_MUSIC.

4. AudioManager.STREAM_NOTIFICATION.

5. AudioManager.STREAM_RING.

6. AudioManager.STREAM_SYSTEM.

7. AudioManager.STREAM_VOICE_CALL.

## **7.4 Using Camera**

=> Android provides working with camera in two ways.

Types of Camera Usage

1. Camera Intent.

2. Camera API.

=> The easiest way to take a picture from within your application is by using an Intent and applying the constants from the MediaStore class ACTION_IMAGE_CAPTURE.

=> This launches a Camera application to take the photo, providing your users with the full suite of camera functionality without having to rewrite the native Camera application.

=> Once users are satisfied with the image, the result is returned to your application within the Intent received by the onActivityResult handler.

Steps to use Camera API

1. Add the CAMERA permission to your application manifest.

2. Use the Camera class to adjust camera settings, specify image preferences, and take pictures.

3. **Access the camera using the static open method on the Camera class**: camera = Camera.open().

4. **When you are finished with the Camera, remember to free the camera resources by calling release**: camera.release().

## **7.5 Recording Video**

=> Android has two methods for recording video.

Types of Methods to Record Video

1. Intents to Record Video.

2. Media Recording API.

=> The easiest way to record a video from within your application is by using an Intent and applying the constants from the MediaStore class ACTION_VIDEO_CAPTURE.

=> Starting a new Activity with this Intent launches the native video recorder, allowing users to start, stop, review, and retake their video.

=> You can use the MediaRecorder class to record video directly.

=> To record any media in Android, your application needs the CAMERA and RECORD_AUDIO and/or RECORD_VIDEO permissions as applicable.

=> Media Recorder manages recording as a state machine, and the order in which you manage and configure the Media Recorder is important.

=> When the recoding is finished free all the resources on your Media Recorder object using mediaRecorder.release().

Processes with sequential order for Media Recorder state machine

1. Create a new Media Recorder.

2. Unlock the Camera and assign it to the Media Recorder.

3. Specify the input sources to record from.

4. Select a profile to use for Android 2.2 and above, or define the output format and specify the audio and video encoder, frame rate, and output size.

5. Select an output file.

6. Assign a preview Surface.

7. Prepare the Media Recorder for recording.

8. Record.

9. End the recording.

## **7.6 Short Questions and Answers**

=> **Definition**: `A SoundPool is a collection of samples that can be loaded into memory from a resource inside the APK or from a file in the file system.`

=> The SoundPool library uses the MediaPlayer service to decode the audio into a raw 16-bit PCM mono or stereo stream.

=> This allows applications to ship with compressed streams without having to suffer the CPU load and latency of decompressing during playback.

=> The Camera.open method will turn on and initialize the camera, getting it ready for you to modify settings, configure the preview surface, and take pictures.

=> Media player class can be used to control playback of audio/video files and streams in Android devices.

=> **Definition**: `ANR stands for Application Not Responding.`

=> It is a notification or pop-up displayed by the Android platform whenever the application is performing too many functions at a time and is suddenly not responding for a long time to the user action.
