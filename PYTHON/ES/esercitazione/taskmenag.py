class TaskManager:
    def __init__(self):

        self.tasks : dict [str, dict[str,str | bool]] = {}


    def createTask(self,task_id : str , descrizione : str ): 

        if task_id in self.tasks:
            return "errore esiste gia"
        else:
            self.tasks[task_id] = {"descrizione":descrizione ,"completato": False}

            return self.tasks[task_id]
        


    def complete_task(s
    elf, task_id : str ):

        if task_id in self.tasks: 
            self.tasks[task_id]["completato"] = True

            return {task_id : self.tasks[task_id]}
        
        else:
            return "Task non presente!" # alternativa | raise KeyError("chiave non presente")
        

    def update_descr(self,task_id : str , nuova_descrizione : str ) : 

        if task_id not in self.tasks: 
            return "Task non presente"
        
        else:
            self.tasks[task_id]["descrizione"] = nuova_descrizione

        return {task_id : self.tasks[task_id]}
    


    def remove_task(self,task_id : str):

        if task_id not in self.tasks: 
            return "Task non presente"
        
        else:
            value = self.tasks.pop(task_id)

            return {task_id : value}


    def list_tasks(self)->list[str]:    

        keys : list[str] = [key for key in self.tasks.keys()]

        return list(self.tasks.keys())
    

    def get_task(self,task_id : str ): 

        if task_id not in self.tasks: 
            return "Errore : Task non presente"
        
        else:
            return {task_id : self.tasks[task_id]}

