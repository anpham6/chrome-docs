========
Features
========

Protocols
=========

- HTTP/2
- FTP/SFTP/BitTorrent/Metalink [#aria]_
- Unix domain socket [#]_

Download Manager
================

- `aria2 <https://aria2.github.io>`_ [#aria]_
- `rclone <https://rclone.org>`__ [#rclone]_

Encoding
========

- Gzip
- Deflate
- Brotli :alt:`(br)`
- Zstandard :alt:`(zstd)` [#]_

.. [#aria] apt/brew install aria2
.. [#rclone] apt/brew install rclone
.. [#] { socketPath: "/tmp/static0.sock", uri: "file:///path/filename" }
.. [#] npm i zstd-codec (until NodeJS 23.8.0)