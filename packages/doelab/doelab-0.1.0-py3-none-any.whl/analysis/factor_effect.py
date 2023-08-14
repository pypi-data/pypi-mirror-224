import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_factor_effects(df: pd.DataFrame, results: pd.DataFrame) -> None:
    """
    Create a factor effects plot for the given orthogonal array and results.

    Args:
    df: pd.DataFrame
        Orthogonal array (factors)
    results: pd.Series
        Experiment results
    """
    n_factors = df.shape[1]
    plt.figure(figsize=(12, 8))

    # Calculate global y-axis limits
    all_means = []
    for col in df.columns:
        levels = df[col].unique()
        means = [results[df[col] == level].mean() for level in levels]
        all_means.extend(means)
    ylim = (min(all_means), max(all_means))
    mean_all = np.mean(all_means)

    for i, col in enumerate(df.columns, 1):
        levels = df[col].unique()
        means = [results[df[col] == level].mean() for level in levels]

        plt.subplot(2, (n_factors + 1) // 2, i)
        plt.plot(levels, len(levels) * [mean_all], color='red')
        plt.plot(levels, means, marker='o', color='blue', linestyle='-')
        # plt.title(col)
        plt.xlabel(col)
        plt.ylabel('target variable')
        plt.ylim(ylim)  # Set uniform y-axis limits
        plt.grid(True)

    plt.tight_layout()
    plt.savefig('tmp.png')
    plt.show()


if __name__ == "__main__":
    import sys
    sys.path.append('./')
    import numpy as np
    from doelab.doe.orthogonal_array import OrthogonalArray as oa
    from doelab.analysis.anova import anova

    # Test by L8
    table_type = 'L8'
    array_obj = oa(table_type)
    table = array_obj.create_orthogonal_array()
    # Dummy results for L8
    # results = pd.Series([10, 11, 12, 13, 14, 15, 16, 17])
    results = pd.Series([8, 11, 5, 13, 7, 18, 7, 10])
    # Create the factor effects plot for L8 orthogonal array
    plot_factor_effects(table, results)