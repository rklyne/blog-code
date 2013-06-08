
class Post(object):
  def __init__(self, title, href, content, desc=None):
    assert title
    assert href
    self.title = title
    self.href = href
    self.content = content
    self.desc = desc


