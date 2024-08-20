import geopandas as gpd
from pathlib import Path
import numpy as np


def count_voter_by_polygon(point_series: gpd.GeoSeries,
                           polygons_series: gpd.GeoSeries):
    # create result GeoDataFrame
    data = np.zeros((len(polygons_series), 2))
    result_gdf = gpd.GeoDataFrame(data=data,
                                  columns=("Count", "Density", ),
                                  geometry=polygons_series)
    # NAD83 / North Carolina (ftUS)
    polygon_2264 = polygons_series.to_crs("EPSG:2264")

    # loop through all polygons
    for i in polygons_series.index:
        print("process %02d of total %03d polygons" % (i, len(polygons_series)))
        polygon = polygons_series.loc[i]
        # loop through all points and check whether the point j is within the polygon i
        for j in point_series.index:
            point = point_series.loc[j]
            if point.within(polygon):
                result_gdf.loc[i, "Count"] += 1.0

        area_in_sqmi = polygon_2264.loc[i].area * 3.86102e-7
        result_gdf.loc[i, "Density"] = result_gdf.loc[i, "Count"] / area_in_sqmi  # person per acre

    return result_gdf


def main():
    data_path = Path("../Output")

    # Party categories: DEM, REP, UNA
    party_groups = ("DEM", "REP", "UNA")

    # read precinct data
    precinct_gpkg_file = data_path / "precinct.gpkg"
    precinct_gdf = gpd.read_file(precinct_gpkg_file)

    for party in party_groups:
        print("process party: %s" % party)
        voter_gpkg_file = data_path / ("%s_voters.gpkg" % party.lower())
        voter_gdf = gpd.read_file(voter_gpkg_file)

        voter_count_gdf = count_voter_by_polygon(voter_gdf["geometry"], precinct_gdf["geometry"])
        output_gpkg_file = data_path / ("%s_count_by_precinct.gpkg" % party.lower())
        voter_count_gdf.to_file(output_gpkg_file, driver="GPKG")


if __name__ == "__main__":
    main()
