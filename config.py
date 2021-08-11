import tempfile

# User settings
completedAppendStart: str = "compressed_"
completedAppendEnd: str = ""
extenionsList: list[str] = [".mp4",".avi",".mov",".wmv",".mkv",".webm",".flv",".vob",".ogg",".avi",".drc",".gif",".gifv",".mng",".mts",".m2ts",".ts",".mov",".qt",".wmv",".yuv",".rm",".rmvb",".viv",".asf",".amv",".m4p",".m4v",".mpg",".mp2",".mpeg",".mpe",".mpv",".m2v",".m4v",".svi",".3gp",".3g2",".mxf",".roq",".nsv",".flv",".f4v",".f4p",".f4a",".f4b"]
extenionsOutputList: list[str] = [".mp4",".avi",".ogv",".webm",".mkv"]

# Testing settings
verboseLogs: bool = False

# Video compression settings
presetSettingLow: str = "slow" # difference between ultrafast and slow is like 17mins and 50 mb on a movie
bitrateSettingLow: str = "500k"
audiobitrateSettingLow: str = "130k"
resizeHeightLow: int = 480

# Default variables specific to this program. Do not touch unless you know what you're doing.
stepProgressSecondsDefault: float = 3
trialMinSeconds: float = 3600 #Default to 0
averageEndTimePerInputMin: float = 1
averageProcessTimePerMin: float = 2.2
progressStages: list[int] = [96]
tempDirectory: str = tempfile.gettempdir() + "\\brollgentemp\\"
concatentateDuration: float = 1800
fadesDefaultSeconds: float = 0.01
