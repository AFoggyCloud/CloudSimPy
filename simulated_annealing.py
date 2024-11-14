from core.algorithm import Algorithm


class SimulatedAnnealing(Algorithm):
    def __init__(self, temp=1e10, alpha=0.95, epsilon=0.95):
        self.temp = temp
        self.alpha = alpha
        self.epsilon = epsilon

    def __call__(self, cluster):
        # initial setup from environment variables
        machines = cluster.machines
        tasks = cluster.tasks_which_has_waiting_instance
        candidate_task = None
        candidate_machine = None

        # algorithm


        return candidate_machine, candidate_task
