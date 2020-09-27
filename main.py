from neural_network import Nerual_Network
import psudeo_generator import Generate
Net0 = Nerual_Network(2500, .625)
Net1 = Nerual_Network(2000, .2)
Net2 = Nerual_Network(1500, 0.0375)
Net3 = Nerual_Network(1000, 0.025)
Net4 = Nerual_Network(500, 0.0125)
prob = Generate(2500)
Net0.create(prob)
