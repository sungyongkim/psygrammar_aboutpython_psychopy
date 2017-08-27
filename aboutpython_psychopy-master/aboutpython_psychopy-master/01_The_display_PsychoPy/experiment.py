from constants import DISPSIZE
from psychopy.visual import Window
from psychopy.core import wait

# Initialise a new Window instance.
disp = Window(size=DISPSIZE, units='pix', fullscr=True)

# Wait for two seconds.
wait(2)

# Close the Display again.
disp.close()