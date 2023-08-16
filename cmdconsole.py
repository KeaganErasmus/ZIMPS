from cmd import Cmd


class CMDConsole(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_print_commands(self):
        print("E")

    def do_quit(self, line):
        print("Quitting ......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

    do_q = do_quit


if __name__ == "__main__":
    cmdc = CMDConsole()
    cmdc.cmdloop()
