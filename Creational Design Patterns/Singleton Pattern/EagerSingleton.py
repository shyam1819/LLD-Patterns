# Dummy class to 
class DBConnect:
  def __init__(self):
    pass
  def connect(self):
    print("Connected")

class EagerSingleton:
  __instance = None

  def __init__(self):
    if __instance is not None:
      raise Exception("Instance is not None")
    EagerSingleton.__instance = DBConnect()

  @staticmethod
  def get_instance():
    return EagerSingleton.__instance

if __name__ == "__main__":
  singleton_class = EagerSingleton()
  db_connect = singleton_class.get_instance()
