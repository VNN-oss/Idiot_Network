from environment import Set
from neural_network import Neural_Network
Net0 = Neural_Network(1000000, .2,0)
Net1 = Neural_Network(15000, .2,0)
Net2 = Neural_Network(1000,0.0375,0)
Net3 = Neural_Network(500, 0.025,0)
prob = Set()
d1 = prob.generate(100000)
Net0.create(frame_data(d1, 0.2))
Net1.create(frame_data(prob.Cut(10000), 0.2))
Net2.create(frame_data(prob.Cut(1000), 0.2))
Net3.create(frame_data(prob.Cut(100), 0.2))
