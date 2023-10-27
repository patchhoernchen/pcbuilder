#!/usr/bin/env python3


import yaml
import os
import sys

from pprint import pprint, pformat

import argparse


class NoSuchPartException(Exception):
    pass


class Build():

    def __init__(self, name, build, parts):
        self.name = name
        self.build = build
        self.parts = parts
        self.price = 0
        self.partlist = []

    def find_part(self, type_, part):
        selection = [ p for p in self.parts.get(type_, []) if part in p.keys() ]
        if len(selection) > 0:
            s = selection[0].get(part)
            return (s.get("name"), s.get("price"), s.get("link"))
        else:
            raise NoSuchPartException(f"{type_}: {part} not defined")

    def update(self, name, price, link, amount):
        self.price += price*amount
        self.partlist.append(
            ( name, amount, price, link)
        )

    def add_part(self, type_, item, amount):
        name, price, link = self.find_part(type_, item)
        self.update(name, price, link, amount)

    def assemble(self):
        for type_, item_ in self.build.items():
            if isinstance(item_, str):
                item = item_
                amount = 1
                self.add_part(type_, item, amount)
            elif isinstance(item_, list):
                for item__ in item_:
                    item = list(item__.keys())[0]
                    amount = list(item__.values())[0]
                    self.add_part(type_, item, amount)

    def __str__(self):
        header = f"{self.name}: {round(self.price, 2)} Euro"
        partlist = '\n'.join([
            f"{amount}x {name} ({price}€ pp) - {link}"
            for name, amount, price, link
            in self.partlist
        ])
        return f"{header}\n{partlist}"


def get_args():
    parser = argparse.ArgumentParser(
        prog='PC Builder',
        description='build different pc combinations from a set of components',
        epilog='-l and -L only work when a build is specified',
    )
    parser.add_argument(
        'build',
        metavar="build",
        help="use this specific build, use 'all' for all builds"
    );
    parser.add_argument(
        '-B', '--buildsfile',
        metavar="buildsfile",
        default="builds.yml",
        help="file containing builds"
    );
    parser.add_argument(
        '-C', '--componentsfile',
        metavar="componentsfile",
        default="components.yml",
        help="file containing parts"
    );
    parser.add_argument(
        '-l', '--links',
        help="open links for build",
        action="store_true"
    );
    parser.add_argument(
        '-L', '--show-links',
        help="show links for build",
        action="store_true"
    );
    parser.add_argument(
        '-w', '--webbrowser',
        metavar="webbrowser",
        default="firefox",
        help="open link for build"
    );

    return parser.parse_args()


def main():

    args = get_args()

    parts = yaml.load(open(args.componentsfile).read(), Loader=yaml.Loader)
    builds = yaml.load(open(args.buildsfile).read(), Loader=yaml.Loader)

    if args.build == 'all':
        for name, build in builds.items():

            b = Build(name, build, parts)
            b.assemble()

            print(f"{b}\n")

        if args.links or args.show_links:
            print("link operations (-l and -L) are ignored", file=sys.stderr)

    else:
        build_data = builds.get(args.build)

        if build_data is None:
            print(f"no such build: {args.build}", file=sys.stderr)
            exit(-2)

        b = Build(args.build, build_data, parts)
        b.assemble()

        if args.links or args.show_links:
            linklist = ( link for name, amount, price, link in b.partlist )
            if args.links:
                browserlinks = ' '.join( f"'{link}'" for link in linklist)
                os.system(f"{args.webbrowser} {browserlinks}")
            elif args.show_links:
                linklist = '\n'.join(linklist)
                print(f"{linklist}")
        else:
            print(f"{b}")


if __name__ == "__main__":
    main()
