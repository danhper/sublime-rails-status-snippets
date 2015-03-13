template = """<snippet>
  <content><![CDATA[
{status}
]]></content>
  <tabTrigger>s{code}</tabTrigger>
  <scope>source.ruby</scope>
</snippet>"""


def get_codes():
    with open('codes.txt', 'r') as f:
        return f.read().splitlines()


def write_snippets(codes):
    for info in codes:
        code, status = info.split()
        snippet = template.format(code=code, status=status)
        with open("{0}.sublime-snippet".format(status[1:]), 'w') as f:
            f.write(snippet)


def generate_snippets():
    codes = get_codes()
    write_snippets(codes)


if __name__ == '__main__':
    generate_snippets()
