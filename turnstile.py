"""
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. 
It appears as if the object changed its class.
"""

import time
from abc import abstractmethod

class TurnstileStates():
    """
    The base State class
    """  
    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def pay(self):
        pass

class ClosedTurnstile(TurnstileStates):

    def __init__(self, g):
        self.gate = g

    def enter(self) :
        print("You must pay $1.00")

    def pay(self) :
        self.gate.transition_to(ProcessPayment(self.gate))
        print("Processing Payment")

class ProcessPayment(TurnstileStates):
    
    def __init__(self,g):
        self.gate=g

    def enter(self) :
        print("Procesing Payment")

    def pay(self) :
        print("Procesing Payment")

class OpenTurnstile(TurnstileStates):

    def __init__(self,g):
        self.gate=g

    def enter(self) :
        print("Client Entered")
        self.gate.transition_to(ClosedTurnstile(self.gate))
        print("Gate Closed")

    def pay(self) :
        print("Already Paid")
    

class Turnstile():
    def __init__(self):
        self.state = ClosedTurnstile(self) 

    def transition_to(self, state):
        self.state = state

    def enter(self):
        self.state.enter()

    def pay(self):
        self.state.pay()
