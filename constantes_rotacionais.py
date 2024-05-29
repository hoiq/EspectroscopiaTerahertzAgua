# Importar biblioteca
import numpy as np

# Constantes físicas
u = 1.66053886e-27
h = 6.62606957e-34
c = 2.99792458e8

# Função para calcular o centro de massa -> xyz = (Σ mi * xi) / M 
def centro_de_massa(massas, xyz):
    # Posição do centro de massa nas coordenadas originais
    cm = sum(massas[:, np.newaxis] * xyz) / np.sum(massas)
    # Transforme em coordenadas cm e retorne
    xyz -= cm
    return xyz

# Função para obter a matriz de inércia
def obter_matriz_de_inercia(massas, xyz):
    # Calcula o centro de massa
    xyz = centro_de_massa(massas, xyz)
    x, y, z = xyz.T # Inverte a ordem dos eixos
    # Calculos intermediários
    x2 = x**2
    y2 = y**2
    z2 = z**2
    xy = x * y
    xz = x * z
    yz = y * z
    # Momento de inercia
    Ixx = np.sum(massas * (y2 + z2)) # np.sum (retorna a soma dos arrays)
    Iyy = np.sum(massas * (x2 + z2))
    Izz = np.sum(massas * (x2 + y2))
    Ixy = -np.sum(massas * xy)
    Iyz = -np.sum(massas * yz)
    Ixz = -np.sum(massas * xz)
    return np.array([[Ixx, Ixy, Ixz], [Ixy, Iyy, Iyz], [Ixz, Iyz, Izz]])

# Função para obter os momentos principais de inércia
def obter_momento_principal_de_inercia(I):
    Ip = np.linalg.eigvals(I) # Calcular os autovalores da matriz I
    # Ordenar e converter momentos principais de inércia para SI (kg.m2)
    Ip.sort()
    return Ip * u / 1.e20

# Função para classificação das moléculas
def classificacao_moleculas(A, B, C):
    if np.isclose(A, B) and np.isclose(B, C):
        return 'Rotor esférico'
    elif np.isclose(A, B):
        return 'Rotor simétrico oblato'
    elif np.isclose(B, C):
        return 'Rotor simétrico prolato'
    else:
        return 'Rotor assimétrico'

# Função para ler arquivo com informações das moléculas
def ler_arquivo_xyz(nome_arquivo):
    data = np.loadtxt(nome_arquivo, skiprows=2)
    massas = data[:, 0]
    coordenadas = data[:, 1:]
    return massas, coordenadas

# Carregar o arquivo de dados
massas, xyz = ler_arquivo_xyz('H2O.dat')

# Calcular a matriz de inércia
I = obter_matriz_de_inercia(massas, xyz)

# Calcular os momentos principais de inércia
Ip = obter_momento_principal_de_inercia(I)

# Calcular as constantes rotacionais
A, B, C = h / (8 * np.pi**2 * c * 100 * Ip)

# Classificação da molécula
tipo_rotor = classificacao_moleculas(A, B, C)

# Calcular o momento de inércia total da molécula
inercia_da_molecula = sum(Ip)

# Imprimir resultados
print('Centro de massa:', xyz)
print('Momento de inércia:', I)
print('Momentos principais de inércia:', Ip)
print('{}: A={:.6f}, B={:.6f}, C={:.6f} cm-1'.format(tipo_rotor, A, B, C))
print('Momento de inércia total da molécula:', inercia_da_molecula)
