====
Task
====

- https://gulpjs.com/docs/en/getting-started/quick-start
- **npm** i *@pi-r/gulp*

.. note:: *Gulp* is used as the reference implementation for a **Task** module.

Example configuration
=====================

- `CLI <https://github.com/gulpjs/gulp-cli#flags>`_

.. code-block::
  :caption: squared.json
  
  {
    "task": {
      "gulp": {
        "handler": "@pi-r/gulp",
        "settings": {
          "minify": "./gulpfile.js", // Will execute "minify" task
          "users": {
            "username": {
              "minify": "./username/gulpfile.js" // Will override parent "minify"
            }
          },
          "minify-css": {
            "path": "./gulpfile.css.js", // Required
            "tasks": ["lint", "minify"],
            "opts": ["--series", "--continue"] // CLI
          }
        }
      }
    }
  }

.. important:: To use *Gulp* in a user directory requires a global installation. [#]_

::

  {
    "selector": "head > script:nth-of-type(1)",
    "type": "js",
    "tasks": [
      { "handler": "gulp", "task": "minify" },
      { "handler": "gulp", "task": "beautify", "preceding": "true" }, // Execute tasks before transformations
      {
        "handler": "gulp",
        "task": {
          "path": "../gulp/transform.js", // User defined uses file permissions
          "tasks": ["minify"],
          "opts": ["--verify"]
        }
      }
    ]
  }

Example gulpfile.js
===================

Renaming files with *Gulp* is not recommended. It is better to use the **saveAs** or **filename** properties when the asset is part of the HTML page.

.. code-block:: javascript
  :emphasize-lines: 5,7

  const gulp = require("gulp");
  const uglify = require("gulp-uglify");
  
  gulp.task("minify", () => {
    return gulp.src("*")
      .pipe(uglify())
      .pipe(gulp.dest("./"));
  });
  
  gulp.task("default", gulp.series("minify"));

.. caution:: ``src`` :lower:`(temp)` and ``dest`` :lower:`(original)` always read and write to the current directory.

data-chrome-tasks
=================

Tasks can be performed immediately after the asset has been downloaded :lower:`(preceding)` and during finalization.

.. code-block:: html
  :caption: JSON

  <script
    src="/common/util.js"
    data-chrome-tasks='[{ handler: "gulp", task: "minify" }, { handler: "gulp", task: "lint", preceding: "true" }]'>
  </script>

.. code-block:: html
  :caption: handler \: task \: preceding? ...+

  <script src="/common/util.js" data-chrome-tasks="gulp:minify+gulp:lint:true"></script>

.. [#] npm i -g gulp && cd /path/users/username && npm link gulp