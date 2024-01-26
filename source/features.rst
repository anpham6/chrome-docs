Features
========

Protocols
---------

- HTTP/2
- FTP/SFTP/BitTorrent/Metalink [#]_ (using `aria2 <https://github.com/aria2/aria2/releases>`_)
- Unix domain socket [#]_

Encoding
--------

- Gzip
- Deflate
- Brotli (br)
- Zstandard (zstd) [#]_

.. [#] apt/brew install aria2
.. [#] { socketPath: "/tmp/static0.sock", uri: "file:///path/filename" }
.. [#] npm i zstd-codec