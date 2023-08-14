# Python Library for Hydrological Data Retrieval and Analysis in Brazil

The `acquabr` library offers a comprehensive set of tools and functionalities tailored for hydrological analysis of data within Brazil. It comprises classes such as `HidroWeb`, `DataToolkit`, and `GeoToolKit`, designed to facilitate data manipulation, analysis, and visualization of crucial meteorological parameters including rainfall, flow, and river levels.

## Features

- Seamless integration with the HIDROWEB platform, allowing efficient retrieval of hydrological data. [Access HIDROWEB](https://www.snirh.gov.brhidroweb/apresentacao)
- Robust tools for data preprocessing, advanced statistical analysis, and intuitive visualization of time series datasets.
- Calculation of precise distances between monitoring stations and elevation extraction utilizing high-resolution SRTM data.

## Installation

You can easily install the library using pip:

```bash
pip install acquabr

```

## Usage

The library's classes empower hydrologists, data scientists, and researchers to streamline their analyses and gain valuable insights from hydrological and geospatial datasets. Below are brief descriptions of the three main classes provided by `acquabr`:

### HidroWeb

The `HidroWeb` class serves as a pivotal component for automated data retrieval and processing from the HIDROWEB portal. This facilitates obtaining details about monitoring stations and daily time series data for rainfall, flow, and river levels.

### DataToolkit

The `DataToolkit` class offers a versatile and comprehensive approach for manipulation and analysis of hydrological time series datasets. This includes crucial information related to rainfall, flow, and river levels. The class provides an array of functionalities, such as preprocessing, statistical analysis, resampling, and identifying optimal time windows.

### GeoToolKit

The `GeoToolKit` class provides a powerful toolkit for geospatial data operations, tailored specifically for hydrological analyses. It enables users to manipulate and analyze hydrological station data, calculate distances between geographic coordinates, and retrieve elevation data using the SRTM model.


## Exemplos de Uso

Aqui estão alguns exemplos de como você pode usar as classes da biblioteca:


### HidroWeb

```python
import acquabr

hidro = acquabr.HidroWeb()
stations = hidro.getStation(code='12345678')
print(stations)

```

### DataToolkit

```python
import acquabr


data_toolkit = acquabr.DataToolkit()

```

### GeoToolkit


```python
import acquabr


data_toolkit = acquabr.DataToolkit()

```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




