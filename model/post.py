
class Post(object):
    #def __init__(self, title, href, content, desc=None):
    def __init__(self, path):
        self.path = path
        import os
        assert os.path.isfile(self.path), self.path
        self.src_name = os.path.basename(self.path)
        self.read_file()

    def get_title(self):
        return self.title

    def get_desc(self):
        return self.desc

    def get_content(self):
        return self.content

    def publish_to(self, dest_obj):
        raise RuntimeError("Go through the PageGenerator to get HTML.")
        return dest_obj.publish(self.get_dest_name(), self.html_content())

    def html_content(self):
        c = self.get_content()


    def is_draft(self):
        return 'publish' not in self.headers

    def read_file(self):
        headers = {}
        with open(self.path, 'rb') as src_file:
            content = src_file.read()
            while content.startswith("#!"):
                header, content = content.split("\n", 1)
                header_name, header_value = header[2:].split("=",1)
                headers[header_name] = header_value

        title = headers.get('title', '<Untitled post>')
        desc = headers.get('desc')
        href = self.get_dest_name()
        assert title
        assert href
        self.title = title
        self.href = href
        self.content = content
        self.desc = desc
        self.headers = headers

    def get_src_path(self):
        return self.path

    def get_dest_path(self, dest_dir):
        import os
        return os.path.join(dest_dir, self.get_dest_name())
    def get_dest_name(self):
        name = self.src_name
        if name.endswith(".md"):
            name = name[:-3]
        name = name + ".html"
        return name
             

