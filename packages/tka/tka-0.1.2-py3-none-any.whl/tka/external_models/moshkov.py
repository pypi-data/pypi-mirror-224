import chemprop
import numpy as np
from tka.utils import transform_moshkov_outputs

smiles = [['CCC'], ['CCCC'], ['OCC']]
arguments = [
    '--test_path', '/dev/null',
    '--preds_path', '/dev/null',
    '--checkpoint_dir', '/home/filip/Documents/TKA/tka/tka/data/Moshkov(etal)-single-models/2021-02-cp-es-op',
    '--no_features_scaling'
]

args = chemprop.args.PredictArgs().parse_args(arguments)
preds = chemprop.train.make_predictions(args=args, smiles=smiles)

out = transform_moshkov_outputs(smiles, preds)
print(out)

# def predict_bioactivty_from_chemical_properties(
#     smiles_list,
#     model_path="",
#     preds_path="",
#     test_path="",
# ):
    
    