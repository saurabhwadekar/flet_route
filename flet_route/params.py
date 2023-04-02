

class Params:
    def __init__(self,dic = dict) -> None:
        for i in dic:
            self.__setattr__(str(i),str(dic[i]))

    def get(self,var:str):
        try:
            return self.__getattribute__(var)
        except AttributeError:
            pass
        
    def delete(self,var:str):
        try:
            self.__delattr__(var)
        except AttributeError:
            pass

    def get_all(self):
        return self.__dict__
    
    def __str__(self) -> str:
        show = ""
        dic = self.__dict__
        for key in dic:
            show = show + f"🧥| {key} = {dic[key]}\n"
        if show == "":
            return "--- 🧳 Params Is Emty ---"
        return show[0:-1]
    
