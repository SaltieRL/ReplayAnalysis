import argparse
import carball
import logging
import gzip
import json
import numpy as np
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from google.protobuf.json_format import _Printer


class CarballJsonEncoder(json.JSONEncoder):
    def default(self, o):
        # it cannot normally serialize np.int64 and possibly other np data types
        if type(o).__module__ == np.__name__:
            return o.item()
        return super(CarballJsonEncoder, self).default(o)


def main():
    parser = argparse.ArgumentParser(description='Rocket League replay parsing and analysis.')
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Path to replay file that will be analyzed. Carball expects a raw replay file unless '
                             '--skip-decompile is provided.')
    parser.add_argument('--proto', type=str, required=False,
                        help='The result of the analysis will be saved to this file in protocol buffers format.')
    parser.add_argument('--json', type=str, required=False,
                        help='The result of the analysis will be saved to this file in json file format. This is not '
                             'the decompiled replay json from rattletrap.')
    parser.add_argument('--gzip', type=str, required=False,
                        help='The pandas data frame containing the replay frames will be saved to this file in a '
                             'compressed gzip format.')
    parser.add_argument('-sd', '--skip-decompile', action='store_true', default=False,
                        help='If set, carball will treat the input file as a json file that Rattletrap outputs.')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='Set the logging level to INFO. To set the logging level to DEBUG use -vv.')
    parser.add_argument('-s', '--silent', action='store_true', default=False,
                        help='Disable logging altogether.')
    args = parser.parse_args()

    if not args.proto and not args.json and not args.gzip:
        parser.error('at least one of the following arguments are required: --proto, --json, --gzip')

    log_level = logging.WARNING

    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG

    if args.silent:
        logging.basicConfig(handlers=[logging.NullHandler()])
    else:
        logging.basicConfig(handlers=[logging.StreamHandler()], level=log_level)

    if args.skip_decompile:
        game = Game()
        game.initialize(loaded_json=args.input)
        manager = AnalysisManager(game)
        manager.create_analysis()
    else:
        manager = carball.analyze_replay_file(args.input)

    if args.proto:
        with open(args.proto, 'wb') as f:
            manager.write_proto_out_to_file(f)
    if args.json:
        proto_game = manager.get_protobuf_data()
        with open(args.json, 'w') as f:
            printer = _Printer()
            js = printer._MessageToJsonObject(proto_game)
            json.dump(js, f, indent=2, cls=CarballJsonEncoder)
    if args.gzip:
        with gzip.open(args.gzip, 'wb') as f:
            manager.write_pandas_out_to_file(f)


if __name__ == '__main__':
    main()
