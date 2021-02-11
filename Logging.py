from pathlib import Path
import datetime

workdir = Path.cwd()

def logging(severity, Messange):
    directoryExist = Path.exists(workdir / 'Logs')
    severityString = 'UNKNOWN'
    currentDate = datetime.datetime.today().strftime ('%Y-%m-%d')
    currentTime = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S,%f')
    if not directoryExist:
        Path.mkdir(workdir / 'Logs')
    logFileName = currentDate + '-daily-log.log'
    fileExist = Path.exists(workdir / 'Logs' / logFileName)
    if severity == 1:
        severityString = 'DEBUG'
    elif severity == 2:
        severityString = 'INFORMATION'
    elif severity == 3:
        severityString = 'ERROR'
    else:
        severityString = 'UNKNOWN'
    if fileExist:
        with open(workdir / 'Logs' / logFileName, 'a+', encoding="utf8") as log_file:
            log_file.write(currentTime + ':' + severityString + ': ' + Messange + '\n')
    else:
        with open(workdir / 'Logs' / logFileName, 'w', encoding="utf8") as log_file:
            log_file.write(currentTime + ':' + severityString + ': ' + Messange + '\n')
logging(2, 'Script has been start!')

logging(2, 'Script has been stop!')
