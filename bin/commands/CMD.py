cmds = dict()

class CMD():
    def __init__(self, name, semantics, description, f_model, f_view):
        self.name = name
        self.semantics = semantics
        self.description = description
        self.f_model = f_model
        self.f_view = f_view
        cmds[name] = self

    '''
    # FUNCTIONAL GETTER VERSIONS
    def name(self):
        """
        Returns the name of the command.
        """
        return self.name
    
    def semantics(self):
        """
        Returns the calling semantics of the command (must start with name).
        """
        return self.semantics
    
    def description(self):
        """
        Returns a description of the command.
        """
        return self.description
    
    def f_model(self, args):
        """
        Performs the functionality of the command.
        """
        return self.f_model(args)
    
    def f_view(self, args):
        """
        Performs the functionality of the command and displays it.
        """
        return self.f_view(args)
    '''
