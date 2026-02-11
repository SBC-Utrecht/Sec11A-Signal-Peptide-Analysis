import os
import numpy as np
import csv
from chimerax.core.commands import run

# Configuration
ref_path = "./sec11a_l11_exp.pdb"
models_dir = "./accepted_sp_models"
chain_align = "A"
chain_peptide = "B"
output_csv = "distances.csv"

def get_ca_data(model, chain_id):
    chain = next((c for c in model.chains if c.chain_id == chain_id), None)
    if not chain: return []
    return [a for res in chain.residues for a in [next((atom for atom in res.atoms if atom.name == 'CA'), None)] if a]

# 1. Load Reference
ref_model = run(session, f"open {ref_path}")[0]
ref_ca_b = get_ca_data(ref_model, chain_peptide)
ref_coords = [atom.scene_coord for atom in ref_ca_b]

data_rows = []

# 2. Process Predictions
pdbs = [f for f in os.listdir(models_dir) if f.endswith(".pdb")]
for pdb in pdbs:
    m_path = os.path.join(models_dir, pdb)
    test_model = run(session, f"open {m_path}")[0]
    
    # Align based on the Enzyme (Chain A)
    run(session, f"mmaker #{test_model.id_string}/{chain_align} to #{ref_model.id_string}/{chain_align}")
    
    # Get Chain B (Peptide) CA atoms and reverse for C-term indexing
    test_ca_b_rev = get_ca_data(test_model, chain_peptide)[::-1]
    
    for i in range(min(len(test_ca_b_rev), 22)):
        t_atom = test_ca_b_rev[i]
        t_coord = t_atom.scene_coord
        # Find distance to closest CA in reference
        min_dist = min([np.linalg.norm(t_coord - r_coord) for r_coord in ref_coords])
        
        # Save Model name and the "P" position (1-indexed)
        data_rows.append([pdb, i + 1, min_dist])
    
    run(session, f"close #{test_model.id_string}")

# 3. Export to CSV
with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Model", "Position", "Distance"])
    writer.writerows(data_rows)

print(f"Distance data exported to {output_csv}")