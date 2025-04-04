cadastro = {
    "descricao": "Cadastro de pessoas",
    "versao": "1.0",
    "pessoas": [
        {
            "nome": "Joaquim da Silva",
            "idade": 20,
            "profissao": "Programador",
        },
        {
            "nome": "Maria da Silva",
            "idade": 25,
            "profissao": "Designer",
        },
        {
            "nome": "Pedro da Silva",
            "idade": 30,
            "profissao": "Analista",
        }
    ]
}

if __name__ == "__main__":
    print(cadastro["descricao"])
    print(cadastro["versao"])
    for pessoa in cadastro["pessoas"]:
        print(f"Nome:  {pessoa["nome"]}")
        print(f"Idade: {pessoa["idade"]}")
        print(f"Profissao: {pessoa["profissao"]}")
        print("-" * 30)