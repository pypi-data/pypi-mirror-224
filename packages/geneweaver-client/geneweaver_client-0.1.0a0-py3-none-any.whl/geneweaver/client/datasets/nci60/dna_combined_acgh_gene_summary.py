"""Dataset definition for NCI60's: DNA__Combined_aCGH_gene_summary.xls"""
import pandas as pd
from geneweaver.client.datasets.base import BaseDataset


class DNACombinedaCGHGeneSummary(BaseDataset):

    URL = "https://discover.nci.nih.gov/cellminer/download/processeddataset/" \
          "nci60_DNA__Combined_aCGH_gene_summary.zip"
    DS_FOLDER = "nci60_DNA__Combined_aCGH_gene_summary"
    UNZIPPED_LOC = "output/DNA__Combined_aCGH_gene_summary.xls"

    def __init__(self, base_folder: str = 'data'):
        super().__init__(base_folder)
        self.download_zip_file()
        self.dataset_skip_rows = 10
        self._pandas_read_f = pd.read_excel

    def entrez_ids(self) -> pd.DataFrame:
        """Return the dataset's entrez ids."""
        return self.as_pandas().iloc[:, 1]

    def gene_names(self) -> pd.DataFrame:
        """Return the dataset's gene names."""
        return self.as_pandas().iloc[:, 0]

    def intensity_values(self) -> pd.DataFrame:
        """Return the dataset's intensity values."""
        return self.as_pandas().iloc[:, 6:]
