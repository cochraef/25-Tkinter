"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Evan Cochrane.
"""  # 1: DONE PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
import random


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # 2: DONE After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------

    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # 3: DONE After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

    my_frame = ttk.Frame(root, padding=50)
    my_frame.grid()

    # ------------------------------------------------------------------
    # 4: DONE After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    my_button = ttk.Button(my_frame, text='The Second Coming approaches...')

    # ------------------------------------------------------------------
    # 5: DONE After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------

    my_button['command'] = (lambda: hello())
    my_button.grid()

    # ------------------------------------------------------------------
    # 6: DONE After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

    new_button = ttk.Button(my_frame, text='There is no escape!')
    new_button['command'] = (lambda: ok(my_box))
    new_button.grid()

    my_box = ttk.Entry(my_frame)
    my_box.grid()

    # ------------------------------------------------------------------
    # 7: DONE
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    newer_button = ttk.Button(my_frame, text='Run!!!')
    newer_button['command'] = (lambda: print_n_times(new_box, my_box))
    newer_button.grid()

    new_box = ttk.Entry(my_frame)
    new_box.grid()

    # ------------------------------------------------------------------
    # 8: DONE As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()


def hello():
    if random.randint(0, 200) == 100:
        print('Squirtle Returns...')
    else:
        print('Hello')


def ok(entry_box):
    if entry_box.get() == 'ok':
        print('Hello')
    elif entry_box.get() == 'squirtle' or 'Squirtle':
        print('Do not speak his name!')
    else:
        print('Goodbye')


def print_n_times(entry_box_string, entry_box_int):
    n = int(entry_box_int.get())

    for _ in range(n):
        print(entry_box_string.get())


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
