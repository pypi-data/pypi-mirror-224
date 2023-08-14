from tqdm import tqdm
import os
import requests
import pandas as pd
import zipfile
import chardet
import geopandas as gpd

class HidroWeb:
    def getStation(path_mask= None, station_type=None):
        """
        Retrieves characteristics of rainfall and flow monitoring stations within a specified area.

        Args:
            path_mask (str or None, optional): Path to a vector-shaped filter for geographical area.
            station_type (str): Type of station ('FLOW_STATION' or 'RAINFALL_STATION').

        Returns:
            geopandas.GeoDataFrame: A GeoDataFrame containing station details within the specified area.

        Notes:
            - The 'station_type' parameter specifies the type of stations to retrieve information for.
            - The 'path_mask' parameter is used to filter stations based on a specific geographical area 
              if provided.
            - The returned GeoDataFrame is essential for subsequent data retrieval using the 'getData()' method.

        This function performs the following steps:
        1. Validates the input station_type and checks if it's 'FLOW_STATION' or 'RAINFALL_STATION'.
        2. Validates the format of the vector mask that represents the geographical area, 
        ensuring it can be read by GeoPandas.
        3. Reads station information from online sources based on the station_type.
        4. Creates a GeoDataFrame with station coordinates.
        5. Filters the stations using a geographical area mask if provided.
        6. Returns the GeoDataFrame with station details.

        Raises:
            KeyError: If station_type is not valid.
            RuntimeError: If an issue occurs while obtaining station information.

        Example:
        station_data = HidroWeb.getStation(station_type='FLOW_STATION')
        station_data = HidroWeb.getStation(path_mask='path/to/area_of_interest.shp', station_type='FLOW_STATION')
        """

        # Block 0: Function Parametes Validations
        if station_type not in ["FLOW_STATION", "RAINFALL_STATION"] and station_type is not None:
            raise KeyError("Station type not found, available options:'FLOW_STATION' and 'RAINFALL_STATION'")

        if path_mask is not None:
            if type(path_mask) == str:
                try:
                    mask = gpd.read_file(path_mask)
                    mask["geometry"] = mask.buffer(0)
                    mask = mask.to_crs(crs=4326)
                except Exception as e:
                    raise RuntimeError(f"Error while reading or processing the provided mask: {str(e)}")
            else:
                raise TypeError("Invalid type for 'path_mask'. It should be a string representing the file path.")


        # Block 1: Select stations for a specific area of interest (path_mask), or retrieve all available stations."
        columns_rain = ["X", "Y", "CD", "CDALT","NM", "RESPON", "OPERAD", "EMOPER"]
        columns_flow = ["X", "Y", "CD", "CDALT", "COBACIA", "NM", "RIO", "RESPON", "OPERAD", "EMOPER", "ADKM2"]
        try:
            if station_type== "FLOW_STATION":
                all_stations= pd.read_csv("https://dadosabertos.ana.gov.br/datasets/2a045c4bb2aa4c599fcca73724cae786_3.csv?outSR=%7B%22latestWkid%22%3A4674%2C%22wkid%22%3A4674%7D", usecols=columns_flow)
            elif station_type== "RAINFALL_STATION":
                all_stations= pd.read_csv("https://dadosabertos.ana.gov.br/datasets/9acedfa605b6493f899061d0aca107b9_1.csv?outSR=%7B%22latestWkid%22%3A4674%2C%22wkid%22%3A4674%7D", usecols=columns_rain)
            all_stations["geometry"] = gpd.points_from_xy(all_stations["X"], all_stations["Y"])
            all_stations = gpd.GeoDataFrame(all_stations, crs="EPSG:4326")
            if path_mask is not None:
                stations= gpd.overlay(all_stations, mask, how="intersection", keep_geom_type=True)
                stations= stations[all_stations.columns]
            elif path_mask is None:
                stations= all_stations
            return stations
        except Exception as e:
              raise RuntimeError(f"An issue occurred while obtaining station information: {str(e)}")

    def getData(path_station, data_type, directory=None):

        """
        Retrieve hydrometeorological data organized into daily time series.

        This method fetches processed data on precipitation, flow, and river level from 
        stations available on the HIDROWEB portal.

        Parameters:
        path_station (geopandas.GeoDataFrame): GeoDataFrame of stations obtained from 'HidroWeb.getStation()'.
        data_type (str): Desired data type ("RAINFALL_DATA", "FLOW_DATA", or "FLOW_LEVEL_DATA").
        directory (str or None, optional): Folder path to store processed files and explore HIDROWEB data.

        Returns:
        pandas.DataFrame: DataFrame containing the requested daily temporal hydrometeorological dataset.

        Notes:
        - The 'path_station' parameter should be a GeoDataFrame obtained using the 'HidroWeb.getStation()' method.
        - The 'data_type' parameter specifies the type of hydrometeorological data to retrieve.
        - The 'directory' parameter specifies a folder to store processed files and explore available data.

        This function performs the following steps:

        1. Validation of Function Parameters
        2. Iteration over the Selected Stations
        3. Construction of URL and Download of Data Files
        4. Extraction of Data from Zip Files
        5. Data Processing and Cleaning
        6. Concatenation and Formatting of Station Data

        Example:
        station_data = HidroWeb.getStation(path_mask='path/to/area_of_interest.shp', station_type='FLOW_STATION', )
        data = HidroWeb.getData(path_stations=station_data, data_type='RAINFALL_DATA', directory='data_folder')
        """

        # Block 0: Function Parametes Validations
        if type(path_station) != gpd.geodataframe.GeoDataFrame:
            raise TypeError("The 'path_station' variable must be a GeoDataFrame obtained from the 'getStation()' method.")

        if len(path_station) == 0:
            raise ValueError("No stations were selected in the 'getStation()' for data requisition")

        if data_type not in ["FLOW_DATA", "RAINFALL_DATA", "FLOW_LEVEL_DATA"]:
            raise KeyError("Data type not found, available options: 'FLOW_DATA', 'RAINFALL_DATA', and 'FLOW_LEVEL_DATA'.")

        if directory == None:
            if not os.path.exists("acquabr"):
              os.makedirs("acquabr")
            directory = "acquabr"
        else:
            if not os.path.exists(directory):
              os.makedirs(directory)

        # Block 1: Progress Tracking, URL Template, and Initialization
        progress_bar = tqdm(total=len(path_station), desc="Processing tasks")
        url_template = "https://www.snirh.gov.br/hidroweb/rest/api/documento/convencionais?tipo=2&documentos={}"
        process_counts= 0
        process_errors= 0
        error_stations=[]
        selecteds_stations= []

        # Block 2: Station Code Selection and URL Formatting
        try:
            for codes in path_station["CD"]:
                if data_type== "RAINFALL_DATA":
                    selecteds_stations.append("00"+str(codes))
                else:
                    selecteds_stations.append(str(codes))
        except Exception as e:
            raise RuntimeError(f"Station code 'CD' not found in the 'path_station': {str(e)}")

        for station_code in selecteds_stations:
            try:
                # Block 3: Download and Extraction of ZIP Files Containing Station Data
                url = url_template.format(station_code)
                response = requests.get(url)

                with open(f"{directory}/{station_code}.zip", "wb") as f:
                    f.write(response.content)
                zip_path = f"{directory}/{station_code}.zip"
                with zipfile.ZipFile(zip_path, "r") as zip_file:
                    zip_file.extractall(directory)
                    for name in zip_file.namelist():
                        if name.endswith(".zip"):
                            inner_zip_path = os.path.join(directory, name)
                            with zipfile.ZipFile(inner_zip_path, "r") as inner_zip:
                                inner_zip.extractall(directory)

                # Block 4: Determination of Data Files and Columns
                if data_type== "RAINFALL_DATA":
                    current_station= f"{directory}/chuvas_T_{station_code}.txt"
                    data_column= "Chuva{:02d}"
                if data_type== "FLOW_DATA":
                    current_station= f"{directory}/vazoes_T_{station_code}.txt"
                    data_column= "Vazao{:02d}"
                elif data_type== "FLOW_LEVEL_DATA":
                    current_station= f"{directory}/cotas_T_{station_code}.txt"
                    data_column= "Cota{:02d}"

                # Block 5: Reading and Preprocessing of Data
                with open(current_station, "rb") as f:
                    result = chardet.detect(f.read(10000))

                df = pd.read_csv(current_station, encoding=result["encoding"], sep=';', skiprows=11,
                                     on_bad_lines="error", decimal=",", index_col=False)

                df["Dates"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")
                df["Ano"] = df["Dates"].dt.year
                df["Mes"] = df["Dates"].dt.month

                expected_dates = pd.date_range(start=df["Dates"].min(), end=df["Dates"].max(), freq="MS")
                missing_dates = expected_dates[~expected_dates.isin(df["Dates"])]
                if len(missing_dates) > 0:
                    missing_df = pd.DataFrame({"Dates": missing_dates})
                    missing_df["Ano"] = missing_df["Dates"].dt.year
                    missing_df["Mes"] = missing_df["Dates"].dt.month
                    missing_df = missing_df.reindex(columns=df.columns)
                    df = pd.concat([df, missing_df], ignore_index=True, sort=False)
                    df = df.sort_values(by="Dates")

                # Block 6: Expansion and Export of Daily Data
                df = df.set_index("Dates")
                def expand_monthly_data(row):
                    date = row.name
                    last_day = pd.Period(date, freq="M").days_in_month
                    data_list = []
                    for j in range(1, 32):
                        if j <= last_day:
                            data = date.replace(day=j)
                            row_value = row[data_column.format(j)]
                            data_list.append((data, row_value))
                    return data_list

                data_list = df.apply(expand_monthly_data, axis=1).explode()
                daily_df = pd.DataFrame(data_list.tolist(), columns=["Dates", f"{station_code}"])
                percentage_bar = int(progress_bar.n / progress_bar.total * 100)
                progress_bar.update(1)
                daily_df.to_csv(f"{directory}/{station_code}.csv")
                process_counts+= 1

            except Exception as e:
                print(f"Error occurred while processing station with code: {station_code}. Error: {str(e)}")
                error_stations.append(station_code)
                process_errors+= 1

        progress_bar.close()
        print(f"Total stations processed successfully: {process_counts}")
        print(f"Total errors: {process_errors}")
        if process_errors > 0:
            error_stations_str = ", ".join(str(station) for station in error_stations)
            print(f"Error processing the following stations: {error_stations_str}")

        try:
          # Block 7: Data Organization and Cleaning for Selected Stations
          stations_files = [id for id in os.listdir(directory) if id.endswith(".csv")]
          for file_name in stations_files :
              new_files = [item + ".csv" for item in selecteds_stations]
              if file_name in new_files:
                  df_station = pd.read_csv(os.path.join(directory, file_name), index_col=0)
                  df_station["Dates"] = pd.to_datetime(df_station["Dates"])
                  df_station= df_station.sort_values(by="Dates", ascending=True)
                  df_station.reset_index(drop=True, inplace=True)
                  df_station.to_csv(os.path.join(directory, file_name))

          # Block 8: Concatenation and Resampling of Station Data and Returning the Final DataFrame
          dfs_stations = []
          len_rows = []
          stations_files= sorted(stations_files , key=lambda name: pd.read_csv(os.path.join(directory, name), index_col=0).shape[0], reverse=True)
          for file_station in stations_files :
              df_station = pd.read_csv(os.path.join(directory, file_station), index_col=0)
              df_station = df_station.drop_duplicates(subset="Dates")
              station_dates = pd.date_range(start=df_station["Dates"].min(), end=df_station["Dates"].max(), freq="D")
              df_station = pd.DataFrame({"Dates": station_dates, df_station.columns[1]: df_station[df_station.columns[1]]})
              df_station = df_station.set_index("Dates")
              df_station = df_station.resample("D").asfreq()
              df_station = df_station[~df_station.index.duplicated(keep="month")]
              len_rows.append(len(df_station))
              dfs_stations.append(df_station)

          df_merged = pd.concat(dfs_stations, axis=1)
          start_date = df_merged.index.min()
          end_date = df_merged.index.max()
          new_index = pd.date_range(start=start_date, end=end_date, freq="D")
          df_merged = df_merged.reindex(index=new_index)
          return df_merged

        except Exception as e:
            raise RuntimeError(f"Some error occurred during final data processing, please try again: {str(e)}")
