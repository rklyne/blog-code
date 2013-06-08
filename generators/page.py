
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

class PageGenerator(object):
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
  def regenerate(self):
    import markdown
    with open(self.src, 'rb') as src_file:
      with open(self.dest, 'wb') as dest_file:
        headers, content = self.read_content(src_file.read())
	self.headers = headers
	self.name = headers.get('name', '(untitled)')
	self.desc = headers.get('desc', '')
        dest_file.write(HEADER)
        dest_file.write(markdown.markdown(content))
        dest_file.write(FOOTER)

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

