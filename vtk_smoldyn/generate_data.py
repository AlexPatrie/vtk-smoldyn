from smoldyn import Simulation


def generate_molecules(model_fp: str, duration: int):
    simulation = Simulation.fromFile(model_fp)
    simulation.addOutputData('molecules')
    simulation.addCommand(cmd='listmols2 molecules', cmd_type='E')
    simulation.run(duration, simulation.dt)
    return simulation.getOutputData('molecules')
