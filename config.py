#!/usr/bin/python3
# Copyright 2023 Sam Steele
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys, logging, colorlog

# Steam configuration
STEAM_API_KEY = ''
STEAM_ID = ''
STEAM_LANGUAGE = 'en'

# Logging configuration
LOG_LEVEL = logging.WARNING
LOG_FORMAT = '%(asctime)s %(log_color)s%(message)s'
LOG_COLORS = {
    'WARNING':  'yellow',
    'ERROR':    'red',
    'CRITICAL': 'red',
	}

if sys.stdout.isatty():
    colorlog.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT, log_colors=LOG_COLORS, stream=sys.stderr)
else:
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT.replace(f'%(log_color)s', ''), stream=sys.stderr)

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
