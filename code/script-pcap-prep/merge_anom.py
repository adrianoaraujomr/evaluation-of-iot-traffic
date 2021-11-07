#!/usr/bin/python3

import pandas as pd
import os
from datetime import datetime

col_dict = {
'Src Port': [ 'Src Port', ' Source Port' ],
'Dst Port': [ 'Dst Port', ' Destination Port' ],
'Protocol': [ 'Protocol', ' Protocol' ],
'Flow Duration': [ 'Flow Duration', ' Flow Duration' ],
'Total Fwd Packet': [ 'Tot Fwd Pkts', ' Total Fwd Packets' ],
'Total Bwd packets': [ 'Tot Bwd Pkts', ' Total Backward Packets' ],
'Total Length of Fwd Packet': [ 'TotLen Fwd Pkts', 'Total Length of Fwd Packets' ],
'Total Length of Bwd Packet': [ 'TotLen Bwd Pkts', ' Total Length of Bwd Packets' ],
'Fwd Packet Length Max': [ 'Fwd Pkt Len Max', ' Fwd Packet Length Max' ],
'Fwd Packet Length Min': [ 'Fwd Pkt Len Min', ' Fwd Packet Length Min' ],
'Fwd Packet Length Mean': [ 'Fwd Pkt Len Mean', ' Fwd Packet Length Mean' ],
'Fwd Packet Length Std': [ 'Fwd Pkt Len Std', ' Fwd Packet Length Std' ],
'Bwd Packet Length Max': [ 'Bwd Pkt Len Max', 'Bwd Packet Length Max' ],
'Bwd Packet Length Min': [ 'Bwd Pkt Len Min', ' Bwd Packet Length Min' ],
'Bwd Packet Length Mean': [ 'Bwd Pkt Len Mean', ' Bwd Packet Length Mean' ],
'Bwd Packet Length Std': [ 'Bwd Pkt Len Std', ' Bwd Packet Length Std' ],
'Flow Bytes/s': [ 'Flow Byts/s', 'Flow Bytes/s' ],
'Flow Packets/s': [ 'Flow Pkts/s', ' Flow Packets/s' ],
'Flow IAT Mean': [ 'Flow IAT Mean', ' Flow IAT Mean' ],
'Flow IAT Std': [ 'Flow IAT Std', ' Flow IAT Std' ],
'Flow IAT Max': [ 'Flow IAT Max', ' Flow IAT Max' ],
'Flow IAT Min': [ 'Flow IAT Min', ' Flow IAT Min' ],
'Fwd IAT Total': [ 'Fwd IAT Tot', 'Fwd IAT Total' ],
'Fwd IAT Mean': [ 'Fwd IAT Mean', ' Fwd IAT Mean' ],
'Fwd IAT Std': [ 'Fwd IAT Std', ' Fwd IAT Std' ],
'Fwd IAT Max': [ 'Fwd IAT Max', ' Fwd IAT Max' ],
'Fwd IAT Min': [ 'Fwd IAT Min', ' Fwd IAT Min' ],
'Bwd IAT Total': [ 'Bwd IAT Tot', 'Bwd IAT Total' ],
'Bwd IAT Mean': [ 'Bwd IAT Mean', ' Bwd IAT Mean' ],
'Bwd IAT Std': [ 'Bwd IAT Std', ' Bwd IAT Std' ],
'Bwd IAT Max': [ 'Bwd IAT Max', ' Bwd IAT Max' ],
'Bwd IAT Min': [ 'Bwd IAT Min', ' Bwd IAT Min' ],
'Fwd PSH Flags': [ 'Fwd PSH Flags', 'Fwd PSH Flags' ],
'Bwd PSH Flags': [ 'Bwd PSH Flags', ' Bwd PSH Flags' ],
'Bwd URG Flags': [ 'Bwd URG Flags', ' Bwd URG Flags' ],
'Fwd Header Length': [ 'Fwd Header Len', ' Fwd Header Length' ],
'Bwd Header Length': [ 'Bwd Header Len', ' Bwd Header Length' ],
'Fwd Packets/s': [ 'Fwd Pkts/s', 'Fwd Packets/s' ],
'Bwd Packets/s': [ 'Bwd Pkts/s', ' Bwd Packets/s' ],
'Packet Length Min': [ 'Pkt Len Min', ' Min Packet Length' ],
'Packet Length Max': [ 'Pkt Len Max', ' Max Packet Length' ],
'Packet Length Mean': [ 'Pkt Len Mean', ' Packet Length Mean' ],
'Packet Length Std': [ 'Pkt Len Std', ' Packet Length Std' ],
'Packet Length Variance': [ 'Pkt Len Var', ' Packet Length Variance' ],
'FIN Flag Count': [ 'FIN Flag Cnt', 'FIN Flag Count' ],
'SYN Flag Count': [ 'SYN Flag Cnt', ' SYN Flag Count' ],
'RST Flag Count': [ 'RST Flag Cnt', ' RST Flag Count' ],
'PSH Flag Count': [ 'PSH Flag Cnt', ' PSH Flag Count' ],
'ACK Flag Count': [ 'ACK Flag Cnt', ' ACK Flag Count' ],
'Down/Up Ratio': [ 'Down/Up Ratio', ' Down/Up Ratio' ],
'Average Packet Size': [ 'Pkt Size Avg', ' Average Packet Size' ],
'Fwd Segment Size Avg': [ 'Fwd Seg Size Avg', ' Avg Fwd Segment Size' ],
'Bwd Segment Size Avg': [ 'Bwd Seg Size Avg', ' Avg Bwd Segment Size' ],
'Subflow Fwd Packets': [ 'Subflow Fwd Pkts', 'Subflow Fwd Packets' ],
'Subflow Fwd Bytes': [ 'Subflow Fwd Byts',  ' Subflow Fwd Bytes' ],
'Subflow Bwd Packets': [ 'Subflow Bwd Pkts', ' Subflow Bwd Packets' ],
'Subflow Bwd Bytes': [ 'Subflow Bwd Byts', ' Subflow Bwd Bytes' ],
'FWD Init Win Bytes': [ 'Init Fwd Win Byts', 'Init_Win_bytes_forward' ],
'Bwd Init Win Bytes': [ 'Init Bwd Win Byts', ' Init_Win_bytes_backward' ],
'Fwd Act Data Pkts': [ 'Fwd Act Data Pkts', ' act_data_pkt_fwd' ],
'Fwd Seg Size Min': [ 'Fwd Seg Size Min', ' min_seg_size_forward' ],
'Active Mean': [ 'Active Mean', 'Active Mean' ],
'Active Std': [ 'Active Std', ' Active Std' ],
'Active Max': [ 'Active Max', ' Active Max' ],
'Active Min': [ 'Active Min', ' Active Min' ],
'Idle Mean': [ 'Idle Mean', 'Idle Mean' ],
'Idle Std': [ 'Idle Std', ' Idle Std' ],
'Idle Max': [ 'Idle Max', ' Idle Max' ],
'Idle Min': [ 'Idle Min', ' Idle Min' ],
'Device Class': [ 'Label', ' Label']
}
    
diretorio = './datasets/anomalias'
new_file = diretorio + "/dataset.csv"

mob = pd.read_csv(diretorio + "/mobile" + "/mobile_malware_2_filtered.csv")
tor = pd.read_csv(diretorio + "/normal" + "/normal_malware_2_filtered.csv")
iot = pd.read_csv(diretorio + "/iot"    + "/iot_malware_no_filter.csv", index_col=0)

mob.dropna(inplace=True)
tor.dropna(inplace=True)
iot.dropna(inplace=True)

mob = mob.iloc[:, :84]
mob["Device Class"] = "Mobile Anomaly"
tor = tor.iloc[:, :84]
tor["Device Class"] = "Non Tor Anomaly"
iot = iot.iloc[:, :83]
iot["Device Class"] = "Iot Anomaly"

mob_cols = mob.columns.values.tolist()
tor_cols = tor.columns.values.tolist()
iot_cols = iot.columns.values.tolist()

mob_dict = {}
tor_dict = {}
iot_dict = {}

Renomear colunas
for real_col in col_dict.keys():
    values = col_dict[real_col]
    for aux in values:
        if aux in mob_cols and aux != real_col:
            mob_dict[aux] = real_col
        if aux in tor_cols and aux != real_col:
            tor_dict[aux] = real_col
        if aux in iot_cols and aux != real_col:
            iot_dict[aux] = real_col

mob.rename(columns=mob_dict, inplace=True)
tor.rename(columns=tor_dict, inplace=True)
iot.rename(columns=iot_dict, inplace=True)

Remover colunas
mob_cols = mob.columns.values.tolist()
tor_cols = tor.columns.values.tolist()
iot_cols = iot.columns.values.tolist()

to_drop = [col for col in mob_cols if col not in list(col_dict.keys())]
mob.drop(to_drop, axis=1, inplace=True)
to_drop = [col for col in tor_cols if col not in list(col_dict.keys())]
tor.drop(to_drop, axis=1, inplace=True)
to_drop = [col for col in iot_cols if col not in list(col_dict.keys())]
iot.drop(to_drop, axis=1, inplace=True)

mob.to_csv(diretorio + "/mobile" + "/mobile_malware_cols_changed.csv", index=False)
tor.to_csv(diretorio + "/normal" + "/normal_malware_cols_changed.csv", index=False)
iot.to_csv(diretorio + "/iot"    + "/iot_malware_cols_changed.csv", index=False)

mob = pd.read_csv(diretorio + "/mobile" + "/mobile_malware_cols_changed.csv")
tor = pd.read_csv(diretorio + "/normal" + "/normal_malware_cols_changed.csv")
iot = pd.read_csv(diretorio + "/iot"    + "/iot_malware_cols_changed.csv")

mob = mob.reindex(sorted(mob.columns), axis=1)
tor = tor.reindex(sorted(tor.columns), axis=1)
iot = iot.reindex(sorted(iot.columns), axis=1)

aux1 = mob.columns.values.tolist()
aux2 = tor.columns.values.tolist()
aux3 = iot.columns.values.tolist()

result_df = pd.DataFrame(columns=mob.columns)

result_df = pd.concat([result_df, mob], ignore_index=True)
result_df = pd.concat([result_df, tor], ignore_index=True)
result_df = pd.concat([result_df, iot], ignore_index=True)

result_df.to_csv(new_file, index=False)

chunksize = 80000
do_part1 = True
do_part2 = True
do_part3 = True
part1 = None
part2 = None
part3 = None
aux = None

for chunk in pd.read_csv(new_file, chunksize=chunksize):
    if do_part1:
        part1 = chunk[chunk["Device Class"] == "Iot Anomaly"].head(500)
        if part1.shape[0] != 0:
            do_part1 = False
    if do_part2:
        part2 = chunk[chunk["Device Class"] == "Non Tor Anomaly"].head(500)
        if part2.shape[0] != 0:
            do_part2 = False
    if do_part3:
        part3 = chunk[chunk["Device Class"] == "Mobile Anomaly"].head(500)
        if part3.shape[0] != 0:
            do_part3 = False
    if not do_part1 and not do_part2 and not do_part3:
        break

result_df = pd.DataFrame(columns=part1.columns)

result_df = pd.concat([result_df, part1], axis=0, join='outer', ignore_index=True, sort=False)
result_df = pd.concat([result_df, part2], axis=0, join='outer', ignore_index=True, sort=False)
result_df = pd.concat([result_df, part3], axis=0, join='outer', ignore_index=True, sort=False)

result_df.to_csv(new_file.replace(".csv", "resumo.csv"), index=False)