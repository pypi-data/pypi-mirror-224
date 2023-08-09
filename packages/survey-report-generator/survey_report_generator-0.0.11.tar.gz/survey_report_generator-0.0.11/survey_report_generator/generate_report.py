import os

import pandas as pd
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import warnings
import importlib.resources as pkg_resources


from .report import Report
from . import tables
from . import figures_utils
from .date_time import add_dates, add_summary_dates
from .summary import get_summary
from .koala_habitat import generate_koala_habitat_map
from .pct import generate_pct_map
from .fesm import generate_fesm_map

pd.options.mode.chained_assignment = None  # default='warn'
warnings.filterwarnings("ignore", category=UserWarning, module="numpy", message=".*Intel MKL WARNING.*")


def generate_report(report, report_location='generated-reports'):
    # Import template
    with pkg_resources.path('survey_report_generator', 'report-template.docx') as template_path:
        template = DocxTemplate(template_path)

    if report.summary:
        generate_summary_databases(report.destination_path)
        report.save_summary_databases()
        add_summary_dates(report)

    # The context variable holds all variables to be inserted into the template
    report.context['num_flights'] = len(report.airdata)
    report.context['client'] = 'NSW National Parks'
    add_dates(report)

    get_summary(report)

    # Add tables
    tables.add_survey_results_table(report)
    tables.add_detections_list(report)
    tables.add_species_list(report)
    tables.add_species_list(report)
    tables.add_site_details_table(report)
    tables.add_plots_table(report)

    if report.summary:
        tables.add_survey_results_summary_table(report)
        tables.add_detections_list_summary(report)
        tables.add_species_list_summary(report)
        tables.add_site_details_summary_table(report)

    if report.include_figures:
        # Add figures
        print("Generating survey site map...")
        figures_utils.generate_figure(report.kmls, report.detections, 'map.png')

        # Construct the path to the saved image
        img_path = os.path.join(os.getcwd(), 'figures', 'map.png')
        report.context['figure_1'] = InlineImage(template, img_path, Cm(15))

        print("Generating koala habitat map...")
        generate_koala_habitat_map(report.kmls, report.detections, 'koala-habitat-map.png')
        img_path = os.path.join(os.getcwd(), 'figures', 'koala-habitat-map.png')
        report.context['figure_2'] = InlineImage(template, img_path, Cm(15))

        print("Generating PCT map...")
        generate_pct_map(report.kmls, report.detections, 'pct-map.png')
        img_path = os.path.join(os.getcwd(), 'figures', 'pct-map.png')
        report.context['figure_3'] = InlineImage(template, img_path, Cm(15))

        print("Generating FESM map...")
        generate_fesm_map(report.kmls, report.detections, 'fesm-map.png')
        img_path = os.path.join(os.getcwd(), 'figures', 'fesm-map.png')
        report.context['figure_4'] = InlineImage(template, img_path, Cm(15))


    if report_location:
        # Render automated report
        template.render(report.context)
        if not os.path.exists(report_location):
            # Create a new directory because it does not exist
            os.makedirs(report_location)
        template.save(os.path.join(report_location, f'{report.location_name}.docx'))
        report.export_dataframes(report.database_location)


def generate_multiple_reports(reports_list, report_location):
    """
    This method produces multiple reports one after the other with the given input parameters.

    Args:
        parameter_list (list): This is a list of dictionaries. Each dictionary is a set of parameter values to input
        into the generate_report method e.g. {'location_name': 'Kalateenee State Forest', 'location_filter':
        'kalateenee', 'report_location': 'reports'}
    """
    for report in reports_list:
        print(f"Generating {report.location_name} report...")
        generate_report(report, report_location=report_location)


def generate_summary_databases(database_location):
    willi = Report(location_name='Willi Willi National Park', location_filter='willi', download_databases=False,
                   include_figures=False)
    jellore = Report(location_name='Jellore State Forest', location_filter='jellore', download_databases=False,
                     include_figures=False)
    meryla = Report(location_name='Meryla State Forest', location_filter='meryla', download_databases=False,
                    include_figures=False)
    belanglo = Report(location_name='Belanglo State Forest', location_filter='belanglo', download_databases=False,
                      include_figures=False)
    olney = Report(location_name='Olney State Forest', location_filter='olney', download_databases=False,
                   include_figures=False)
    kuluwan = Report(location_name='Kuluwan Flora Reserve', location_filter='kuluwan', download_databases=False,
                     include_figures=False)
    warrawolong = Report(location_name='Warrawolong Nature Reserve', location_filter='warrawolong',
                         download_databases=False, include_figures=False)
    corrabare = Report(location_name='Corrabare South Flora Reserve', location_filter='corrabare',
    					download_databases=False, include_figures=False)
    watagan = Report(location_name='Watagan State Forest', location_filter='watagan', download_databases=False,
                     include_figures=False)
    comleroy = Report(location_name='Comleroy State Forest', location_filter='comleroy', download_databases=False,
                      include_figures=False)
    lindesay = Report(location_name='Mount Lindesay State Forest', location_filter='lindesay', avoid_kmls=True,
                      download_databases=False, include_figures=False)
    donaldson = Report(location_name='Donaldson State Forest', location_filter='donaldson', avoid_kmls=True,
                       download_databases=False, include_figures=False)
    unumgar = Report(location_name='Unumgar State Forest', location_filter='unumgar', avoid_kmls=True,
                     download_databases=False, include_figures=False)
    crescent = Report(location_name='Crescent Head', location_filter='crescent', download_databases=False,
                      include_figures=False)
    bar = Report(location_name='Bar Flora Reserve', location_filter='Bar', avoid_kmls=True, case=True,
                 download_databases=False, include_figures=False)
    stockrington = Report(location_name='Stockrington State Conservation Area', location_filter='stockrington',
                          download_databases=False, include_figures=False)
    koreelah = Report(location_name='Koreelah State Forest', location_filter=r"[K|k]oo?ree?lah", avoid_kmls=True,
                      regex=True, download_databases=False, include_figures=False)

    report_list = [willi, jellore, meryla, belanglo, olney, kuluwan, warrawolong, corrabare, watagan, comleroy,
                    lindesay, donaldson, unumgar, crescent, bar, stockrington, koreelah]

    airdata = []
    detections = []
    detections_list = []
    kmls = []
    locations = []
    species_list = []
    surveys = []
    table_df = []

    for report in report_list:
        print(f"Generating databases for the {report.location_name} survey...")
        generate_report(report, report_location='')
        airdata.append(report.airdata)
        detections.append(report.detections)
        detections_list.append(report.detections_list)
        kmls.append(report.kmls)
        locations.append(report.locations)
        species_list.append(report.species_list)
        surveys.append(report.surveys)
        table_df.append(report.table_df)

    # Concatenate and export summary databases for each variable
    airdata_summary = pd.concat(airdata, ignore_index=True).drop_duplicates()
    airdata_summary.to_csv(os.path.join(database_location, 'summary', 'airdata.csv'), index=False)

    detections_summary = pd.concat(detections, ignore_index=True).drop_duplicates()
    detections_summary.to_csv(os.path.join(database_location, 'summary', 'detections.csv'), index=False)

    detections_list_summary = pd.concat(detections_list, ignore_index=True).drop_duplicates()

    detections_list_summary.to_csv(os.path.join(database_location, 'summary', 'detections_list.csv'), index=False)

    kmls_summary = pd.concat(kmls, ignore_index=True).drop_duplicates()
    kmls_summary.to_csv(os.path.join(database_location, 'summary', 'kmls.csv'), index=False)

    locations_summary = pd.concat(locations, ignore_index=True).drop_duplicates()
    locations_summary.to_csv(os.path.join(database_location, 'summary', 'locations.csv'), index=False)

    species_list_summary = pd.concat(species_list, ignore_index=True).drop_duplicates()
    species_list_summary.to_csv(os.path.join(database_location, 'summary', 'species_list.csv'), index=False)

    surveys_summary = pd.concat(surveys, ignore_index=True).drop_duplicates()
    surveys_summary.to_csv(os.path.join(database_location, 'summary', 'surveys.csv'), index=False)

    table_df_summary = pd.concat(table_df, ignore_index=True).drop_duplicates()
    table_df_summary.to_csv(os.path.join(database_location, 'summary', 'table_df.csv'), index=False)

if __name__ == '__main__':
    willi = Report(location_name='Willi Willi National Park', location_filter='willi')
    jellore = Report(location_name='Jellore State Forest', location_filter='jellore')
    meryla = Report(location_name='Meryla State Forest', location_filter='meryla')
    belanglo = Report(location_name='Belanglo State Forest', location_filter='belanglo')
    olney = Report(location_name='Olney State Forest', location_filter='olney')
    kuluwan = Report(location_name='Kuluwan Flora Reserve', location_filter='kuluwan')
    warrawolong = Report(location_name='Warrawolong Nature Reserve', location_filter='warrawolong')
    corrabare = Report(location_name='Corrabare South Flora Reserve', location_filter='corrabare')
    watagan = Report(location_name='Watagan State Forest', location_filter='watagan')
    comleroy = Report(location_name='Comleroy State Forest', location_filter='comleroy')
    lindesay = Report(location_name='Mount Lindesay State Forest', location_filter='lindesay', avoid_kmls=True)
    donaldson = Report(location_name='Donaldson State Forest', location_filter='donaldson', avoid_kmls=True)
    unumgar = Report(location_name='Unumgar State Forest', location_filter='unumgar', avoid_kmls=True)
    crescent = Report(location_name='Crescent Head', location_filter='crescent')
    bar = Report(location_name='Bar Flora Reserve', location_filter='Bar', avoid_kmls=True, case=True)
    stockrington = Report(location_name='Stockrington State Conservation Area', location_filter='stockrington')
    koreelah = Report(location_name='Koreelah State Forest', location_filter=r"[K|k]oo?ree?lah", avoid_kmls=True,
                      regex=True)

    reports_list = [willi, jellore, meryla, belanglo, olney, kuluwan, warrawolong, corrabare, watagan, comleroy,
                    lindesay, donaldson, unumgar, crescent, bar, stockrington, koreelah]

    all_location_filters = ['willi', 'jellore', 'meryla', 'belanglo', 'olney', 'kuluwan', 'warrawolong', 'koreelah',
                            'corrabare', 'barrington', 'watagan', 'comleroy', 'lindesay', 'donaldson',
                            'unumgar', 'Bar', 'crescent', 'stockrington']

    gunnedah = Report(location_name='Gunnedah', location_filter='gunnedah')

    generate_report(report=jellore)

    # generate_summary_databases(reports_list)

    # generate_multiple_reports(reports_list, report_location='NPWS')