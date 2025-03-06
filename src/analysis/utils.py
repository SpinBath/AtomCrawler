import matplotlib.colors as mcolors
import numpy as np

def generate_colors(start_color, num_colors):
    start_rgb = np.array(mcolors.to_rgb(start_color)) 
    factor = np.linspace(0.2, 1, num_colors)  
    
    colors = [mcolors.to_hex(start_rgb * f) for f in factor]
    return colors