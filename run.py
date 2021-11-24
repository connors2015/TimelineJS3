'''
run.py
4ier Data Analytics
Nov/23/2021

Author: Chris Connors
'''
import env
import agent
import sys
import inputs
import trade
import logging
import time

def main():

    filename = './logging/env/run_file_{}.log'.format(time.strftime("%Y%m%d-%H%M%S"))
    logging.basicConfig(filename=filename, level=logging.DEBUG)
    log = logging.getLogger('run')
    log.info('Run-Time environment starting...')

    
    '''
    Start new environment at step 0
    '''
    run_environment = env.Env(sys.argv[3])
    run_environment.create_new_environment()



    '''
    User input for number of agents to be created
    We then create a list of new agents with varying genetics
    '''
    numberOfAgents = int(sys.argv[1])
    agentSplitTime = int(sys.argv[2])

    try:
        log.info('Creating %s agents.', numberOfAgents)
        agent_list = [agent.Agent(agentSplitTime, run_environment) for _ in range(numberOfAgents)]
    except Exception:
        return log.exception('Can not create agents in run.py')

    
    '''
    Loop through agents by using update()
    They will step forward, update their inputs, then call their neural networks

    The agent will then perform any trades necessary or wait
    '''
    log.info('Stepping through environment.')

    run_environment.display()
    [run_environment.step() for _ in range(50)]

    agent_list[0].update_inputs()

    [run_environment.step() for _ in range(50)]
    agent_list[0].update_inputs()

    run_environment.display()



    



if __name__ == '__main__':
    main()