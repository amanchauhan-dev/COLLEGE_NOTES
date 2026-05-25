# **5 Location Services and Maps**

## **5.1 Location Services**

=> **Definition**: `Location services are Android features used to find the geographical location of a device.`

=> Location is commonly represented using latitude and longitude.

### Uses

1. Maps and navigation.
2. Cab booking.
3. Food delivery.
4. Fitness tracking.
5. Weather apps.
6. Location tagging.
7. Nearby place search.

## **5.2 Location Providers**

=> Android can obtain location from different providers.

### 1. GPS Provider

=> Uses satellites to determine location.

### Advantages

1. More accurate outdoors.
2. Does not depend on mobile network.

### Disadvantages

1. Slow first fix.
2. Consumes more battery.
3. Works poorly indoors.

### 2. Network Provider

=> Uses mobile towers and Wi-Fi networks.

### Advantages

1. Faster than GPS.
2. Works better indoors.
3. Consumes less battery.

### Disadvantages

1. Less accurate than GPS.
2. Depends on network availability.

## **5.3 LocationManager and LocationListener**

=> `LocationManager` provides access to Android location services.

=> `LocationListener` receives updates when location changes.

### LocationListener callbacks

1. `onLocationChanged(Location location)`: Called when location changes.
2. `onProviderEnabled(String provider)`: Called when provider is enabled.
3. `onProviderDisabled(String provider)`: Called when provider is disabled.
4. `onStatusChanged()`: Older callback for provider status changes.

### Required permissions

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

### Example: Get current location

```java
public class MainActivity extends AppCompatActivity {
    TextView txtLocation;
    LocationManager locationManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtLocation = findViewById(R.id.txtLocation);
        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);

        if (ActivityCompat.checkSelfPermission(this,
                Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                    new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1);
            return;
        }

        locationManager.requestLocationUpdates(
                LocationManager.GPS_PROVIDER,
                5000,
                5,
                location -> {
                    double lat = location.getLatitude();
                    double lng = location.getLongitude();
                    txtLocation.setText("Latitude: " + lat + "\nLongitude: " + lng);
                });
    }
}
```

## **5.4 Fused Location Provider**

=> Fused Location Provider is a Google Play Services API that combines GPS, Wi-Fi, mobile network and sensors to provide efficient location.

### Advantages

1. More battery efficient.
2. Automatically chooses best provider.
3. Provides last known location.
4. Good accuracy for most apps.

### Example: Get last location

```java
FusedLocationProviderClient client =
        LocationServices.getFusedLocationProviderClient(this);

if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.ACCESS_FINE_LOCATION)
        == PackageManager.PERMISSION_GRANTED) {

    client.getLastLocation().addOnSuccessListener(location -> {
        if (location != null) {
            double lat = location.getLatitude();
            double lng = location.getLongitude();
        }
    });
}
```

## **5.5 Google Maps in Android**

=> Google Maps can be integrated into Android applications using Google Maps SDK for Android.

### Uses

1. Display map.
2. Show current location.
3. Add markers.
4. Draw routes.
5. Search places.
6. Change map type.

### Basic steps

1. Create project in Google Cloud Console.
2. Enable Maps SDK for Android.
3. Generate API key.
4. Add API key to app.
5. Add `SupportMapFragment` in layout.
6. Implement `OnMapReadyCallback`.

### Layout example

```xml
<fragment
    android:id="@+id/map"
    android:name="com.google.android.gms.maps.SupportMapFragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

### Manifest API key

```xml
<meta-data
    android:name="com.google.android.geo.API_KEY"
    android:value="YOUR_API_KEY" />
```

### Activity example

```java
public class MapsActivity extends AppCompatActivity
        implements OnMapReadyCallback {

    GoogleMap googleMap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);

        SupportMapFragment mapFragment =
                (SupportMapFragment) getSupportFragmentManager()
                        .findFragmentById(R.id.map);

        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap map) {
        googleMap = map;

        LatLng ahmedabad = new LatLng(23.0225, 72.5714);
        googleMap.addMarker(new MarkerOptions()
                .position(ahmedabad)
                .title("Ahmedabad"));
        googleMap.moveCamera(CameraUpdateFactory.newLatLngZoom(ahmedabad, 12));
    }
}
```

## **5.6 Types of Google Maps**

### Map types

1. `GoogleMap.MAP_TYPE_NORMAL`

=> Standard road map.

2. `GoogleMap.MAP_TYPE_SATELLITE`

=> Satellite imagery.

3. `GoogleMap.MAP_TYPE_HYBRID`

=> Satellite imagery with roads and labels.

4. `GoogleMap.MAP_TYPE_TERRAIN`

=> Terrain and topographic details.

5. `GoogleMap.MAP_TYPE_NONE`

=> Empty grid without map tiles.

### Example

```java
googleMap.setMapType(GoogleMap.MAP_TYPE_HYBRID);
```

## **5.7 Google Maps UI Controls**

=> Google Maps provides built-in UI controls.

### Common controls

1. Zoom controls.
2. Compass.
3. My Location button.
4. Map toolbar.
5. Rotate gestures.
6. Scroll gestures.
7. Zoom gestures.

### Example

```java
UiSettings settings = googleMap.getUiSettings();
settings.setZoomControlsEnabled(true);
settings.setCompassEnabled(true);
settings.setMyLocationButtonEnabled(true);
```

### Show current location on map

```java
if (ActivityCompat.checkSelfPermission(this,
        Manifest.permission.ACCESS_FINE_LOCATION)
        == PackageManager.PERMISSION_GRANTED) {
    googleMap.setMyLocationEnabled(true);
}
```

## **5.8 Geocoding**

=> **Definition**: `Geocoding is the process of converting an address or place name into latitude and longitude.`

### Example

```java
Geocoder geocoder = new Geocoder(this);
List<Address> list =
        geocoder.getFromLocationName("Ahmedabad, Gujarat", 1);

if (!list.isEmpty()) {
    double lat = list.get(0).getLatitude();
    double lng = list.get(0).getLongitude();
}
```

### Uses

1. Search address on map.
2. Convert city name to coordinates.
3. Navigation and delivery apps.
4. Place search.

## **5.9 Reverse Geocoding**

=> **Definition**: `Reverse geocoding is the process of converting latitude and longitude into a readable address.`

### Example

```java
Geocoder geocoder = new Geocoder(this);
List<Address> list =
        geocoder.getFromLocation(23.0225, 72.5714, 1);

if (!list.isEmpty()) {
    String address = list.get(0).getAddressLine(0);
}
```

### Difference

| Geocoding | Reverse Geocoding |
|---|---|
| Address to coordinates. | Coordinates to address. |
| Input is place name/address. | Input is latitude and longitude. |
| Example: Ahmedabad -> lat/lng. | Example: lat/lng -> Ahmedabad address. |

## **5.10 Challenges in Location-Based Services**

### Challenges

1. **Battery consumption**

=> GPS and continuous location updates consume battery.

2. **Accuracy**

=> Location may be inaccurate indoors or in dense city areas.

3. **Network dependency**

=> Network provider needs Wi-Fi or mobile network.

4. **Permission handling**

=> App must request location permission and handle denial.

5. **Privacy**

=> Location is sensitive personal data.

6. **Provider disabled**

=> User may disable GPS or location services.

7. **Latency**

=> First location fix can take time.

8. **Background restrictions**

=> New Android versions restrict background location access.

### Good practices

1. Request location only when needed.
2. Stop location updates after use.
3. Use coarse location when exact location is not required.
4. Explain why permission is needed.
5. Use Fused Location Provider for better battery efficiency.

## **5.11 Google Maps vs Google Earth**

| Google Maps | Google Earth |
|---|---|
| Mainly used for navigation and places. | Mainly used for 3D earth visualization. |
| Provides routes, traffic and directions. | Provides rich satellite and 3D imagery. |
| Lightweight for daily use. | More visual and exploration-focused. |

## **5.12 AlarmManager Short Note**

=> AlarmManager is used to schedule work at a specific future time.

=> It fires a `PendingIntent` at the scheduled time.

### Example

```java
AlarmManager alarmManager =
        (AlarmManager) getSystemService(ALARM_SERVICE);

Intent intent = new Intent(this, AlarmReceiver.class);
PendingIntent pendingIntent = PendingIntent.getBroadcast(
        this, 1, intent, PendingIntent.FLAG_IMMUTABLE);

alarmManager.set(
        AlarmManager.RTC_WAKEUP,
        System.currentTimeMillis() + 10000,
        pendingIntent);
```

## **5.13 Exam Short Questions**

=> **Question**: `What is LocationManager?`

=> **Answer**: LocationManager provides access to Android location services.

=> **Question**: `What is GPS provider?`

=> **Answer**: GPS provider uses satellites to determine device location.

=> **Question**: `What is geocoding?`

=> **Answer**: Geocoding converts address or place name into latitude and longitude.

=> **Question**: `What is reverse geocoding?`

=> **Answer**: Reverse geocoding converts latitude and longitude into a readable address.

=> **Question**: `Which permission is used for exact location?`

=> **Answer**: `ACCESS_FINE_LOCATION`.
