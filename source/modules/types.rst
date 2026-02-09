===========
@e-mc/types
===========

Interface
=========

.. code-block:: typescript
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/index.d.ts>`_
  :emphasize-lines: 49,69

  import type { LogArguments } from "./lib/logger";
  import type { ErrorCode, HighResolutionTime } from "./lib/node";

  import type { BinaryLike, BinaryToTextEncoding, CipherGCMTypes, Encoding, RandomUUIDOptions } from "node:crypto";
  import type { BytesOptions } from "bytes";

  function createAbortError(reject: true): Promise<never>;
  function createAbortError(): DOMException;
  function hasBit(value: unknown, flags: number): boolean;
  function ignoreFlag(value: unknown): boolean;
  function cloneFlag(value: unknown): boolean;
  function usingFlag(value: unknown): boolean;
  function watchFlag(value: unknown): boolean;
  function modifiedFlag(value: unknown): boolean;
  function processFlag(value: unknown): boolean;
  function mainFlag(value: unknown): boolean;
  function existsFlag(value: unknown): boolean;
  function getLogCurrent(): LogArguments | null;
  function setLogCurrent(value: LogArguments): void;
  function setTempDir(value: string): boolean;
  function getTempDir(create: true, prefix?: string): string;
  function getTempDir(...values: string[]): string;
  function isArray(value: unknown): value is unknown[];
  function isObject(value: unknown): value is object;
  function isPlainObject(value: unknown): value is Record<string | number | symbol, unknown>;
  function isString(value: unknown): value is string;
  function isEmpty(value: unknown): boolean;
  function isErrorCode(err: unknown, ...code: unknown[]): err is Required<ErrorCode>;
  function asFunction(value: unknown, sync?: boolean): ((...args: unknown[]) => Promise<unknown> | unknown) | null;
  function parseTime(value: number | string, epoch: true): number;
  function parseTime(value: number | string, negative: false): number;
  function parseTime(value: number | string, start?: number): number;
  function parseExpires(value: number | string, epoch: true): number;
  function parseExpires(value: number | string, start?: number | boolean): number;
  function formatTime(value: number, char: string): string;
  function formatTime(value: number, elapsed?: boolean, char?: string): string;
  function convertTime(value: number | string): number;
  function convertTime(value: HighResolutionTime, format: true): string;
  function convertTime(value: HighResolutionTime, format?: boolean): number;
  function hasGlob(value: string): boolean;
  function escapePattern(value: unknown, symbols?: boolean): string;
  function renameExt(value: string, ext: string, when?: string): string;
  function formatSize(value: string): number;
  function formatSize(value: number, options?: BytesOptions): string;
  function alignSize(value: unknown, kb?: number, factor?: number): number;
  function cascadeObject(data: object, query: string, fallback?: unknown): unknown;
  function cloneObject(data: unknown, deep: boolean): unknown;
  /** @deprecated WeakMap<object> */
  function cloneObject(data: unknown, deepIgnore: WeakSet<object> | WeakMap<object, object>): unknown;
  function cloneObject(data: unknown, options?: CloneObjectOptions<unknown>): unknown;
  function coerceObject(data: unknown, cache: boolean): unknown;
  function coerceObject(data: unknown, parseString?: (...args: [string]) => unknown, cache?: boolean): unknown;
  function getEncoding(value: unknown, fallback?: BufferEncoding): BufferEncoding;
  function encryptUTF8(algorithm: CipherGCMTypes, key: BinaryLike, iv: BinaryLike, data: string, encoding?: Encoding): string | undefined;
  function decryptUTF8(algorithm: CipherGCMTypes, key: BinaryLike, iv: BinaryLike, data: string, encoding?: Encoding): string | undefined;
  function hashKey(data: BinaryLike, algorithm?: string, encoding?: BinaryToTextEncoding): string;
  function incrementUUID(restart?: boolean): string;
  function validateUUID(value: unknown): boolean;
  function sanitizeCmd(value: string, ...args: unknown[]): string;
  function sanitizeArgs(value: string, doubleQuote?: boolean): string;
  function sanitizeArgs(values: string[], doubleQuote?: boolean): string[];
  function randomString(format: string, dictionary?: string): string;
  function errorValue(value: string, hint?: string): Error;
  function errorMessage(title: number | string, value: string, hint?: string): Error;
  function supported(major: number, minor: number, lts: boolean): boolean;
  function supported(major: number, minor?: number, patch?: number, lts?: boolean): boolean;
  function importESM(name: string | URL, isDefault: boolean, fromPath?: boolean): Promise<unknown>;
  function importESM(name: string | URL, options?: ImportAttributes, fromPath?: boolean): Promise<unknown>;
  function requireESM(name: string, url?: string | URL, expect?: string): unknown;
  function purgeMemory(percent?: number): number;

  interface LOG_TYPE {
      UNKNOWN: 0;
      SYSTEM: 1;
      NODE: 2;
      PROCESS: 4;
      COMPRESS: 8;
      WATCH: 16;
      FILE: 32;
      CLOUD: 64;
      TIME_ELAPSED: 128;
      TIME_PROCESS: 256;
      FAIL: 512;
      HTTP: 1024;
      IMAGE: 2048;
      EXEC: 4096;
      PERMISSION: 8192;
      TIMEOUT: 16384;
      STDOUT: 32768;
      DB: 65536;
  }

  interface LOG_STATE {
      STDIN: 0;
      STDOUT: 1;
      STDERR: 2;
  }

  interface STATUS_TYPE {
      UNKNOWN: 0;
      FATAL: 1;
      ERROR: 2;
      WARN: 3;
      INFO: 4;
      DEBUG: 5;
      ASSERT: 6;
      TRACE: 7;
  }

  interface ASSET_FLAG {
      NONE: 0;
      IGNORE: 1;
      CLONE: 2;
      USING: 4;
      WATCH: 8;
      MODIFIED: 16;
      PROCESS: 32;
      MAIN: 64;
      EXISTS: 128;
  }

  interface FILE_TYPE {
      UNKNOWN: 0;
      ASSET: 1;
      TRANSFORM: 2;
      COMPRESSED: 4;
      SOURCEMAP: 8;
      TORRENT: 16;
  }

  interface ACTION_FLAG {
      NONE: 0;
      IGNORE: 1;
  }

  interface ERR_CODE {
      MODULE_NOT_FOUND: "MODULE_NOT_FOUND";
      ERR_MODULE_NOT_FOUND: "ERR_MODULE_NOT_FOUND";
  }

  interface DOWNLOAD_TYPE {
      HTTP: 0;
      DISK: 1;
      CACHE: 2;
  }

  interface FETCH_TYPE {
      UNKNOWN: 0;
      HTTP: 1;
      TORRENT: 2;
      FTP: 3;
      UNIX_SOCKET: 4;
  }

  interface DB_TYPE {
      SQL: 1;
      NOSQL: 2;
      DOCUMENT: 4;
      KEYVALUE: 8;
  }

  interface DB_TRANSACTION {
      ACTIVE: 1;
      PARTIAL: 2;
      COMMIT: 4;
      TERMINATE: 8;
      ABORT: 16;
      FAIL: 32;
      AUTH: 64;
      CACHE: 128;
  }

  interface TRANSFER_TYPE {
      DISK: 1;
      STREAM: 2;
      CHUNK: 4;
  }

  interface WATCH_EVENT {
      MODIFIED: "modified";
      BROADCAST: "broadcast";
      CLOSE: "close";
      ERROR: "error";
  }

  interface READDIR_SORT {
      FILE: number;
      DIRECTORY: number;
      DESCENDING: number;
  }

  interface THRESHOLD {
      FILEMANAGER_INTERVAL: number;
      WATCH_INTERVAL: number;
      WATCH_CHANGE: number;
      LOGGER_METER_INCREMENT: number;
  }

  const IMPORT_MAP: StringMap;

Changelog
=========

.. versionadded:: 0.13.9

  - :alt:`function` **requireESM** for extracting a default export was created.

.. note:: Backported: 0.12.16

.. versionchanged:: 0.13.4

  - ``BREAKING`` :alt:`function` **cloneObject** uses a :target:`WeakMap<object, object>` for reference tracking and does not contain any references from the source object.

.. note:: Backported: 0.12.11

.. versionadded:: 0.13.0

  - :alt:`function` **isErrorCode** for checking *Error* properties was imported from :doc:`module`.

.. versionchanged:: 0.13.0

  - :alt:`function` **parseTime** argument :target:`epoch` as :alt:`true` for starting the interval from Unix or Epoch time.
  - :alt:`function` **parseTime** argument :target:`negative` as :alt:`false` for including plus and minus operators.
  - :alt:`function` **parseExpires** argument :target:`epoch` as :alt:`true` for starting the interval from Unix or Epoch time.

.. versionchanged:: 0.12.5

  - :alt:`function` **importESM** argument :target:`options` as :alt:`ImportAttributes` was implemented.

.. versionchanged:: 0.12.4

  - :alt:`function` **getTempDir** argument :target:`create` as :alt:`boolean` using **fs.mkdtemp** was implemented.

.. versionchanged:: 0.12.2

  - :alt:`function` **sanitizeCmd** optionally concatenates arguments without altering the supplied values.

.. versionadded:: 0.12.0

  - :alt:`function` **sanitizeCmd** | **sanitizeArgs** for escaping shell characters were imported from :doc:`module`.
  - :alt:`interface` **CloneObjectOptions** property **structured** for using the native :target:`structuredClone` was implemented.

.. versionchanged:: 0.12.0

  - :alt:`function` **getTempDir** optionally concatenates path segments :alt:`(path.join)` without creating any directories.

.. deprecated:: 0.12.0

  - :alt:`global` types in :target:`object` were relocated:

    .. hlist::
      :columns: 2

      - lib/image: **Point** | **Dimension**
      - lib/http: **AuthValue**
      - lib/node: **ErrorCode** | **HighResolutionTime**
      - lib/settings: **MinMax**
      - lib/squared: **KeyValue**

.. versionremoved:: 0.12.0

  - :alt:`function` **generateUUID** was an alias for :target:`crypto.randomUUID`.
  - :alt:`global` types in :target:`types`:

    .. hlist::
      :columns: 4

      - **Undef**
      - **Null**
      - **NumString**
      - **TupleOf**

.. versionchanged:: 0.11.7

  - ``BREAKING`` Method **decryptUTF8** did not consistently reproduce data output from **encryptUTF8**.

.. versionadded:: 0.11.2

  - :alt:`interface` **THRESHOLD** property **LOGGER_METER_INCREMENT** was created.

.. versionchanged:: 0.11.1

  - ``BREAKING`` :alt:`function` **escapePattern** optional argument :target:`lookBehind` was replaced with :target:`symbols` as :alt:`boolean`:

    .. hlist::
      :columns: 4

      - \\x26 &
      - \\x21 !
      - \\x23 #
      - \\x25 %
      - \\x2c ,
      - \\x3a :
      - \\x3b ;
      - \\x3c <
      - \\x3d =
      - \\x3e >
      - \\x40 @
      - \\x60 \`
      - \\x7e ~
      - \\x22 " :alt:`(0.13.8)`

  - :alt:`function` **supported** argument :target:`lts` as :alt:`boolean` can be used as the :target:`patch` argument.

.. versionchanged:: 0.11.0

  - :alt:`type` **HighResolutionTime** in :alt:`object` with :target:`bigint` primitive was implemented.

.. versionremoved:: 0.11.0

  - :alt:`interface` **AsSourceFileOptions** property **persist** in :alt:`document` was never implemented.

.. deprecated:: 0.10.2

  - :alt:`type` **TupleOf** as a shorter alias does not convey explicit intent.
  - :alt:`interface` **OpenOptions** property **follow_redirect** in :alt:`request` was renamed :target:`followRedirect`.

.. versionadded:: 0.10.0

  - :alt:`function` **hashKey** for single-pass encoding was created.
  - :alt:`function` **supported** for NodeJS versioning was imported from :doc:`module`.
  - :alt:`function` **importESM** for dynamic module loading was created.

.. versionchanged:: 0.10.0

  - :alt:`function` **createAbortError** uses built-in *DOMException* :alt:`(NodeJS 17)` with name "**AbortError**" and code **20**.
  - :alt:`function` **formatTime** with argument :target:`char` as "**:**" displays using digital clock format.
  - :alt:`interface` **CloneObjectOptions** in :alt:`module` was relocated to :target:`types`.
  - :alt:`type` **Writeable** was renamed :target:`Writable`.
  - :alt:`interface` **GetTempDirOptions** in :alt:`module` was renamed :target:`TempDirOptions`.

.. versionremoved:: 0.10.0

  - :alt:`interface` **AsHashOptions** property **minLength** in :alt:`module`.
  - :alt:`type` **NormalizeFlags** in :alt:`module`.
  - :alt:`export` definitions in :alt:`squared`:

    .. hlist::
      :columns: 4

      - FinalizedElement
      - ConditionProperty
      - CssConditionData
      - ControllerSettingsDirectoryUI

.. deprecated:: 0.9.2

  - :alt:`function` **generateUUID** is a reference to :target:`crypto.randomUUID`.
  - :alt:`type` **NumString** as a union is not a standard convention.

.. versionadded:: 0.9.0

  - :alt:`enum` **LOG_STATE** for queuing console output was created.

.. versionchanged:: 0.9.0

  - :alt:`type` **StringOfArray** was renamed :target:`ArrayOf<string>`.
  - :alt:`type` **BufferContent** was renamed :target:`Bufferable`.
  - :alt:`interface` **PoolConfig** in :alt:`db` was relocated to :target:`settings`.
  - :alt:`interface` **LoggerFormat** in :alt:`logger` was relocated to :target:`settings`.
  - :alt:`interface` **AddEventListenerOptions** in :alt:`dom` was relocated to :target:`core`.

.. versionadded:: 0.8.4

  - :alt:`function` **alignSize** was created.

References
==========

- https://www.unpkg.com/@e-mc/types/index.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/module.d.ts

* https://developer.mozilla.org/en-US/docs/Web/API/DOMException
* https://www.npmjs.com/package/@types/bytes