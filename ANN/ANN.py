import numpy as np
x=np.array([[2,9],[1,3],[3,6]],dtype=float)
y=np.array([[92],[86],[89]],dtype=float)
deno=np.amax(x,axis=0)
x=x/deno
print("x is:",x)
y=y/100
print("y is:",y)


def sigmoid(x):
  return 1/(1+np.exp(-x))

#derivative of sig
def derivatives_sigmoid(x):
  return x*(1-x)


iteration=100
learning_rate=0.1
inputlayer_neurons=2
hiddenlayer_neurons=3
output_neurons=1

weight_for_hidden=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bias_for_hidden=np.random.uniform(size=(1,hiddenlayer_neurons))
weight_for_output=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bias_for_output=np.random.uniform(size=(1,output_neurons))


for i in range(iteration):
  hidden=np.dot(x,weight_for_hidden)+bias_for_hidden
  print(hidden)
  hidden_output=sigmoid(hidden)
  output_y=np.dot(hidden_output,weight_for_output)+bias_for_output
  predicted_output=sigmoid(output_y)
  print("y is",predicted_output)


  #backprop

  #output layer
  Error_for_output=y-predicted_output
  outgrad=derivatives_sigmoid(predicted_output)
  d_output=Error_for_output*outgrad

  #hidden layer
  Error_for_hidden=d_output.dot(weight_for_output.T)
  hiddengrad=derivatives_sigmoid(hidden_output)
  d_hiddenlayer=Error_for_hidden*hiddengrad



weight_for_output+=hidden_output.T.dot(d_output)*learning_rate
weight_for_hidden+=x.T.dot(d_hiddenlayer)*learning_rate


print("x is as follows:",x)
print("actual output",y)
print("predicted output",predicted_output)
