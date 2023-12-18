from smoldyn import Simulation


def generate_molecules(model_fp: str, duration: int):
    simulation = Simulation.fromFile(model_fp)
    simulation.addOutputData('molecules')
    simulation.addCommand(cmd='listmols molecules', cmd_type='E')
    simulation.run(duration, simulation.dt)
    return simulation.getOutputData('molecules')


def generate_molecule_coordinates(model_fp: str, duration: int):
    data = generate_molecules(model_fp, duration)
    mol_coords = []
    for mol in data:
        mol_coords.append(mol[2:5])
    return mol_coords
