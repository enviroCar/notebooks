import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd


def plot(df: pd.DataFrame, freq_seconds: int):
    """
    Creates a time-series plot

    Parameters
    ----------
    df: pd.DataFrame
        Time indexed data frame
    freq_seconds:
        x-label tick frequency
    """
    time_index = df.index
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(x=time_index, y="value", hue="pid", style="pid", markers=True, data=df, ax=ax)
    ax.set_xlim(time_index[0], time_index[-1])
    ax.set_ylim(bottom=0)
    ax.set(xlabel="Time", ylabel="Measurement")
    ax.xaxis.set_major_locator(mdates.SecondLocator(interval=freq_seconds))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    ax.tick_params(axis="x", rotation=90)
    return fig, ax
