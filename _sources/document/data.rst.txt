============
Data Sources
============

Using the same concept as a database you can read from these files:

- **JSON**
- **YAML**
- JSON5 [#]_
- XML [#]_
- TOML [#]_

Then optionally select nested objects with these :target:`query` expressions:

- `JSONPath <https://github.com/dchester/jsonpath>`_ [#]_
- `JMESPath <https://jmespath.org>`_ [#]_

.. tip:: These examples can also be used with :doc:`Cloud </cloud/interface>` and :doc:`DB </db/interface>` data sources except every provider has a different way to *query* their data.

Interface
=========

.. code-block:: typescript

  import type { DataSource as IDataSource } from "../db/interface";

  interface DataSource extends IDataSource {
      source: "uri" | "local" | "export" | "json";
      type: "text" | "attribute" | "display"; // Element action

      viewEngine?: {
          name: string; // NPM package name
          singleRow?: boolean;
      };
      viewEngine?: string; // settings.view_engine[name]? + settings.users[username].view_engine[name]? (overlay)
      /* OR */
      value?: string | string[] | Record<string, unknown>; // Replace placeholders per row of results
      /* OR */
      template?: string; // Will replace "value" from local file
      /* OR */
      dynamic?: boolean; // Uses element.innerXml rather than element.textContent

      query?: string; // startsWith("$") JSONPath otherwise JMESPath

      ignoreCache?: boolean; // Bypass cache without saving
      ignoreCache?: 1; // purge cache with saving
      ignoreEmpty?: boolean; // Will not modify anything when there are no results
      ignoreCoerce?: boolean; // Will not convert inline constructors to native objects
  }

  interface TextDataSource extends DataSource {
      type: "text";
      leadingText?: string;
      trailingText?: string;
  }

  interface DataObject {
      format: "json" | "yaml" | "json5" | "xml" | "toml";
      options?: PlainObject; // Parser options (yaml + xml)
  }

  interface CascadeAction {
      /*
        When array [{ a: 1 }, { b: 2 }] then "0.a == 1" OR "1.b == 2" (leading only)
        When multi-dimensional array { a: [[1], [2,3]] } then "a[0].0 == 1" OR "a.1.1 == 3" (brackets are optional)
        When key has spaces { " a ": { "b ": { c: 1 } } } then " a "["b "].c OR " a "."b "[c] == 1 (quotes are optional)
        When key has dot operator  { a: { "b.c": 1 } } then a[b\\.c] == 1
        Invalid usage a[0][1][2] instead use a.0.1.0 or a[0].1[2] (max is 1 consequetive bracket)
      */
      cascade?: string; // Called before "query"
      fallback?: object; // Used when there are missing fields
  }

Inline "json"
=============

.. code-block:: typescript

  interface JSONDataSource extends DataSource, CascadeAction {
      source: "json";
      items?: unknown;
  }

Example usage
-------------

::

  {
    "selector": "main",
    "type": "text",
    "dataSource": {
      "source": "json",

      "items": [
        { "title": "1", "description": "first item" },
        { "title": "2", "description": "second item" }
      ],
      "leadingText": "<ul>",
      "value": "<li><b>${title}</b>: ${description}</li>", // <ul><li><b>1</b>: first item</li><li><b>2</b>: second item</li></ul>
      "trailingText": "</ul>",

      "items": { "title": "1", "description": "first item" },
      "value": "<b>${title}</b>: ${description}", // <b>1</b>: first item
      /* OR */
      "items": {},
      "value": "<b>1</b>: first item"
    }
  }

Remote file "uri"
=================

.. code-block:: typescript

  interface UriDataSource extends DataSource, DataObject, CascadeAction {
      source: "uri";
      uri: string; // Will perform a fetch request
      /* Method "POST" */
      body?: unknown; // Required
      contentType?: string;
  }

Example usage
-------------

Reusing configuration templates is possible with URL search parameters. All parameters :lower:`(excluding "value")` from any source can be replaced using the **{{param}}** syntax.

.. code-block::
  :caption: *http://localhost:3000/project/index.html?file=demo&format=json*

  {
    "selector": "main img",
    "type": "attribute",
    "dataSource": {
      "source": "uri",
      "format": "{{format}}", // json
      "uri": "http://hostname/project/{{file}}.{{format}}", // http://hostname/project/demo.json

      "query": "$[1]", // Row #2 in result array (JSONPath)

      /* Result: { "src": "image.png", "other": { "alt": "description" } } */
      "value": {
        "src": "src",
        "alt": "other.alt"
      }
    }
  }

.. caution:: Query parameters will also replace values inside the **attributes** property.

.. code-block::
  :caption: POST

  {
    "selector": "h1",
    "type": "text",
    "dataSource": {
      "source": "uri",
      "uri": "https://hostname/api/v1/items", // Perform secure API request
      "body": {
        "id": "1"
      },
      "format": "json", // Response headers["Accept"] (generated)
      "contentType": "application/json", // Request headers["Content-Type"] (optional)

      "value": "<b>${title}</b>: ${description}"
    }
  }

.. note:: JSON will be sent by default for *POST* when both **format** and **contentType** are empty.

Local file "local"
==================

.. code-block:: typescript

  interface LocalDataSource extends DataSource, DataObject, CascadeAction {
      source: "local";
      pathname: string;
  }

Example usage
-------------

::

  {
    "selector": "main img",
    "type": "attribute",
    "dataSource": {
      "source": "local",
      "format": "xml",

      "pathname": "./path/data.xml", // yaml + json5 + toml + xml + cjs (settings.directory.data + users/username/?)
      /* OR */
      "pathname": "/path/to/data.xml", // Local files require read permissions

      "query": "$.root.row[1]", // Second item in "row" array (JSONPath)

      /* Result: { "title": "Tokyo", "description": "Japan" } */
      "value": "<b>${__index__}. ${title}</b>: ${description}" // "__index__": Row index value
    }
  }

.. code-block::
  :caption: Conditional statement

  {
    "selector": "main div",
    "type": "display",
    "dataSource": {
      "source": "mongodb",
      "uri": "mongodb://localhost:27017",
      "removeEmpty": true, // Includes invalid conditions

      "value": "attr1", // Remove when: null or undefined
      "value": "-attr2", // Remove when: attr2=falsey
      "value": "+attr3", // Remove when: attr3=truthy
      /* OR */
      "value": [
        "attr1", // AND
        ":is(OR)",
        "-attr2", "-attr3", // OR
        ":is(AND)",
        "+attr4" // Remove when: attr1=null + attr2|attr3=falsey + attr4=truthy
      ]
    }
  }

To completely remove an element all *AND* conditions have to be ``true`` and one *OR* per group is ``true``. Using a view engine is recommended if you require a more advanced statement.

Returning an empty result or a blank string :lower:`(view engine)` is ``false``.

External source "export"
========================

Custom functions or packages can be used to return any kind of dataset from any source providing a temporary solution during development.

.. code-block:: typescript

  interface ExportDataSource {
      source: "export";
      params: unknown; // Passed into custom function (required)

      pathname?: string; // Module file (.cjs) | Local file (.js) | inline function | NPM package
      /* OR */
      settings?: string;
      /* OR */
      execute?: (...args: unknown[]) => unknown;

      persist?: boolean; // Default is "true"
  }

Example settings
----------------

.. code-block::
  :caption: squared.json

  {
    "document": {
      "chrome": {
        "handler": "@pi-r/chrome",
        "eval": {
          "function": true // Enable inline functions
        },
        "settings": {
          "export": {
            "data-example": "(params, resolve, require) => { const fs = require('fs'); resolve(JSON.parse(fs.readFileSync(params.uri))); }",
            "async-example": "async (params, require) => { const fs = require('fs'); const result = await fs.promises.readFile(params.uri); return JSON.parse(result); }"
          }
        }
      }
    }
  }

Example file ".cjs"
-------------------

.. code-block:: javascript
  :caption: /path/to/postgres.cjs

  const pg = require("pg");

  const config = {
    host: "localhost",
    user: "**********",
    password: "**********",
    database: "squared",
    port: 5432,
    ssl: true
  };

  module.exports = async function (params) {
    const client = new pg.Client();
    await client.connect();
    const { rows } = await client.query("SELECT * FROM demo WHERE id = $1", [params.id]);
    await client.end();
    return rows;
  };

Example file ".js"
------------------

.. code-block:: javascript
  :caption: /path/to/mysql.js

  function (params, resolve, require) { // async function (params, require)
    const mysql = require("mysql");
    const conn = new mysql.createConnection({
      host: "localhost",
      user: "**********",
      password: "**********",
      database: "squared",
      port: 3306,
      ssl: true
    });
    conn.connect();
    conn.query("SELECT * FROM demo WHERE id = ?", [params.id], (err, result) => {
      if (!err) {
        resolve(result);
      }
      else {
        console.log(err);
        resolve(null);
      }
    });
    conn.end();
  }

.. note:: Using this approach with databases is not recommended.

Example usage
-------------

::

  {
    "selector": "main p",
    "type": "text",
    "dataSource": {
      "source": "export",

      "pathname": "npm:postgres-custom", // npm i postgres-custom
      /* OR */
      "pathname": "./path/to/postgres.cjs", // settings.directory.export + users/username/?
      /* OR */
      "settings": "data-example", // settings.export

      "value": "`<b>${this.title}</b>: ${this.description} (${this.total * 2})`", // Function template literal (settings.eval.function)

      /* golang template syntax - partial support */
      "value": "{{if !expired}}<b>${title}</b>: ${description}{{else}}Expired{{end}}", // Non-nested single conditional truthy property checks
      "value": "{{if not expired}}<b>${title}</b>: ${description}{{else}}Expired{{end}}", // Case sensitive
      "value": "{{if and (user.total) (ge user.total postMin) (lt user.total postMax)}}<b>${title}</b>: ${description}{{else if (eq user.total 0)}}Expired{{end}}"
    }
  }

.. important:: Parenthesis where noted in ``value`` are required.

View Engine
===========

.. code-block:: typescript

  interface ViewEngine {
      name: string; // NPM package name
      singleRow?: boolean; // Template data is sent in one pass using an Array[]
      outputEmpty?: boolean; // Pass empty results to template engine
      options?: {
          compile?: PlainObject; // template = engine.compile(value, options)
          output?: PlainObject; // template({ ...options, ...result[index] })
      };
  }

.. note:: `Template engines <https://js.libhunt.com/libs/templating-engines>`_ with a :code:`compile(string[, options]): (data?: Record<string, any>) => string` method are compatible.

Example usage
-------------

Using ``template`` :lower:`(external)` is the same as ``value`` :lower:`(inline)` except the reusable content is stored inside a cacheable template server directory.

::

  {
    "selector": "main",
    "type": "text",
    "dataSource": {
      "source": "local",
      "format": "json",
      "pathname": "./path/to/data.json",

      "viewEngine": "main-ejs", // settings.view_engine[viewEngine]
      /* OR */
      "viewEngine": {
        "name": "ejs", // NPM package name
        "singleRow": true
      },

      "value": "<b><%= title %></b>: <%= description %>",
      /* OR */
      "template": "./path/to/content.ejs", // settings.directory.template + users/username/?
      /* OR */
      "dynamic": true, // element.innerXml? (with tags)
      "dynamic": false, // element.textContent? (plain text) || outerXml (parsed from source)

      "encoding": "utf-8"
    }
  }

.. hint:: `EJS <https://ejs.co/#docs>`_ [#]_ is used as the reference templating engine.

Event callbacks
===============

You can create named callbacks for **postQuery** and **preRender** anywhere inside the *HTML*. It is more readable than inside a configuration file and can be reused for similiar queries.

.. code-block:: typescript

  interface DataSource {
      postQuery?: string | ((result: unknown[], item: DataSource) => unknown[] | void);
      preRender?: string | ((output: string, item: DataSource) => string | void);
      whenEmpty?: string | ((result: unknown[], item: DataSource) => unknown[] | void);
  }

Example usage
-------------

Only one function can be defined per ``<script type="text/template">`` element.

.. code-block:: html

  <script type="text/template" data-chrome-template="data::postQuery-example">
    async function (result /* PlainObject[] */, dataSource) {
      if (result.length) {
        return await fetch("/db/url", { method: "POST", body: JSON.stringify(result) }).then(data => data.map(item => ({ name: item.key, value: item.value })));
      }
      return null; // "result" will display unmodified when not an array
    }
  </script>

  <script type="text/template" data-chrome-template="data::preRender-example">
    function (value /* string */, dataSource) {
      return value.replaceAll("<", "&lt;");
    }
  </script>

  <script type="text/template" data-chrome-template="data::whenEmpty-example">
    function (result /* PlainObject[] */, dataSource) {
      result[0] = { value: "Empty" }; // result.length is 0
    }
  </script>

.. code-block::
  :caption: Alternate

  {
    "selector": "",
    "type": "data",
    "template": {
      "identifier": "postQuery-example",
      "value": "async function (result, dataSource) {/* Same */}" // Arrow functions not supported
    }
  }

.. warning:: Using ``<script>`` templates requires the setting :code:`eval.template = true`.

Changelog
=========

@pi-r/chrome
------------

.. versionadded:: 0.7.0

  - *DataSource* property **ignoreCoerce** was created.

.. versionadded:: 0.6.4

  - *UriDataSource* property **contentType** | **body** for HTTP method *POST* was implemented.
  - *DataSource* property **source** option "**json**" as *JSONDataSource* was implemented.
  - *TextDataSource* property **leadingText** | **trailingText** were created.

.. [#] npm i json5
.. [#] npm i fast-xml-parser
.. [#] npm i toml
.. [#] npm i jsonpath
.. [#] npm i jmespath
.. [#] npm i ejs