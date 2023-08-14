import numpy as np
import pandas as pd


class OrthogonalArray:
    def __init__(self, table_type: str) -> None:
        assert table_type in ('L4', 'L8', 'L9')

        self.table_type = table_type

    def create_orthogonal_array(self):
        if self.table_type == "L4":
            return self.L4()
        elif self.table_type == "L8":
            return self.L8()
        elif self.table_type == "L9":
            return self.L9()

    def L4(self):
        """
        Create L4(2^3) of two level orthogonal array
        """
        L4 = np.array(
            [
                [1, 1, 1],
                [1, 2, 2],
                [2, 1, 2],
                [2, 2, 1]
            ],
        )
        return pd.DataFrame(L4, columns=[f"v{i+1}" for i in range(3)])

    def L8(self):
        """
        Create L8(2^7) of two level orthogonal array
        """
        L8 = np.array([
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 2, 2, 2, 2],
            [1, 2, 2, 1, 1, 2, 2],
            [1, 2, 2, 2, 2, 1, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 2, 1, 2, 1],
            [2, 2, 1, 1, 2, 2, 1],
            [2, 2, 1, 2, 1, 1, 2]
        ])
        return pd.DataFrame(L8, columns=[f"v{i+1}" for i in range(7)])

    def L9(self):
        """
        Create L9 (3^4) of three-level orthogonal array
        """
        L9 = np.array(
            [
                [1, 1, 1, 1],
                [1, 2, 2, 2],
                [1, 3, 3, 3],
                [2, 1, 2, 3],
                [2, 2, 3, 1],
                [2, 3, 1, 2],
                [3, 1, 3, 2],
                [3, 2, 1, 3],
                [3, 3, 2, 1]
            ]
        )
        return pd.DataFrame(L9, columns=[f"v{i+1}" for i in range(4)])


if __name__ == "__main__":
    pass
