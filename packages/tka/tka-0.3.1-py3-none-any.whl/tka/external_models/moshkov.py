import chemprop
import numpy as np
from tka.utils import (
    transform_moshkov_outputs,
    prepare_df_for_mobc_predictions,
    load_mobc_ordered_feature_columns,
)
from typing import List, Union
import pandas as pd
import os


def predict_from_smiles(smiles_list: List[str], checkpoint_dir: str) -> pd.DataFrame:
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

    return transform_moshkov_outputs(
        identifier_col_vals=smiles_list, output=preds, use_full_assay_names=True
    )


def predict_from_mobc(df_real: List[str], checkpoint_dir: str) -> pd.DataFrame:
    """
    Make predictions from a list of SMILES strings using a trained checkpoint.

    Args:
        df_real (pd.DataFrame): a pd.DataFrame with the columns being CellProfiler features (1746 features)
            and the first column being the identification column (a total of 1747 columns)
        checkpoint_dir (str): Directory containing the trained checkpoint.

    Returns:
        pd.DataFrame: Predictions with df_real's first column as indices and assays as columns.
    """
    # Generate and save a dummy smiles CSV file to compy with chemprop_predict
    # Serves no real purpose and does not affect the final predictions in any way
    dummy_smiles = ["CCCC" for _ in range(len(df_real))]
    with open("tmp_smiles.csv", "w") as file:
        for item in ["smiles"] + dummy_smiles:
            file.write(item + "\n")

    # Load the MOBC ordered features to generate .npz file
    mobc_features = load_mobc_ordered_feature_columns()

    # Save the pd.DataFrame so that you can load it from a path
    np.savez("out.npz", features=df_real[mobc_features].to_numpy())

    arguments = [
        "--test_path", "tmp_smiles.csv",
        "--preds_path", "/dev/null",
        "--checkpoint_dir", checkpoint_dir,
        "--features_path", "out.npz",
        "--no_features_scaling",
    ]

    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args)

    # Remove temporary files
    os.remove("out.npz")
    os.remove("tmp_smiles.csv")

    return transform_moshkov_outputs(
        identifier_col_vals=list(df_real.index), output=preds, use_full_assay_names=True
    )


if __name__ == "__main__":
    # predict_from_smiles(
    #     smiles_list=["CCC"],
    #     checkpoint_dir="/home/filip/Downloads/Moshkov(etal)-single-models/2021-02-cp-es-op"
    # )
    common_path = "/home/filip/Documents/TKA/2023_Moshkov_NatComm/analysis/"
    df_real = pd.read_csv(common_path + "real.csv")
    df_real = df_real.iloc[:10, :]
    df_dmso = pd.read_csv(common_path + "dmso.csv")
    out_df = prepare_df_for_mobc_predictions(
        df_dmso=df_dmso, df_real=df_real, identifier_col="Metadata_pert_id"
    )
    out = predict_from_mobc(
        df_real=out_df,
        checkpoint_dir="/home/filip/Downloads/Moshkov(etal)-single-models/2021-02-mobc-es-op",
    )
    print(out)
