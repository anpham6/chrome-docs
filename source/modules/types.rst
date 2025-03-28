===========
@e-mc/types
===========

Interface
=========

.. code-block:: typescript
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/index.d.ts>`_
  :emphasize-lines: 32-33,35,57,185

  import type { LogArguments } from "./lib/logger";

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
  function getTempDir(): string;
  function isArray(value: unknown): value is unknown[];
  function isObject(value: unknown): value is object;
  function isPlainObject(value: unknown): value is Record<string | number | symbol, unknown>;
  function isString(value: unknown): value is string;
  function isEmpty(value: unknown): boolean;
  function asFunction(value: unknown, sync?: boolean): ((...args: unknown[]) => Promise<unknown> | unknown) | null;
  function parseTime(value: number | string, start?: number): number;
  function parseExpires(value: number | string, start?: number): number;
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
  function cloneObject(data: unknown, deepIgnore: WeakSet<object>): unknown;
  function cloneObject(data: unknown, options?: CloneObjectOptions<unknown>): unknown;
  function coerceObject(data: unknown, cache: boolean): unknown;
  function coerceObject(data: unknown, parseString?: (...args: [string]) => unknown, cache?: boolean): unknown;
  function getEncoding(value: unknown, fallback?: BufferEncoding): BufferEncoding;
  function encryptUTF8(algorithm: CipherGCMTypes, key: BinaryLike, iv: BinaryLike, data: string, encoding?: Encoding): string | undefined;
  function decryptUTF8(algorithm: CipherGCMTypes, key: BinaryLike, iv: BinaryLike, data: string, encoding?: Encoding): string | undefined;
  function hashKey(data: BinaryLike, algorithm?: string, encoding?: BinaryToTextEncoding): string;
  /** @deprecated - crypto.randomUUID */
  function generateUUID(options?: RandomUUIDOptions): string;
  function incrementUUID(restart?: boolean): string;
  function validateUUID(value: unknown): boolean;
  function randomString(format: string, dictionary?: string): string;
  function errorValue(value: string, hint?: string): Error;
  function errorMessage(title: number | string, value: string, hint?: string): Error;
  function supported(major: number, minor: number, lts: boolean): boolean;
  function supported(major: number, minor?: number, patch?: number, lts?: boolean): boolean;
  function importESM<T = unknown>(name: string, fromPath?: boolean): Promise<T>;
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

.. versionadded:: 0.11.2

  - :alt:`interface` **THRESHOLD** property **LOGGER_METER_INCREMENT** was created.

.. versionchanged:: 0.11.1

  - ``BREAKING`` Method **escapePattern** argument :target:`lookBehind` was replaced with :target:`symbols`.
  - Method **supported** argument :target:`lts` as :alt:`boolean` can be used in place of :target:`patch`.

.. versionchanged:: 0.11.0

  - :alt:`type` **HighResolutionTime** in :alt:`object` with :target:`bigint` primitive was implemented.

.. versionremoved:: 0.11.0

  - :alt:`interface` **AsSourceFileOptions** property **persist** in :alt:`document` was not used.

.. deprecated:: 0.10.2

  - :alt:`type` **TupleOf** as a shorter alias does not convey explicit intent.
  - :alt:`interface` **OpenOptions** property **follow_redirect** in :alt:`request` was renamed :target:`followRedirect`.

.. versionadded:: 0.10.0
  
  - Method **hashKey** for single-pass encoding was created.
  - Method **supported** for NodeJS versioning from :target:`module` were imported.
  - Method **importESM** for dynamic module loading was created.

.. versionchanged:: 0.10.0

  - Method **createAbortError** uses built-in *DOMException* :alt:`(NodeJS 17)` with name "**AbortError**" and code **20**.
  - Method **formatTime** with argument :target:`char` as "**:**" displays using digital clock format.

.. versionremoved:: 0.10.0

  - :alt:`interface` **CloneObjectOptions** in :alt:`module` was relocated to :target:`types`.
  - :alt:`interface` **AsHashOptions** property **minLength** in :alt:`module` was deleted.
  - :alt:`type` **Writeable** was renamed :target:`Writable`.
  - :alt:`interface` **GetTempDirOptions** in :alt:`module` was renamed :target:`TempDirOptions`.
  - :alt:`type` **NormalizeFlags** in :alt:`module` was removed.
  - :alt:`export` definitions in :alt:`squared` were deleted:

    .. hlist::
      :columns: 4

      - FinalizedElement
      - ConditionProperty
      - CssConditionData
      - ControllerSettingsDirectoryUI

.. deprecated:: 0.9.2

  - Method **generateUUID** is a reference to :target:`crypto.randomUUID`.
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

  - Method **alignSize** was created.

References
==========

- https://www.unpkg.com/@e-mc/types/index.d.ts
- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/module.d.ts

* https://www.npmjs.com/package/@types/bytes