[![Build Status](https://travis-ci.org/SaltieRL/carball.svg?branch=master)](https://travis-ci.org/SaltieRL/carball)
[![PyPI version](https://badge.fury.io/py/carball.svg)](https://badge.fury.io/py/carball)
[![codecov](https://codecov.io/gh/SaltieRL/carball/branch/master/graph/badge.svg)](https://codecov.io/gh/SaltieRL/carball)
[![Build status](https://ci.appveyor.com/api/projects/status/jxsa56l11fxv4jn4/branch/master?svg=true)](https://ci.appveyor.com/project/SaltieRL/carball/branch/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/SaltieRL/carball.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/SaltieRL/carball/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/SaltieRL/carball.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/SaltieRL/carball/alerts/)


# carball
Carball is an open-source project that combines multiple tools for decompiling Rocket League replays and then analysing them.

## Requirements

- Python 3.6.7+ (3.7 and 3.8 included)
- Windows, Mac or Linux

## Install

#### Install from pip:

`pip install carball`

#### Clone for development

##### Windows
```
git clone https://github.com/SaltieRL/carball
cd carball/
python init.py
```

##### Linux
```
git clone https://github.com/SaltieRL/carball
cd carball/
./_travis/install-protoc.sh
python init.py
```

## Examples / Usage
One of the main data structures used in carball is the pandas.DataFrame, to learn more, see [its wiki page](https://github.com/SaltieRL/carball/wiki/data_frame).

Decompile and analyze a replay:
```Python
import carball

analysis_manager = carball.analyze_replay_file('9EB5E5814D73F55B51A1BD9664D4CBF3.replay', 
                                      output_path='9EB5E5814D73F55B51A1BD9664D4CBF3.json', 
                                      overwrite=True)
proto_game = analysis_manager.get_protobuf_data()

# you can see more example of using the analysis manager below

```

Just decompile a replay to a JSON object:

```Python
import carball

_json = carball.decompile_replay('9EB5E5814D73F55B51A1BD9664D4CBF3.replay', 
                                output_path='9EB5E5814D73F55B51A1BD9664D4CBF3.json', 
                                overwrite=True)
```

Analyze a JSON game object:
```Python
import carball
import os
import gzip
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
# _json is a JSON game object (from decompile_replay)
game = Game()
game.initialize(loaded_json=_json)

analysis_manager = AnalysisManager(game)
analysis_manager.create_analysis()

# write proto out to a file
# read api/*.proto for info on the object properties
with open(os.path.join('output.pts'), 'wb') as fo:
    analysis_manager.write_proto_out_to_file(fo)
    
# write pandas dataframe out as a gzipped numpy array
with gzip.open(os.path.join('output.gzip'), 'wb') as fo:
    analysis_manager.write_pandas_out_to_file(fo)
    
# return the proto object in python
proto_object = analysis_manager.get_protobuf_data()

# return the proto object as a json object
json_oject = analysis_manager.get_json_data()

# return the pandas data frame in python
dataframe = analysis_manager.get_data_frame()
```

### Command Line

Carball comes with a command line tool to analyze replays. To use carball from the command line:

```bash
carball -i 9EB5E5814D73F55B51A1BD9664D4CBF3.replay --json analysis.json
```

To get the analysis in both json and protobuf and also the compressed replay frame data frame:

```bash
carball -i 9EB5E5814D73F55B51A1BD9664D4CBF3.replay --json analysis.json --proto analysis.pts --gzip frames.gzip
```

#### Command Line Arguments

```
usage: carball [-h] -i INPUT [--proto PROTO] [--json JSON] [--gzip GZIP] [-sd]
               [-v] [-s]

Rocket League replay parsing and analysis.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to replay file that will be analyzed. Carball
                        expects a raw replay file unless --skip-decompile is
                        provided.
  --proto PROTO         The result of the analysis will be saved to this file
                        in protocol buffers format.
  --json JSON           The result of the analysis will be saved to this file
                        in json file format. This is not the decompiled replay
                        json from rattletrap.
  --gzip GZIP           The pandas dataframe will be saved to this file in a
                        compressed gzip format.
  -sd, --skip-decompile
                        If set, carball will treat the input file as a json
                        file that Rattletrap outputs.
  -v, --verbose         Set the logging level to INFO. To set the logging
                        level to DEBUG use -vv.
  -s, --silent          Disable logging altogether.
```

## Pipeline
![pipeline is in Parserformat.png](Parser%20format.png)

If you want to add a new stat it is best to do it in the advanced stats section of the pipeline.
You should look at:

[Stat base classes](carball/analysis/stats/stats.py)

[Where you add a new stat](carball/analysis/stats/stats_list.py)

If you want to see the output format of the stats created you can look [here](api)

Compile the proto files by running in this directory
`setup.bat` (Windows) or `setup.sh` (Linux/mac)

[![Build Status](https://travis-ci.org/SaltieRL/carball.svg?branch=master)](https://travis-ci.org/SaltieRL/carball)
[![codecov](https://codecov.io/gh/SaltieRL/carball/branch/master/graph/badge.svg)](https://codecov.io/gh/SaltieRL/carball)


## Tips

Linux set `python3.6` as `python`:
```Python3
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
```
This assumes you already have 3.6 installed.

Linux Error (Potential):
`PermissionError: [Errno 13] Permission denied: 'carball/rattletrap/rattletrap-6.2.2-linux'`
Fix:
`chmod +x "carball/rattletrap/rattletrap-6.2.2-linux"`


## Developing
Everyone is welcome to join the carball (and calculated.gg) project! Even if you are a beginner, this can be used as an opportunity to learn more - you just need to be willing to learn and contribute.

### Learning about carball
Currently, there is active creation of the carball wiki on GitHub - it aims to provide all relevant information about carball and development, so if you are a beginner, definitely have a look there. If you can't find information that you were looking for, your next option is the calculated.gg Discord server, where you may send a message to the #help channel.

The carball code is also documented, although sparsely. However, you still may find information there, too.

### Testing
The main requirement is to run PyTest. If you are using an IDE that supports integrated testing (e.g. PyCharm), you should enable PyTest there. 

If you've never tested your code before, it is a good idea to learn that skill with PyTest! Have a look at their official documentation, or any other tutorials. 

### carball Performance
Carball powers calculated.gg, which analyses tens of thousands of replays per day. Therefore, performance is very important, and it is monitored and controlled using PyTest-Benchmarking, which is implemented via GitHub Actions. However, you may see your contribution's performance locally - look into PyTest-Benchmarking documentation. If your contribution is very inefficient - it will fail automatically.

If you wish to see the current carball analysis performance, it is split into 5 replay categories, and can be accessed below:
* [Short Sample](https://saltierl.github.io/carball/dev/bench/short_sample/)
  * A very short soccar replay - for fast benchmarking.
* [Short Dropshot](https://saltierl.github.io/carball/dev/bench/short_dropshot/)
  * A very short dropshot replay - to test dropshot performance.
* [Rumble](https://saltierl.github.io/carball/dev/bench/full_rumble/)
  * A full game of rumble - to test rumble performance.
* [RLCS](https://saltierl.github.io/carball/dev/bench/oce_rlcs/)
  * A full soccar RLCS game.
* [RLCS (Intensive)](https://saltierl.github.io/carball/dev/bench/oce_rlcs_intensive/)
  * A full soccar RLCS game, but run with the intense analysis flag.
