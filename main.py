# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import geopandas as gpd
from fastkml import kml
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # Load the shapefile
    gdf = gpd.read_file("CED_2024_AUST_GDA2020.shp")

    # save to kml

    gdf.to_file("CED_2024_AUST_GDA2020.kml", driver="KML")

def read_kml():
    # load the kml file
    k = kml.KML()
    with open("CED_2024_AUST_GDA2020.kml", 'rt', encoding='utf-8') as file:
        output = k.from_string(file.read())
    print(output)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('Morgan!!')
    read_kml()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
