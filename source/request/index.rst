=======
Request
=======

- `aria2 <https://aria2.github.io/manual/en/html/README.html>`_
- `rclone <https://rclone.org/overview>`_

.. important:: Program binaries are expected to already be installed on the host system.

.. _request-aria:

aria2
=====

Protocols
---------

- HTTP/S
- FTP
- SFTP
- BitTorrent
- Metalink

Configuation
------------

.. code-block::
  :caption: squared.json [#opt]_

  {
    "download": {
      "aria2": {
        "bin": "",
        "exec": {
          "uid": "",
          "gid": ""
        },
        "update_status": {
          "interval": 0,
          "broadcast_only": false
        },
        "max_concurrent_downloads": 4,
        "max_connection_per_server": 2,
        "check_integrity": false,
        "min_split_size": "",
        "lowest_speed_limit": 0,
        "bt_stop_timeout": 60,
        "bt_tracker_connect_timeout": 30,
        "bt_tracker_timeout": 60,
        "disk_cache": "",
        "always_resume": false,
        "file_allocation": "none",
        "proxy": {
          "http": "",
          "https": "",
          "ftp": "",
          "all": ""
        },
        "no_proxy": "",
        "conf_path": ""
      }
    }
  }

.. tip:: Local user installations are supported. Setting "**bin**" to ``false`` will disable auto-detection by `which <https://www.npmjs.com/package/which>`_.

Example Usage
-------------

- `Options <https://aria2.github.io/manual/en/html/aria2c.html#options>`_

.. code-block:: javascript

  const Request = require("@e-mc/request");

  new Request().aria2c("https://example.com/file.torrent", {
    command: "copyto",
    pathname: "images/",
    shellExpansion: true,
    binOpts: [
      '--conf-path="$HOME/.aria2/aria2.conf"'
    ]
  });

  /* OR */

  {
    "pathname": "images/", // FileManager
    "uri": "magnet:?xt=urn:btih:a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8",
    "uri": "https://example.com/file.torrent",
    "uri": "sftp://example.com/file.metalink",

    /* Optional */
    "shellExpansion": true,
    "binOpts": [
      "--conf-path=\"$HOME/.aria2/aria2.conf\"",
      "--keep-unfinished-download-result"
    ],
    "mimeType": "image/png",
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "silent": true
  }

Unsupported options
-------------------

.. hlist::
  :columns: 3

  * --daemon
  * --input-file
  * --dir
  * --download-result
  * --follow-torrent
  * --follow-metalink
  * --seed-time
  * --max-overall-upload-limit
  * --bt-max-peers
  * --allow-overwrite
  * --dry-run
  * --enable-color
  * --stderr
  * --log

.. _request-rclone:

Rclone
======

- `Install <https://rclone.org/install>`_

Commands
--------

- `copy <https://rclone.org/commands/rclone_copy>`_
- `copyto <https://rclone.org/commands/rclone_copyto>`_
- `copyurl <https://rclone.org/commands/rclone_copyurl>`_

.. code-block::
  :caption: squared.json [#opt]_

  {
    "download": {
      "rclone": {
        "bin": "",
        "exec": {
          "uid": "",
          "gid": ""
        },
        "check_first": false,
        "checksum": false,
        "cutoff_mode": "HARD",
        "ignore_case_sync": false,
        "ignore_checksum": false,
        "ignore_existing": false,
        "ignore_size": false,
        "ignore_times": false,
        "immutable": false,
        "inplace": true,
        "max_backlog": 10000,
        "max_duration": "0s",
        "max_transfer": "off",
        "metadata": false,
        "modify_window": "1ns",
        "multi_thread_chunk_size": "64Mi",
        "multi_thread_cutoff": "256Mi",
        "multi_thread_streams": 4,
        "multi_thread_write_buffer_size": "128Ki",
        "no_check_dest": false,
        "no_traverse": false,
        "no_update_dir_modtime": false,
        "refresh_times": false,
        "size_only": false,
        "update": false,
        "fast_list": false,
        "bind": "",
        "contimeout": "",
        "disable_http2": false,
        "timeout": "",
        "config": ""
      }
    }
  }

Example Usage
-------------

.. highlight:: javascript

.. code-block::
  :caption: copy

  const Request = require("@e-mc/request");

  new Request().rclone("gdrive:Archive", {
    command: "copy", // Optional (default)
    pathname: "/home/user/cloud/Archive",

    /* Optional */
    shellExpansion: true,
    binOpts: [
      '--config="$HOME/.config/rclone/rclone.conf"',
      '--inplace=false'
    ]
  });

.. code-block::
  :caption: copyto

  const Request = require("@e-mc/request");

  new Request().rclone("gdrive:Archive/file.tar.gz", {
    command: "copyto",
    pathname: "/home/user/cloud/Archive/out.tar.gz"
  });

  /* OR */

  {
    "pathname": "/home/user/cloud/Archive", // FileManager
    "filename": "out.tar.gz",
    "uri": "rclone:?gdrive:Archive/file.tar.gz"
  }

.. attention:: The pseudo protocol ``rclone:?`` is required when using :doc:`FileManager <../modules/file-manager>`.

.. code-block::
  :caption: copyurl

  const Request = require("@e-mc/request");

  new Request().rclone("https://example.com/file.tar.gz", {
    command: "copyurl",
    pathname: "/home/user/cloud/Archive/", // Explicit "/" is recommended
    binOpts: [
      "--auto-filename",
      "--contimeout=30s",
      "--disable-http2"
    ]
  });

Unsupported options
-------------------

.. hlist::
  :columns: 3

  * --interactive
  * --dry-run
  * --partial-suffix
  * --verbose
  * --links
  * --delete-excluded
  * --interactive
  * --log-level
  * --use-json-log

.. [#opt] Default options can be overriden by **binOpts**.