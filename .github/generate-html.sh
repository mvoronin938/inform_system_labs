#!/bin/bash

# Execute the Python script and capture its output
#python_output=$(python3 lab2/main.py)

echo $python_output

mkdir .github/out

# Use `sed` to replace the {{output}} placeholder with the Python output
sed "s/{{test}}/$(echo $(python3 lab2/main.py))/" .github/report-template.html > .github/out/output.html
