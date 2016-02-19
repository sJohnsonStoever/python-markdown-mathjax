

import markdown

class EqnMathPattern(markdown.inlinepatterns.Pattern):

    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(self, r'(\\begin\{equation.*\})(.+?)(\\end\{equation.*\})')

    def handleMatch(self, m):
        node = markdown.util.etree.Element('mathjax')
        node.text = markdown.util.AtomicString(m.group(2) + m.group(3) + m.group(4))
        return node

class EqnMathExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching because \ is pretty important in LaTeX
        md.inlinePatterns.add('eqnmath', EqnMathPattern(), '<escape')

def makeExtension(**kwargs):
    return EqnMathExtension(**kwargs)

