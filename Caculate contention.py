#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys

def read():
    file = sys.stdin.read()
#     for i in files:
#         df = pd.read_csv(i)
#         dfs.append(df)
    df = pd.read_csv(file)
    l = list(set(df['node'].values))
    return df, l
################################ Generate pics #####################################
def timelines(y, xstart, xstop, color, label):
    """Plot timelines at y from xstart to xstop with given color."""
    plt.hlines(y, xstart, xstop, color, lw=4, label =label)
#     plt.vlines(xstart, y+0.03, y-0.03, color, lw=2)
#     plt.vlines(xstop, y+0.03, y-0.03, color, lw=2)
def gen_pics(df, l):
    clr = ['r', 'b']
    #Plot ok tl black
    for i,j in enumerate (l):
        df_new = df[df['node']==j]
        timelines(df_new['job'], df_new['start_time'], df_new['end_time'], clr[i], j)
        plt.legend()
####################################################################################

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
    # gen_pics(df, l)
    contention = calc_contention(df, l)
    print("nodes: ", l)
    for i in l:
        df_new = df[df['node']==i]
        print(f'complete time of {i}:', df_new['complete_time'].values)
    print("contention: ", contention)

main()
