#!/usr/bin/python -tt
# Project: demo_infrahub_sdk
# Filename: test1.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "5/12/25"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"

import argparse
from infrahub_sdk import InfrahubClientSync, Config

def some_function():
    pass


def main():


    config = Config(
        address="https://demo.infrahub.app",
        api_token="183ed170-c08e-885e-d7ef-1065d6c0f009",
    )

    client = InfrahubClientSync(config=config)

    all_items = client.all(arguments.kind)

    if arguments.kind == "InfraVLAN":
        print("InfraVLAN")
        for vlan in all_items:
            print(vlan)
            print(f"VLAN ID: {vlan.vlan_id.value}, Name: {vlan.name.value}")

    if arguments.kind == "LocationGeneric":
        print("LocationGeneric")
        for item in all_items:
            print(item)
            print(item.name.value)
            # print(dir(item))
            # print(f"VLAN ID: {vlan.vlan_id.value}, Name: {vlan.name.value}")

# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: ' python test1.py' ")

    # parser.add_argument('all', help='Execute all exercises in week 4 assignment')
    parser.add_argument('-k', '--kind', help='Specify the kind for client.all', action='store',default="InfraVLAN")
    arguments = parser.parse_args()
    main()
