# **7 Audio, Video and Camera Use**

## **7.1 Android Multimedia Framework**

=> Android provides multimedia APIs to play, record and manage audio, video and camera data.

### Important multimedia classes

1. `MediaPlayer`: Plays audio and video.
2. `VideoView`: Displays video in a view.
3. `MediaController`: Provides video controls such as play, pause and seek.
4. `MediaRecorder`: Records audio and video.
5. `AudioRecord`: Records raw audio from microphone.
6. `AudioTrack`: Plays raw audio data.
7. `SoundPool`: Plays short sound effects with low latency.
8. `Camera` / CameraX: Used to capture images and video.

## **7.2 MediaPlayer**

=> **Definition**: `MediaPlayer is an Android class used to play audio and video files or streams.`

=> MediaPlayer can play media from:

1. `res/raw` resources.
2. Local file path.
3. Content URI.
4. Network URL.

### Common methods

1. `create()`: Creates MediaPlayer for a resource.
2. `setDataSource()`: Sets file, URI or URL as source.
3. `prepare()`: Prepares player synchronously.
4. `prepareAsync()`: Prepares player asynchronously.
5. `start()`: Starts or resumes playback.
6. `pause()`: Pauses playback.
7. `stop()`: Stops playback.
8. `seekTo()`: Moves playback to a specific position.
9. `isPlaying()`: Checks whether media is playing.
10. `release()`: Releases resources.

### MediaPlayer state sequence

```text
Idle -> Initialized -> Prepared -> Started
                       |          |
                       v          v
                    Paused      Stopped
                       |
                       v
                    Playback completed
```

### Example: Play audio from res/raw

Place file:

```text
res/raw/song.mp3
```

```java
MediaPlayer mediaPlayer = MediaPlayer.create(this, R.raw.song);

btnPlay.setOnClickListener(v -> mediaPlayer.start());

btnPause.setOnClickListener(v -> {
    if (mediaPlayer.isPlaying()) {
        mediaPlayer.pause();
    }
});

btnStop.setOnClickListener(v -> {
    mediaPlayer.stop();
    mediaPlayer.release();
});
```

=> Always call `release()` when MediaPlayer is no longer needed.

## **7.3 Recording and Playing Sound**

=> Android provides classes for both high-level and low-level audio handling.

### Audio recording classes

1. **MediaRecorder**

=> Used to record audio in common formats with less code.

2. **AudioRecord**

=> Used to record raw audio from hardware buffers. It gives more control but requires more code.

### Audio playback classes

1. **MediaPlayer**

=> Used for normal music or audio playback.

2. **AudioTrack**

=> Used to play raw PCM audio data directly.

3. **SoundPool**

=> Used for short sound effects.

### Supported audio formats

1. MP3
2. AAC
3. AMR-NB
4. AMR-WB
5. FLAC
6. MIDI
7. OGG/Vorbis
8. PCM/WAVE

### Example: Record audio using MediaRecorder

```xml
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

```java
MediaRecorder recorder = new MediaRecorder();

recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
recorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
recorder.setOutputFile(getExternalFilesDir(null) + "/record.3gp");

recorder.prepare();
recorder.start();

// Stop recording later
recorder.stop();
recorder.release();
```

## **7.4 Playing Video**

=> Android can play video using `VideoView` with `MediaController`.

=> `VideoView` displays the video, while `MediaController` provides playback controls.

### Supported video formats

1. MP4
2. 3GP
3. MKV
4. WEBM
5. TS

### Common codecs

1. H.263
2. H.264
3. MPEG-4
4. VP8/VP9

### Example: Play video from res/raw

```xml
<VideoView
    android:id="@+id/videoView"
    android:layout_width="match_parent"
    android:layout_height="300dp" />
```

```java
VideoView videoView = findViewById(R.id.videoView);

Uri uri = Uri.parse("android.resource://" + getPackageName() + "/" + R.raw.video);
videoView.setVideoURI(uri);

MediaController controller = new MediaController(this);
controller.setAnchorView(videoView);
videoView.setMediaController(controller);

videoView.start();
```

## **7.5 SoundPool**

=> **Definition**: `SoundPool is used to load and play short audio clips with low latency.`

=> It is suitable for games and apps that need quick sound effects.

### Uses

1. Button click sound.
2. Game sound effects.
3. Notification-like short sound.
4. Multiple sounds at the same time.

### SoundPool vs MediaPlayer

| SoundPool | MediaPlayer |
|---|---|
| Best for short sounds. | Best for long audio/video. |
| Low latency. | More suitable for music/video. |
| Can play multiple sounds. | Usually handles one media stream. |

### Example

```java
SoundPool soundPool = new SoundPool.Builder()
        .setMaxStreams(5)
        .build();

int soundId = soundPool.load(this, R.raw.click, 1);

button.setOnClickListener(v -> {
    soundPool.play(soundId, 1, 1, 1, 0, 1);
});
```

## **7.6 AudioManager and Audio Streams**

=> `AudioManager` is used to manage audio volume, stream type and audio modes.

### Common audio streams

1. `AudioManager.STREAM_MUSIC`
2. `AudioManager.STREAM_RING`
3. `AudioManager.STREAM_ALARM`
4. `AudioManager.STREAM_NOTIFICATION`
5. `AudioManager.STREAM_VOICE_CALL`
6. `AudioManager.STREAM_SYSTEM`

### Example: Set music stream volume

```java
AudioManager audioManager =
        (AudioManager) getSystemService(AUDIO_SERVICE);

audioManager.setStreamVolume(
        AudioManager.STREAM_MUSIC,
        5,
        AudioManager.FLAG_SHOW_UI);
```

## **7.7 Using Camera**

=> Android provides two common ways to use camera.

### 1. Camera Intent

=> This is the easiest method. It opens the built-in camera app and returns the captured image.

```java
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
startActivityForResult(intent, 100);
```

### 2. Camera API / CameraX

=> Used when the app needs a custom camera screen, preview, focus control or advanced camera features.

### Required permission

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

### Camera Intent example

```java
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

if (intent.resolveActivity(getPackageManager()) != null) {
    startActivityForResult(intent, 100);
}
```

### Receive thumbnail image

```java
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);

    if (requestCode == 100 && resultCode == RESULT_OK) {
        Bitmap photo = (Bitmap) data.getExtras().get("data");
        imageView.setImageBitmap(photo);
    }
}
```

### Camera API steps

1. Add camera permission.
2. Open camera.
3. Configure preview surface.
4. Capture photo or video.
5. Release camera resources.

## **7.8 Recording Video**

=> Android supports video recording using Intent or MediaRecorder.

### 1. Recording video using Intent

```java
Intent intent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
startActivityForResult(intent, 200);
```

### 2. Recording video using MediaRecorder

=> MediaRecorder provides more control over camera, audio source, video source, output format and output file.

### Required permissions

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

### MediaRecorder sequence

1. Create `MediaRecorder`.
2. Set audio source.
3. Set video source.
4. Set output format.
5. Set audio and video encoder.
6. Set output file.
7. Prepare recorder.
8. Start recording.
9. Stop recording.
10. Release recorder.

### Example

```java
MediaRecorder recorder = new MediaRecorder();

recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
recorder.setVideoSource(MediaRecorder.VideoSource.CAMERA);
recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4);
recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AAC);
recorder.setVideoEncoder(MediaRecorder.VideoEncoder.H264);
recorder.setOutputFile(getExternalFilesDir(null) + "/video.mp4");

recorder.prepare();
recorder.start();

// Stop later
recorder.stop();
recorder.release();
```

## **7.9 ANR**

=> **Definition**: `ANR stands for Application Not Responding.`

=> Android shows ANR when an app does not respond to user input for a long time.

### Common reasons

1. Long task on main UI thread.
2. Network operation on main thread.
3. Heavy database operation on main thread.
4. Infinite loop.
5. BroadcastReceiver taking too long.

### Prevention

1. Run heavy work in background thread.
2. Use WorkManager, Executor, Thread or Coroutine.
3. Keep `BroadcastReceiver.onReceive()` short.
4. Avoid blocking UI thread.

## **7.10 Exam Short Questions**

=> **Question**: `What is MediaPlayer?`

=> **Answer**: MediaPlayer is used to play audio and video files or streams in Android.

=> **Question**: `What is SoundPool?`

=> **Answer**: SoundPool is used to play short sound effects with low latency.

=> **Question**: `How can camera be used in Android?`

=> **Answer**: Camera can be used using Camera Intent or Camera API/CameraX.

=> **Question**: `Why is release() important in MediaPlayer?`

=> **Answer**: It frees system resources used by the player.

=> **Question**: `What is VideoView?`

=> **Answer**: VideoView is a UI component used to display and play video.
