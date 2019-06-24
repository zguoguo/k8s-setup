#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys

def read():
    file = sys.stdin
#     for i in files:
#         df = pd.read_csv(i)
#         dfs.append(df)
    df = pd.read_csv(file)
    l = list(set(df['node'].values))
    return df, l

def calc_contention(df, l):
    contention = []
    for i,j in enumerate (l):
        df_new = df[df['node']==j]
        #\sum_(Time_Length_of_Overlapping) * (Number_of_Jobs - 1)
        contention.append(sum(df_new['complete_time']) - (max(df_new['end_time'].values) - min(df_new['start_time'].values)))

    return contention

def main():
    # Location of the file which Yuqi generated
#     path = 'data/10vae.csv'
    df,l = read()
    contention = calc_contention(df, l)
    print("nodes: ", l)
    for i in l:
        df_new = df[df['node']==i]
        print(f'complete time of {i}:', df_new['complete_time'].values)
    print("contention: ", contention)

main()
