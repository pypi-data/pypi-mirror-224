# A terminal-based UI uses Curses, which offers one-key access to most common
# operations.


import curses
from argparse import Namespace
from string import capwords
from time import sleep

from busy.ui.ui import Chooser, Prompt, TerminalUI, UserCancelError

# Set the number of columns to be centered
FIX_WIDTH = 72

class CursesError(Exception):
    pass


class CursesUI(TerminalUI):  # pragma: nocover

    name = "curses"

    def start(self):
        self._mode = "WORK"
        chooser = Chooser()
        commands = self.handler.get_commands('key')
        scommands = sorted(commands, key=lambda c: c.name)
        for command in scommands:
            chooser.add_choice(
                keys=[command.key],
                words=[command.name],
                action=command
            )
        chooser.add_choice(keys=['q'], words=['quit'])
        self._command_prompt = chooser

        curses.wrapper(self.term_loop)

    def output(self, intro=""):
        """
        Output is a shell operation.
        """
        # maxy, maxx = self._descwin.getmaxyx()
        # x, y = self._descwin.getyx()
        # limit = maxy - y - 1
        # lines = intro.split("\n")
        # self._descwin.addstr('\n'.join(lines[0:limit]))
        # self._descwin.refresh()

    def write_prompt(self, prompt):
        """
        Output a chooser prompt with underlines to a window.
        """
        if prompt.intro:
            self._descwin.addstr(prompt.intro + " ")
        if prompt.default:
            self._descwin.addstr(f"[{prompt.default}] ", self._action_colors)
        for choice in prompt.choices:
            if choice.word == prompt.default:
                continue
            pre, it, post = choice.word.partition(choice.key)
            self._descwin.addstr(pre,  self._action_colors)
            self._descwin.addstr(it, curses.A_UNDERLINE | self._action_colors)
            self._descwin.addstr(post + " ",  self._action_colors)
        cursor = self._descwin.getyx()
        self._descwin.refresh()
        self._descwin.move(*cursor)


    # TODO: Use a better editing component
    #
    # NOTE: get_string assumes that everything has been cleared and we are in
    # the right place.

    def get_string(self, intro, default=""):
        prompt = Prompt(intro=intro, default=default)
        self._update()
        self.write_prompt(prompt)
        curses.echo()
        try:
            string = self._descwin.getstr()
        except KeyboardInterrupt:
            raise UserCancelError
        value = string.decode() or default
        curses.noecho()
        self._descwin.clear()
        self._descwin.refresh()
        return value

    def get_option(self, chooser):
        """Get a 1-keystroke choice from the user"""
        self._update()
        self.write_prompt(chooser)
        key = self._get_key(self._descwin)
        self._descwin.clear()
        self._descwin.refresh()
        return chooser.choice_by_key(key)

    def term_loop(self, fullwin):
        self._init_colors()
        self._init_windows(fullwin)
        self.queue = "tasks"
        self._status = "Welcome to Busy!"
        list = ""
        cursor = 0
        while True:
            self._update()
            self._descwin.clear()
            self.write_prompt(self._command_prompt)
            try:
                key = self._get_key(self._descwin)
            except UserCancelError:
                break
            except CursesError:
                sleep(1)
                continue
            if key == "q":
                break
            command = self.handler.get_command(
                'key', key, ui=self, storage=self.handler.storage,
                queue=self.queue)
            if not command:
                self._status = f"Invalid command {key}"
                continue
            command_name = capwords(command.name)
            self._descwin.clear()
            try:
                result = command.execute()
                self._status = command.status or ""
                if hasattr(command, 'queue'):
                    self.queue = command.queue
            except UserCancelError:
                self._status = f"{command_name} command canceled"

    def _init_windows(self, fullwin):
        h, oldw = fullwin.getmaxyx()
        x, w = int((oldw - FIX_WIDTH) / 2), FIX_WIDTH
        bkwin = curses.newwin(h, w+2, 0, x-1)
        bkwin.bkgdset(" ", curses.color_pair(3))
        bkwin.clear()
        bkwin.refresh()
        
        self._queuewin = curses.newwin(2, w, 1, x)
        self._queuewin.bkgd(" ", self._queue_colors)

        self._todowin = curses.newwin(4, w, 3, x)
        self._todowin.bkgd(" ", self._item_colors)

        self._descwin = curses.newwin(h-11, w, 8, x)
        self._descwin.bkgd(" ", self._bg_colors)

        self._statuswin = curses.newwin(2, w, h-2, x)
        self._statuswin.bkgd(" ", self._status_colors)

    def _init_colors(self):
        dark = 8
        light = 9
        curses.init_color(light, 700, 700, 700)
        curses.init_color(dark, 200, 200, 200)
        curses.init_color(curses.COLOR_BLACK, 100, 100, 100)
        curses.init_pair(1, curses.COLOR_CYAN, dark)
        curses.init_pair(2, curses.COLOR_YELLOW, dark)
        curses.init_pair(3, curses.COLOR_GREEN, dark)
        curses.init_pair(4, light, dark)
        curses.init_pair(5, curses.COLOR_MAGENTA , dark)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)

    @property
    def _queue_colors(self):
        return curses.color_pair(1)

    @property
    def _item_colors(self):
        return curses.color_pair(2)
    
    @property
    def _action_colors(self):
        return curses.color_pair(3)
    
    @property
    def _bg_colors(self):
        return curses.color_pair(4)
    
    @property
    def _status_colors(self):
        return curses.color_pair(5)


    def _update(self):
        self._queuewin.clear()
        self._queuewin.move(0, 0)
        self._queuewin.addstr(capwords(self.queue) + " / Todo")
        self._queuewin.move(0, FIX_WIDTH-len("Busy"))
        self._queuewin.addstr("Busy")
        self._queuewin.refresh()

        collection = self.handler.storage.get_collection(self.queue)
        self._todowin.clear()
        self._todowin.border()
        if collection:
            value = collection[0].first
            if len(value) > FIX_WIDTH - 2:
                value = value[0:FIX_WIDTH - 5] + "..."
            self._todowin.move(1, 1)
            self._todowin.addstr(value, curses.A_BOLD)
            if (value := collection[0].next):
                if len(value) > FIX_WIDTH - 8:
                    value = value[0:FIX_WIDTH - 11] + "..."
                self._todowin.move(2, 3)
                self._todowin.addstr('--> ' + value)
        self._todowin.refresh()

        self._statuswin.clear()
        self._statuswin.move(0,0)
        self._statuswin.addstr(self._status)
        self._statuswin.refresh()


    # Convenience method to get one keystroke from the user.
    #
    def _get_key(self, window):
        try:
            key = window.getkey()
        except KeyboardInterrupt:
            raise UserCancelError
        except curses.error:
            raise CursesError
        return key

    # def listmode(self):
    #     length = len(list.splitlines())
    #     if length:
    #         listpad = curses.newpad(length, curses.COLS)
    #         listpad.addstr(list)
    #         self.listmode = True
    #         listpad.move(cursor, 0)
    #         listpad.addstr(">")
    #         listpad.refresh(0, 0, 5, 0, curses.LINES - 5, curses.COLS)
    #     if self.listmode:
    #         if key == "KEY_UP" and cursor > 0:
    #             cursor = cursor - 1
    #         if key == "KEY_DOWN" and cursor < length:
    #             cursor = cursor + 1
