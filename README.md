# Device Info Activity
Execution of the "run.sh" file will run the "Device_Info.py" script. This script will populate a JSON file containing various system specs for whichever device it is run on.

The shell script first checks to see if an "output.json" file exists. If so, it deletes the old one and runs the python script to create a new one. If not, it simply runs the python script and creates one.