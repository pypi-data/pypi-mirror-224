# import pandas as pd

# from doelab.doe.orthogonal_array import OrthogonalArray as oa
# from doelab.analysis.anova import anova


# def test_anova_L4():
#     table_obj = oa('L4')
#     table_L4 = table_obj.create_orthogonal_array()
#     results_L4 = pd.Series([10, 15, 12, 14])
#     assert anova(table_L4, results_L4).equals(expected_anova_L4)

# def test_anova_L9():
#     results_L9 = pd.Series([5, 8, 7, 10, 8, 9, 6, 7, 8])
#     assert anova(L9, results_L9).equals(expected_anova_L9)
