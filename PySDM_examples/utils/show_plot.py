import tempfile, os, sys
from IPython.display import FileLink, display
from ipywidgets import HTML, Button
from matplotlib import pyplot
if 'google.colab' in sys.modules:
    from google import colab


def make_link(fig, filename=None):
    outdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')
    if filename is None:
        _, tempfile_path = tempfile.mkstemp(
            dir=outdir,
            suffix='.pdf'
        )
    else:
        tempfile_path = os.path.join(outdir, filename)
    fig.savefig(tempfile_path)
    basename = os.path.basename(tempfile_path)
    if 'google.colab' in sys.modules:
        link = Button(description=basename)
        link.on_click(lambda _:colab.files.download(os.path.join('/content/PySDM/PySDM_examples/utils/output/', basename)))
    else:
        link = HTML()
        filename = str(os.path.join('../utils/output', basename))
        link.value = FileLink(filename)._format_path()
    return link


def show_plot(filename=None):
    link = make_link(pyplot, filename)
    pyplot.show()
    display(link)
