# displaying the game board, capturing user input, updating the game state based on user actions
# from PIL import Image, ImageTk  # pip install pillow
from const import *
from tkinter import *
from database import register_user, login_user
from game import Cell, start_game
from random import randint  # TEMP


# TODO class for LoginWindow to reduce amount of functions arguments, breakup functions into smaller

def login_button_clicked(entry_username, entry_password, login_window, login_status_label, player):
    username = entry_username.entry.get()
    password = entry_password.entry.get()

    login_status_label.grid_forget()  # hide old status line

    login_status = login_user(username, password)  # check with db

    if login_status == 'Ok':
        player.set(username)
        login_window.destroy()
    elif login_status != 'Ok':  # update status line
        login_status_label = Label(login_window, text=login_status, bd=1, relief=SUNKEN, pady=5)
        login_status_label.grid(row=1, column=0, sticky='ews', pady=10)


def register_button_clicked(entry_username, entry_password, player, window):
    # get the username, password from the UI
    username = entry_username.entry.get()
    password = entry_password.entry.get()
    # add to db
    register_user(username, password)
    player.set(username)
    window.destroy()  # could be self.destroy() without argument if class


#
# MAIN UI DRAW
def draw_interface():

    root = Tk()
    root.title('Tic-tac-toe')
    root.geometry('500x600')
    root.resizable(False, False)

    # background image
    bg_image = PhotoImage(file='images/bg.png')
    bg_image_label = Label(root, image=bg_image)
    bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)

    #
    # Player 1, Player 2 BUTTONS frame
    top_menu_frame = Frame(root, bg=WIDGETS_BG)
    top_menu_frame.pack(pady=10, padx=20, fill='x')

    # TODO remove buttons, make usernames buttons, FLAT, hand2
    button_player1 = Button(top_menu_frame, text='Player 1',  padx=10, cursor='hand2',
                            command=lambda: draw_login_window(root, name1), bg='#262c34', fg='gray', relief=FLAT)
    # in Button ^ can also set activebackground, activeforeground
    button_player1.grid(row=0, column=0, sticky='w')

    button_player2 = Button(top_menu_frame, text='Player 2', padx=10, cursor='hand2',
                            command=lambda: draw_login_window(root, name2), bg='#262c34', fg='gray', relief=FLAT)
    button_player2.grid(row=0, column=1, sticky='e')

    top_menu_frame.grid_columnconfigure((0, 1), weight=1)  # evenly distribute columns

    #
    # players INFO frame
    players_info_frame = Frame(root, bg=WIDGETS_BG)
    players_info_frame.pack(pady=5, padx=10, fill='x')
    #
    # NAME 1 UPDATE
    x_icon = PhotoImage(file='images/x_icon.png')
    x_icon_label = Label(players_info_frame, image=x_icon, bd=0, bg=WIDGETS_BG)
    x_icon_label.grid(row=0, column=0, padx=20, sticky='w')

    name1 = StringVar()  # StringVar - tkinter class to update text dynamically
    name1.set('Bobka')
    player1_name_label = Label(players_info_frame, textvariable=name1, font=('Helvetica', 15, 'bold'), fg='white', bg=WIDGETS_BG)
    player1_name_label.grid(row=0, column=1, sticky='w')

    spacer_label = Label(players_info_frame, width=10, bg=WIDGETS_BG)
    spacer_label.grid(row=0, column=2)

    # WINS
    wins_label = Label(players_info_frame, text='0 | 0', fg='white', bg=WIDGETS_BG)
    wins_label.grid(row=0, column=3)

    spacer_label = Label(players_info_frame, width=10, bg=WIDGETS_BG)
    spacer_label.grid(row=0, column=4)

    #
    # NAME 2 UPDATE
    name2 = StringVar()
    name2.set('Gopka')
    player2_name_label = Label(players_info_frame, textvariable=name2, font=('Helvetica', 15, 'bold'), fg='white', bg=WIDGETS_BG)
    player2_name_label.grid(row=0, column=5, sticky='e')

    o_icon = PhotoImage(file='images/o_icon.png')
    o_icon_label = Label(players_info_frame, image=o_icon, bd=0, bg=WIDGETS_BG)
    o_icon_label.grid(row=0, column=6, padx=20, sticky='e')

    players_info_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)  # evenly distribute columns

    #
    # mark with LINE whose turn is now
    # active_player = start_game()
    # LINE frame
    # active_players_frame = Frame(root, bg=WIDGETS_BG)
    # active_players_frame.pack(pady=0, padx=10, fill='x')
    # if active_player == 1:
    #     line_image = PhotoImage(file='images/line_01.png')
    # elif active_player == 2:
    #     line_image = PhotoImage(file='images/line_02.png')
    # line1_label = Label(active_players_frame, image=line_image, bd=0, bg=WIDGETS_BG)
    # line1_label.pack()


    #
    # tic-tac-toe FIELD
    # fill Field with Cells (clear at beginning)
    cells = []  # empty list to store Cell instances
    for row in range(ROWS):
        for col in range(COLS):
            cell_instance = Cell(root, FIELD_X_0 + 140 * col, FIELD_Y_0 + 140 * row)
            cell_instance.spawn()
            cells.append(cell_instance)  # to reference a specific Cell
    # selected_cell = cells[i]  # to reference a specific Cell
    # selected_cell.image_label.configure(image=x_image)


    def cell_click(e, cell):
        first_move = randint(1, 2)
        print(f'click + {first_move}')
        # change this cell to X or O
        # c_image_label.place_forget()
        # TODO check if old image (clear_cell) gone
        # TODO ^ https://stackoverflow.com/questions/41657449/tkinter-not-changing-image-on-button-press
        if first_move == 1:
            cell.configure(image=x_image)
        else:
            cell.configure(image=o_image)


    # c_image_label1 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)  # bd=0 - border to 0
    # c_image_label1.place(x=50, y=122)
    # c_image_label1.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label1))
    #
    # c_image_label2 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label2.place(x=190, y=122)
    # c_image_label2.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label2))
    # c_image_label3 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label3.place(x=330, y=122)
    # c_image_label3.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label3))
    #
    # c_image_label4 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label4.place(x=50, y=262)
    # c_image_label4.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label4))
    # c_image_label5 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label5.place(x=190, y=262)
    # c_image_label5.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label5))
    # c_image_label6 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label6.place(x=330, y=262)
    # c_image_label6.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label6))
    #
    # c_image_label7 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label7.place(x=50, y=402)
    # c_image_label7.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label7))
    # c_image_label8 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label8.place(x=190, y=402)
    # c_image_label8.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label8))
    # c_image_label9 = Label(root, image=c_image, bd=0, bg=WIDGETS_BG)
    # c_image_label9.place(x=330, y=402)
    # c_image_label9.bind('<ButtonRelease-1>', lambda e: cell_click(e, c_image_label9))

    # TODO maybe classes for placement of X and O

    # bottom menu frame
    # TODO Exit Button(..., command=root.quit)

    root.mainloop()


#
# LOGIN window
def draw_login_window(root, player):  # draw login/register
    # TODO change background color to main window and text color to white
    # login_window = Tk() - instead passed root to set position of login window
    login_window = Toplevel(root)  # Toplevel - tkinter widget for separate, top-level window to get root geometry
    login_window.geometry('250x213')
    login_window.title('Join Game')

    # to open login window in the center of main window ('+%d+%d' % (x, y) - format string):
    x = root.winfo_rootx() + root.winfo_width() // 2 - login_window.winfo_reqwidth() // 2
    y = root.winfo_rooty() + root.winfo_height() // 2 - login_window.winfo_reqheight() // 2
    login_window.geometry('+%d+%d' % (x, y))

    userinfo_fields_frame = Frame(login_window)
    userinfo_fields_frame.grid(row=0, column=0, pady=10, padx=20)

    class LabelEntry:  # TODO maybe without class, only two Entries
        def __init__(self, parent_frame, row, column, width, text):
            self.label = Label(parent_frame, text=text)
            self.label.grid(row=row, column=column, padx=5, pady=10, sticky='e')
            self.entry = Entry(parent_frame, width=width)  # show='*'
            self.entry.grid(row=row, column=column + 1, padx=5, pady=10, sticky='w')

    entry_username = LabelEntry(userinfo_fields_frame, 0, 0, 20, 'Username: ')
    entry_password = LabelEntry(userinfo_fields_frame, 1, 0, 20, 'Password: ')

    button_login = Button(userinfo_fields_frame, text='Login', padx=30,
                          command=lambda: login_button_clicked(entry_username, entry_password, login_window, login_status_label, player))
    button_login.grid(row=2, column=0, pady=5, columnspan=2, sticky='ew')

    button_register = Button(userinfo_fields_frame, text='Register', padx=30,
                             command=lambda: register_button_clicked(entry_username, entry_password, player, login_window))
    button_register.grid(row=3, column=0, pady=5, columnspan=2, sticky='ew')

    #
    # bottom STATUS bar
    login_status_label = Label(login_window, text='Enter Username and Password', bd=1, relief=SUNKEN, pady=5)
    login_status_label.grid(row=1, column=0, sticky='ews', pady=10)

    # return player, entry_username.entry.get()  # player1/2 username
    # TODO clean up ^^^

    # login_window.mainloop()  # no need because login_window = Toplevel(root)

