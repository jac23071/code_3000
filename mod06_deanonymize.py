import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    match_dict = {"anon_id":[], "matched_id":[]}
    anon_dict = anon_df.to_dict()
    aux_dict = aux_df.to_dict()
    for i in reac
    potential_matches = []
    pm_scores = []
    for i in range(len(aux_df)):
        potential_matches.append(aux_dict["name"][i])

    
    for pm in potential_matches:
        pm_score = 0;
        
        

    #raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    raise NotImplementedError
