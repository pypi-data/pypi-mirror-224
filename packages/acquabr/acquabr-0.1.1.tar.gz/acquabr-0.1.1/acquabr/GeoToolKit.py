import pandas as pd
import geopandas as gpd
import pyproj
import utm
from srtm import get_data
import math
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


class GeoToolKit:

    def frameToShape(path_station, data_list, output):
        """
        Merges multiple DataFrames into a GeoDataFrame and saves it as a vector file in various GeoPandas-supported formats.

        Args:
            path_stations (GeoDataFrame): Base GeoDataFrame containing station information.
            data_list (list): List of DataFrames to be merged with path_stations.
            output (str): Output path for the saved vector file.

        Returns:
            GeoDataFrame: Merged GeoDataFrame.

        This function performs the following steps:
        1. Validates the input GeoDataFrame and checks if the 'CD' column exists.
        2. Concatenates each DataFrame from data_describe_list to the GeoDataFrame path_stations.
        3. Merges the data based on the 'CD' and 'STATIONS' columns.
        4. Creates a GeoDataFrame from the merged data with a geometry column.
        5. Saves the GeoDataFrame as a vector file using the provided output path. Supported formats include:
          - Shapefile (.shp)
          - GeoJSON (.geojson)
          - ... and other formats supported by GeoPandas and its dependencies.
        Raises:
            ValueError: If required columns are missing or empty.
            TypeError: If input types are incorrect or an error occurs during processing.

        Example:
        shape = GeoToolkit.frameToShape(path_station, [df_elev, df_sts], "out_shape.shp")
        """

        # Block 0: Function Parametes Validations
        if type(path_station) != gpd.geodataframe.GeoDataFrame:
            raise TypeError("The 'path_stations' variable must be a GeoDataFrame obtained from the 'Hidroweb.getStation()' method.")

        if type(data_list) != list:
            raise TypeError("The 'data_describe_list' parameter must be a list of DataFrames.")

        if "CD" not in path_station.columns:
            raise KeyError("Column 'CD' does not exist in the 'path_station'. Please check your data or column renaming.")

        if len(path_station) == 0:
            raise ValueError("No stations were selected in the 'HidroWeb.getStation()' or the search area.")

        if len(data_list) == 0:
            raise ValueError("No dataframes were provided for the merged operation.")

        # Block 1: Function Input Parametes
        merged_df = path_station.copy()

        # Block 2: Concatenate each DataFrame from the 'data_describe_list' to the GeoDataFrame 'path_stations' based on the 'STATIONS' column.
        try:
            for idx, data_describe in enumerate(data_list):
                if 'STATIONS' not in data_describe.columns:
                    raise ValueError(f"'STATIONS' column not found in DataFrame at index {idx} of data_describe_list.")
                data_describe["STATIONS"] = data_describe["STATIONS"].astype(int)

                merged_df = merged_df.merge(data_describe, left_on="CD", right_on="STATIONS", how="left")
                merged_df.drop(columns=["STATIONS"], inplace=True)

            for col in merged_df.columns:
                if pd.api.types.is_datetime64_any_dtype(merged_df[col]):
                    merged_df[col] = merged_df[col].dt.strftime("%Y-%m-%d")

            geo_merged_df = gpd.GeoDataFrame(merged_df, geometry="geometry")
            geo_merged_df.to_file(output)
            return geo_merged_df
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing data: {str(e)}")


    def DistMatrix(path_station, method):

        """
        Calculate the Distance Matrix between stations' coordinates.

        Args:
            path_station (GeoDataFrame): A GeoDataFrame obtained from the 'HidroWeb.getStation()' method.
            method (str): Method for calculating distance. Options:'EUCLIDEAN', 'HAVERSINE', 'COSINE', 'MINKOWSKI'.

        Returns:
            pandas.DataFrame: A DataFrame representing the Distance Matrix.

        This function calculates the distance matrix between station coordinates based on the chosen method.

        Raises:
            ValueError: If the GeoDataFrame is empty or if the 'CD' column is missing.
            TypeError: If the input is not a GeoDataFrame or if an error occurs during coordinate transformation.
            RuntimeError: If an error occurs while calculating the distance matrix.

        Example:
        matrix = DistMatrix(path_station, method='HAVERSINE')
        """

        # Block 0: Function Parametes Validations
        if type(path_station) != gpd.geodataframe.GeoDataFrame:
            raise TypeError("The 'path_station' variable must be a GeoDataFrame obtained from the 'HidroWeb.getStation()' method.")

        if "CD" not in path_station.columns:
            raise KeyError("Column 'CD' does not exist in the 'path_station'. Please check your data or column renaming.")

        if len(path_station) == 0:
            raise ValueError("No stations were selected in the 'HidroWeb.getStation()' or the search area.")

        # Block 1: Function Input Parametes
        gdf = path_station.copy()
        gdf.rename(columns={"CD": "STATIONS"}, inplace=True)

        # Block 2: Obtaining Coordinates in Meters for Each Station
        try:
            for i, row in gdf.iterrows():
                lat = row["Y"]
                lon = row["X"]
                utm_x, utm_y, zona_utm, letra_utm = utm.from_latlon(lat, lon)
                EPSG = 31960 + zona_utm
                wgs84 = pyproj.CRS("EPSG:4326")
                sirgas2000 = pyproj.CRS(f"EPSG:{EPSG}")
                transformer = pyproj.Transformer.from_crs(wgs84, sirgas2000, always_xy=True)
                x, y = transformer.transform(row["X"], row["Y"])
                gdf.at[i, "Ym"] = y
                gdf.at[i, "Xm"] = x
        except Exception as e:
            raise RuntimeError(f"Error occurred while transforming coordinates: {str(e)}")


        # Block 3: Calculating the Euclidean Distance Matrix, Returning the Result in a DataFrame 'distances'
        try:
            def euclidean_distance(x1, x2, y1, y2):
                return (((x2 - x1)**2 + (y2 - y1)**2)**0.5)/1000

            def haversine_distance(lat1, lon1, lat2, lon2):
                R = 6371.0  # Raio médio da Terra em quilômetros
                lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distance = R * c
                return distance

            def law_of_cosines_distance(lat1, lon1, lat2, lon2):
                R = 6371.0  # Raio médio da Terra em quilômetros
                lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
                if lat1 == lat2 and lon1 == lon2:
                    return 0  # Pontos coincidentes, distância é zero
                dlon = lon2 - lon1
                distance = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(dlon)) * R
                return distance

            def minkowski_distance(lat1, lon1, lat2, lon2, p):
                R = 6371.0  # Raio médio da Terra em quilômetros
                lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
                dx = R * (lon2 - lon1) * math.cos(0.5 * (lat2 + lat1))
                dy = R * (lat2 - lat1)
                distance = (abs(dx)**p + abs(dy)**p)**(1/p)
                return distance

            distances = pd.DataFrame(index=gdf["STATIONS"], columns=gdf["STATIONS"])
            for i, row1 in gdf.iterrows():
                for j, row2 in gdf.iterrows():
                    if method == "EUCLIDEAN":
                        distance = euclidean_distance(row1["Xm"], row2["Xm"], row1["Ym"], row2["Ym"])
                    elif method == "HAVERSINE":
                        distance = haversine_distance(row1["Y"], row1["X"], row2["Y"], row2["X"])
                    elif method == "COSINE":
                        distance = law_of_cosines_distance(row1["Y"], row1["X"], row2["Y"], row2["X"])
                    elif method == "MINKOWSKI":
                        # Define o valor de p (parâmetro da Distância de Minkowski)
                        p = 2
                        distance = minkowski_distance(row1["Y"], row1["X"], row2["Y"], row2["X"], p)
                    else:
                        raise KeyError("Invalid method. Available options: 'EUCLIDEAN', 'HAVERSINE', 'COSINE', 'MINKOWSKI'")
                    distances.at[row1["STATIONS"], row2["STATIONS"]] = distance

            distance_matrix = distances.apply(pd.to_numeric, errors="coerce")
            for index, row in distance_matrix.iterrows():
                station = index
                neighbors = row.nsmallest(len(row) - 1).index.tolist()
                print(f"Station: {station}, Neighbors in order of distance: {neighbors}")

            return distances
        except Exception as e:
            raise RuntimeError(f"Error occurred while calculating distance matrix: {str(e)}")


    def getElevation(path_station):

        """
        Get elevations for each station using SRTM 90-meter data, returning a GeoDataFrame.

        Args:
            path_station (GeoDataFrame): A GeoDataFrame obtained from the 'HidroWeb.getStation()' method.

        Returns:
            GeoDataFrame: A GeoDataFrame with station IDs and their corresponding elevations.

        This function performs the following steps:
        1. Validates the input GeoDataFrame and checks if the 'CD' column exists.
        2. Renames the 'CD' column to 'STATIONS' for consistency.
        3. Obtains elevation data for each station using the SRTM 90-meter data source.
        4. Returns a GeoDataFrame containing station IDs and their elevations.

        Raises:
            ValueError: If no stations are selected or if the 'CD' column is missing.
            TypeError: If the input is not a GeoDataFrame.
            RuntimeError: If an error occurs while obtaining elevation data.

        Example:
        elev_station = GeoToolkit.getElevation(path_station)
        """

        # Block 0: Function Parametes Validations
        if type(path_station) != gpd.geodataframe.GeoDataFrame:
            raise TypeError("The 'path_stations' variable must be a GeoDataFrame obtained from the 'HidroWeb.getStation()' method.")

        if "CD" not in path_station.columns:
            raise KeyError("Column 'CD' does not exist in the 'path_station'. Please check your data or column renaming.")

        if len(path_station) == 0:
            raise ValueError("No stations were selected in the 'HidroWeb.getStation()' or the search area.")

        # Block 1: Function Input Parametes
        gdf = path_station.copy()
        gdf.rename(columns={"CD": "STATIONS"}, inplace=True)

        # Block 2: Obtaining Elevation for Each Station Using SRTM 90-meter Data, Returning a GeoDataFrame as Result
        try:
            def getData(lat, lon):
                elevation_data = get_data()
                elevation = elevation_data.get_elevation(lat, lon)
                return elevation
            gdf["ELEVATIONS"] = gdf.apply(lambda row: getData(row["Y"], row["X"]), axis=1)
            return gdf[["STATIONS", "ELEVATIONS"]]

        except Exception as e:
            raise RuntimeError(f"Error occurred while obtaining elevation data: {str(e)}")
