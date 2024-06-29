# BandGap_ML
### Introduction
The band gap is a fundamental property in materials science which plays a significant role in determining the applications of a material in fields such as optoelectronics, quantum computing, etc. The process of determining the band gap of a material through direct means (opticalabsorption spectroscopy, photoluminescence spectroscopy, and photoconductivity measurements) or indirect means involving theoretical calculations (Density Functional Theory) requires significant time and capital investment. 

### Current Results
A simple Feed Forward Neural Network (FFNN) showed promising results in predicting the band gap of crystalline materials. Further experimentation with different models, learning rates and data samples is needed to improve accuracy to a sufficient degree.
<p align="center">
  <img src="Images/SimpleFFNN_Loss_Training1.png" alt="FFNN loss curve", width="700">
</p>
Losses ae reported as average loss per batch, with batch size of 32 data points.

### Data and Citations
Band gap data compiled in /DataFiles/UpdatedMaterialsDF.csv was taken from **MaterialsProject.org** <br>
1. Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek, Shreyas Cholia, Dan Gunter, David Skinner, Gerbrand Ceder, Kristin A. Persson; Commentary: The Materials Project: A materials genome approach to accelerating materials innovation. APL Mater. 1 July 2013; 1 (1): 011002. https://doi.org/10.1063/1.4812323
