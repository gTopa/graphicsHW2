from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(screen, 250, 250, 350, 300, color)

draw_line(screen, 250, 250, 150, 300, color)

draw_line(screen, 250, 250, 150, 200, color)

draw_line(screen, 250, 250, 350, 200, color)

draw_line(screen, 250, 250, 300, 350, color)

draw_line(screen, 250, 250, 300, 150, color)

draw_line(screen, 250, 250, 200, 150, color)

draw_line(screen, 250, 250, 200, 350, color)

draw_line(screen, 250, 250, 250, 350, color)

draw_line(screen, 250, 250, 250, 150, color)

draw_line(screen, 250, 250, 350, 250, color)

draw_line(screen, 250, 250, 150, 250, color)

display(screen)

save_extension(screen, 'img.png')
