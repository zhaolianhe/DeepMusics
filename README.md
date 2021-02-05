# DeepMultiOmics
  
  For any cancer type or subtype, it is difficult to see the whole landscape of molecular features with high dimensions and multiple sequencing data sources. 
The Multi-Omics including mutations,expressions,methylations,clinical information and cancer pathway prior knowledge information.
Our goal is to use deep learning method to fit embedding from all kinds of omics to analysis pan cancers in a general way.
Here we use several common cancer types to show how the framework was built and tested.

  Deep learning methods have been applied in bioinformatics because of their strong ability for capturing of nonlinear relationships, from their fitted trails and a flexible model design. 

## Install
To use DeepMultiOmics, do the following:

1.Install the environment

2.Prepare data

3.Train and evaluate DeepMultiOmics

## Data

Pathway prior knowledge information is from the Molecular Signatures Database(MSigDB).

Mutations,expressions,methlations,clinical information of all cancer types are from TCGA Database(https://portal.gdc.cancer.gov/).

## Model
 
The multi-omics data are preprocessed into three sets of matrixes.
1.mutation matrix 
2.expression matrix
3.methylations matrix 

The shapes for them are genes * samples, which are inputs of the model.
