#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json

from config import JSON_FILE, SQL_FILE
from generator import Generator


def run_strava_sync(client_id, client_secret, refresh_token):
    generator = Generator(SQL_FILE)
    generator.set_strava_config(client_id, client_secret, refresh_token)
    # if you want to refresh data change False to True
    generator.sync(False)

    activities_list = generator.load()
    with open(JSON_FILE, "w") as f:
        json.dump(activities_list, f)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("client_id", help="strava client id")
    # parser.add_argument("client_secret", help="strava client secret")
    # parser.add_argument("refresh_token", help="strava refresh token")
    # options = parser.parse_args()
    # run_strava_sync(options.client_id, options.client_secret, options.refresh_token)
    client_id = 123659
    client_secret = '22f75e9331e8dcb37b3a1405005790600990d592'
    refresh_token = '37bdabcac7049bdcfc31004ab488cc90bbe581f5'
    run_strava_sync(client_id, client_secret, refresh_token)
