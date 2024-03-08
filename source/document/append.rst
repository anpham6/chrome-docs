================
Appending source
================

You can **append** or **prepend** a sibling element :lower:`(not child)` to be processed as a typical ``script`` or ``link`` element.

.. code-block:: html

  <html>
  <head>
    <title></title>
    <!-- Google Analytics -->
    <script>
    window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
    ga('create', 'UA-XXXXX-Y', 'auto');
    ga('send', 'pageview');
    </script>
    <script async src='https://www.google-analytics.com/analytics.js'></script>
    <!-- End Google Analytics -->
  </head>
  <body>
  </body>
  </html>

The equivalent command through a configuration file. [#]_

::

  [
    {
      "selector": "title",
      "type": "append/script", // All tags except "html"
      "textContent": "\\nwindow.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;\\nga('create', 'UA-XXXXX-Y', 'auto');\\nga('send', 'pageview');\\n"
    },
    {
      "selector": "title",
      "type": "append/js", // prepend/css
      "download": false, // Explicit "false"
      "attributes": {
        "src": "https://www.google-analytics.com/analytics.js", // CSS: href (required)
        "async": null
      }
    }
  ]

.. _document-append-build-options:

Build Options
=============

useOriginalHtmlPage = false
---------------------------

The current state of the DOM is sent including any updates made with JavaScript. Every element being modified will have an auto-generated locator **UUID**.

useOriginalHtmlPage = true 
--------------------------

Will attempt to parse the page as it stored on file. Dynamic content :alt:`(e.g. php)` that create additional elements are not supported. Scripts which insert elements as the page is loading should be performed after parsing the document. Errors can also occur with ``<p>`` tags when they contain block-level elements. If you are having problems using this option then make sure your page is a valid `HTML5 <https://validator.w3.org>`_ document. As a last resort you can try adding an element "**id**" to directly inject the content.

.. [#] All commands in relation to the base type are supported.