==========
@e-mc/use
==========

.. rst-class:: first-center

============= =========
  Component    Version
============= =========
cpu-mem        0.15.0
file-type      0.15.0
form-data      0.15.0
parse-ip       0.15.0
parse-string   0.15.0
============= =========

Interface
=========

.. highlight:: typescript

cpu-mem
-------

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/use/cpu-mem.d.ts>`_

  import type { CpuMemExtras } from ".";

  function initCpuUsage(target?: object | symbol, thread?: boolean): NodeJS.CpuUsage;
  function purgeMemory(): void;
  function send(target: (object | symbol)[], cpuUsage: boolean, memUsage: boolean, extras?: CpuMemExtras): string | undefined;

file-type
---------

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/use/file-type.d.ts>`_

  import type { FileTypeFormat, FileTypeResult } from ".";

  function send(data: FileTypeFormat): Promise<FileTypeResult | undefined>;

form-data
---------

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/use/form-data.d.ts>`_

  import type { FormDataExtras, FormDataResult } from ".";

  import type { PostFileParts } from "@e-mc/types/lib/request";

  function send(form: FormData | null, parts: PostFileParts, extras: FormDataExtras): Promise<FormDataResult>;

parse-ip
--------

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/use/parse-ip.d.ts>`_

  import type { ParseIpExtras } from ".";

  function send(value: string, extras?: ParseIpExtras): string;

parse-string
------------

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/use/parse-string.d.ts>`_

  import type { ParseStringExtras } from ".";

  function send(source: string, extras?: ParseStringExtras): unknown;

References
==========

- https://www.unpkg.com/@e-mc/types/lib/index.d.ts
- https://www.unpkg.com/@e-mc/types/lib/request.d.ts

* https://developer.mozilla.org/en-US/docs/Web/API/FormData