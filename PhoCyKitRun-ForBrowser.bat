@REM @REM Alienbook Pre 2023-02-16
CALL C:\Users\pho\Anaconda2\Scripts\activate.bat C:\Users\pho\Anaconda2\envs\CyKit-AnacondaPython36
cd C:\Users\pho\bin\CyKit-master\Py3\
@REM Python.exe C:\Users\pho\bin\CyKit-master\Py3\CyKIT.py 127.0.0.1 5555 2
Python.exe C:\Users\pho\bin\CyKit-master\Py3\CyKIT.py 127.0.0.1 5555 6


@REM Apogee 2023-02-16
@REM cd C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\
@REM C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 2
@REM I'm confused because I thought it was supposed to be 6 for the Epoc+
@REM C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 2 info+pywinusb+verbose
@REM C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 5 info+verbose

@REM Use the correct Keymodel (6 is used for EPOC+ in 16-bit mode, 7 would be used for EPOC+ 14-bit EPOC mode)
@REM Premium models are likely prototypes, that are not often used. If you are in doubt, always try the consumer model.
@REM 	1 - Epoc    (Premium  Model)
@REM 	2 - Epoc    (Consumer Model)
@REM 	3 - Insight (Premium  Model)
@REM 	4 - Insight (Consumer Model)
@REM 	5 - Epoc+   (Premium  Model)
@REM 	6 - Epoc+   (Consumer Model) [16-bit EPOC+ mode]
@REM 	7 - EPOC+   (Consumer Model) [14-bit EPOC  mode]



@REM info+generic+outputdata
@REM 2 stands for consumer model
@REM pywinusb

@REM outputdata - Seems to dump the raw output data to the CMD console. 

@REM 127.0.0.1:5555
@REM python.exe .\CyKIT.py 127.0.0.1 5555 6 outputdata+noweb


PAUSE