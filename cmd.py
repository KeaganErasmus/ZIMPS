from cmd import Cmd


class Quitter(Cmd):

    def __init__(self, *args):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.args = args
        self.userinput = ""

    def do_quit(self, line):
        print("Quitting ......")
        return True


    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))


    do_q = do_quit

if __name__ == "__main__":
    quitter = Quitter()
    quitter.cmdloop()