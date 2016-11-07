Youtube Closed Captions
-----------------------

Downloads the closed captions(subtitles) from Youtube videos
============================================================

Requirements
~~~~~~~~~~~~

* Currently requires python >= 3.5 but will likely change to 2.7 soon

To Use
~~~~~~

.. code:: python

   from ytcc.download import Download

   video_id = 'jNQXAC9IVRw'
   download = Download()
   captions = download.get_captions(video_id)


Known Issues
============

This is currently just written for the English(en-US) language as that is what my use case required. Definitely would love to see it support all languages

Development
===========

Run Tests
~~~~~~~~~

*Note:* Functional tests do download directly from Youtube

.. code:: bash

   ## All tests
   python -m unittest discover

   ## Unit tests
   python -m unittest discover test/unit

   ## Functional tests
   python -m unittest discover test/functional

