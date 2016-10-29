#!/usr/bin/env python

import os
import pylast

network = pylast.LastFMNetwork(api_key=os.environ["LAST_API_KEY"],
                               api_secret=os.environ["LAST_API_SECRET"],
                               username=os.environ["LAST_USERNAME"],
                               password_hash=os.environ["LAST_PASSWORD"])

now = network.get_authenticated_user().get_now_playing()

print now
