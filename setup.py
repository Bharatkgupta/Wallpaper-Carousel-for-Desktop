import datetime as dt
import win32com.client
import os

Path = input("Enter Python PATH(location of python.exe ex. 'C:\Program Files\Python39\python.exe')\n-> ")

#Connection to Task Scheduler
task = win32com.client.Dispatch('Schedule.Service')
task.Connect()
root_folder = task.GetFolder('\\')
newtask = task.NewTask(0)

# Trigger
dt_obj = dt.datetime.now()
tm_obj = dt.datetime.strptime("14:00:00", "%H:%M:%S")
start_boundary = "{}T{}".format(dt_obj.strftime("%Y-%m-%d"), tm_obj.strftime("%H:%M:%S"))
TASK_TRIGGER_DAILY = 2
trigger = newtask.Triggers.Create(TASK_TRIGGER_DAILY)
trigger.StartBoundary = start_boundary

# Action
TASK_ACTION_EXEC = 0
action = newtask.Actions.Create(TASK_ACTION_EXEC)
dir_path = os.getcwd()
action.Path = Path
action.Arguments = "downloader.py"
action.WorkingDirectory = os.getcwd()

# Parameters
newtask.RegistrationInfo.Author = "Bharat Kumar Gupta"
newtask.RegistrationInfo.Description = 'Desktop Wallpaper Downloader for Windows 10/8/7'
newtask.Settings.Enabled = True
newtask.Settings.Hidden = True
newtask.Settings.RunOnlyIfIdle = False
newtask.Settings.DisallowStartIfOnBatteries = False
newtask.Settings.StopIfGoingOnBatteries = False
newtask.Settings.RunOnlyIfNetworkAvailable = True
newtask.Settings.AllowDemandStart = True
newtask.Settings.StartWhenAvailable = True
newtask.Settings.RestartInterval = "PT1H"
newtask.Settings.RestartCount = 5

# Saving
TASK_CREATE_OR_UPDATE = 6
TASK_LOGON_NONE = 0
root_folder.RegisterTaskDefinition(
    'Wallpaper_Downloader',
    newtask,
    TASK_CREATE_OR_UPDATE,
    '',  # No user
    '',  # No password
    TASK_LOGON_NONE)