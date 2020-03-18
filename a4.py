class KB:    
    def __init__(self):
        self.atoms = {}
        super().__init__()
        
    #Q1 

    # Given
    # returns True if, and only if, string s is a valid variable name
    def is_atom(self, s):
        if not isinstance(s, str):
            return False
        if s == "":
            return False
        return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

    def is_letter(self, s):
        return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

    def takeCmd(self):
        cmd=input("kb>")
        
    # what type of excepts should we expect to deal with?
    def loadTxtFile(self, aName):
        try:
            aFile = open(aName,'w+')
            aFile.readline()       
            pass
        except:
            # what type of except is this?
            print("Error: ", aName, " is not a valid knowledge base")
            pass
        else:
            pass
        finally:
            pass

    def tell(self, aString):
        names = aString.split()
        if len(aString) == 0 or len(names) == 0:
            print("Error: tell needs at least one atom")
            return False
        for i in names:
            if not is_atom(i):
                print("Error: ", i, " is not a valid atom")
                return False
            else:
                if i in self.atoms:
                    print("atom ", i, " already known to be true")
                else:
                    self.atoms[i] = True
    
    def inferAll(self, kb):
        rules = {}
        # how to parse string line by line to yield rules to be thrown into dict as key&item?
        print("Newly inferred atoms:")
        print("Atoms already known to be true:")
        