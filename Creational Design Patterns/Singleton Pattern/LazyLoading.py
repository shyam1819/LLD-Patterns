class DBConnect:
  def __init__(self):
    pass
  def connect(self):
    print("Connected")

class LazyLoading:
  __instance = None

  def __init__(self):
    if LazyLoading.__instance is not None:
      raise Exception("Instance is not None")
    LazyLoading.__instance = DBConnect()

  @staticmethod
  def get_instance():
    if LazyLoading.__instance  is None:
      LazyLoading()
    return LazyLoading.__instance

if __name__ == "__main__":
  db_connect = LazyLoading.get_instance()
  db_connect.connect()
