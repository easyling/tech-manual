project = u'Translation Proxy Documentation'
copyright = u'2024'
source_suffix = ['.rst', '.md']		

extensions = ["myst_parser"]
myst_all_links_external = True

htmlhelp_basename = 'easyling-technical-docs'
latex_documents = [
  ('index', 'easyling-tech-manual.tex', u'Translation Proxy Online Documentation',
   u'', 'manual'),
]
version = 'latest'
release = 'latest'

html_theme = 'sphinx_rtd_theme'
