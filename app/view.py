from tkinter import *
from tkinter import ttk


class View:

    def __init__(self, root: Tk):
        self.__root = root

        self.__root.title('Panopto-Video-DL')
        self.__root.geometry('500x290')
        self.__root.resizable(False, False)

        ttk.Label(self.__root,
                  text='Panopto Video DL',
                  font='-family {Segoe UI} -size 20',
                  justify='center')\
            .place(relx=0.28, rely=0.05, height=35, width=486)

        ttk.Label(self.__root, text='URL (copied from Browser Extension):') \
            .place(relx=0.107, rely=0.241, height=22, width=205)

        self.url_entry = ttk.Entry(self.__root)
        self.url_entry.place(relx=0.107, rely=0.31, relheight=0.072, relwidth=0.615)

        self.paste_button = ttk.Button(self.__root, text='Paste')
        self.paste_button.place(relx=0.75, rely=0.305, height=25, width=76)

        ttk.Label(self.__root, text='Filename:').place(relx=0.107, rely=0.414, height=22, width=205)

        self.string = StringVar()
        self.filepath_entry = ttk.Entry(self.__root, textvariable=self.string)
        self.filepath_entry.place(relx=0.107, rely=0.483, relheight=0.072, relwidth=0.615)

        self.filepath_button = ttk.Button(self.__root, text='Open')
        self.filepath_button.place(relx=0.75, rely=0.477, height=25, width=76)

        self.download_button = Button(self.__root, text='Download', font=('arial', 11, 'normal'))
        self.download_button.place(relx=0.385, rely=0.621, height=35, width=106)

        self.progressbar = ttk.Progressbar(self.__root, orient=HORIZONTAL, length=100, mode='determinate')
        self.progressbar.place(relx=0.107, rely=0.8, relwidth=0.793, relheight=0.0, height=22)

        self.state_label = Label(self.__root)
        self.state_label.place(relx=0.107, rely=0.893)

    def update_idletasks(self) -> None:
        self.__root.update_idletasks()
