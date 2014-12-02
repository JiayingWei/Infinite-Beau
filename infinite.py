import curve_generator
import write_png

def main():
    Ak = [1,2,3,2]
    ak = [4,3.3,1,2]
    mu0 = curve_generator.calculate_mu0(Ak,ak)

    L = 10          #length of the line
    delta0 = 1      #no idea what units this should be in
    Z0 = (0,0)      #not sure if this is right

    (x1,y1) = curve_generator.draw_curves(Ak,ak,mu0,L,delta0,Z0)

    (x2,y2) = write_png.map_coordinates(x1,y1)

    write_png.paint_canvas(x2,y2)
    print 'lol'


if __name__ == '__main__':
    main()
