import requests, zipfile, io
from pathlib import Path
import pandas as pd


class BaseDataset:

    URL = None
    DS_FOLDER = None
    UNZIPPED_LOC = None

    def __init__(self, base_folder: str = 'data'):
        self.base_folder = Path(base_folder)

    @property
    def dataset_path(self):
        return self.base_folder / self.DS_FOLDER / self.UNZIPPED_LOC

    def download_zip_file(self, redownload: bool = False) -> None:
        """Download the zip file from the dataset's URL."""
        if not redownload and self.dataset_path.is_file():
            return None

        response = requests.get(self.URL)
        response.raise_for_status()

        z = zipfile.ZipFile(io.BytesIO(response.content))

        z.extractall(self.base_folder / self.DS_FOLDER)

    def as_pandas(self) -> pd.DataFrame:
        """Return the dataset as a Pandas DataFrame."""
        return self._pandas_read_f(
            self.dataset_path,
            skiprows=self.dataset_skip_rows
        )