import tadgroupset as gs
import tadchoiceset as cs
import tadGroupSetTable as gst


def main():
    gstable = gst.create()
    gs_A = gs.create_exp("t0,t1 xor t2,t3,t8,t9,t10")
    gs_D = gs.create_exp("t2 or t3")
    gs_B = gs.create_exp("t5 or t6")
    gs_C = gs.create_exp("t0 or t1")
    gs_E = gs.create_exp("t2,t3 xor t8,t9,t10")
    gs_F = gs.create_exp("t8 xor t9,t10")
    gs_G = gs.create_exp("t9 or t10")

    gstable = gst.addGS(gstable, gs_A)     
    
    gstable = gst.addGS(gstable, gs_C)
    gstable = gst.addGS(gstable, gs_B)
    
    #     gstable = gst.addGS(gstable, gs_D)
    #     gstable = gst.addGS(gstable, gs_E)
    #     gstable = gst.addGS(gstable, gs_F)
    #     gstable = gst.addGS(gstable, gs_G)

    gst.printTabGS(gstable)

    return 0


# fim main

main()