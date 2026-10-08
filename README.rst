Youtube Closed Captions
-----------------------

Downloads the closed captions(subtitles) from Youtube videos
============================================================

.. image:: https://github.com/mkly/youtube-closed-captions/actions/workflows/ci.yml/badge.svg
  :target: https://github.com/mkly/youtube-closed-captions/actions/workflows/ci.yml

Requirements
~~~~~~~~~~~~

* Currently requires Python >= 3.12

Install
~~~~~~~

.. code:: bash

   pip install youtube-closed-captions

To Use
~~~~~~

.. code:: python

   from ytcaptions import Download

   video_id = 'jNQXAC9IVRw'
   download = Download()
   # Language is optional and default to "en"
   # YouTube uses "en","fr" not "en-US", "fr-FR"
   captions = download.get_captions(video_id, 'en')

Upgrading to 1.0.0
~~~~~~~~~~~~~~~~~~

The Python package is now ``ytcaptions`` to avoid a conflict with the unrelated
``ytcc`` package. Update ``from ytcc.download import Download`` to
``from ytcaptions import Download``. ``DownloadException`` is also exported
from ``ytcaptions``. Imports from ``ytcaptions.download`` and
``ytcaptions.storage`` remain available. The old ``ytcc`` import is removed.

The PyPI distribution name is ``youtube-closed-captions``, and Python 3.12 or
newer is required.

Development
===========

Install the library and test dependencies from this directory:

.. code:: bash

   pip install -e . -r requirements.txt

Run Tests
~~~~~~~~~

*Note:* Functional tests do download directly from Youtube

.. code:: bash

   ## All tests
   pytest

   ## Or using unittest
   python -m unittest discover

   ## Unit tests
   python -m unittest discover test/unit

   ## Functional tests
   python -m unittest discover test/functional

Prepare a release
~~~~~~~~~~~~~~~~~

Build and validate the release files locally:

.. code:: bash

   pip install build twine
   pytest test/unit
   python -m build
   python -m twine check --strict dist/youtube_closed_captions-1.0.0-py3-none-any.whl dist/youtube_closed_captions-1.0.0.tar.gz

These commands do not upload or publish the package. Live YouTube tests require
network access and are skipped in CI because YouTube blocks datacenter IPs.
