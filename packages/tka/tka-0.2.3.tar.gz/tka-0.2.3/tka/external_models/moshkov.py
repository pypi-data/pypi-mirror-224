import chemprop
import numpy as np
from tka.utils import transform_moshkov_outputs
from typing import List, Union
import pandas as pd


def predict_from_smiles(smiles_list: List[str], checkpoint_dir: str, output_type: str = "pandas") -> pd.DataFrame:
    """
    Make predictions from a list of SMILES strings using a trained checkpoint.

    Args:
        smiles_list (List[str]): List of SMILES strings for which to make predictions.
        checkpoint_dir (str): Directory containing the trained checkpoint.

    Returns:
        pd.DataFrame: Predictions with SMILES as indices and assays as columns.
    """
    arguments = [
        '--test_path', '/dev/null',
        '--preds_path', '/dev/null',
        '--checkpoint_dir', checkpoint_dir,
        '--no_features_scaling'
    ]

    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args, smiles=smiles_list)

    return transform_moshkov_outputs(smiles_list, preds, use_full_assay_names=True)

if __name__ == "__main__":
    predict_from_smiles(
        smiles_list=["CCC"],
        checkpoint_dir="/home/filip/Downloads/Moshkov(etal)-single-models/2021-02-cp-es-op"
    )