
class StaticGenerator(object):
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
  def regenerate(self):
    import os
    for name in os.listdir(self.src):
      if name.endswith('.swp'): continue
      import shutil
      src = os.path.join(self.src, name)
      dest = os.path.join(self.dest, name)
      if os.path.isdir(dest):
        shutil.rmtree(dest)
      if os.path.isfile(src):
        shutil.copyfile(src, dest)
      else:
        shutil.copytree(src, dest)


