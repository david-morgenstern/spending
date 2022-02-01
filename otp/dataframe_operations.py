from pandas import DataFrame


def get_by_date_group(df: DataFrame) -> DataFrame:
    return df.groupby('date', as_index=True)['amount'].sum().to_frame()


def get_by_target_group(df: DataFrame) -> DataFrame:
    return df.groupby('target', as_index=True)['amount'].sum().to_frame()
