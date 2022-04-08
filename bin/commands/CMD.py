cmds = dict()

class CMD():
    def __init__(self, name, semantics, description, f_view, argc):
        self.name = name
        self.semantics = semantics
        self.description = description
        self.f_view = f_view
        self.argc = argc
        cmds[name] = self

