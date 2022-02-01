from typing import List

import pandas as pd


def csv_to_dataframe(file_paths: List[str]) -> pd.DataFrame:
    df_list = [
        pd.read_csv(file_path,
                    delimiter=";", skipinitialspace=True,
                    names=
                    [1, 2, 'amount', 'currency', 5, 'date', 7, 8, 'target', 'comment', 11, 12, 'type', 14, 15],
                    index_col=None, header=0) for file_path in file_paths]

    df = pd.concat(df_list, axis=0, ignore_index=True)
    df.drop(axis=1, columns=[1, 2, 5, 7, 8, 11, 12, 14, 15], inplace=True)
    df['date'] = df['date'].fillna(method='ffill')
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    df['target'].fillna(df['type'], inplace=True)
    df.replace({"^\s*|\s*$": ""}, regex=True, inplace=True)

    return df
