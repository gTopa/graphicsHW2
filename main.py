from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(screen, 3, 3, 100, 10, color)

display(screen)

draw_line(screen, 3, 200, 150, 250, color)

display(screen)

draw_line(screen, 3, 300, 80, 377, color)

display(screen)

save_extension(screen, 'img.png')
