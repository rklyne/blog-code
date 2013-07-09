
class SiteGenerator(object):
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
  def regenerate(self):
    import os
    from generators import StaticGenerator, BlogGenerator
    blog = BlogGenerator(os.path.join(self.src, 'posts'), os.path.join(self.dest, 'blog'), '/blog/')
    blog.regenerate()
    static = StaticGenerator(os.path.join(self.src, 'static'), self.dest)
    static.regenerate()

  def make_dest_name(self, name):
    if name.endswith(".md"):
      name = name[:-3]
    name = name + ".html"
    return name

