from numpy import dot, array, random, exp

class NeuralNetwork():
	def __init__(self):
		# seed the random number generator,
		# every time the program runs
		random.seed(1)

		# we model a single neuron, with 3 input connections and 1 output connection.
		# assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
		# and mean 0
		self.synaptic_weights = 2 * random.random((3,1)) - 1

	# The sigmoid function, which describes an s shaped curve 
	# we pass the weighted sum of the inputs through this function
	# to normalize them between 0 and 1
	def __sigmoid(self, x):
		return 1 /(1+ exp(-x))
	# gradient of the sigmoid curve
	def __sigmoid_derivative(self, x):
		return x * (1-x)

	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		for iteration in xrange(number_of_training_iterations):
			# pass the training set through our neural net
			output = self.predict(training_set_outputs)
			# calculate the error
			error - training_set_outputs - output
			# multiply the error by the input and again by the gradient of the sigmoid curve
			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
			# adjust the weights
			self.synaptic_weights += adjustment

	def predict(self, inputs):
		# pass inputs through our neural network (our single neuron)
		return self.__sigmoid(dot(input, self.synaptic_weights))

if __name__ == "__main__":
	# initialise a single neuron neural network
	neural_network = NeuralNetwork()

	print 'Random starting synaptic weights:'
	print neural_network.synaptic_weights

	# The training set. We have 4 examples, each consisting of 3 input values
	# and 1 output value.
	training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
	training_set_outputs = array([[0,1,1,0]]).T 

	# train the neural network using a training set.
	# do it 10,000 times and make small adjustment
	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print 'New synaptic weights after training: '
	print neural_network.synaptic_weights

	# Test the neural network
	print 'Considering the new situation [1, 0, 0] -> ?: '
	print neural_network.think(array([1,0,0]))