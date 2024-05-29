import numpy as np
import matplotlib.pyplot as plt

# Dados dos níveis de energia da água (H₂O) da tabela
niveis_energia_dados = {
    "JKaKc": ["0₀₀", "1₁₀", "1₁₁", "1₀₁", "2₂₀", "2₂₁", "2₁₁", "2₁₂", "2₀₂", 
              "3₃₀", "3₃₁", "3₂₁", "3₂₂", "3₁₂", "3₁₃", "3₀₃"],
    "Energia": [
        "0",
        "A + B",
        "A + C",
        "B + C",
        "2(A + B + C) + 2√((B - C)² + (A - C)(A - B))",
        "4A + B + C",
        "A + 4B + C",
        "A + B + 4C",
        "2(A + B + C) - 2√((B - C)² + (A - C)(A - B))",
        "5A + 5B + 2C + 2√((A - B)² + (A - C)(B - C))",
        "5A + 2B + 5C + 2√((A - C)² - (A - B)(B - C))",
        "2A + 5B + 5C + 2√((B - C)² + (A - B)(A - C))",
        "4A + 4B + 4C",
        "5A + 5B + 2C - 2√((A - B)² + (A - C)(B - C))",
        "5A + 2B + 5C - 2√((A - C)² - (A - B)(B - C))",
        "2A + 5B + 5C - 2√((B - C)² + (A - B)(A - C))"
    ]
}

# Transformar as fórmulas de energia em uma função para cada nível
def calcular_energia(A, B, C, nivel):
    if nivel == "0₀₀":
        return 0
    elif nivel == "1₁₀":
        return A + B
    elif nivel == "1₁₁":
        return A + C
    elif nivel == "1₀₁":
        return B + C
    elif nivel == "2₂₀":
        return 2 * (A + B + C) + 2 * np.sqrt((B - C) ** 2 + (A - C) * (A - B))
    elif nivel == "2₂₁":
        return 4 * A + B + C
    elif nivel == "2₁₁":
        return A + 4 * B + C
    elif nivel == "2₁₂":
        return A + B + 4 * C
    elif nivel == "2₀₂":
        return 2 * (A + B + C) - 2 * np.sqrt((B - C) ** 2 + (A - C) * (A - B))
    elif nivel == "3₃₀":
        return 5 * A + 5 * B + 2 * C + 2 * np.sqrt((A - B) ** 2 + (A - C) * (B - C))
    elif nivel == "3₃₁":
        return 5 * A + 2 * B + 5 * C + 2 * np.sqrt((A - C) ** 2 - (A - B) * (B - C))
    elif nivel == "3₂₁":
        return 2 * A + 5 * B + 5 * C + 2 * np.sqrt((B - C) ** 2 + (A - B) * (A - C))
    elif nivel == "3₂₂":
        return 4 * A + 4 * B + 4 * C
    elif nivel == "3₁₂":
        return 5 * A + 5 * B + 2 * C - 2 * np.sqrt((A - B) ** 2 + (A - C) * (B - C))
    elif nivel == "3₁₃":
        return 5 * A + 2 * B + 5 * C - 2 * np.sqrt((A - C) ** 2 - (A - B) * (B - C))
    elif nivel == "3₀₃":
        return 2 * A + 5 * B + 5 * C - 2 * np.sqrt((B - C) ** 2 + (A - B) * (A - C))
    else:
        return None

# Constantes específicas para H2O
A = 27.877  # cm^-1
B = 14.512  # cm^-1
C = 9.285   # cm^-1

# Calcular os níveis de energia
niveis_energia_calculados = []
for nivel in niveis_energia_dados["JKaKc"]:
    energia = calcular_energia(A, B, C, nivel)
    niveis_energia_calculados.append(energia)

# Separar os níveis de energia em dois conjuntos
JKaKc = niveis_energia_dados["JKaKc"]
left_indices = [0, 2, 4, 6, 8, 10, 12, 14]  # Índices para o lado esquerdo
right_indices = [1, 3, 5, 7, 9, 11, 13, 15]  # Índices para o lado direito

left_labels = [JKaKc[i] for i in left_indices]
left_energies = [niveis_energia_calculados[i] for i in left_indices]
right_labels = [JKaKc[i] for i in right_indices]
right_energies = [niveis_energia_calculados[i] for i in right_indices]

# Plotar os níveis de energia
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o lado esquerdo
for i, energia in enumerate(left_energies):
    ax.hlines(y=energia, xmin=-0.4, xmax=0.4, colors='b', linestyles='-', lw=2)
    ax.text(-0.45, energia, f'{left_labels[i]}', ha='right', va='center', color='black')
    ax.text(0.45, energia, f'{energia:.0f}', ha='left', va='center', color='black')

# Plotar o lado direito
for i, energia in enumerate(right_energies):
    ax.hlines(y=energia, xmin=1.6, xmax=2.4, colors='b', linestyles='-', lw=2)
    ax.text(1.55, energia, f'{right_labels[i]}', ha='right', va='center', color='black')
    ax.text(2.45, energia, f'{energia:.0f}', ha='left', va='center', color='black')

ax.set_xticks([])
ax.set_yticks(np.arange(0, 300, 50))
ax.set_xlabel('Níveis de energia (JKaKc)')
ax.set_ylabel('Energia (cm^-1)')
ax.set_title('Níveis de energia rotacional da molécula de H₂O')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlim(-1, 3)

# Salvar a figura com alta resolução
fig.savefig('niveis_energia_H2O_alta_resolucao.png', dpi=300, bbox_inches='tight')

plt.show()
