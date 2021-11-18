import pandas as pd
import plotly.express as px
import os
from chemcharts.core.container.chemdata import ChemData
from copy import deepcopy
import numpy as np
import ffmpeg

from chemcharts.core.container.embedding import Embedding
from chemcharts.core.container.fingerprint import FingerprintContainer
from chemcharts.core.container.smiles import Smiles


class BasePlot:
    def __init__(self):
        pass

    @staticmethod
    def _path_update_snapshot(ori_path: str, epoch_id: int) -> str:
        path, file_name = os.path.split(os.path.abspath(ori_path))
        updated_path = f'{path}/{epoch_id:04}_{file_name}'
        # TODO replace everthing after the last '.' by ".png"
        return updated_path

    def make_movie(self, chemcharts: ChemData, movie_path: str):
        chemcharts = deepcopy(chemcharts)
        sorted_epochs = chemcharts.sort_epoch_list()                                 # [0,1,2]
        indices_list = chemcharts.find_epoch_indices(sorted_epochs)                      # [[0,3,6], [1,2,5], [4]]
        updated_path_list = []
        for idx in range(len(sorted_epochs)):                                         #idx= #0 #1 #2
            epoch_chemdata = chemcharts.filter_epoch(epoch=idx, epoch_indices_list=indices_list[idx])    #indices_list= #[0,3,6] #[1,2,5] #[4]
            updated_snapshot_path = self._path_update_snapshot(ori_path=movie_path, epoch_id=idx)
            updated_path_list.append(updated_snapshot_path)
            self.plot(chemdata=epoch_chemdata, path=updated_snapshot_path)

        path, file_name = os.path.split(os.path.abspath(movie_path))
        (
            ffmpeg
            .input(f"{path}/*.png", pattern_type='glob', framerate=1)
            .output(movie_path)
            .run()
        )

    @staticmethod
    def plot(chemdata: ChemData, path: str):
        raise NotImplemented("This method needs to be overloaded in a child class.")
