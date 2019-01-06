import tadgroupset as gs
import tadchoiceset as cs
import tadGroupSetTable as gst


def main():
    gstable = gst.create()
   # gs_A = gs.create_exp("t0,t1 xor t2,t3,t8,t9,t10")
    #gs_D = gs.create_exp("t2 or t3")
    #gs_B = gs.create_exp("t5 or t6")
   # gs_C = gs.create_exp("t0 or t1")
#    gs_E = gs.create_exp("t2,t3 xor t8,t9,t10")
 #   gs_F = gs.create_exp("t8 xor t9,t10")
 #   gs_G = gs.create_exp("t9 or t10")

    gs_1 = gs.create_exp("t1,t2 xor t3,t4")
    gs_2 = gs.create_exp("t1 xor t2")
    gs_3 = gs.create_exp("t3 or t4")
    gstable = gst.addGS(gstable, gs_1)
    gstable = gst.addGS(gstable, gs_2)
    gstable = gst.addGS(gstable, gs_3)

    # gstable = gst.addGS(gstable, gs_A)
    
    #  gstable = gst.addGS(gstable, gs_C)
    #gstable = gst.addGS(gstable, gs_B)
    
    #     gstable = gst.addGS(gstable, gs_D)
    #     gstable = gst.addGS(gstable, gs_E)
    #     gstable = gst.addGS(gstable, gs_F)
    #     gstable = gst.addGS(gstable, gs_G)
    print("Vamos lá")
    #gst.printTabGS(gstable)
    print(len(gstable))
    print(gstable[0])
    print(gstable[1])
    return 0


# fim main

main()