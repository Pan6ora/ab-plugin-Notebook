# Configuration file for jupyter-notebook.

c = get_config()  # noqa

#------------------------------------------------------------------------------
# NotebookApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Reload the webapp when changes are made to any Python src files.
#  Default: False
# c.NotebookApp.autoreload = False

## Whether to enable MathJax for typesetting math/TeX
#  
#          MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
#          very large, so you may want to disable it if you have a slow internet
#          connection, or for offline use of the notebook.
#  
#          When disabled, equations etc. will appear as their untransformed TeX
#  source.
#  Default: True
# c.NotebookApp.enable_mathjax = True

## extra paths to look for Javascript notebook extensions
#  Default: []
# c.NotebookApp.extra_nbextensions_path = []

## Extra paths to search for serving static files.
#  
#          This allows adding javascript/css to be available from the notebook server machine,
#          or overriding individual files in the IPython
# Default: []
#c.NotebookApp.extra_static_paths = [""]

## Extra paths to search for serving jinja templates.
#  
#          Can be used to override templates from notebook.templates.
#  Default: []
# c.NotebookApp.extra_template_paths = []

## Supply extra arguments that will be passed to Jinja environment.
#  Default: {}
# c.NotebookApp.jinja_environment_options = {}

## Extra variables to supply to jinja templates when rendering.
#  Default: {}
# c.NotebookApp.jinja_template_vars = {}

## The MathJax.js configuration file that is to be used.
#  Default: 'TeX-AMS-MML_HTMLorMML-full,Safe'
# c.NotebookApp.mathjax_config = 'TeX-AMS-MML_HTMLorMML-full,Safe'

## A custom url for MathJax.js.
#          Should be in the form of a case-sensitive url to MathJax,
#          for example:  /static/components/MathJax/MathJax.js
#  Default: ''
# c.NotebookApp.mathjax_url = ''

## Dict of Python modules to load as notebook server extensions. Entry values can
#  be used to enable and disable the loading of the extensions. The extensions
#  will be loaded in alphabetical order.
#  Default: {}
# c.NotebookApp.nbserver_extensions = {}

## The directory to use for notebooks and kernels.
#  Default: ''
# c.NotebookApp.notebook_dir = ''

## Whether to open in a browser after starting.
#                          The specific browser used is platform dependent and
#                          determined by the python standard library `webbrowser`
#                          module, unless it is overridden using the --browser
#                          (NotebookApp.browser) configuration option.
#  Default: True
c.NotebookApp.open_browser = False

## The port the notebook server will listen on (env: JUPYTER_PORT).
#  Default: 8888
c.NotebookApp.port = 9000

## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
#  Default: 'disabled'
# c.NotebookApp.pylab = 'disabled'

## If True, display a button in the dashboard to quit
#          (shutdown the notebook server).
#  Default: True
#c.NotebookApp.quit_button = False

## Token used for authenticating first-time connections to the server.
#  
#          The token can be read from the file referenced by JUPYTER_TOKEN_FILE or set directly
#          with the JUPYTER_TOKEN environment variable.
#  
#          When no password is enabled,
#          the default is to generate a new, random token.
#  
#          Setting to an empty string disables authentication altogether, which
#  is NOT RECOMMENDED.
#  Default: '<generated>'
c.NotebookApp.token = ""

## Specify Where to open the notebook on startup. This is the
#          `new` argument passed to the standard library method `webbrowser.open`.
#          The behaviour is not guaranteed, but depends on browser support. Valid
#          values are:
#  
#           - 2 opens a new tab,
#           - 1 opens a new window,
#           - 0 opens in an existing window.
#  
#          See the `webbrowser.open` documentation for details.
#  Default: 2
c.NotebookApp.webbrowser_open_new = 1