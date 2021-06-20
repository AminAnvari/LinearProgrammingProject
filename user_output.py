from print_table import print_table
from print_text import print_text


def user_output(window, ans, x):
    if ans == 'Finished!':
        print_table(window, 100, x)
    else:
        print_text(window, 100, ans)
