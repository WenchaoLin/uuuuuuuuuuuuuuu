#!/usr/bin/env python
# Composition of dimer/trimer/etc oligomers
# 计算fasta序列中dimer,trimer 等oligomer的百分比

from Bio import SeqIO
from collections import Counter
import pandas as pd
import sys

NMER = 2

seq_obj = SeqIO.parse(sys.argv[1],'fasta')
df_list = []

for seq in seq_obj:
    name = seq.id
    sequence = seq.seq
    tmp_list = [str(sequence[i:i + NMER]) for i in range(0, len(sequence) - NMER)]
    ctr = Counter(tmp_list)
    df = pd.DataFrame.from_dict(dict(ctr), columns=[name],orient='index')
    df_list.append(df)

appended_data = pd.concat(df_list, axis=1)
result = df_list/df_list.sum()
result.to_csv(sys.argv[1] + '.csv', sep='\t')
