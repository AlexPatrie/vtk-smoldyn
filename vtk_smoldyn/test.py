from vtk_smoldyn.generate_data import generate_molecule_coordinates, generate_molecules


model_fp = 'vtk_smoldyn/models/minE_Andrews_052023/model.txt'
#mol_data = generate_molecule_coordinates(model_fp, 2)

molecules = generate_molecules(model_fp, 2)

print(molecules[:5])
