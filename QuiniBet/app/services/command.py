from abc import ABC, abstractmethod

class TareaCommand(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, model):
        pass

class Tarea(TareaCommand):
    def __init__(self):
        self.__tareas = []

    def execute(self, model):
        for tarea in self.__tareas:
            tarea.execute(model)

    def add_tarea(self, tarea):
        self.__tareas.append(tarea)
