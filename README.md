# Sec11A-Peptide Structural Analysis Pipeline

Author: Dr. Ioannis Skalidis
This repository contains the analysis workflow used in the manuscript **"Structural basis of signal peptide recognition by the signal peptidase complex, by Liaci, Vismpas et al., 2026"**. The pipeline processes AlphaFold2-Multimer models to identify, filter, and validate peptide-enzyme docking orientations against experimental references.

## 1. Overview
The workflow is split into three main stages:
1. **Filtering & Annotation (Python):** Filters raw PDB models based on pLDDT, membrane insertion topology, and proximity to the S1 hydrophobic pocket.
2. **Structural Alignment (ChimeraX):** Aligns accepted models to an experimental reference and calculates positional $C\alpha$ deviations.
3. **Data Visualization (Python):** Generates publication-quality plots correlating prediction confidence (pLDDT) with spatial deviation (Å).

## 2. Installation
Ensure you have Python 3.11+ installed. Clone this repository and install dependencies:
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
pip install -r requirements.txt
```
## 3. Usage
### Step 1: Pre-processing & Filtering

Run the main analysis script to filter your AF2-multimer models. Place your PDB files in ./topranked_af2m_sp_models. Scripts are included as jupyter notebooks.

```bash
pLDDT_filtering.ipynb
```
This generates sp_modeling_final_analysis.csv and several diagnostic plots.

### Step 2: Alignment & Deviation

Open ChimeraX and run the alignment script in the ChimeraX command line GUI:

```bash
open sp_residue_rmsd.py # requires a reference PDB experimental model, a folder with all the filtered models from the previous step, and outputs distances.csv.
```
### Step 3: Final Plotting

Generate the positional variation plots:

```bash
positional_variation_plotting.ipynb # requires distances.csv from previous step
```
## 4. Citation
If you use this code or the associated data, please cite:

Liaci, Vismpas et al., "Structural basis of signal peptide recognition by the signal peptidase complex." Nature Communications, 2026. DOI: TBD

## 5. License
This project is licensed under the MIT License - see the LICENSE file for details.
