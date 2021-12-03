import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from chemcharts.core.container.chemdata import ChemData
from chemcharts.core.plots import BasePlot

from chemcharts.core.utils.enums import PlottingEnum
_PE = PlottingEnum


class ScatterBoxplotPlot(BasePlot):
    def __init__(self):
        super().__init__()

    def plot(self, chemdata: ChemData, parameters: dict, settings: dict):
        xlim = parameters[_PE.PARAMETERS_XLIM]
        ylim = parameters[_PE.PARAMETERS_YLIM]
        path = settings[_PE.SETTINGS_PATH]

        self._prepare_folder(path=path)

        scatter_df = pd.DataFrame({"UMAP_1": chemdata.get_embedding().np_array[:, 0],
                                  "UMAP_2": chemdata.get_embedding().np_array[:, 1],
                                   "z": chemdata.get_scores()})

        sns.set_context("talk", font_scale=0.5)
        plt.figure(figsize=(17, 17))
        g = sns.JointGrid(data=scatter_df,
                          x="UMAP_1",
                          y="UMAP_2",
                          xlim=xlim,
                          ylim=ylim
                          )
        g.plot_joint(sns.scatterplot)
        g.plot_marginals(sns.boxplot)

        plt.subplots_adjust(top=0.9)
        plt.suptitle('Scatter Boxplot ChemCharts Plot', fontsize=14)

        plt.savefig(path, format='png', dpi=150)
        plt.close("all")
