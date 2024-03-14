from enum import Enum


class SearchSpaceEnum(Enum):
    A = ['a', 'q', 'w', 's', 'z', 'o', 'e', 'd', 'b', 'p', 'q']
    B = ['b', 'v', 'n', 'g', 'h', 'd', 'a', 'p', 'q']
    C = ['c', 'z', 'x', 'v', 's', 'd', 'f', 'o', 'e']
    D = ['d', 'w', 'e', 'r', 's', 'f', 'x', 'c', 'a', 'b', 't', 'p', 'q']
    E = ['e', 'w', 'r', 's', 'd', 'f', 'a', 'o']
    F = ['f', 'e', 'r', 't', 'd', 'g', 'c', 'v']
    G = ['g', 'r', 't', 'y', 'f', 'h', 'v', 'b', 'j']
    H = ['h', 't', 'y', 'u', 'g', 'j', 'b', 'n', 'a', 'e', 'i', 'o', 'u']
    I = ['i', 'u', 'o', 'j', 'k', 'l', 'y', 'h']
    J = ['j', 'y', 'u', 'i', 'h', 'k', 'n', 'm', 'g']
    K = ['k', 'u', 'i', 'o', 'j', 'l', 'm', 'c', 'f']
    L = ['l', 'i', 'o', 'p', 'k', 'y']
    M = ['m', 'h', 'j', 'k', 'n', 'w']
    N = ['n', 'h', 'j', 'v', 'b', 'm', 'ñ']
    Ñ = ['ñ', 'o', 'p', 'l', 'n', 'm']
    O = ['o', 'i', 'p', 'k', 'l', 'a', 'e', 'u', 'p', 'q']
    P = ['p', 'o', 'l', 'ñ', 'q', 'b', 'd']
    Q = ['q', 'w', 'a', 's', 'd', 'b', 'p']
    R = ['r', 'e', 't', 'd', 'f', 'g', 'l', 'n']
    S = ['s', 'q', 'w', 'e', 'a', 'd', 'z', 'x', 'c']
    T = ['t', 'r', 'y', 'f', 'g', 'd', 'l']
    U = ['u', 'y', 'i', 'h', 'j', 'v', 'o', 'n', 'c']
    V = ['v', 'f', 'g', 'c', 'b', 'u', 'w']
    W = ['w', 'q', 'e', 'a', 's', 'm', 'v']
    X = ['x', 'z', 's', 'd', 'c', 'k', 'j', 'h', 'y']
    Y = ['y', 't', 'u', 'g', 'h', 'j', 'l', 'i', 'v', 'x']
    Z = ['z', 'a', 's', 'x', 'c']

if __name__ == '__main__':
    # Ejemplo de uso:
    char = 'n'
    enum_member = SearchSpaceEnum[char.upper()]
    if enum_member:
        print(enum_member)  # Esto imprimirá el enum correspondiente a 'A'
        print(enum_member.value)  # Esto imprimirá la lista de valores de 'A'
    else:
        print(f"No se encontró ninguna enum que contenga el caracter '{char}'")