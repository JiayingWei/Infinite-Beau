from math import pi as pi

import curve_generator
import write_png
import DFT

def main():
    DFT.signal_Assignment = DFT.signal_dictionary()
    depth = 5
    Ak = DFT.find_coeff(depth)[0]
    ak = DFT.find_coeff(depth)[1]
    mu0 = curve_generator.calculate_mu0(Ak,ak)
    
    colors = write_png.pickColor(Ak)

    L = 10          #length of the line
    delta0 = 1      #no idea what units this should be in
    Z0 = (0,0)      #not sure if this is right

    (x1,y1) = curve_generator.draw_curves(Ak,ak,mu0,L,delta0,Z0)

    (x2,y2) = write_png.map_coordinates(x1,y1)

    write_png.paint_canvas(x2,y2, colors)
    print 'Je suis fini'


if __name__ == '__main__':
    main()

#draw contour