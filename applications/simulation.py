# Implementation of the main simulation class.
import random
from llistqueue import Queue
from simpeople import TicketAgent, Passenger


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = [None] * numAgents
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print "Number of passengers served = ", numServed
        print("Number of passengers remaining in line = %d" %
              len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    # The remaining methods that have yet to be implemented.
    # Rule 1: If a customer arrives, he is added to the queue. At most, one customer
    # can arrive during each time step.
    # Rule 2: If there are customers waiting, for each free server, the next customer in
    # line begins her transaction.
    # Rule 3: For each server handling a transaction, if the transaction is complete, the
    # customer departs and the server becomes free.

    # Handles simulation rule #1.
    def _handleArrival(self, curTime):
        randomnumber = random.random()
        if randomnumber < self._arriveProb:
            passenger = Passenger(self._numPassengers + 1, curTime)
            self._numPassengers += 1
            self._passengerQ.enqueue(passenger)

    # Handles simulation rule #2.
    def _handleBeginService(self, curTime):
        if not self._passengerQ.isEmpty():
            for agent in self._theAgents:
                if agent.isFree():
                    passenger = self._passengerQ.dequeue()
                    agent.startService(passenger, curTime + self._serviceTime)
                    self._totalWaitTime += curTime - passenger.timeArrived()
                    break

    # Handles simulation rule #3.
    def _handleEndService(self, curTime):
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                agent.stopService()
