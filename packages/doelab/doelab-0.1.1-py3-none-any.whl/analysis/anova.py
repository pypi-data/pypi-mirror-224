import pandas as pd
import numpy as np


def anova(df, results):
    """
    Perform ANOVA(Analysis Pf Variance)
    on orthogonal array with given results.

    Args:
    df: pd.DataFrame
        Orthogonal array (factors)
    results: pd.Series
        Experiment results

    Returns:
        pd.DataFrame, ANOVA table
    """
    # Number of experiments
    n_exp = len(df)
    # Number of factors
    n_factor = df.shape[1]

    # Total sum of squares
    SST = results.var() * (n_exp - 1)

    # Compute sum of squares for each factor
    SS = []
    for col in df.columns:
        levels = df[col].unique()
        means = [results[df[col] == level].mean() for level in levels]
        total_mean = results.mean()
        SS.append(
            sum([(m - total_mean) ** 2 for m in means]) * len(results) / len(levels)
        )

    # Error sum of squares
    SSE = SST - sum(SS)

    # Degrees of freedom
    df_factors = [len(df[col].unique()) - 1 for col in df.columns]
    df_error = n_exp - n_factor

    # Mean sum of squares
    MS = [ss / df_ for ss, df_ in zip(SS, df_factors)]
    MSE = SSE / df_error

    # F-values
    F = [ms / MSE for ms in MS]

    # Create ANOVA table
    anova_table = pd.DataFrame(
        {
            "Source": df.columns.tolist() + ["Error", "Total"],
            "DF": df_factors + [df_error, n_exp - 1],
            "SS": SS + [SSE, SST],
            "MS": MS + [MSE, "-"],
            "F": F + ["-", "-"],
        }
    )

    return anova_table


if __name__ == "__main__":
    pass
