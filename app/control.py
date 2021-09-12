import os.path
from tkinter import Tk
from tkinter import Entry, StringVar
from tkinter import messagebox, filedialog
from PanoptoDownloader import PanoptoDownloader
from PanoptoDownloader.exceptions import RegexNotMach

from app.view import View


class App:

    def __init__(self):
        self.__root = Tk()

        self.__view = View(self.__root)

        self.__view.filepath_button.config(command=lambda: self._get_directory(self.__view.string))
        self.__view.paste_button.config(command=lambda: self._paste(self.__view.url_entry))

        self.__view.download_button.config(command=self._start)

        self.__root.mainloop()

    def _start(self) -> None:
        url = self.__view.url_entry.get()
        filepath = self.__view.filepath_entry.get()

        if not url:
            messagebox.showinfo('Missing URL', 'The URL of the lesson is missing')
            return
        if not filepath:
            messagebox.showinfo('Missing Filename', 'The Filename of the lesson is missing')
            return

        if os.path.isdir(filepath):
            messagebox.showerror('Error', 'Cannot be a folder')
            return
        if not os.path.isdir(os.path.split(filepath)[0]):
            messagebox.showerror('Error', 'Folder not exist')
            return

        self.__view.download_button.config(state='disabled')
        self.__view.state_label.config(text='Downloading...')

        PanoptoDownloader().download(url, filepath, self._callback, self._error_hook)

    def _callback(self, progress: int) -> None:
        self.__view.progressbar['value'] = progress
        self.__view.update_idletasks()

        if progress >= 100:
            self.__view.state_label.config(text='Done')
            messagebox.showinfo('Completed', 'Download completed')
            self._done()

    def _done(self) -> None:
        self.__view.progressbar['value'] = 0
        self.__view.download_button.config(state='normal')
        self.__view.state_label.config(text='')
        self.__view.update_idletasks()

    def _error_hook(self, args, /) -> None:
        if isinstance(args.exc_type, RegexNotMach):
            messagebox.showerror('Error', 'URL not correct. Paste the automatically copied link from Browser Extension')
        else:
            messagebox.showerror('Error', str(args.exc_value))
        self._done()

    @staticmethod
    def _get_directory(element: StringVar) -> None:
        filetypes = [
            ('MP4', '*.mp4'),
            ('MKV', '*.mkv'),
            ('FLV', '*.flv'),
            ('AVI', '*.avi')
        ]

        filepath = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension='*.*')
        if filepath:
            element.set(filepath)

    @staticmethod
    def _paste(element: Entry) -> None:
        element.select_range(0, 'end')
        element.event_generate('<<Paste>>')
