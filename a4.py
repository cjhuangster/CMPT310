import copy
class KB:    
    def __init__(self):
        self.atoms = []
        self.kb = ""
        # super().__init__()
        
    #Q1 
    # Given
    # returns True if, and only if, string s is a valid variable name
    def is_atom(self, s):
        if not isinstance(s, str):
            return False
        if s == "":
            return False
        return self.is_letter(s[0]) and all(self.is_letter(c) or c.isdigit() for c in s[1:])

    def is_letter(self, s):
        return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

    def takeCmd(self):
        count = 0
        while True:
            cmd=input("kb>")
            if cmd.find("load") == 0:
                aFile = cmd.replace("load", "")
                self.loadTxtFile(aFile.strip())
            elif cmd.find("tell") == 0:
                toTell = cmd.replace("tell", "")
                told = self.tell(toTell.strip())
                if told:
                    count+=1
            elif cmd == "infer_all":
                if count > 0:
                    validCmd = self.inferAll(self.kb)
                else:
                    print("Can't infer_all without calling tell")  
            elif cmd == "end":
                break
            else:
                print("Unknown command ", cmd)
        
    # what type of excepts should we expect to deal with?
    def loadTxtFile(self, aName):
        try:
            aFile = open(aName,'r')
            self.kb = aFile.read()
            # pass
        except FileNotFoundError:
            print("File, ", aName, " not found, try again")
        except PermissionError:
            aName.close()
            aFile = open(aName,'r')
            self.kb = aFile.read()
        lines = self.kb.splitlines()
        for i in lines:
            parsed = i.split("<--", 1)
            toInfer = parsed[0].strip()
            variables = parsed[1]
            head = toInfer.split(" ")
            if len(head)!=1 or len(variables.strip())==0:
                print("Error: ", aName, " is not a valid knowledge base")
                break
            variableList = variables.split("&")
            variableList = [x.strip(" ") for x in variableList]
            for i in variableList:
                if not self.is_atom(i):
                    print("Error: ", aName, " is not a valid knowledge base")
                    break
        
    def tell(self, aString):
        names = aString.split()
        if len(aString) == 0 or len(names) == 0:
            print("Error: tell needs at least one atom")
            return False
        for i in names:
            if not self.is_atom(i):
                print("Error: ", i, " is not a valid atom")
                return False
            else:
                if i in self.atoms:
                    print("atom ", i, " already known to be true")
                else:
                    self.atoms.append(i)
                    print(i, "told")
                    return True
    
    def inferAll(self, kb):
        alreadyInferred = copy.deepcopy(self.atoms)
        rules = {}
        inferred = []
        lines = kb.splitlines()
        newInferrences = True
        while newInferrences:
            count = 0
            for i in lines:
                parsed = i.split("<--", 1)
                toInfer = parsed[0].strip()
                variables = parsed[1]
                variableList = variables.split("&")
                variableList = [x.strip(" ") for x in variableList]
                rules[toInfer] = variableList
                result = all(i in self.atoms or i in inferred for i in variableList)
                if result and toInfer not in self.atoms and toInfer not in inferred:
                    print(toInfer, i)
                    inferred.append(toInfer)
                    count+=1
        
            if count == 0:
                newInferrences = False
                    
        print("Newly inferred atoms:")
        print(inferred)
        print("Atoms already known to be true:")
        print(alreadyInferred)
        for i in inferred:
            if i not in self.atoms:
                self.atoms.append(i)
        return True
    
aKB = KB()
aKB.takeCmd()