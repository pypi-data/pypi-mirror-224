import os
import pytest
from testbook import testbook

notebook_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'notebooks')

# Parameterized notebook names
notebook_names = ['prune_example_custom_trainloop.ipynb', 
                  'prune_example.ipynb',
                  'quantization_example.ipynb']

# The below notebooks will be tested in femtocrux CI
# This is because we need Docker for femtocrux, which is setup during femtocrux CI

# Skipped Notebooks:
#   'imdb_stream_custom_trainloop.ipynb',
#   'imdb_stream.ipynb',
#   'mnist_dense.ipynb'

@pytest.fixture(scope='module', params=notebook_names)
def tb(request):
    notebook_path = os.path.join(notebook_dir, request.param)
    with testbook(notebook_path, execute=True, timeout=600) as tb:
        yield tb

def test_notebook_runs(tb):
    """ This just runs the notebook. """
    pass
