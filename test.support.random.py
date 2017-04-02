# Imports the agent check Python class
from checks import AgentCheck

# imports the standard random number generator class from Python
import random
# Dlares the agent check class
class randomCheck(AgentCheck):
	#declares a check
    def check(self, instance):
	# creates a metric
	
        self.gauge('test.support.random', random.random())
        print(random.random())
