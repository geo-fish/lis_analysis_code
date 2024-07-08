import pandas as pd
import itertools


def return_row_data_lists(data):
    """
    Read in data from dataframe and store each row as a list, excluding the index row

    Parameters
    -----------
    data: pandas dataframe object

    Returns
    ---------
    row_data_lists: list[lists]
        Individual lists of data in each row of the input dataframe

    """
    row_data_lists = []

    for index, row in data.iterrows():
        row_data = row.tolist()[1:]
        row_data_lists.append(row_data)

    return row_data_lists


def clean_node_names(node_csv):
    """ Remove colons and letters from node labels, store as clean node csv for Gephi input
    Parameters
    -----------
    node_csv: pandas dataframe object
        data from Nvivo matrix output
    """
    node_names = node_csv["Label"].to_list()
    cleaned_node_names = [name.split(": ")[1] for name in node_names]
    node_csv["Label"] = cleaned_node_names
    node_csv.to_csv("./network_analysis/aim_network_nodes.csv", index=False)


def write_all_permutations(all_row_data):
    """
    Store and output all permutations of node relationships as csv file

    Parameters
    -----------
    all_row_data: list[lists]
        lists of the row data from a relationship matrix, where columns are themes and rows are articles
        0 indicates no presence of the theme in an article, and a 1 indicates the presence of a theme in an article

    """
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
    """
    Return permutations of pairs of objects in an ordered list, where each item represents a theme, and theme order
    is consistent in each list.
    Parameters
    ----------
    row_data: list

    Returns
    --------
    permutations: list(tuples)
        list of tuple permutations of length 2, where each tuple indicates the co-presence of two themes in an article

    """
    keys = []
    for count, item in enumerate(row_data, start=1):    # Return counts of related themes
        if item == 1:
            keys.append(count)

    permutations = list(itertools.combinations(keys, 2))
    return permutations
