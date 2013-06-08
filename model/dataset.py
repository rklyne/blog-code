
class Dataset(object):
  def __init__(self, data_dir):
    self.dir = data_dir
    self.posts = []
    self.loaded = False

  def ensure_loaded(self):
    if self.loaded: return
    self.load()

  def load(self):
    from model import Post
    for name in os.listdir(self.dir):
      path = os.path.join(self.dir, name)
      post = Post.from_file(path)
      self.posts.append(post)
    self.loaded = True

  def get_all_posts(self):
    return self.posts


