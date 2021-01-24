# ExperimentDesign


### For producing the results of the CMN paper read through (or the provided pdf: Commands used.pdf):

### GitHub repositories used:

“Collaborative Memory Network for Recommendation Systems” (SIGIR 18): https://github.com/tebesu/CollaborativeMemoryNetwork  

“Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches” (RecSys 19):
https://github.com/MaurizioFD/RecSys2019_DeepLearning_Evaluation 

Python packages versions:
Used the requirement.txt file from the second GitHub repository

### Commands executed: 

Pre-train the data:
Citeulike dataset: 
python pretrain.py --gpu 0 --dataset data/citeulike-a.npz --output pretrain/citeulike-a_eX.npz –e -X \
For X in [20,40,50,60,80,100]

Epinions dataset:
python pretrain.py --gpu 0 --dataset data/epinions.npz --output pretrain/epinions_e50.npz 


Variation of number of hops:
python train.py --gpu 0 --dataset data/citeulike-a.npz --pretrain pretrain/citeulike-a_e50.npz -–hops H \
For H in [1,2,3]

Comparison to ItemKNN: 
python run_SIGIR_18_CMN.py –b True –a True –p True

Variation of embedding sizes:
python train.py --gpu 0 --dataset data/citeulike-a.npz --pretrain pretrain/citeulike-a_eX.npz -–hops H –e X \
For H in [1,2,3] and X in [20,40,50,60,80,100]


Variation of number of negative samples:
python train.py --gpu 0 --dataset data/citeulike-a.npz --pretrain pretrain/citeulike-a_e50.npz -–hops H --neg N \
For H in [1,2,3] and N in [2,3,4,5,6,7,8,9,10]
