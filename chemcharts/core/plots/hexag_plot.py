import seaborn as sns
import matplotlib.pyplot as plt

from chemcharts.core.container.chemdata import ChemData


class HexagonalPlot:
    def __init__(self):
        pass

    @staticmethod
    def plot(chemdata: ChemData, path: str):

        sns.jointplot(x=chemdata.get_embedding().np_array[:, 0],
                      y=chemdata.get_embedding().np_array[:, 1],
                      kind="hex",
                      color="#4CB391")

        plt.subplots_adjust(top=0.9)
        plt.suptitle('Hexagonal ChemCharts Plot', fontsize=14)

        plt.savefig(path)
