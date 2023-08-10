import pandas as pd

def transform_l1000_ids(from_id, to_id, gene_ids, dataset_path="tka/data/l1000_mapped.csv", ignore_missing=False):
    """
    Transforms L1000 gene IDs from one format to another.

    Args:
        from_id (str): The source probe type ("affyID", "entrezID", "ensemblID").
        to_id (str): The target probe type ("affyID", "entrezID", "ensemblID").
        gene_ids (list): List of L1000 gene IDs to transform.
        dataset_path (str): Path to the DataFrame containing L1000 gene IDs for each probe type.
        ignore_missing (bool): If set to True, it will not raise an error on missing or invalid probe IDs.

    Returns:
        dict: Original and transformed L1000 gene IDs as keys and values respectively.

    Raises:
        ValueError: If either from_id or to_id is not one of the allowed values.
        ValueError: If any of the gene IDs in the dataset is not within the scope of L1000.

    """
    # Initialize dataset pd.DataFrame
    l1000 = pd.read_csv(dataset_path)

    # Define the allowed probe types
    allowed_probes = ["affyID", "entrezID", "ensemblID"]

    # Check if the probe types are valid
    if from_id not in allowed_probes or to_id not in allowed_probes:
        raise ValueError("Invalid probe type. Allowed values: 'affyID', 'entrezID', 'ensemblID'.")
    
    # Initialize the output dict
    transformed_ids = {}

    # Perform the transformation
    for gene_id in gene_ids:

        # Safety check for missing IDs
        if gene_id not in l1000[from_id].values:
            if ignore_missing:
                continue
            raise ValueError(f"Gene ID '{gene_id}' is not within the scope of L1000 {from_id} values.")

        # Find the mapping from L1000 and save it to transformed_ids
        transformed_ids[gene_id] = l1000[l1000[from_id] == gene_id][to_id].values[0]

    return transformed_ids

def transform_moshkov_outputs(smiles_list, output):
    # Load the PUMA_ASSAY_ID values from the CSV file
    assay_metadata = pd.read_csv('/home/filip/Documents/TKA/tka/tka/data/assay_metadata.csv')
    puma_assay_ids = assay_metadata['PUMA_ASSAY_ID'].tolist()

    # Create a dictionary to store the data for DataFrame creation
    data_dict = {'smiles': smiles_list}

    # Loop through each PUMA_ASSAY_ID and add its values to the dictionary
    for idx, puma_assay_id in enumerate(puma_assay_ids):
        column_values = [row[idx] for row in output]
        data_dict[puma_assay_id] = column_values

    # Create a Pandas DataFrame from the data dictionary
    df = pd.DataFrame(data_dict)

    return df

if __name__ == "__main__":
    transform_l1000_ids(
        from_id="affyID",
        to_id="ensemblID",
        gene_ids=["201225_s_at", "204418_x_at"]
    )