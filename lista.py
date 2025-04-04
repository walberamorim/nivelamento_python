FRUTAS = ["Banana", "Maca", "Laranja", "Manga", "Uva"]

if __name__ == "__main__":
    print(f"Lista de frutas: {FRUTAS}")
    
    FRUTAS.append("Abacaxi")

    for posicao, fruta in enumerate(FRUTAS):
        print(f"{fruta} é uma fruta na posicao {posicao}")