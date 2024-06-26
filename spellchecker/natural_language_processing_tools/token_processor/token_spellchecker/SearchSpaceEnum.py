from enum import Enum


class SearchSpaceEnum(Enum):
    A = ['a', 'o', 'e', 'd', 'b', 'h', 'q', 'w', 's', 'z', 'p', 'q']
    A_ACC = ['á', 'a', 'o', 'e', 'd', 'b', 'h', 'q', 'w', 's', 'z', 'p', 'q']
    B = ['b', 'v', 'd', 'a', 'p', 'q', 'n', 'g', 'h']
    C = ['c', 's', 'd', 'f', 'o', 'e', 'z', 'x', 'v']
    D = ['d', 'a', 'b', 't', 'p', 'q', 'e', 's', 'f', 'x', 'c']
    E = ['e', 'a', 'o', 'h', 'w', 'r', 's', 'd', 'f']
    E_ACC = ['é', 'e', 'a', 'o', 'h', 'p', 'w', 'r', 's', 'd', 'f']
    F = ['f', 'e', 'r', 't', 'd', 'g', 'c', 'v']
    G = ['g', 'r', 't', 'y', 'f', 'h', 'v', 'b', 'j']
    H = ['h', 'a', 'e', 'i', 'o', 'u', 't', 'y', 'u', 'g', 'j', 'b', 'n']
    I = ['i', 'l', 'y', 'h', 'u', 'o', 'j', 'k']
    I_ACC = ['í', 'i', 'l', 'y', 'h', 'p', 'u', 'o', 'j', 'k']
    J = ['j', 'g', 'h', 'y', 'u', 'i', 'k', 'n', 'm']
    K = ['k', 'c', 'f', 'u', 'i', 'o', 'j', 'l', 'm']
    L = ['l', 'y', 'i', 'o', 'p', 'k']
    M = ['m', 'n', 'w', 'h', 'j', 'k']
    N = ['n', 'm', 'ñ', 'h', 'j', 'v', 'b']
    Ñ = ['ñ', 'o', 'p', 'l', 'n', 'm']
    O = ['o', 'a', 'e', 'u', 'p', 'q', 'h', 'p', 'i', 'k', 'l']
    O_ACC = ['ó', 'o', 'a', 'e', 'u', 'p', 'q', 'h', 'p', 'i', 'k', 'l']
    P = ['p', 'q', 'b', 'd', 'o', 'l', 'ñ', 'á', 'é', 'í', 'ó', 'ú']
    Q = ['q', 'd', 'b', 'p', 'k', 'c', 'w', 'a', 's']
    R = ['r', 'l', 'n', 'e', 't', 'd', 'f', 'g']
    S = ['s', 'z', 'c', 'x', 'q', 'w', 'e', 'a', 'd']
    T = ['t', 'd', 'l', 'r', 'y', 'f', 'g']
    U = ['u', 'v', 'o', 'n', 'c', 'y', 'i', 'h', 'j']
    U_ACC = ['ú', 'u', 'v', 'o', 'n', 'c', 'p', 'y', 'i', 'h', 'j']
    V = ['v', 'b', 'u', 'w', 'c', 'f', 'g']
    W = ['w', 'm', 'v', 'q', 'e', 'a', 's']
    X = ['x', 'z', 's', 'k', 'j', 'h', 'y', 'd', 'c']
    Y = ['y', 'l', 'i', 'v', 'x', 't', 'u', 'g', 'h', 'j']
    Z = ['z', 's', 'x', 'c', 'a']
