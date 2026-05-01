import pandas as pd

def load_and_process_data(
    filepath="data/dataset.csv",
    output_path="data/processed_dataset.csv"
):

    df = pd.read_csv(filepath)

    print("Original shape:", df.shape)

    df_clean = df.drop_duplicates()

    print("After removing duplicates:", df_clean.shape)

    df_clean.to_csv(output_path, index=False)

    return df_clean
