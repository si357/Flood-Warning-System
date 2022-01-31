from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
stations = build_station_list()
x=stations_by_distance(stations, (52.2053, 0.1218))
close= x[:10]
far=x[-10:]
print(close)
print(far)