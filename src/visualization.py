import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_offense_description_frequency(df, output_path):
    offense_counts = df["OFFENSE_DESCRIPTION"].value_counts()

    # Create a bar plot
    plt.figure(figsize=(50, 50))
    sns.barplot(x=offense_counts.values, y=offense_counts.index, palette="viridis")
    plt.xlabel("Frequency")
    plt.ylabel("Offense Description")
    plt.title("Frequency of Each Offense Description")
    plt.tight_layout()

    output_file = os.path.join(output_path, "offense_description_frequency.png")
    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    data_folder = "data"
    output_path = "output/plots"
    compiled_file = os.path.join(data_folder, "processed/compiled_data.csv")
    df = pd.read_csv(compiled_file, low_memory=False)
    os.makedirs(output_path, exist_ok=True)

    df.groupby(["OFFENSE_DESCRIPTION", "OFFENSE_CODE"]).size().to_csv(
        "output/offense_count.csv"
    )
