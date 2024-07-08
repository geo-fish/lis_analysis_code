import pandas as pd
from matplotlib import pyplot as plt

from clean import clean_column_data_and_store_summary


def plot_and_summarise_col_data(
    col_name, data, plot_name
):
    """ Plot and store summary data from a single column
     Parameters
     -----------
        col_name: str
            Name of target column in dataframe
        data: pandas dataframe
            Dataframe of raw review data
        plot_name: str
            Title for output plot
    """
    keys, counts = clean_column_data_and_store_summary(col_name, data)

    x_max = max(counts) + 5     # Set max x-axis value as the max count plus 5
    x_min = 0                   # Set min x-axis value as 0
    x_ticks = list(range(x_min, x_max, 5))  # Create list of x ticks

    y_max = len(keys)           # Mimic above for y-axis
    y_min = 0
    y_ticks = list(range(y_min + 1, y_max + 1))

    plt.figure(figsize=(5, 5))

    for y_tick, x_val in zip(y_ticks, counts):  # Plot a horizontal line graph of current column data
        plt.plot((0, x_val), (y_tick, y_tick), c="black", linewidth=3)
        plt.plot(x_val, y_tick, linewidth=0, marker="o", c="black")

    plt.yticks(y_ticks, keys, fontfamily="Arial", fontsize=10)
    plt.xticks(x_ticks, x_ticks, fontfamily="Arial", fontsize=10)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max + 1)
    plt.xlabel("N included studies", fontfamily="Arial", fontsize=12)
    plt.title(plot_name, fontfamily="Arial", fontsize=12)

    plt.grid(alpha=0.5)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig_path = f"./plots/{col_name}_fig.png"

    plt.savefig(fig_path, dpi=200, bbox_inches="tight")
    print(f'Plot created for {col_name} column, saved in {fig_path}')
    plt.close()


def plot_nielsen_data(
    keys, values, plot_name
):  # Define function to plot data from a single column

    x_max = max(values) + 5
    x_min = 0
    x_ticks = list(range(x_min, x_max, 5))

    y_max = len(keys)
    y_min = 0
    y_ticks = list(range(y_min + 1, y_max + 1))

    plt.figure(figsize=(5, 10))

    for y_tick, x_val in zip(y_ticks, values):
        plt.plot((0, x_val), (y_tick, y_tick), c="black", linewidth=3)
        plt.plot(x_val, y_tick, linewidth=0, marker="o", c="black")

    plt.yticks(y_ticks, keys, fontfamily="Arial", fontsize=10)
    plt.xticks(x_ticks, x_ticks, fontfamily="Arial", fontsize=10)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max + 1)
    plt.xlabel("N included studies", fontfamily="Arial", fontsize=12)
    plt.title(plot_name, fontfamily="Arial", fontsize=12)

    plt.grid(alpha=0.5)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    all = {"Nielsen Component": keys, "Counts": values}
    all_out = pd.DataFrame(all)
    all_out.to_csv("data_summaries/summary_data/nilsen_sub_component_summary.csv")

    plt.savefig(f"./plots/nilsen.png", dpi=200, bbox_inches="tight")
    print(f'Plot created for summary of Nilsen sub-components, saved to ./plots/nilsen.png')
    plt.close()
