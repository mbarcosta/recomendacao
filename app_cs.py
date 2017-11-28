import tadchoiceset

def main():
    dados_cs = ["A", "B", "C"]

    var_cs = tadchoiceset.create_cs(dados_cs)

    print(tadchoiceset.to_string(var_cs))

    return 0
# fim main

main()

