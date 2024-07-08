import pandas as pd
from collections import Counter
from operator import itemgetter

from utils import nilsen_column_names, nilsen_plot_names


def clean_column_data_and_store_summary(col_name, df):
    """
    Clean, summarise, and save the data from a single column in the review dataframe

    Parameters
    ----------
    col_name: str
        Target column name from review raw data
    df: pandas dataframe
        Review raw data

    Returns
    ----------
    keys: list
        Unique items in the dataframe column
    counts: list
        Counts of each unique item in the dataframe column
    """
    col_data = df[col_name].to_list()
    col_data = [
        x.strip() if type(x) is str else x for x in col_data
    ]  # Strip spaces from all column data points

    new_col_data = []  # Create empty list for new column data

    for x in col_data:
        if (
            type(x) is str
        ):  # Split strings with multiple items into individual string items, clean up string formatting
            column_items = x.split(",")
            column_items = [
                item.title().strip() if len(item) > 7 else item.upper().strip()
                for item in column_items
            ]
            new_col_data.extend(column_items)  # Add all strings to new_col_data
        else:
            new_col_data.append(x)  # Append integers and floats to list

    out = {f"{col_name}": new_col_data}
    out_df = pd.DataFrame(out)
    out_df.to_csv(
        f"./data_summaries/long_format/{col_name}_long_format.csv"
    )  # Export all items to data frame and csv

    unique_items = Counter(new_col_data)  # Calculate counts of each item in list
    keys = []
    counts = []
    for key, value in unique_items.items():
        keys.append(key)
        counts.append(value)

    res = [
        list(x) for x in zip(*sorted(zip(counts, keys), key=itemgetter(0)))
    ]  # Sort keys and values by counts

    counts = res[0]
    keys = res[1]

    summary_data = {"keys": keys, "values": counts}
    summary_df = pd.DataFrame(summary_data)
    save_path = f"./data_summaries/summary_data/{col_name}_summary.csv"
    summary_df.to_csv(save_path)
    print(f"Data summary of {col_name} column saved to {save_path}")

    return keys, counts


def add_spaces(key):  # Function to add spaces to cell text after any commas
    new_key = ""
    for x in key:
        if x == ",":
            new_key = new_key + ", "
        else:
            new_key = new_key + x
    return new_key


def combine_all_nilsen_components(all_data):
    """
    Clean, summarise, and save the data from the columns describing Nilsen components

    Parameters
    ----------
    all_data: pandas dataframe
        Review raw data

    Returns
    ----------
    clean_keys: list
        Unique items in the dataframe column
    clean_counts: list
        Counts of each unique item in the dataframe column
    """
    all_keys = []
    all_counts = []
    components = [
        "Process Models",
        "Implementation Theories",
        "Determinant Frameworks",
        "Classic Theories",
        "Evaluation Frameworks",
    ]

    for col, name, component in zip(nilsen_column_names, nilsen_plot_names, components):
        keys, values = clean_column_data_and_store_summary(col, all_data)
        keys = keys[:-1]  # Remove key for NaNs
        values = values[:-1]  # Remove count of NaNs
        all_keys.append(component)
        all_counts.append(sum(values))
        all_keys.extend(keys)
        all_counts.extend(values)
        all_keys.append("")
        all_counts.append(0)

    clean_keys = []
    clean_counts = []

    for key, value in zip(all_keys, all_counts):
        if type(key) is not float:
            clean_keys.append(key)
            clean_counts.append(value)

    return clean_keys, clean_counts
