import numpy as np

J_het = np.nan

class Constant:
    @staticmethod
    def _check():
        assert np.isfinite(J_het)

    @staticmethod
    def J_het():
        return J_het
