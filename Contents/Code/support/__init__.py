import sys
# thanks, https://github.com/trakt/Plex-Trakt-Scrobbler/blob/master/Trakttv.bundle/Contents/Code/core/__init__.py

import config

sys.modules["support.config"] = config

import helpers

sys.modules["support.helpers"] = helpers

import lib

sys.modules["support.lib"] = lib

import plex_media
sys.modules["support.plex_media"] = plex_media

import localmedia

sys.modules["support.localmedia"] = localmedia

import subtitlehelpers

sys.modules["support.subtitlehelpers"] = subtitlehelpers

import items

sys.modules["support.items"] = items

import missing_subtitles

sys.modules["support.missing_subtitles"] = missing_subtitles

import scheduler

sys.modules["support.scheduler"] = scheduler

import tasks

sys.modules["support.tasks"] = tasks

import storage

sys.modules["support.storage"] = storage

import ignore

sys.modules["support.ignore"] = ignore

import history

sys.modules["support.history"] = history

import data

sys.modules["support.data"] = data

import activities
sys.modules["support.activities"] = activities

import download
sys.modules["support.download"] = download
