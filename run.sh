if [ -f "output.json" ]
then
	rm output.json
    python Device_Info.py
    echo "Detected prior system specs file. Deleted and Replaced with new 'output.json' file containing system specs."
else
    python Device_Info.py
    echo "No prior system specs file detected. Created new 'output.json' file containing system specs."
fi

