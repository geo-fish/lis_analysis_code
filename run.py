import clean
import network
import plot
from utils import column_names, plot_titles, check_data_present
import pandas as pd
from utils import create_directories
import os

# Create project directories
create_directories()


for filename in ['raw_data.csv', 'aims_matrix_final.csv', 'aim_network_nodes.csv']:
    check_data_present(filename)

# Read in data from csv file
all_data = pd.read_csv("./data/raw_data.csv")
network_data = pd.read_csv("./data/aims_matrix_final.csv")
node_name_data = pd.read_csv("./data/aim_network_nodes.csv")


#   Plot data for all columns
for col_name, plot_title in zip(column_names, plot_titles):
    plot.plot_col_data(col_name, all_data, plot_title)

#   Plot data for nielsen components
nilsen_keys, nilsen_counts = clean.combine_all_nielsen_components(all_data)
plot.plot_nielsen_data(nilsen_keys, nilsen_counts, "Nilsen")


#   Run network analysis on aim data
network.clean_node_names(node_name_data)
all_row_data = network.return_row_data_lists(network_data)
network.write_all_permutations(all_row_data)

