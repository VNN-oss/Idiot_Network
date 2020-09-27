from neural_network import Nerual_Network
import psudeo_generator import Generate
Net0 = Nerual_Network(5000, .2, 0,0)
Net1 = Nerual_Network(2500, .2,0,0)
Net2 = Nerual_Network(2000, 0.0375,0,0)
Net3 = Nerual_Network(1500, 0.025,0,0)
Net4 = Nerual_Network(1000, 0.0125,0,0)
Net5 = Nerual_Network(500,0.00125,0,0)
prob = Generate(60000)
Net0.create(prob)
