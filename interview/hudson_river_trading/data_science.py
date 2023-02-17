from typing import Any

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class AnalysisDataAndFitLinearRegression:

    def __init__(self):
        self.version = 1

    def analyze_and_fit_lrm(self, path: str) -> dict[str, dict[str, dict]]:
        df = pd.read_csv(path)

        return {
            'summary_dict': self.get_summary_dict(df),
            'regression_dict': self.get_regression_dict(df.dropna()),
        }

    def get_summary_dict(self, df: pd.DataFrame) -> dict[str, Any]:
        return {
            'statistics': self.get_statistics(df),
            'data_frame': self.get_data_frame(df),
            'number_of_observations': self.get_number_of_observations(df),
        }

    def get_statistics(self, df: pd.DataFrame) -> list[float]:
        df = df[(df['Bathroom'] == 2) & (df['Bedroom'] == 4)]
        tax = df['Tax']
        return [
            tax.mean(),
            tax.std(),
            tax.median(),
            tax.min(),
            tax.max(),
        ]

    def get_data_frame(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[df['Space'] > 800]
        df = df.sort_values(by='Price', ascending=False)
        return df

    def get_number_of_observations(self, df: pd.DataFrame) -> int:
        df = df[df['Lot'] >= df['Lot'].quantile(4/5)]
        return len(df)

    def get_regression_dict(self, df: pd.DataFrame) -> dict[str, Any]:
        lrm = self.train_lrm(df)
        return {
            'model_parameters': self.get_model_parameters(lrm),
            'price_prediction': self.get_price_prediction(lrm),
        }

    def train_lrm(self, df: pd.DataFrame) -> LinearRegression:
        X = df.drop(columns='Price').to_numpy()
        y = df['Price'].to_numpy()
        return LinearRegression().fit(X, y)

    def get_model_parameters(self, lrm: LinearRegression) -> dict[str, float]:
        intercept = lrm.intercept_
        coefficients = lrm.coef_
        return {
            'Intercept': intercept,
            'Bedroom': coefficients[0],
            'Space': coefficients[1],
            'Room': coefficients[2],
            'Lot': coefficients[3],
            'Tax': coefficients[4],
            'Bathroom': coefficients[5],
            'Garage': coefficients[6],
            'Condition': coefficients[7],
        }

    def get_price_prediction(self, lrm: LinearRegression) -> float:
        # Bedroom Space Room Lot Tax Bathroom Garage Condition
        test = np.array([
            [3, 1500, 8, 40, 1000, 2, 1, 0]
        ])
        predictions = lrm.predict(test)
        return predictions[0]

sol = AnalysisDataAndFitLinearRegression()
print(sol.analyze_and_fit_lrm('./data/realest.csv'))
