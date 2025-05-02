Headset: EmotivEpoc+ - Performed all while off head, on battery
RecieverUSB: Epoc+ Green Circle Sticker - connected via ~3ft USB extender, plugged into internal Apogee USB ports

Issue 1 - VM Not starting - Resolved - Had issues starting my previously working VirtualBox "EmotivWindows" machine, despite not changing anything from before. Fixed this by reboot the host (Apogee) machine, after which the VM started without any changes.

Finally, got "EmotivWindows" working completely by passing the USB reciever to the VM USB.
I confirmed that EEG signals were plotting in the browser.
`CMD.exe` window looks like: 
```bat

C:\Users\pho\repos\CyKit>CALL C:\Users\pho\repos\CyKit\.venv\Scripts\activate.bat

(CyKit) C:\Users\pho\repos\CyKit>cd "C:\Users\pho\repos\CyKit\Py3"

(CyKit) C:\Users\pho\repos\CyKit\Py3>python C:\Users\pho\repos\CyKit\Py3\CyKIT.py 127.0.0.1 5555 6

> Found EEG Device [EEG Signals]

══════════════════════════════════════════════════

> Listening on 127.0.0.1 : 5555
> Trying Key Model #: 6
(-) Connecting . . .
(+) Connected.
```
when running `PhoCyKitRun-OriginalEpoc-ForBrowser.bat`

Took an online snapshot of the VM.

After the snapshot finished, I tried running again with nothing changed, and kept getting
```bat

 ░░░ Device Interference or Turned Off ░░░ 
```
a few seconds after connecting via the browser despite the CMD.exe window looking identical otherwise, and running IDENTICAL scripts that I just tested.

Trying again a few seconds later led to it WORKING.

Running with `info+verbose` while working (confirmed plots) produced:
```bat
C:\Users\pho\repos\CyKit>CALL C:\Users\pho\repos\CyKit\.venv\Scripts\activate.bat

(CyKit) C:\Users\pho\repos\CyKit>cd "C:\Users\pho\repos\CyKit\Py3"

(CyKit) C:\Users\pho\repos\CyKit\Py3>python C:\Users\pho\repos\CyKit\Py3\CyKIT.py 127.0.0.1 5555 6 info+verbose
> Importing (pyusb) \cyPyUSB
══════════════════════════════════════════════════
 Company: Emotiv
  Device: EEG Signals
  Vendor: 0x1234
 Product: 0xed02

> Found EEG Device [EEG Signals]

[32, 13, 6, 255, 6, 38, 59, 154, 204, 166, 43, 1, 128, 0, 16, 32, 16]
 Device Firmware = 0x6ff
 Software Firmware = 0x626
> Using Device: EEG Signals

 ░░ Serial Number: UD201502090001F6 ░░

══════════════════════════════════════════════════
 Company: VirtualBox
  Device: USB Tablet
  Vendor: 0x80ee
 Product: 0x21
══════════════════════════════════════════════════
 Company: None
  Device: None
  Vendor: 0x8086
 Product: 0x1e31
══════════════════════════════════════════════════════════════════════════════════════════
   AES Key = [54, 70, 70, 49, 49, 49, 70, 48, 54, 48, 70, 70, 48, 48, 70, 54]
    Format = 0
 Delimiter = ,
══════════════════════════════════════════════════════════════════════════════════════════

 Config Options = {

   blankdata            False
   blankcsv             False
   nocounter            False
   nobattery            False
   baseline             False
   noheader             False
   integer              False
   outputdata           False
   generic              False
   openvibe             False
   baseline             False
   outputraw            False
   filter               False
   allmode              False
   eegmode              False
   gyromode             False
   verbose               True  *
   noweb                False

 }
══════════════════════════════════════════════════

> Listening on 127.0.0.1 : 5555
> Trying Key Model #: 6
(-) Connecting . . .
(+) Connected.


Active Threads = {
   ['MainThread', 'ioThread', 'eegThread']
}

 Cipher Key = [54, 70, 70, 49, 49, 49, 70, 48, 54, 48, 70, 70, 48, 48, 70, 54]
CLIENT >>> CyKITv2.setDataMode.1
>>> Client Setting >>> DataMode = 1
CLIENT >>> CyKITv2.setBaselineMode.0
CLIENT >>> CyKITv2.setBaselineMode.0
CLIENT >>> CyKITv2.setBaselineMode.0
```




