rCilindro  = 8
m_cilindro = 10
h_cilindro = 150 
centro_cilindro = Ponto(0, -150, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_poste = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)

rCilindro  = 8
m_cilindro = 10
h_cilindro = 30 
centro_cilindro = Ponto(0, -10, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(1, 0, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_poste2 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)

rCilindro  = 8
m_cilindro = 10
h_cilindro = 20 
centro_cilindro = Ponto(30, -20, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_poste3 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
rCilindro  = 12
m_cilindro = 10
h_cilindro = 8 
centro_cilindro = Ponto(30, -25, -200) #Ponto(0, -60, -200) -150
#d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil = Vetor(0, 1, 0)
K_d_cilindro= Vetor(0.824, 0.706, 0.549)
K_a_cilindro= Vetor(0.824, 0.706, 0.549)
K_e_cilindro= Vetor(0.824, 0.706, 0.549)
cilindro_poste4 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)

rEsfera        = 10
m_esfera       = 10
centro_esfera  = Ponto(30, -25, -200)
K_d_esfera     = Vetor(1,1,1)
K_a_esfera     = Vetor(1,1,1)
K_e_esfera     = Vetor(1,1,1)
esfera_poste = Esfera(centro_esfera, rEsfera, Cor(255,0,0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)
#objeto_esfera2 = Esfera(Ponto(10, 0, -(janela['d'] +rEsfera +20)), rEsfera, Cor(0, 255, 0))

