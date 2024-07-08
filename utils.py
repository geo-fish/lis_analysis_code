import os
import warnings

column_names = [
    "method",
    "sites",
    "setting_type",
    "system_level",
    "system_country",
    "implementation_science",
    "implementation_stage",
    "proctor_outcomes",
    "service_outcomes",
    "client_oucomes",
    "implementation_outcomes"
]
plot_titles = [
    "Study method",
    "Sites",
    "Healthcare setting",
    "Health system level",
    "Country",
    "Nielsen Component",
    "Implementation stage",
    "Proctor Component",
    "Service outcomes",
    "Client outcomes",
    "Implementation outcomes"
]


def create_directories():
    """
    Create required subdirectories in current project directory

    """
    dir_names = ['plots', 'data_summaries', 'network_analysis']
    sub_dir_names = ['long_format', 'summary_data']
    for directory_name in dir_names:
        if not os.path.exists(f'./{directory_name}'):
            os.mkdir(f'./{directory_name}')
            print(f'Created directory at ./{directory_name}/')
        else:
            print(f'Directory at ./{directory_name} exists, continuing.')

    for directory_name in sub_dir_names:
        if not os.path.exists(f'./data_summaries/{directory_name}'):
            os.mkdir(f'./data_summaries/{directory_name}')
            print(f'Created directory at ./data_summaries/{directory_name}/')
        else:
            print(f'Directory at ./data_summaries/{directory_name} exists, continuing.')

    print('\n\n\n\n\n')


nilsen_column_names = [
    "process_model",
    "implementation_theory",
    "determinant_framework",
    "classic_theory",
    "evaluation_framework",
]

nilsen_plot_names = [
    "Process Model",
    "Implementation Theory",
    "Determinant Framework",
    "Classic Theory",
    "Evaluation Framework",
]


def check_data_present(filename):
    """
    Check required data files are present, raise error if not
    Parameters
    ----------
    filename: str
        name of a single required file

    """
    filepath = f'./{filename}'
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file '{filename}' was not found in the project directory."
                                f"Please check that your working directory contains all relevant data files, "
                                f"maintaining their filenames as downloaded from the repo")
