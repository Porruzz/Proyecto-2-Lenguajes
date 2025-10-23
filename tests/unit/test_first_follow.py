from src.first_follow import calcular_first, calcular_follow

def test_first_follow_basico():
    G = {
        "E": [["T", "E'"]],
        "E'": [["+", "T", "E'"], ["ε"]],
        "T": [["F", "T'"]],
        "T'": [["*", "F", "T'"], ["ε"]],
        "F": [["(", "E", ")"], ["id"]]
    }
    first = calcular_first(G)
    follow = calcular_follow(G, first, "E")
    assert "(" in first["E"]
    assert ")" in follow["E"]
