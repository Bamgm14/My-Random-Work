import gym
import numpy as np
env=gym.make("MountainCar-v0")
env.reset()
done=False
Learn=0.1
Discount=0.95
Epsi=25000
Dis=[20]*len(env.observation_space.low)
Diswin=(env.observation_space.high-env.observation_space.low)/Dis
q_table=np.random.uniform(low=-2,high=0,size=(Dis+[env.action_space.n]))
def DiscreteState(state):
    discrete_state=(state-env.observation_space.low)/Diswin
    return tuple(discrete_state.astype(np.int))
discrete_state=DiscreteState(env.reset())
epsilon=0.5
startepde=1
endepde=Epsi//2
decayvalue=epsilon/(endepde-startepde)
for x in range(Epsi):
    print(x)
    while not done:
        if np.random.random()>epsilon:
            action=np.argmax(q_table[discrete_state])
        else:
            action=np.random.randint(0,env.action_space.n)
        new_state,reward,done,_=env.step(action)
        new_dis_state=DiscreteState(new_state)
        if x%1000==0:
            render=True
            env.render()
        if not done:
            max_fut_q=np.max(q_table[new_dis_state])
            current_q=q_table[discrete_state+(action, )]
            new_q=(1-Learn)*current_q+Learn*(reward+Discount*max_fut_q)
            q_table[discrete_state+(action, )]=new_q
        elif new_state[0]>=env.goal_position:
            print(x)
            q_table[discrete_state+(action, )]=0
        discrete_state=new_dis_state
    if endepde>=x>=startepde:
        epsilon-=decayvalue
env.close()
