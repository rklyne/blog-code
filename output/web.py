
class WebFiles(object):
    def __init__(self, base_dir, web_dir=None):
        if not base_dir.endswith('/'):
            base_dir = base_dir + '/'
        self.base_dir = base_dir
        self.always_replace = False
        assert web_dir, "This really doesn't work unless you provide the (possibly relative) base url the blog will be at"
        web_dir = ""
        self.web_dir = web_dir

    def publish(self, name, content, replace=False):
        import os
        path = os.path.join(self.base_dir, name)
        if not (replace or self.always_replace):
            if os.path.exists(path):
                raise ValueError("file already exists")
        with open(path, 'wb') as f:
            f.write(content)
        link = self.make_link(path)
        return link

    def make_link(self, rel_path):
        assert rel_path.startswith(self.base_dir), rel_path
        web_path = rel_path[len(self.base_dir):]
        if self.web_dir:
            web_path = self.web_dir + '/' + web_path
        return web_path
                
