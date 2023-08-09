#!/usr/bin/python
# encoding=utf-8
import argparse
import sys

from pitrix import __description__, __version__
from pitrix.scaffold import init_parser_scaffold, main_scaffold


def main():
    # 命令行处理程序入口
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-V", "--version", dest="version", action="store_true", help="show version")
    subparsers = parser.add_subparsers(help="sub-command help")
    sub_parser_scaffold = init_parser_scaffold(subparsers)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    elif len(sys.argv) == 2:
        if sys.argv[1] in ["-V", "--version"]:
            print(f"{__version__}")
        elif sys.argv[1] in ["-h", "--help"]:
            parser.print_help()
        elif sys.argv[1] == "startproject":
            sub_parser_scaffold.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.version:
        print(f"{__version__}")
        sys.exit(0)

    if sys.argv[1] == "startproject":
        main_scaffold(args)
