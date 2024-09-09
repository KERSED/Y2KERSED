Y2KERSED is prankware developed by Kersed. This malware makes the target Windows system randomly play AIM audio files from the 90s and early 00s. Kill switch can be enabled by setting system clock between 2000-01-01 00:00:00 and 2000-01-02 00:00:00.

In order to create an executable file that runs without the console on the victims machine you will need to run the Python file through pyinstaller.exe using the command below:

pyinstaller.exe Y2KAudioPlugin.py --onefile --noconsole

This is for educational purposes only. Users should ensure they adhere to all applicable laws when using the information provided.
