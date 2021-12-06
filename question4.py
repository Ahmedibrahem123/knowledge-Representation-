# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:42:25 2021

@author: ibrah
"""

# Import libraries
import aima.utils
import aima.logic
# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and fact)
    clauses.append(aima.utils.expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)"))
    clauses.append(aima.utils.expr("Healthy(John)"))
    clauses.append(aima.utils.expr("Wealthy(jia)"))
    clauses.append(aima.utils.expr("Wealthy(John)"))
    clauses.append(aima.utils.expr("Man(John)"))
    clauses.append(aima.utils.expr("Woman(Jia)"))
    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)
    # Get information from the knowledge base with ask
    travel = KB.ask(aima.utils.expr('Traveler(x)'))
    wealthy = KB.ask(aima.utils.expr('Wealthy(x)'))
    healthy = KB.ask(aima.utils.expr('Healthy(x)'))
    # Print answers
    print('Who can travel?')
    print(travel,'\n')
    print('who are wealthy?')
    print(wealthy,'\n')
    print('who are healthy?')
    print(healthy,'\n')
    print()
# Tell python to run main method
if __name__ == "__main__": main()