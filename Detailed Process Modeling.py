# process_simulation.py
import aspenplus

def run_simulation(parameters):
    simulation = aspenplus.Simulation()
    simulation.load_model('model_file')
    simulation.set_parameters(parameters)
    results = simulation.run()
    return results
