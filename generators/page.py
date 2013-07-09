
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

    def read_content(self, content):
        headers = {}
        while content.startswith("#!"):
            header, content = content.split("\n", 1)
            header_name, header_value = header[2:].split("=",1)
            headers[header_name] = header_value
        return headers, content
    def get_title(self):
        return self.name

    def get_desc(self):
        return self.desc

