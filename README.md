
python-markdown-mathjax
=======================

A set of extensions (but really, plugins) for the python [markdown][1]
module that allow for proper integration with LaTeX markup embedded in
the markdown.

`mdx_mathjax.py` The original extension taken from the project of the
same name (but different scope) as this one:
[python-markdown-mathjax][2]. Allows for LaTeX markup enclosed as
`$...$` and `$$...$$` to be found and enclosed within
`<math>...</math>` tags as the markdown is processed, in addition to
coercing the markdown processor to ignore everything inside.

`mdx_eqnmath.py` This plugin does the same as `mdx_mathjax.py` but
does so for LaTeX markup enclosed within
`\begin{equation}...\end{equation}` and `\begin{equation*}...\end{equation*}`.

`mdx_alignmath.py` This plugin does the same as `mdx_mathjax.py` but
does so for LaTeX markup enclosed within
`\begin{aligned}...\end{aligned}` and `\begin{aligned*}...\end{aligned*}`.

## Usage

To use all of the plugins and convert a block of markdown text to
html:

```
:::python
import markdown
md_options = ['mathjax',
              'eqnmath',
              'alignmath']
html = markdown.Markdown(extensions=md_options).convert(markdown)
```

The plugin files can be included in the same directory as the script,
or in the root directory of the web application (e.g., Pyramid, Flask).



[1]: https://pythonhosted.org/Markdown/
[2]: https://github.com/mayoff/python-markdown-mathjax
