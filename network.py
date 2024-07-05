import pandas as pd
import itertools


def return_row_data_lists(data):
    row_data_lists = []

    for index, row in data.iterrows():
        row_data = row.tolist()[1:]
        row_data_lists.append(row_data)

    return row_data_lists


def clean_node_names(node_csv):  # remove colons and letters from node labels
    node_names = node_csv["Label"].to_list()
    cleaned_node_names = [name.split(": ")[1] for name in node_names]
    node_csv["Label"] = cleaned_node_names
    node_csv.to_csv("./network_analysis/aim_network_nodes.csv", index=False)


def write_all_permutations(all_row_data):
    permutations = []
    for row_data_list in all_row_data:
        x = create_permutations(row_data_list)
        permutations.extend(x)

    data_dicts = [
        {"Source": x[0], "Target": x[1], "Type": "Undirected", "Weight": 1}
        for x in permutations
    ]
    data_frame = pd.DataFrame(data_dicts)
    data_frame.to_csv("./network_analysis/network_edges.csv", index=False)


def create_permutations(row_data):
    keys = []
    for count, item in enumerate(row_data, start=1):
        if item == 1:
            keys.append(count)

    permutations = list(itertools.combinations(keys, 2))
    return permutations
