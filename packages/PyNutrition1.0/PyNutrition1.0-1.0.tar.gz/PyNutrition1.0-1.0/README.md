PyNutrition1.0.0
===========

#### Esse é um pacote que realiza cálculos relacionados a avaliação nutrtional. Cálculos retirados do site://www.drnutricao.com.br/.
#### Veja o exemplo de resultado do pacote:
## Litros agua: litrosAgua(75)

## Instalação:

    pip install PyNutrition1.0

# Uso:

'''python
from PyNutrition1.0 import imc, litrosAgua, qtdCalorias, qtdProteina, qtdCarboidratos, qtdGorduras

# Calcula o IMC
peso = 70
altura = 1.75
resultado_imc = imc(peso, altura)
print("IMC:", resultado_imc)

# Calcula a quantidade de água recomendada
litros_agua = litrosAgua(peso)
print("Litros de Água Recomendados:", litros_agua)

# Calcula a quantidade de calorias necessárias
idade = 30
sexo = 'm'
resultado_calorias = qtdCalorias(peso, altura, idade, sexo)
print("Calorias Necessárias:", resultado_calorias)

# Calcula a quantidade de proteína necessária
qtd_calorias = 2000  # substitua pelo valor real
qtd_proteina = qtdProteina(qtd_calorias)
print("Proteína Necessária:", qtd_proteina)

# Calcula a quantidade de carboidratos necessária
qtd_carboidratos = qtdCarboidratos(qtd_calorias)
print("Carboidratos Necessários:", qtd_carboidratos)

# Calcula a quantidade de gorduras necessária
qtd_gorduras = qtdGorduras(qtd_calorias)
print("Gorduras Necessárias:", qtd_gorduras)
'''