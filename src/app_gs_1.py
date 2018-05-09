import tadgroupset as gs
import tadchoiceset as cs

def main():
    expr_gs_a = "ABCD or EFG"
    expr_gs_b = "EFG xor HIJ"
    
    var_gs_A = gs.create_exp(expr_gs_a)
    var_gs_B = gs.create_exp(expr_gs_b)
    
    

    return 0
# fim main  

main()
    
'''
    #expgsA = tadexpgs.create("ABCD ou (EFG xor HIJ)")

    #print(expgsA) --> GS1 = ABCD ou EFGHIJ e GS2 = EFG xor HIJ



    #gsA = gs.create("ABCD ou (EFG xor HIJ)")

    #ou

    #gsA = gs.create("ABCD ou EFGHIJ e GS2 = EFG xor HIJ")
    
   # Protótipo para desenvolvimento.


    # retorna GS1 = ou ABCD EFGHIJ
    # retorna GS1 = ABCD ou EFGHIJ e GS2 = EFG xor HIJ ?
    # ou retorna GS1 = ABCD ou EFG xor HIJ ??
'''