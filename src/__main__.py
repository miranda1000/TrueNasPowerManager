from argparse import ArgumentParser
from os import path

from TrueNasPowerManager import TrueNasPowerManager

DEFAULT_CONFIG_FILE_PATH = path.join(path.dirname(path.abspath(__file__)), '../config/config.json')

def main(config_path: str):
    TrueNasPowerManager(config_path).sync_run()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--config-path", help="config file path", default=DEFAULT_CONFIG_FILE_PATH)
    args = parser.parse_args()
    main(args.config_path)