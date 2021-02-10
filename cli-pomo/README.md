# POMODORO CLI

A simple **CLI** pomodoro app.

## Pomodoro
The **Pomodoro Method** is a study method, based on the use of a kitchen tomato (Pomodoro)

This method  divides your working time in small work/break cycles, usually 25 minutes for a work session, 5 minutes for a small break and 10 minutes for a long break (usually made after 3-4 small breaks)

## Technology

Languages: Python3, Json

Modules: tqdm, colorama, playsound, time, os, sys, json

## Usage

### Instalation
- Download/Clone this repository
- Open a terminal window on the directory where the repo is located
- Install the modules in [**requirements.txt**](./requirements.txt)
    ```
    pip3 install -r requirements.txt
    ```

### Running
The base command to run this app is:
```
python3 "path to pomo.py"
```
You can also provide several flags to change the behavior of the app:
    
- **-h** or **--help** --> show the various options
- **-s** or **--settings** --> you will be prompt the values (minutes) you want each work/break to take
- **-r** or **--reset** --> the work/break values will be set to default (25, 5, 10, 3) and the data will be deleted
- **-d** or **--data** --> the time you have spent on each activity will be dumped on the console
- **number** **string** --> a pomodoro with ***number*** cycles will be started and the time spend on this will be stored on the corresponding ***string***
- **number** --> a pomodoro with ***number*** cycles will be started and at the end tyou will be asked for a ***string***