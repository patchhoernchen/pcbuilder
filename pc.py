#!/usr/bin/env python3

import yaml
import os

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

    def assemble(self):
        for type_, item_ in self.build.items():
            if isinstance(item_, str):
                item = item_
                amount = 1
                name, price, link = self.find_part(type_, item)
                self.update(name, price, link, amount)
            elif isinstance(item_, list):
                for item__ in item_:
                    item = list(item__.keys())[0]
                    amount = list(item__.values())[0]
                    name, price, link = self.find_part(type_, item)
                    self.update(name, price, link, amount)

    def __str__(self):
        header = f"{self.name}: {round(self.price, 2)} Euro"
        partlist = '\n'.join([ f"{amount}x {name} ({price}€ pp) - {link}" for name, amount, price, link in self.partlist ])
        return f"{header}\n{partlist}"


def main():

    parser = argparse.ArgumentParser(
        prog='PC Builder',
        description='build different pc combinations from a set of components',
    )
    parser.add_argument('-B', '--buildsfile', metavar="buildsfile", default="builds.yml", help="file containing builds");
    parser.add_argument('-C', '--componentsfile', metavar="componentsfile", default="components.yml", help="file containing parts");
    parser.add_argument('-b', '--build', metavar="build", help="use this specific buld");
    parser.add_argument('-l', '--links', help="open link for build", action="store_true");
    parser.add_argument('-w', '--webbrowser', metavar="webbrowser", default="firefox", help="open link for build");
    parser.add_argument('-a', '--all-builds', help="show all builds", action="store_true");

    args = parser.parse_args()
    pprint(args)


    parts = yaml.load(open(args.componentsfile).read(), Loader=yaml.Loader)
    builds = yaml.load(open(args.buildsfile).read(), Loader=yaml.Loader)
    #pprint(parts)
    #pprint(builds)
    if args.all_builds:
        for name, build in builds.items():
            b = Build(name, build, parts)
            b.assemble()
            print(f"{b}\n")
    elif args.build is not None:
        build_data = builds.get(args.build)
        if build_data is None:
            print(f"no such build: {args.build}")
            exit(-2)
        b = Build(args.build, build_data, parts)
        b.assemble()
        print(f"{b}\n")
        if args.links:
            linklist = ' '.join( f"'{link}'" for name, amount, price, link in b.partlist )
            os.system(f"{args.webbrowser} {linklist}")
    else:
        exit(-1)


if __name__ == "__main__":
    main()
