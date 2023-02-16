@REM @REM Alienbook Pre 2023-02-16
@REM CALL C:\Users\pho\Anaconda2\Scripts\activate.bat C:\Users\pho\Anaconda2\envs\CyKit-AnacondaPython36
@REM cd C:\Users\pho\bin\CyKit-master\Py3\
@REM REM Python.exe C:\Users\pho\bin\CyKit-master\Py3\CyKIT.py 127.0.0.1 5555 2 openvibe+nocounter+noheader+nobattery+ovdelay:100+float+ovsamples:004
@REM Python.exe C:\Users\pho\bin\CyKit-master\Py3\CyKIT.py 127.0.0.1 5555 2 openvibe+generic+nocounter+noheader+nobattery+integer+ovsamples:004


@REM Apogee 2023-02-16
@REM pyenv install 3.7.9

cd C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\
@REM pyenv local 3.7.9 @REM # Breaks Execution
@REM pyenv exec python --version
@REM pyenv exec python 

@REM # Find Python Executable Location by doing:
@REM C:\Users\pho\repos\EmotivEpoc\CyKit\Py3>pyenv which python
@REM 	C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe

C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 2 openvibe+generic+nocounter+noheader+nobattery+integer+ovsamples:004

PAUSE