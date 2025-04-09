# 2025-04-09-Missing libusb backend -- due to wrong directory

```cmd
PS C:\Users\pho\repos\EmotivEpoc\CyKit> C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 2
Error loading libusb 1.0 backend
> Driver could not be found or unsuccessfully loaded.
PS C:\Users\pho\repos\EmotivEpoc\CyKit> C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 2 info+verbose
> Importing (pyusb) \cyPyUSB
Error loading libusb 1.0 backend
> Driver could not be found or unsuccessfully loaded.
```

## SOLUTION: just changing directory `cd C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\` solved the issue
```cmd
PS C:\Users\pho\repos\EmotivEpoc\CyKit> cd C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\
PS C:\Users\pho\repos\EmotivEpoc\CyKit\Py3> C:\Users\pho\.pyenv\pyenv-win\versions\3.7.9\python.exe C:\Users\pho\repos\EmotivEpoc\CyKit\Py3\CyKIT.py 127.0.0.1 5555 2 info+verbose
> Importing (pyusb) \cyPyUSB
```




2025-04-09 - 12:53pm - Conclusion: Not working on Apogee and had to give up. Not seeing any packets/data in either the browser or the terminal. Just because it loaded on 
