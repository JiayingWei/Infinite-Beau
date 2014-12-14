import curve_generator
import write_png
import DFT
import random
from audio_record import record 

def main():
    """Calculates and saves a colored curve generated from a waveform.
    """
    DFT.signal_Assignment = DFT.signal_dictionary("Audio/recordtest.wav")
    depth = 4
    Ak = DFT.find_coeff(depth)[0]   #amplitude fourier descriptor of the waveform
    ak = DFT.find_coeff(depth)[1]   #phase fourier descriptor of the waveform
    mu0 = curve_generator.calculate_mu0(Ak,ak)  #coefficiant needed to generate the wave (calculated from Ak and ak)

    colors = write_png.pickColor(Ak)    #picks the colors to color the image in based on the amplitude fourier wa

    L = 1          #length of the line
    delta0 = 1     #initial direction
    Z0 = (0,0)     #initial starting coefficient

    #(makes for a more interesting picture)
    Ak1 = [x*10*random.randint(1,100) for x in Ak]  #introduces a amplification and randomizes the Ak coefficient 
    ak1 = [x*.1*random.randint(1,100) for x in ak]  #introduces a diminisher and randomizes the ak coefficient

    (x1,y1) = curve_generator.draw_curves(Ak1[::-1],ak1,mu0,L,delta0,Z0)    #generates (x,y) coordinates of the curve

    (x2,y2) = write_png.map_coordinates(x1,y1)  #remaps all the (x,y) coordinates

    write_png.paint_canvas(x2,y2, colors)   #writes coordinates to a PNG file

if __name__ == '__main__':
    main()
