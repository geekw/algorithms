from simulation import TicketCounterSimulation

simulation = TicketCounterSimulation(numAgents=3, numMinutes=100, betweenTime=1, serviceTime=3)
simulation.run()
simulation.printResults()

