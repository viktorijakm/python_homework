import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        num_rows = len(self)
        for start in range(0, num_rows, 10):
            end = min(start + 10, num_rows)
            print(f"\nRows {start} to {end - 1}")
            print(self.iloc[start:end])

# ---- Main code ----
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
