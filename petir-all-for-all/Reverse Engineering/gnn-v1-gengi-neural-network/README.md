# GNN v1 - (gengi neural network)
This is a custom neural network using pytorch sequential model with linear activation function

The network structure has 3 layers:
Input Layer    = 40 features (input)
Hidden layer 1 = 222 neurons
Hidden layer 2 = 100 neurons
Output layer   = 33 outputs

why this network vulnerable?
1. Using Linear activation function"
   Original:
   $$f(x) = x$$
   Reversed:
   $$x = f(x)$$

2. Doesn't use optimizers such as gradient descent

Solver:
1. generate and analyze the using test inputs
2. recovering the bias and weight using the difference of each inputs
3. plug the test inputs using inverse linear function