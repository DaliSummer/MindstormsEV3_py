#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile

# Create your objects here.
ev3 = EV3Brick()

# set speaker volume 50%
ev3.speaker.set_volume(50)

# adjust speech
ev3.speaker.set_speech_options(language="en", voice="whisperf", speed=19, pitch=60)
# say
ev3.speaker.say("Robot love minecraft")

# adjust speech
ev3.speaker.set_speech_options("ru", "f4", 29, 99)
# say again
ev3.speaker.say("Робот любит майнкррррррррафт")

# set speaker volume 10%
ev3.speaker.set_volume(10)

# Plays a sequence of musical notes
ev3.speaker.play_notes(['E4/4', 'E4/4', 'E4/2'], 150)
ev3.speaker.play_notes(['E4/4', 'E4/4', 'E4/2'], 150)
ev3.speaker.play_notes(['E4/4', 'G4/4', 'C4/4', 'D4/4'], 150)
ev3.speaker.play_notes(['E4/1'], 150)
ev3.speaker.play_notes(['F4/4', 'F4/4', 'F4/4', 'F4/4'], 150)
ev3.speaker.play_notes(['F4/4', 'E4/4', 'E4/4', 'E4/8', 'E4/8'], 150)
ev3.speaker.play_notes(['E4/4', 'D4/4', 'D4/4', 'E4/4'], 150)
ev3.speaker.play_notes(['D4/2', 'G4/4'], 150)

# Plays music from file
ev3.speaker.play_file(SoundFile.FANTASTIC)
ev3.speaker.play_file("../data/pcm0808m.wav")
ev3.speaker.play_file("../data/a2002011001-e02.wav")
