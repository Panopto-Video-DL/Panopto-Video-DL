import os
import threading
import webbrowser
from tkinter import Tk
from tkinter import Entry, StringVar
from tkinter import messagebox, filedialog

import PanoptoDownloader
from PanoptoDownloader import SUPPORTED_FORMATS
from PanoptoDownloader.exceptions import *

import app.utils as utils
from app.view import View


class App:

    def __init__(self):
        self.__root = Tk()
        self.__root.protocol('WM_DELETE_WINDOW', self._on_closing_window)

        self.__view = View(self.__root)
        self.__view.filepath_button.config(command=lambda: self._get_directory(self.__view.string))
        self.__view.paste_button.config(command=lambda: self._paste(self.__view.url_entry))
        self.__view.download_button.config(command=self._start)

        # Variables
        self.__thread = None

        threading.Thread(target=self._check_update).start()
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
            messagebox.showerror('Error', 'Folder does not exist')
            return

        if os.path.exists(filepath):
            os.remove(filepath)

        self.__view.download_button.config(state='disabled')
        self.__view.state_label.config(text='Downloading...')

        self.__thread = threading.Thread(target=self._download, args=(url, filepath))
        self.__thread.start()

    def _download(self, url, filepath):
        try:
            PanoptoDownloader.download(url, filepath, self._callback)

            self.__view.state_label.config(text='Done')
            messagebox.showinfo('Completed', 'Download completed')
        except RegexNotMatch:
            messagebox.showerror('Error',
                                 'URL not correct.\nPaste the automatically copied link from Browser Extension')
        except Exception as e:
            messagebox.showerror('Error', str(e))
        finally:
            self._reset()

    def _callback(self, progress: int) -> None:
        self.__view.progressbar['value'] = progress
        self.__view.update_idletasks()

    def _reset(self) -> None:
        self.__view.progressbar['value'] = 0
        self.__view.download_button.config(state='normal')
        self.__view.state_label.config(text='')
        self.__view.update_idletasks()

    def _on_closing_window(self):
        if self.__thread is not None and self.__thread.is_alive():
            messagebox.showwarning('Warning', 'The download is still in progress. Unable to close')
        else:
            self.__root.destroy()

    @staticmethod
    def _get_directory(element: StringVar) -> None:
        filetypes = [(f[1:].upper(), f'*{f}') for f in SUPPORTED_FORMATS]

        filepath = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension='')
        if filepath:
            element.set(filepath)

    @staticmethod
    def _paste(element: Entry) -> None:
        element.select_range(0, 'end')
        element.event_generate('<<Paste>>')

    @staticmethod
    def _check_update():
        update = utils.get_release_update()
        if update is not None:
            body = 'Version: ' + update.get('tag') + '\nChangelog:\n' + update.get('body') + '\n\nDownload it?'
            if messagebox.askyesno('New Update!', body):
                webbrowser.open(update.get('url'))
