import biathlonresults
import json

biathlonresults.api.athletes()

events = biathlonresults.events("2526", level=biathlonresults.consts.LevelType.BMW_IBU_WC)

print(events)