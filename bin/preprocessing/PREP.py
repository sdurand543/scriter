preprocessors = dict()

class PREP():
    def __init__(self, name, description, f_preprocess):
        self.name = name
        self.description = description
        self.f_preprocess = f_preprocess
        preprocessors[name] = self

