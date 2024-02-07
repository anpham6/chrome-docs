========
Document
========

.. toctree::
  :maxdepth: 2

  interface
  inline
  attributes
  append
  merge
  data
  watch
  broadcast
  plugins/index
  finalize

.. note:: **JSON/YAML** is the preferred way to configure commands due to the limitiations of storing data inline using the ``data-chrome-`` dataset namespace. Any assets inside the configuration file will override any settings either inline or from JavaScript.