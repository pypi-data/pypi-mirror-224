# fixreprod
This is under review.

It is still undergoing improvement.

fixreprod is an indispensable tool to solve reproducibility problems in pseudorandom numbers by fixing all seeds used in libraries of AI systems.

To run fixreprod, install it by the following commanad. ($) indicates the prompt from the system in the terminal.

$ pip install fixreprod

# How to run fixreprod

For example, assume reinforcement_q_learning.py is a source code. Use grep command to generate test.py.
test.py contains imported libraries which will be checked by fixreprod.

$ grep import cartpole_reinforce.py >test.py

Before running fixreprod, you must install all libraries used in the source code.
In reinforcement_q_learning.py, gym, random, numpy, and torch must be installed.

<pre>
Run fixrepdod and enter "test.py" for checking.
fixreprod will show the all seeds to be fixed to eliminate 
reproducibility problems from your code. 
9 seeds and 1 fixing deterministic algorithms are found in this example.
  
$ fixreprod
Enter the source code file name: test.py
env.action_space.seed(0)
env.reset(seed=0)
np.random.seed(0)
random.Random().seed(0)
random.seed(0)
torch.Generator().manual_seed(0)        
torch.cuda.manual_seed(0)
torch.cuda.manual_seed_all(0)
torch.manual_seed(0)
torch.use_deterministic_algorithms(True)

</pre>
