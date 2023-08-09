import pandas as pd
from shapely.geometry import Polygon
import warnings
import importlib.resources as pkg_resources
import numpy as np

from .filter_utils import filter_datetime, filter_location

warnings.filterwarnings("ignore", category=UserWarning, module="numpy", message=".*Intel MKL WARNING.*")
pd.options.mode.chained_assignment = None  # default='warn'
# Suppress the DtypeWarning
warnings.filterwarnings(action='ignore', category=pd.errors.DtypeWarning)


def get_csv_from_package(database_location, folder, file_name):
    package_path = f"{database_location}.{folder}"
    with pkg_resources.path(package_path, file_name) as csv_path:
        return pd.read_csv(csv_path)



def generate_survey_database(report):
    """
    This method filters the survey database to select rows only relevant to the selected survey location.
    """
    survey_match = get_csv_from_package(report.database_location, 'original', 'survey_match.csv')


    columns_to_search = ['survey_start', 'flight_date']
    survey_match = filter_datetime(survey_match, columns_to_search, report.start_date, report.end_date)

    columns_to_search = ['mission', 'location', 'location_id']
    if report.location_filter == 'Bar':
        columns_to_search = ['location_id']
    filtered_df = filter_location(report, columns_to_search, survey_match)

    surveys = pd.DataFrame({
        'survey_start': filtered_df['survey_start'],
        'flight_date': filtered_df['flight_date'],
        'drone': filtered_df['drone'],
        'drone_height': filtered_df['drone_height'],
        'drone_speed': filtered_df['drone_speed'],
        'end_time': filtered_df['end_time'],
        'mission': filtered_df['mission'],
        'wind_speed': filtered_df['wind_speed'],
        'ground_temp': filtered_df['ground_temp'],
        'location': filtered_df['location'],
        'location_id': filtered_df['location_id'],
        'location_area': filtered_df['location_area'],
        'pilot': filtered_df['pilot']
    })
    surveys, locations = add_location_dataframe(surveys, report)
    surveys = add_survey_sites(surveys)
    return surveys, locations


def add_location_dataframe(surveys, report):
    # Integrate the area variable from the locations database
    location_dataframe = get_csv_from_package(report.database_location, 'original', 'location_dataframe.csv')

    locations = pd.DataFrame({
        'location_id': location_dataframe['location_id'],
        'area_nsew_box': location_dataframe['area_nsew_box'],
        'total_area': location_dataframe['total_area'],
        'avg_area': location_dataframe['avg_area'],
        'lat_min': location_dataframe['lat_min'],
        'lat_max': location_dataframe['lat_max'],
        'lon_min': location_dataframe['lon_min'],
        'lon_max': location_dataframe['lon_max']
    })
    survey_location_ids = surveys['location_id'].drop_duplicates().tolist()
    surveys = pd.merge(left=surveys, right=locations, on='location_id', validate='many_to_one')
    locations = locations[locations['location_id'].isin(survey_location_ids)]
    if surveys['total_area'].sum() == 0:
        raise Exception("The total area parameter is zero for all sites. This parameter is needed to create the "
                        "figures.")

    return surveys, locations


def add_survey_sites(surveys):
    survey_sites = []
    for idx, row in surveys.iterrows():
        valid_coordinates = (pd.notnull(row['lat_min']) and pd.notnull(row['lat_max']) and pd.notnull(row['lon_min'])
                             and pd.notnull(row['lon_max']))
        if valid_coordinates:
            coords = [
                (row['lon_min'], row['lat_min']),
                (row['lon_max'], row['lat_min']),
                (row['lon_max'], row['lat_max']),
                (row['lon_min'], row['lat_max'])
            ]
            survey_sites.append(Polygon(coords))
        else:
            survey_sites.append(np.nan)

    surveys['survey_sites'] = survey_sites
    return surveys.drop(columns=['lat_min', 'lat_max', 'lon_min', 'lon_max'])


def generate_detections_database(report):
    """
    This method filters the detections database to extract only relevant parameters and creates a second Pandas
    Dataframe which contains information about the target species.
    """
    det_match = get_csv_from_package(report.database_location, 'original', 'det_match.csv')

    columns_to_search = ['detection_time']
    det_match = filter_datetime(det_match, columns_to_search, report.start_date, report.end_date)

    columns_to_search = ['mission', 'location', 'location_id']
    if report.location_filter == 'Bar':
        columns_to_search = ['location_id']
    filtered_df = filter_location(report, columns_to_search, det_match)

    filtered_df['detection_time'] = pd.to_datetime(filtered_df['detection_time'])
    filtered_df = filtered_df.sort_values('detection_time')
    filtered_df['date'] = pd.to_datetime(filtered_df['detection_time']).dt.date
    filtered_df['time'] = pd.to_datetime(filtered_df['detection_time']).dt.strftime("%-I:%M %p")
    detections = pd.DataFrame({
        'date': filtered_df['date'],
        'time': filtered_df['time'],
        'species_name': filtered_df['species_name'],
        'detection_count': filtered_df['detection_count'],
        'probability': filtered_df['probability'],
        'lat': filtered_df['drone_lat'],
        'lon': filtered_df['drone_lon'],
        'gt_outcome': filtered_df['gt_outcome'],
        'gt_method': filtered_df['gt_method'],
        'drone': filtered_df['drone'],
        'comments': filtered_df['comments'],
        'location': filtered_df['location'],
        'location_id': filtered_df['location_id']
    })
    return detections


def generate_airdata_database(report):
    airdata_matches = get_csv_from_package(report.database_location, 'original', 'airdata_matches.csv')

    columns_to_search = ['flight_start', 'start_time', 'finish_time']
    airdata_matches = filter_datetime(airdata_matches, columns_to_search, report.start_date, report.end_date)

    columns_to_search = ['kml_matches', 'surveyID', 'kml_location']
    filtered_df = filter_location(report, columns_to_search, airdata_matches)

    airdata = pd.DataFrame({
        'flight_start': filtered_df['flight_start'],
        'start_time': filtered_df['start_time'],
        'finish_time': filtered_df['finish_time'],
        'pilot': filtered_df['pilot'],
        'drone': filtered_df['drone'],
        'drone_type': filtered_df['drone_type'],
        'survey_location_id': filtered_df['survey_location_id'],
        'kml_location_id': filtered_df['kml_location_id'],
        'kml_matches': filtered_df['kml_matches'],
        'surveyID': filtered_df['surveyID'],
        'kml_location': filtered_df['kml_location']
    })
    return airdata


def generate_kml_database(report):
    """
    This method filters the kml database to extract only high probability koalas (or another chosen animal
    filter) for the chosen survey location and selects only relevant columns for generating a report.
    """
    kml_gdf = get_csv_from_package(report.database_location, 'original', 'kml_gdf.csv')

    survey_location_ids = report.surveys['location_id'].drop_duplicates().tolist()
    detection_location_ids = report.detections['location_id'].drop_duplicates().tolist()
    location_ids = list(set(survey_location_ids) | set(detection_location_ids))
    column_mask = kml_gdf['location_id'].isin(location_ids)
    filtered_df = kml_gdf[column_mask]

    kmls = pd.DataFrame({
        'filename': filtered_df['filename'],
        'linestring': filtered_df['geometry'],
        'polygon': filtered_df['boxes'],
        'area': filtered_df['true_area'],
        'length': filtered_df['true_length'],
        'location_id': filtered_df['location_id']
    })
    return kmls
