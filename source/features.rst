========
Features
========

Protocols
=========

- HTTP/2
- FTP/SFTP/BitTorrent/Metalink
- Unix domain socket [#]_

Download Manager
================

- :ref:`aria2 <request-aria>` [#]_
- :ref:`rclone <request-rclone>` [#]_

Encoding
========

- Gzip
- Deflate
- Brotli :alt:`(br)`
- Zstandard :alt:`(zstd)` [#]_

.. [#] { socketPath: "/tmp/static0.sock", uri: "file:///path/filename" }
.. [#] apt install aria2 | pacman -S aria2
.. [#] apt install rclone | pacman -S rclone
.. [#] npm i zstd-codec (until NodeJS 22.15)