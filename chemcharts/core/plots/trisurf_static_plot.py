from typing import List

import matplotlib.pyplot as plt

from chemcharts.core.container.chemdata import ChemData
from chemcharts.core.plots.base_plot import BasePlot

from chemcharts.core.utils.enums import PlottingEnum
from chemcharts.core.utils.enums import PlotLabellingEnum
_PE = PlottingEnum
_PLE = PlotLabellingEnum


class TrisurfStaticPlot(BasePlot):
    def __init__(self):
        super().__init__()

    def plot(self, chemdata_list: List[ChemData], parameters: dict, settings: dict):
        if isinstance(chemdata_list, list):
            print("Function does not support multiple input objects (yet).")
            chemdata_list = chemdata_list[0]

        xlim = parameters.get(_PE.PARAMETERS_XLIM, None)
        ylim = parameters.get(_PE.PARAMETERS_YLIM, None)
        path = settings.get(_PE.SETTINGS_PATH, None)
        scorelim = parameters.get(_PE.PARAMETERS_SCORELIM, None)

        self._prepare_folder(path=path)

#        fig = plt.figure(settings.get(_PE.SETTINGS_FIG_SIZE, (9, 9)))
        fig = plt.figure(figsize=(9, 9))

        ax = plt.axes(projection='3d')

        ax.plot_trisurf(chemdata_list.get_embedding().np_array[:, 0],
                        chemdata_list.get_embedding().np_array[:, 1],
                        chemdata_list.get_scores(),
                        cmap=parameters.get(_PE.PARAMETERS_PLOT_COLOR, plt.get_cmap('twilight_shifted'))
                        )

        # Adding labels
        ax.set_title(parameters.get(_PE.PARAMETERS_PLOT_TITLE, "Trisurf Static ChemCharts Plot"))
        ax.set_xlabel(_PLE.UMAP_1)
        ax.set_ylabel(_PLE.UMAP_2)
        ax.set_zlabel(_PLE.SCORES)

        # Setting axes ranges
        if xlim is not None:
            plt.xlim(xlim[0], xlim[1])
        if ylim is not None:
            plt.ylim(ylim[0], ylim[1])
        if scorelim is not None:
            ax.set_zlim(scorelim[0], scorelim[1])

        plt.savefig(path,
                    format=settings.get(_PE.SETTINGS_FIG_FORMAT, 'png'),
                    dpi=settings.get(_PE.SETTINGS_FIG_DPI, 250))

        plt.close(fig)
