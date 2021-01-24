import numpy as np
import pandas as pd
import random as rd

epinions_txt = pd.read_csv('data/ratings_data.txt',sep=" ",header=None)
epinions_txt.rename(columns={0: "user", 1: "item", 2: "rating"},inplace = True)

epinions_users = list(epinions_txt["user"].unique())
epinions_items = list(epinions_txt["item"].unique())

epinions_test = {}
single_items = []

for u in epinions_users:
    epi_u = epinions_txt.loc[epinions_txt['user']==u]
    pos_id = epi_u.sample()['item'].values[0]
    remaning_items = [id for id in epinions_items if id not in list(epi_u['item'])]
    neg_ids = rd.sample(remaning_items,100)
    epinions_test[u] = (pos_id,neg_ids)
    if epi_u.shape[0] == 1:
        single_items.append(u)


#epinions_train = np.array(epinions_txt[["user","item"]], dtype='uint32')
epinions_train = epinions_txt[["user","item"]].values.tolist()
for u in epinions_users:
    if u not in single_items:
        epinions_train.remove([u,epinions_test[u][0]])


np.savez('data/epinions.npz', train_data=epinions_train, test_data=epinions_test)

