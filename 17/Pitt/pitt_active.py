import pandas as pd
pitt = pd.read_table("pitt_voter.txt", encoding = "ISO-8859-1")

active_series   = pitt["voter_status_desc"]=="ACTIVE"
verified_series = pitt["voter_status_reason_desc"]=="VERIFIED"

active_pitt = pitt[active_series] 
active_pitt.to_csv("active_pitt.csv")

active_verified = pitt[active_series & verified_series]
active_verified.to_csv("active_verified_pitt.csv")
