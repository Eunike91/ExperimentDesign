import matplotlib.pyplot as plt

x = [20,40,60,80,100]

ndcg_1 = [0.424,0.454,0.536,0.4463,0.4305]
hr_1 = [0.626,0.643,0.784,0.6604,0.6493]

ndcg_2 = [0.6068693733553174, 0.6570301763109194, 0.6668575479566532, 0.6676215549837085,0.6788677319195672]
hr_2 = [0.8589443343541704, 0.8929922536479914, 0.8920915150423347, 0.8899297423887588,0.8929922536479914]

ndcg_3 = [0,0,0,0,0]
hr_3 = [0,0,0,0,0]

ndcg_4 = [0,0,0,0,0]
hr_4 = [0,0,0,0,0]

fig, ax = plt.subplots(ncols=2, figsize=(15,5))
ax[0].plot(x, hr_1, marker='D',color='tab:blue',label='1 Hop')
ax[0].plot(x, hr_2, marker='o',color='tab:green',label='2 Hops')
#ax[0].plot(x, hr_3, marker='*',color='tab:red',label='3 Hops')
#ax[0].plot(x, hr_4, marker='>',color='tab:purple',label='4 Hops')

ax[1].plot(x, ndcg_1, marker='D',color='tab:blue',label='1 Hop')
ax[1].plot(x, ndcg_2, marker='o',color='tab:green',label='2 Hops')
#ax[1].plot(x, ndcg_3, marker='*',color='tab:red',label='3 Hops')
#ax[1].plot(x, ndcg_4, marker='>',color='tab:purple',label='4 Hops')

ax[0].set_xlabel('Embedding Size')
ax[0].set_ylabel('HR@10')

ax[1].set_xlabel('Embedding Size')
ax[1].set_ylabel('NDCG@10')

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, loc = 'lower center', ncol = 4)

plt.savefig("Varying_sizes.png")
plt.show()

