# **TNFepitope**
A tool for prediction and scanning of TNF-inducing epitopes/peptides using the sequence information.
## Introduction
TNF-α is a multifunctional pro-inflammatory cytokine released by T cells or macrophages and control a number of signalling pathways within the immune cells; leads to necrosis or cell death.In the past several studies show that high levels of TNF-α is associated with number of diseases such as autoimmunity, rheumatoid arthritis, diabetes, inflammatory bowel disease, etc. 
TNFepitope is also available as web-server at https://webs.iiitd.edu.in/raghava/tnfepitope. Please read/cite the content about the TNFepitope for complete information including algorithm behind the approach.

## Reference
 Dhall et al. (2023) TNFepitope: A webserver for the prediction of TNF-α inducing epitopes. <a href="https://doi.org/10.1016/j.compbiomed.2023.106929">Comput Biol Med. doi.org/10.1016/j.compbiomed.2023.106929</a>
## Standalone
The Standalone version of transfacpred is written in python3 and following libraries are necessary for the successful run:
- scikit-learn
- Pandas
- Numpy
- blastp

## Minimum USAGE
To know about the available option for the stanadlone, type the following command:
```
 tnfepitope -h
```
To run the example, type the following command:
```
tnfepitope -i example_input.fa
```
This will predict if the submitted sequences are TNF-inducer or TNF non-inducer. It will use other parameters by default. It will save the output in "outfile.csv" in CSV (comma seperated variables).

## Full Usage
```
usage: tnfepitope [-h] 
                       [-i INPUT 
                       [-o OUTPUT]
                       [-s {1,2}]
		       [-j {1,2,3}]
		       [-t THRESHOLD]
                       [-w {9,10,11,12,13,14,15,16,17,18,19,20}]
		       [-d {1,2}]
```
```
Please provide following arguments for successful run

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input: protein or peptide sequence(s) in FASTA format
                        or single sequence per line in single letter code
  -o OUTPUT, --output OUTPUT
                        Output: File for saving results by default outfile.csv
  -s {1,2}, --Source {1,2}
                        Source Type: 1:Human, 2:Mouse, by default 1
  -j {1,2,3}, --job {1,2,3}
                        Job Type: 1:Predict, 2: Design, 3:Scan, by default 1
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold: Value between 0 to 1 by default 0.45 for human and 0.5 for mouse
  -w {9,10,11,12,13,14,15,16,17,18,19,20}, --winleng {9,10,11,12,13,14,15,16,17,18,19,20}
                        Window Length: 9 to 20 (scan mode only), by default 9
  -d {1,2}, --display {1,2}
                        Display: 1:TNF-inducer only, 2: All peptides, by default 1
```

**Input File:** It allow users to provide input in the FASTA format.

**Output File:** Program will save the results in the CSV format, in case user do not provide output file name, it will be stored in "outfile.csv".

**Threshold:** User should provide source 1 and 2, by default its 1 for human and 2 for mouse.

**Threshold:** User should provide threshold between 0 and 1, by default its 0.45 for human and 0.5 for mouse.

**Job:** User is allowed to choose between three different modules, such as, 1 for prediction, 2 for Designing and 3 for scanning, by default its 1.

**Window length**: User can choose any pattern length between 9 and 20 in long sequences. This option is available for only scanning module.

**Display type:** This option allow users to fetch either only TNF-inducing peptides by choosing option 1 or prediction against all peptides by choosing option 2.

TNFepitope Package Files
=======================
It contantain following files, brief descript of these files given below

INSTALLATION                    : Installations instructions

LICENSE                         : License information

README.md                       : This file provide information about this package

model.zip                       : This zipped file contains the compressed version of model

envfile                         : This file compeises of paths for the database and blastp executable

tnfepitope.py                  : Main python program

example_input.fa                : Example file contain peptide sequenaces in FASTA format

example_predict_output.csv      : Example output file for predict module

example_scan_output.csv         : Example output file for scan module

example_design_output.csv       : Example output file for design module
