Youtube Closed Captions
-----------------------

Downloads the closed captions(subtitles) from Youtube videos
============================================================

.. image:: https://github.com/mkly/youtube-closed-captions/actions/workflows/ci.yml/badge.svg
  :target: https://github.com/mkly/youtube-closed-captions/actions/workflows/ci.yml

Requirements
~~~~~~~~~~~~

* Currently requires Python >= 3.12

To Use
~~~~~~

.. code:: python

   from ytcc.download import Download

   video_id = 'jNQXAC9IVRw'
   download = Download()
   # Language is optional and default to "en"
   # YouTube uses "en","fr" not "en-US", "fr-FR"
   captions = download.get_captions(video_id, 'en')

Development
===========

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


