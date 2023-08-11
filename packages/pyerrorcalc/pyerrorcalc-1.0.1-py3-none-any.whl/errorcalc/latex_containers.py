class Container:
    pass

class Text(Container):
    def __init__(self, text:str):
        self._text = text
    def latex(self) -> str:
        return self._text

class Latex_Container(Container):
    def __init__(self):
        self._contents = []
    def add(self, item:Container):
        self._contents.append(item)
    def latex(self) -> str:
        s = ""
        for item in self._contents:
            if type(item) == str:
                s+=item
            else:
                s+=item.latex()
            s+='\n'
        return s

class Equation(Container):
    def __init__(self,content:str, numbered:bool = False):
        super().__init__()
        self._content = content
        self._numbered = numbered
    def latex(self) -> str:
        identifier = f"equation{'' if self._numbered else '*'}"
        return "\\begin{%s}\n%s\n\\end{%s}" % (identifier,self._content,identifier)

class Math(Container):
    def __init__(self):
        self._contents = []
    def add(self, item:Container):
        self._contents.append(item)
    def latex(self) -> str:
        return "\\begin{math}\n%s\n\\end{math}\n\\\\" % "\\\\\n".join(self._contents)


    

