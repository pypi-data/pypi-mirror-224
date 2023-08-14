import matplotlib.pyplot as plt
import pandas as pd


def plot_anova_results(anova_table: pd.DataFrame) -> None:
    """
    Visualize the ANOVA table
    
    Args:
    anova_table: pd.DataFrame
        ANOVA table

    Returns:
        None
    """
    # Exclude 'Error' and 'Total' rows
    anova_table = anova_table[:-2]
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(anova_table['Source'], anova_table['SS'], color='steelblue')
    plt.xlabel('Factors')
    plt.ylabel('Sum of Squares (SS)')
    plt.title('Contribution of Factors to Variance')
    plt.grid(axis='y')
    plt.tight_layout()
    # plt.savefig('tmp.png')
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
    print(table)
    result = np.array([40, 46, 28, 18, 32, 26, 32, 58])
    anova_table = anova(table, result)
    print(anova_table)
    plot_anova_results(anova_table)