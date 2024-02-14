===========
@e-mc/types
===========

- **npm** i *@e-mc/types*

Interface
=========

.. code-block:: typescript

  import type { LogArguments } from "./lib/logger";
  import type { CloneObjectOptions } from "./lib/module";

  import type { BinaryLike, CipherGCMTypes, Encoding } from "crypto";
  import type { HighResolutionTime } from "perf_hooks";

  import type { BytesOptions } from "bytes";

  function createAbortError(): Error;
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
  function convertTime(value: HighResolutionTime, format: true): string;
  function convertTime(value: HighResolutionTime, format?: boolean): number;
  function hasGlob(value: string): boolean;
  function escapePattern(value: unknown, lookBehind?: boolean): string;
  function renameExt(value: string, ext: string, when?: string): string;
  function formatSize(value: string): number;
  function formatSize(value: number, options?: BytesOptions): string;
  function convertSize(value: unknown, alignKb?: number, factor?: number): number;
  function cascadeObject(data: object, query: string, fallback?: unknown): unknown;
  function cloneObject(data: unknown, deep: boolean): unknown;
  function cloneObject(data: unknown, deepIgnore: WeakSet<object>): unknown;
  function cloneObject(data: unknown, options?: CloneObjectOptions<unknown>): unknown;
  function coerceObject(data: unknown, cache: boolean): unknown;
  function coerceObject(data: unknown, parseString?: (...args: [string]) => unknown, cache?: boolean): unknown;
  function getEncoding(value: unknown, fallback?: BufferEncoding): BufferEncoding;
  function encryptUTF8(algorithm: CipherGCMTypes, key: BinaryLike, iv: BinaryLike, data: string, encoding?: Encoding): string | undefined;
  function decryptUTF8(algorithm: CipherGCMTypes, key: BinaryLike, iv: BinaryLike, data: string, encoding?: Encoding): string | undefined;
  function generateUUID(): string;
  function incrementUUID(restart?: boolean): string;
  function validateUUID(value: unknown): boolean;
  function randomString(format: string, dictionary?: string): string;
  function errorValue(value: string, hint?: string): Error;
  function errorMessage(title: number | string, value: string, hint?: string): Error;
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
  }

  const IMPORT_MAP: Record<string, string | undefined>;

.. versionadded:: 0.8.4

  Method **convertSize** was created.

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/logger.d.ts
- https://www.unpkg.com/@e-mc/types/lib/module.d.ts

* https://www.npmjs.com/package/@types/bytes