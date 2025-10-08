<img src="https://raw.githubusercontent.com/CymatiCorp/CyKit/git-images/Images/CyKIT5.png" width=34% height=34%  />


CyKIT 3.0 for Python 3.x (Linux)
=
Until MAC/Linux support can be integrated into this repository, <br>
Please see this branch for MAC/Linux support. <br>
https://github.com/tahesse/CyKITv2

CyKIT 3.0 for Python 3.7.x (Windows)
=

Last Updated: [ December 27, 2018 - 1:00pm ]

Language Support (Python 3.x)
----------------
```

 Supported Python 3 Versions
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

Python 3.4.x  (32-bit or 64-bit)
Python 3.6.x  (32-bit or 64-bit) 
Python 3.7.x  (32-bit or 64-bit) 
Python 3.8.x  (32-bit or 64-bit) 
Python 3.9.x  (32-bit or 64-bit)

Latest Python Build: Python 3.9.5

Python 2.7.6 support will now be limited.
Python 3+ will be the focus. (Please upgrade accordingly.)

```

Headset Support
----------------
Does not currently work with Epoc-X  <br>
See Discord for details about Flex. 

Program Flowchart
-------------------

<img src="https://raw.githubusercontent.com/CymatiCorp/CyKit/git-images/Images/CyKIT-Flowchart.png" />
(MATLAB/Unity3D plugins have been created, but currently not included in repository) <br><br>

Browser Interface
-------------------

<img src="https://raw.githubusercontent.com/CymatiCorp/CyKit/git-images/Images/CyKIT-Preview.png" />

Documentation
-------------------
```
Introduction
```
* [CyKIT 3.0 (wikipage)](https://github.com/CymatiCorp/CyKit/wiki/CyKIT-3.0-Documentation)
```
Software (How To)
```
* [How to Install CyKIT](https://github.com/CymatiCorp/CyKit/wiki/How-to-Install-CyKIT)
* [How to Stream Data to OpenViBE](https://github.com/CymatiCorp/CyKit/wiki/How-to-Stream-Data-to-OpenViBE)
* [How to Pair USB device](https://github.com/CymatiCorp/CyKit/wiki/How-to-Pair-USB-device)
* [How to Change EPOC+ hertz modes](https://github.com/CymatiCorp/CyKit/wiki//How-to-Change-EPOC(plus)--modes)  


Communication
-
Chat Discussion: https://discordapp.com/invite/gTYNWc7 <br>
(Do not need discord app, just click for browser chat)

Version History
-
Deprecated CyKIT versions can be found here: <br>
[(CyKIT Version History)](https://github.com/CymatiCorp/CyKit/tree/git-images/History/) <br>

```
CyKIT v1.0 python 2.7.6 (2014)
CyKIT v1.0 python 3.3.x (2015)
CyKIT v2.0 Python 2.7.6 (2018.Jan.29)
```

Documentation
-

[Bluetooth Development Documentation](https://github.com/CymatiCorp/CyKit/blob/git-images/Documentation/Bluetooth_Development-Epoc.pdf)


<br><br>

(C:\Users\pho\Anaconda2\envs\nintendoSwitch) C:\Users\pho>conda list -n CyKit-AnacondaPython36
# packages in environment at C:\Users\pho\Anaconda2\envs\CyKit-AnacondaPython36:
#
astroid                   1.5.3                    py36_0
certifi                   2016.2.28                py36_0
isort                     4.2.15                   py36_0
lazy-object-proxy         1.3.1                    py36_0
pip                       9.0.1                    py36_1
pylint                    1.7.2                    py36_0
python                    3.6.2                         0
setuptools                36.4.0                   py36_1
singledispatch            3.4.0.3                  py36_0
six                       1.10.0                   py36_0
vc                        14                            0
vs2015_runtime            14.0.25420                    0
wheel                     0.29.0                   py36_0
wincertstore              0.2                      py36_0
wrapt                     1.10.11                  py36_0


(NeuroPy) C:\Users\pho\repos\EmotivEpoc\CyKit\Py3>python CyKIT.py 127.0.0.1 5555 2
> USB Device (No Additional Information)
> USB Device (No Additional Information)
> USB Device (No Additional Information)
> USB Device (No Additional Information)

> Found EEG Device [Emotiv RAW DATA] 

> USB Device (No Additional Information)
> USB Device (No Additional Information)
> USB Device (No Additional Information)
══════════════════════════════════════════════════

> Listening on 127.0.0.1 : 5555
> Trying Key Model #: 2
(-) Connecting . . .
(+) Connected.

KeyError: Exception in line: 185, message: 'Sec-WebSocket-Key'
Traceback (most recent call last):
  File "C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyWebSocket.py", line 185, in run
    secKey = header['Sec-WebSocket-Key']
KeyError: 'Sec-WebSocket-Key'

127.0.0.1:5555


## 2025-05-01 - Micromamba Apogee Setup Attempt


Added `MAMBA_ROOT_PREFIX` using Rapid Environment Editor for both User Variables and System Variables


```ps1
cd ~/Downloads
Invoke-Webrequest -URI https://micro.mamba.pm/api/micromamba/win-64/latest -OutFile micromamba.tar.bz2
tar xf micromamba.tar.bz2

MOVE -Force Library\bin\micromamba.exe micromamba.exe
.\micromamba.exe --help

# You can use e.g. $HOME\micromambaenv as your base prefix
$Env:MAMBA_ROOT_PREFIX="K:\FastSwap\Environments\micromamba"

# Invoke the hook
.\micromamba.exe shell hook -s powershell | Out-String | Invoke-Expression

# ... or initialize the shell
.\micromamba.exe shell init -s powershell -r K:\FastSwap\Environments\micromamba
# and use micromamba directly
micromamba create -f ./test/env_win.yaml -y
micromamba activate yourenv

```


## Produces

```

PS C:\Users\pho> cd .\bin\
PS C:\Users\pho\bin> .\micromamba.exe shell init -s powershell -r K:\FastSwap\Environments\micromamba
Init powershell profile at 'C:\Users\pho\Documents\WindowsPowerShell\profile.ps1'
The following has been added in your "C:\\Users\\pho\\Documents\\WindowsPowerShell\\profile.ps1" file

#region mamba initialize
# !! Contents within this block are managed by 'mamba shell init' !!
$Env:MAMBA_ROOT_PREFIX = "K:\FastSwap\Environments\micromamba"
$Env:MAMBA_EXE = "C:\Users\pho\bin\micromamba.exe"
(& $Env:MAMBA_EXE 'shell' 'hook' -s 'powershell' -r $Env:MAMBA_ROOT_PREFIX) | Out-String | Invoke-Expression
#endregion

Init pwsh profile at 'C:\Users\pho\Documents\PowerShell\profile.ps1'
The following has been added in your "C:\\Users\\pho\\Documents\\PowerShell\\profile.ps1" file

#region mamba initialize
# !! Contents within this block are managed by 'mamba shell init' !!
$Env:MAMBA_ROOT_PREFIX = "K:\FastSwap\Environments\micromamba"
$Env:MAMBA_EXE = "C:\Users\pho\bin\micromamba.exe"
(& $Env:MAMBA_EXE 'shell' 'hook' -s 'powershell' -r $Env:MAMBA_ROOT_PREFIX) | Out-String | Invoke-Expression
#endregion


```

## Extras

```ps1

cd "C:\Users\pho\repos\EmotivEpoc\CyKit\EXTERNAL\Environments\ALIENBOOK"


micromamba config set ssl_verify false
micromamba create -f cykit_environment.yml

micromamba create -p K:\FastSwap\Environments\micromamba\envs\cykit python=3.6

$Env:MAMBA_ROOT_PREFIX="C:\Users\pho\micromamba"
micromamba create -p C:\Users\pho\micromamba\envs\cykit python=3.


```

# Use with working `$Env:MAMBA_ROOT_PREFIX="C:\Users\pho\micromamba"`

Note: Using the external SSD (I think it's ExFAT formatted) did not work, failing at the linking steps. Had to use the C:/ drive
 
```ps1
$Env:MAMBA_ROOT_PREFIX="C:\Users\pho\micromamba"
micromamba create -f .\cykit_environment_minimal.yml
micromamba activate cykit
```



## 2025-04-14 - Alienbook Export

pip freeze > requirements.txt





```powershell
& c:/Users/pho/repos/EmotivEpoc/CyKit/.venv/Scripts/Activate.ps1
cd .\Py3\   
# python .\CyKIT.py 127.0.0.1 5555 6 info+verbose+bluetooth+allmode+path


python .\CyKIT.py 127.0.0.1 5555 6 info+verbose+bluetooth+allmode+path+outputdata+noweb



```

# Emotiv EEG Bluetooth Flutter App

This Flutter application provides Bluetooth connectivity to Emotiv EEG devices (EPOC+, EPOC, Insight) for real-time EEG and MEMS/motion data streaming.

## Features

- **Bluetooth LE Connectivity**: Connects to Emotiv EEG devices via Bluetooth Low Energy
- **Real-time Data Streaming**: Receives both EEG and MEMS/motion data streams
- **Device Auto-detection**: Automatically finds and connects to compatible Emotiv devices
- **Data Visualization**: Real-time display of received data packets
- **Cross-platform**: Works on both Android and iOS (with appropriate permissions)

## Files Overview

### Core Files

1. **`bluetooth_eeg_service.dart`** - Main service class that handles:
   - Bluetooth device scanning and connection
   - GATT service and characteristic discovery
   - Data streaming setup
   - Sending the `0x100` command to initiate data transmission

2. **`eeg_data_widget.dart`** - Flutter widget that provides:
   - User interface for device connection
   - Real-time data display
   - Connection status monitoring

3. **`pubspec.yaml`** - Dependencies configuration

## Key Conversion Points from Python

### 1. Bluetooth Device Detection
**Python (original):**
```python
getBTname = eegDLL.get_bluetooth_id()
BTid = str(c_wchar_p(getBTname).value)
if "EPOC" in BTid or "Insight" in BTid:
    # Process device
```

**Dart (converted):**
```dart
String deviceName = result.device.platformName;
if (deviceName.contains("EPOC") || deviceName.contains("Insight")) {
    // Process device
}
```

### 2. Device ID Parsing
**Python (original):**
```python
BTid = BTid.replace("(","").replaceAll(")","")
BT_key = BTid.split(" ")
BTLE_device_name = BT_key[0]
BT_key = BT_key[1]
```

**Dart (converted):**
```dart
String btId = deviceName;
btId = btId.replaceAll("(", "").replaceAll(")", "");
List<String> btKey = btId.split(" ");
btleDeviceName = btKey[0];
String btKeyValue = btKey[1];
```

### 3. Serial Number Creation
**Python (original):**
```python
self.serial_number = bytes(("\x00" * 12),'utf-8') + bytearray.fromhex(str(BT_key[6:8] + BT_key[4:6] + BT_key[2:4] + BT_key[0:2]))
```

**Dart (converted):**
```dart
Uint8List zeros = Uint8List(12);
String reversedKey = btKey.substring(6, 8) + 
                    btKey.substring(4, 6) + 
                    btKey.substring(2, 4) + 
                    btKey.substring(0, 2);
List<int> keyBytes = [];
for (int i = 0; i < reversedKey.length; i += 2) {
    keyBytes.add(int.parse(reversedKey.substring(i, i + 2), radix: 16));
}
Uint8List serialNumber = Uint8List.fromList([...zeros, ...keyBytes]);
```

### 4. BLE Command (0x100)
**C++ (original):**
```cpp
newValue.Data[0] = 0x100;
```

**Dart (converted):**
```dart
Uint8List startCommand = Uint8List.fromList([0x00, 0x01, 0x00, 0x00]); // 0x100 in little-endian
await characteristic.write(startCommand, withoutResponse: true);
```

## Setup Instructions

### 1. Install Dependencies
```bash
flutter pub get
```

### 2. Platform Permissions

#### Android (`android/app/src/main/AndroidManifest.xml`)
```xml
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
<uses-permission android:name="android.permission.BLUETOOTH_SCAN" />
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

<uses-feature android:name="android.hardware.bluetooth_le" android:required="true" />
```

#### iOS (`ios/Runner/Info.plist`)
```xml
<key>NSBluetoothAlwaysUsageDescription</key>
<string>This app needs Bluetooth to connect to EEG devices</string>
<key>NSBluetoothPeripheralUsageDescription</key>
<string>This app needs Bluetooth to connect to EEG devices</string>
```

### 3. Usage Example

```dart
import 'package:flutter/material.dart';
import 'eeg_data_widget.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Emotiv EEG App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: EEGDataWidget(),
    );
  }
}
```

## Key Features

### 1. UUIDs Used
- **Device Service UUID**: `{81072f40-9f3d-11e3-a9dc-0002a5d5c51b}`
- **EEG Data UUID**: `{81072f41-9f3d-11e3-a9dc-0002a5d5c51b}`
- **MEMS Data UUID**: `{81072f42-9f3d-11e3-a9dc-0002a5d5c51b}`

### 2. Data Streams
- **EEG Data**: Real-time brain wave data from the headset
- **MEMS Data**: Motion and accelerometer data from the headset

### 3. Connection Process
1. Scan for Bluetooth devices
2. Filter for Emotiv devices (EPOC, Insight)
3. Parse device ID and extract Bluetooth key
4. Connect to device and discover GATT services
5. Subscribe to EEG and MEMS characteristics
6. Send `0x100` command to start data streaming
7. Receive and process incoming data

## Troubleshooting

### Common Issues

1. **Bluetooth not supported**: Ensure device has Bluetooth LE capability
2. **Permission denied**: Check platform-specific permissions
3. **Device not found**: Ensure Emotiv device is paired and discoverable
4. **Connection timeout**: Try reconnecting or check device battery

### Debug Information

The app provides detailed console output for debugging:
- Device discovery process
- Connection status
- Data packet information
- Error messages

## Dependencies

- `flutter_blue_plus`: Bluetooth LE functionality
- `typed_data`: For byte array manipulation
- `flutter`: Core Flutter framework

## License

This code is converted from the original CyKit Python implementation and maintains the same functionality for Emotiv EEG device connectivity.




--------

```
cd .\Py3
python .\CyKIT.py 127.0.0.1 5555 6 info+verbose+bluetooth+allmode+path+outputdata+noweb

```


```
----
# Packet 23209 from C:\Users\pho\AppData\Local\Temp\wireshark_nRF Sniffer for Bluetooth LE COM8LGSID3.pcapng
- 23210
- 191.850095
- Intel_b7:b9:1a
- c7:52:c2:63:6a:84
- LE LL
- 60
- 
- CONNECT_IND
```


btle.access_address == 0x8e89bed6

btatt


### 
1. Why use the Access Address?

Every BLE connection gets a unique 32-bit access address (different from the advertising address/MAC).

All data channel packets (after CONNECT_IND) will carry that access address.

Filtering on it isolates only that connection, even if other BLE devices are nearby.

2. Where to find it in Wireshark

Click on your CONNECT_IND packet.

Expand the Link Layer (LE LL) section in the packet details pane.

You’ll see a field like:

Access Address: 0x8e89bed6


(example value — yours will differ).

3. Apply the filter

Once you have that value, apply this display filter:

btle.access_address == 0x8e89bed6


(replace with your actual hex value).

Now Wireshark will show only packets from the Epoc+ connection.

4. Combine with higher-level filters

If you want only specific traffic within that connection:

Show ATT/GATT messages from that connection:

btatt && btle.access_address == 0x8e89bed6


Show only L2CAP data:

btl2cap && btle.access_address == 0x8e89bed6


### Main Address
```
btle.access_address == 0x8e89bed6
```