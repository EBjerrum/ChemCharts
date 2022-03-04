import unittest
import pandas as pd

from chemcharts.core.container.chemdata import ChemData
from chemcharts.core.container.fingerprint import *
from chemcharts.core.functions.binning import Binning


class TestBinning(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        smiles = Smiles(["COc1ccc(-c2c(-c3ccc(S(N)(=O)=O)cc3)[nH]c3ccccc23)cc1",
                         "COc1ccc(-c2c(-c3ccc(S(N)(=O)=O)cc3)oc3ccccc23)cc1F",
                         "Cc1cc(C)c(S(=O)(=O)N2CCN(C(C)c3nc(C(C)(C)C)no3)CC2)c(C)c1",
                         "C1ccc2c(c1)-c1ccc3ccccc3c1C2Cc1nn[nH]n1",
                         "Cc1ccccc1-c1c(C(=O)N=c2cccc[nH]2)cnc2ccccc12",
                         "N=c1[nH]c(=O)c2ncn(Cc3cccc4ccccc34)c2[nH]1",
                         "O=C1c2cccc3c(F)ccc(c23)CN1c1cccnc1"])
        values = pd.DataFrame([1, 3, 4, 5, 2, 1, 6], columns=["test_value"])

        test_data_set = ChemData(smiles)
        test_data_set.set_values(values)
        cls.test_chemdata = test_data_set
    """
    def test_preparation(self):
        binning = Binning()
        test_sorted_bin_idx, test_bin_idx = binning._preparation(scores=[1.333, 2.33, -1, 4.3, 7.9, 9.5, 5.1],
                                                                 num_bins=4)
        self.assertListEqual([0, 1, 2], test_sorted_bin_idx)
        self.assertListEqual([0, 0, 0, 1, 2, 2, 1], test_bin_idx)

    def test_group_scores_bins(self):
        binning = Binning()
        test_group_scores_bins = binning._group_scores_bins(scores=[1.333, 2.33, -1, 4.3, 7.9, 9.5, 5.1],
                                                            sorted_bin_idx=[0, 1, 2],
                                                            bin_idx=[0, 0, 0, 1, 2, 2, 1])
        self.assertListEqual([1.333, 2.33, -1], test_group_scores_bins[0])

    def test_calculate_medians(self):
        binning = Binning()
        test_median_scores = binning._calculate_medians(grouped_scores_bins=[[1.333, 2.33, -1], [4.3, 5.1], [7.9, 9.5]])
        self.assertListEqual([1.333, 4.699999999999999, 8.7], test_median_scores)

    def test_overwrite_scores_medians(self):
        binning = Binning()
        test_new_scores = binning._overwrite_scores_medians(bin_idx=[0, 0, 0, 1, 2, 2, 1],
                                                            median_scores=[1.333, 4.699999999999999, 8.7])
        self.assertListEqual([1.333, 1.333, 1.333, 4.699999999999999, 8.7, 8.7, 4.699999999999999], test_new_scores)

    def test_binning(self):
        binning = Binning()
        test_binning = binning.binning(self.test_chemdata, 4)
        self.assertListEqual([1.333, 1.333, 1.333, 4.699999999999999, 8.7, 8.7, 4.699999999999999],
                             test_binning.get_scores())
    """

    def test_preparation(self):
        binning = Binning()
        test_sorted_bin_idx, test_bin_idx = binning._preparation(values=[1, 3, 4, 5, 2, 1, 6],
                                                                 num_bins=4)
        self.assertListEqual([0, 1, 2], test_sorted_bin_idx)
        self.assertListEqual([0, 1, 1, 2, 0, 0, 2], test_bin_idx)

    def test_group_value_bins(self):
        binning = Binning()
        test_group_value_bins = binning._group_values_bins(values=[1, 3, 4, 5, 2, 1, 6],
                                                           sorted_bin_idx=[0, 1, 2],
                                                           bin_idx=[0, 1, 1, 2, 0, 0, 2])
        self.assertListEqual([1, 2, 1], test_group_value_bins[0])

    def test_calculate_medians(self):
        binning = Binning()
        test_median_values = binning._calculate_medians(grouped_value_bins=[[1, 2, 1], [3, 4], [5, 6]])
        self.assertListEqual([1, 3.5, 5.5], test_median_values)

    def test_overwrite_values_medians(self):
        binning = Binning()
        test_new_values = binning._overwrite_value_medians(bin_idx=[0, 1, 1, 2, 0, 0, 2],
                                                           median_values=[1, 3.5, 5.5])
        self.assertListEqual([1, 3.5, 3.5, 5.5, 1, 1, 5.5], test_new_values)

    def test_binning(self):
        binning = Binning()
        test_binning = binning.binning(self.test_chemdata, 4)
        value_df = test_binning.get_values()
        self.assertListEqual(list([1, 3.5, 3.5, 5.5, 1, 1, 5.5]),
                             value_df["test_value"].tolist())
