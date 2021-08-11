import time
import numpy as np
import random
from moviepy.editor import VideoFileClip, concatenate, AudioFileClip
import os

import config

class editing:
    def compress(self, INPUTFILEPATHListed, EDITOUTPUTFILEPATHListed, EDITQUALITY: int = 0, gui_queue=None):
        # Start of compressing
        self.INPUTFILEPATHListed: str = INPUTFILEPATHListed
        self.EDITOUTPUTFILEPATHListed: str = EDITOUTPUTFILEPATHListed
        self.EDITQUALITY: int = EDITQUALITY
        self.final = VideoFileClip(self.INPUTFILEPATHListed)

        if self.final.duration > config.trialMinSeconds > 0:
            self.final = self.final.subclip(0, config.trialMinSeconds)

        # Settings for video to be compressed to
        self.fpsSetting: float = self.final.fps
        if self.EDITQUALITY == 0:
            self.presetSetting: str = config.presetSettingLow # difference between ultrafast and slow is like 17mins and 50 mb on a movie
            self.bitrateSetting: str = config.bitrateSettingLow
            self.audiobitrateSetting: str = config.audiobitrateSettingLow
            if self.final.fps > 50:
                self.fpsSetting: float = self.final.fps / 2
            self.final = self.final.resize(height=config.resizeHeightLow)
        else:
            self.presetSetting: str = config.presetSettingLow # difference between ultrafast and slow is like 17mins and 50 mb on a movie
            self.bitrateSetting: str = config.bitrateSettingLow
            self.audiobitrateSetting: str = config.audiobitrateSettingLow
            if self.final.fps > 50:
                self.fpsSetting: float = self.final.fps / 2
            self.final = self.final.resize(height=config.resizeHeightLow)
        # moviepy parameter details: https://zulko.github.io/moviepy/_modules/moviepy/video/VideoClip.html#VideoClip.write_videofile
        #self.final.write_videofile(self.EDITOUTPUTFILEPATHListed, preset=self.presetSetting, bitrate=self.bitrateSetting, audio_bitrate=self.audiobitrateSetting, fps=self.fpsSetting)  # low quality is the default
        self.final.to_videofile(self.EDITOUTPUTFILEPATHListed, audio_bitrate=self.audiobitrateSetting, preset=self.presetSetting, bitrate=self.bitrateSetting, fps=self.fpsSetting)
        # End of compressing
        VideoFileClip(self.INPUTFILEPATHListed).close()
        return
