# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine 
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    "Given a list of stations and coordinates p returns a list of (station, distance) tuples, sorted in order of distance"
    list = []
    for station in stations:
        distance = haversine(p,station.coord)
        tuple = (station, distance)
        list.append(tuple)
    list = sorted_by_key(list,1)
    return list

    