# Definição do cone
#centro_cone   = Calcula_ponto_raio(centro_esfera, h_cilindro, d_cil)
centro_cone   = Ponto(-150, -100, -350)
rCone         = 40
hCone         = 25
d_cone        = Vetor(0, 1 , 0)
#d_cone        = d_cil

K_a_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
K_d_cone      = Vetor(0, 1, 0.498)
K_e_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
m_cone        = 100
cone_celeiro   = Cone(centro_cone,
                    rCone, hCone, d_cone,
                    Cor(255, 0, 0), K_e_cone, K_d_cone, K_a_cone, m_cone, 1)

# Definição do cilindro
rCilindro  = 40
m_cilindro = 10
h_cilindro = 50 
centro_cilindro = Ponto(-150, -150, -350) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_celeiro = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
