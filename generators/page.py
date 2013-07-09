
class PageGenerator(object):

    HEADER = """
    <html>
    <head>
    <title>Ronan's blog</title>
    <link rel="stylesheet" href="/css/main.css"></link>
    </head>
    <body>
    """
    FOOTER = """
    </body>
    </html>
    """
    def __init__(self, post):
        self.post = post
       
    def get_html(self):
        import markdown
        import cStringIO as StringIO
        out = StringIO.StringIO()
        post = self.post
        content = post.get_content()
        out.write(self.HEADER)
        out.write(markdown.markdown(content))
        out.write(self.FOOTER)
        return out.getvalue()

    def get_title(self):
        return self.name

    def get_desc(self):
        return self.desc

