#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
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
def timelines(y, xstart, xstop, color, label):
    """Plot timelines at y from xstart to xstop with given color."""
    plt.hlines(y, xstart, xstop, color, lw=4, label =label)
#     plt.vlines(xstart, y+0.03, y-0.03, color, lw=2)
#     plt.vlines(xstop, y+0.03, y-0.03, color, lw=2)
def all_in_one(df, l):
    fig = plt.figure()
    color=cm.rainbow(np.linspace(0,1,len(l)))
    #Plot ok tl black
    for i, j in enumerate(l):
        df_new = df[df['node']==j]
        timelines(df_new['job'], df_new['start_time'], df_new['end_time'], color[i], j)
        plt.legend()
    fig.savefig('all_in_one.pdf')

def per_worker(df, l):
    #Plot ok tl black
    for i, j in enumerate(l):
        fig = plt.figure()
        df_new = df[df['node']==j]
        timelines(df_new['job'], df_new['start_time'], df_new['end_time'], 'b', j)
        fig.savefig(f'{j}.pdf')

def main():
    # Location of the file which Yuqi generated
#     path = 'data/10vae.csv'
    df,l = read()
    all_in_one(df, l)
    per_worker(df, l)
main()
