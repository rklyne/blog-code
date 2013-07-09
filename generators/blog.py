
class BlogGenerator(object):
    def __init__(self, src, dest, web_dest):
        self.src = src
        self.dest = dest
        self.web_dest = web_dest

    def regenerate(self):
        import os, shutil
        if os.path.isdir(self.dest):
            shutil.rmtree(self.dest)
        os.makedirs(self.dest)

        from generators import PageGenerator
        from model import Dataset
        from output import WebFiles
        items = []
        data = Dataset('data')
        dest = WebFiles(self.dest, self.web_dest)
        for post in data.get_all_posts():
            #src = post.get_src_path()
            #src = os.path.join(self.src, name)
            #link = self.make_dest_name(name)
            dest_name = post.get_dest_name()
            #dest = os.path.join(self.dest, link)
            #raise RuntimeError(name, src, dest)
            #page_gen = PageGenerator(src, dest)
            #link = post.publish_to(dest)
            page_gen = PageGenerator(post)
            html_content = page_gen.get_html()
            link = dest.publish(dest_name, html_content)
            #page_gen.regenerate()
            items.append((post.get_title(), post.get_desc(), link))
        self.generate_index(items)

    def generate_index(self, items):
        import os
        import cStringIO as StringIO
        html = StringIO.StringIO()
        html.write('''<html>
        <head>
        <title>Ronan's blog</title>
        <link rel="stylesheet" href="/css/main.css"></link>
        </head>
        <body>
        <div class="posts">''')
        for name, desc, href in items:
            html.write('<a href="')
            html.write(href)
            html.write('">')
            html.write('<div class="blog-post"><h2>')
            html.write(name)
            html.write('</h2><p>')
            html.write(desc)
            html.write('</p></div></a>')
        html.write('''</div></body></html>''')
        index_file = os.path.join(self.dest, 'index.html')
        with open(index_file, 'wb') as f:
            f.write(html.getvalue())


    def make_dest_name(self, name):
        if name.endswith(".md"):
            name = name[:-3]
        name = name + ".html"
        return name

