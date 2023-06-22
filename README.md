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
* [How to Change EPOC+ hertz modes](https:// github.com/CymatiCorp/CyKit/wiki//How-to-Change-EPOC(plus)--modes)  


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
