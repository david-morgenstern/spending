from pandas import DataFrame


class Operations:
    def __init__(self, df: DataFrame):
        self.df = df

    @property
    def get_by_date_group(self) -> DataFrame:
        return self.df.groupby('date', as_index=True)['amount'].sum().to_frame()

    @property
    def get_by_target_group(self) -> DataFrame:
        return self.df.groupby('target', as_index=True)['amount'].sum().to_frame()
