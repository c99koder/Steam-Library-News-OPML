# Steam-Library-News-OPML

Generate an OPML file containing the RSS news links for every game in your Steam library

## Configuration

Register for an API key at https://steamcommunity.com/dev/apikey and look up your SteamID at https://steamidfinder.com/ (use the `steamID64 (Dec)` value).  Open `config.py` and set your API credentials at the top of the file.

## Usage

Check your Python version and make sure version 3.7 or newer is installed on your system:

```shell
$ python3 --version
```

Install required python3 modules:

```shell
$ pip3 install requests colorlog
```

Run the Python script from the terminal and it will output the OPML file.
Redirect the output to a file to save it and then import it into your RSS reader.

```shell
$ python3 ./opml.py > ~/steam.opml
```

# License

Copyright (C) 2023 Sam Steele. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
