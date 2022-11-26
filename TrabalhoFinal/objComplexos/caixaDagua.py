# Definição do cone
#centro_cone   = Calcula_ponto_raio(centro_esfera, h_cilindro, d_cil)
centro_cone   = Ponto( 0, -70, -200)
rCone         = 30
hCone         = 15
d_cone        = Vetor(0, 1 , 0)
#d_cone        = d_cil

K_a_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
K_d_cone      = Vetor(0, 1, 0.498)
K_e_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
m_cone        = 100
cone_caixa_dagua   = Cone(centro_cone,
                    rCone, hCone, d_cone,
                    Cor(255, 0, 0), K_e_cone, K_d_cone, K_a_cone, m_cone, 1)

# Definição do cilindro
rCilindro  = 30
m_cilindro = 10
h_cilindro = 40 
centro_cilindro = Ponto(0, -110, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_caixa_dagua = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
# Definição do cilindro
rCilindro  = 5
m_cilindro = 10
h_cilindro = 40 
centro_cilindro = Ponto(0, -150, -215) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_apoio1 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
rCilindro  = 5
m_cilindro = 10
h_cilindro = 40 
centro_cilindro = Ponto(0, -150, -185) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_apoio2 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
rCilindro  = 5
m_cilindro = 10
h_cilindro = 40 
centro_cilindro = Ponto(15, -150, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_apoio3 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
rCilindro  = 5
m_cilindro = 10
h_cilindro = 40 
centro_cilindro = Ponto(-15, -150, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_apoio4 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
