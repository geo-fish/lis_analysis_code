#### Code to analyse data associated with "Leveraging implementation science to solve the big problems:A scoping review of health system preparations for the impact of pandemics and climate change."

The code in this library completes all analyses reported in the submitted manuscript *"Leveraging implementation science to solve the big problems: A scoping review of health system preparations for the impact of pandemics and climate change."*

To run this package, please first download all files and directory structures to a new directory in your Documents folder. 

To run the code from your command line:
1. Ensure Python is installed on your machine and added to your path variables
2. Open a terminal and navigate to the directory in which the code is saved.
2. Run the line: `pip install -r requirements.txt`
3. Run the run.py file with `python run.py`

To run the code from your preferred Python interpreter or IDE:
1. Open your IDE and navigate to the directory in which the code is saved
2. Install all packages in requirements.txt
3. Run all lines in the run.py file 

Note that error messages will display if the project data files are not stored appropriately. 
To prevent such an error, please ensure that your project directory contains the following three files, names as below:
1. aim_network_nodes.csv
2. aims_matrix_final.csv
3. raw_data.csv

##### Outputs

Three subdirectories will be created in your project directory: data_summaries/, network_analysis/, and plots/.

Once run.py is run, the resultant project directory will be:

```
lis_analysis_code
├── aim_network_nodes.csv
├── aims_matrix_final.csv
├── clean.py
├── data_summaries/
│   ├── long_format/    # Data from raw dataframe in long format
│   │   ├── classic_theory_long_format.csv
│   │   ├── client_oucomes_long_format.csv
│   │   ├── determinant_framework_long_format.csv
│   │   ├── evaluation_framework_long_format.csv
│   │   ├── implementation_outcomes_long_format.csv
│   │   ├── implementation_science_long_format.csv
│   │   ├── implementation_stage_long_format.csv
│   │   ├── implementation_theory_long_format.csv
│   │   ├── method_long_format.csv
│   │   ├── process_model_long_format.csv
│   │   ├── proctor_outcomes_long_format.csv
│   │   ├── service_outcomes_long_format.csv
│   │   ├── setting_type_long_format.csv
│   │   ├── sites_long_format.csv
│   │   ├── system_country_long_format.csv
│   │   └── system_level_long_format.csv
│   └── summary_data/   # Counts of unique items in each dataframe column
│       ├── classic_theory_summary.csv
│       ├── client_oucomes_summary.csv
│       ├── determinant_framework_summary.csv
│       ├── evaluation_framework_summary.csv
│       ├── implementation_outcomes_summary.csv
│       ├── implementation_science_summary.csv
│       ├── implementation_stage_summary.csv
│       ├── implementation_theory_summary.csv
│       ├── method_summary.csv
│       ├── nilsen_sub_component_summary.csv
│       ├── process_model_summary.csv
│       ├── proctor_outcomes_summary.csv
│       ├── service_outcomes_summary.csv
│       ├── setting_type_summary.csv
│       ├── sites_summary.csv
│       ├── system_country_summary.csv
│       └── system_level_summary.csv
├── network.py
├── network_analysis/   # .csv files to enter into Gephi network analysis
│   ├── aim_network_nodes.csv
│   └── network_edges.csv
├── plot.py
├── plots/      # Plots of review outcomes
│   ├── client_oucomes_fig.png
│   ├── implementation_outcomes_fig.png
│   ├── implementation_science_fig.png
│   ├── implementation_stage_fig.png
│   ├── method_fig.png
│   ├── nilsen.png
│   ├── proctor_outcomes_fig.png
│   ├── service_outcomes_fig.png
│   ├── setting_type_fig.png
│   ├── sites_fig.png
│   ├── system_country_fig.png
│   └── system_level_fig.png
├── raw_data.csv
├── README.md
├── requirements.txt
├── run.py
└── utils.py
```