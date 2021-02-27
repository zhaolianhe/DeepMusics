from DataLoader import load_data, load_pathway
from Train import trainDeepMusicsNet

import torch
import numpy as np

torch.cuda.set_device(1)
dtype = torch.FloatTensor
''' Net Settings'''
In_Nodes = 5000 ##gene nodes in need of change for users
functional_Nodes = 800 ##functinal modules nodes in need of change for user
Hidden_Nodes = 100 
Out_Nodes = 30 
''' Initialize '''
Initial_Learning_Rate = [0.03, 0.01, 0.001, 0.00075]
L2_Lambda = [0.1, 0.01, 0.005, 0.001]
num_epochs = 3000 
Num_EPOCHS = 20000 

Dropout_Rate = [0.7, 0.5]
''' load data and pathway '''
pathway_mask = load_pathway("~/functional_mask.csv", dtype)

x_train, ytime_train, yevent_train, age_train = load_data("~/train.csv", dtype)
x_valid, ytime_valid, yevent_valid, age_valid = load_data("~/test.csv", dtype)
x_test, ytime_test, yevent_test, age_test = load_data("~/validation.csv", dtype)

opt_l2_loss = 0
opt_lr_loss = 0
opt_loss = torch.Tensor([float("Inf")])

if torch.cuda.is_available():
	opt_loss = opt_loss.cuda()
opt_c_index_va = 0
opt_c_index_tr = 0
for l2 in L2_Lambda:
	for lr in Initial_Learning_Rate:
		loss_train, loss_valid, c_index_tr, c_index_va = trainDeepMusicsNet(x_train, age_train, ytime_train, yevent_train, \
																x_valid, age_valid, ytime_valid, yevent_valid, pathway_mask, \
																In_Nodes, Pathway_Nodes, Hidden_Nodes, Out_Nodes, \
																lr, l2, num_epochs, Dropout_Rate)
		if loss_valid < opt_loss:
			opt_l2_loss = l2
			opt_lr_loss = lr
			opt_loss = loss_valid
			opt_c_index_tr = c_index_tr
			opt_c_index_va = c_index_va
		print ("L2: ", l2, "LR: ", lr, "Loss in Validation: ", loss_valid)

loss_train, loss_test, c_index_tr, c_index_te = trainDeepMusicsNet(x_train, age_train, ytime_train, yevent_train, \
							x_test, age_test, ytime_test, yevent_test, pathway_mask, \
							In_Nodes, Pathway_Nodes, Hidden_Nodes, Out_Nodes, \
							opt_lr_loss, opt_l2_loss, Num_EPOCHS, Dropout_Rate)
print ("Optimal L2: ", opt_l2_loss, "Optimal LR: ", opt_lr_loss)
print("C-index in Test: ", c_index_te)
