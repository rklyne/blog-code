class Dataset(object):
    def __init__(self, data_dir):
        self.dir = data_dir
        self.draft_posts = []
        self.posts = []
        self.loaded = False

    def ensure_loaded(self):
        if self.loaded: return
        self.load()

    def load(self):
        import os
        from model import Post
        posts_dir = os.path.join(self.dir, 'posts')
        for name in os.listdir(posts_dir):
            path = os.path.join(posts_dir, name)
            post = Post(path)
            if post.is_draft():
                self.draft_posts.append(post)
            else:
                self.posts.append(post)
        self.loaded = True

    def get_all_posts(self):
        self.ensure_loaded()
        return self.posts


