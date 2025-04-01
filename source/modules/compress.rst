==============
@e-mc/compress
==============

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 21-22,29,37

  import type { IModule, ModuleConstructor } from "./index";
  import type { BrotliCompressLevel, BufferResult, CompressFormat, CompressLevel, TryFileCompressor } from "./compress";
  import type { CompressModule, CompressSettings } from "./settings";

  import type { WriteStream } from "node:fs";
  import type { Readable } from "node:stream";
  import type { BrotliCompress, BrotliOptions, Gzip, ZlibOptions } from "node:zlib";

  interface ICompress extends IModule {
      module: CompressModule;
      level: Record<string, number>;
      compressors: Record<string, TryFileCompressor>;
      init(...args: unknown[]): this;
      register(format: string, callback: TryFileCompressor): void;
      getLevel(value: string, fallback?: number): number | undefined;
      getReadable(file: string | URL | Buffer): Readable;
      createGzip(file: string | Buffer, options?: CompressLevel): Gzip;
      createBrotliCompress(file: string | Buffer, options?: BrotliCompressLevel): BrotliCompress;
      createWriteStreamAsGzip(file: string | Buffer, output: string, options?: CompressLevel): WriteStream;
      createWriteStreamAsBrotli(file: string | Buffer, output: string, options?: CompressLevel): WriteStream;
      intoGzipStream(output: string, options?: ZlibOptions): WriteStream;
      intoBrotliStream(output: string, options?: BrotliOptions): WriteStream;
      writeGzip(file: string | Buffer, output: string, options?: CompressLevel): Promise<void>;
      writeBrotli(file: string | Buffer, output: string, options?: CompressLevel): Promise<void>;
      tryFile(file: string | Buffer, options: CompressFormat): Promise<BufferResult>;
      tryFile(file: string | Buffer, output: string, options?: CompressFormat): Promise<BufferResult>;
      tryImage(file: string, options: CompressFormat): Promise<BufferResult>;
      tryImage(file: string | Buffer, output: string, options?: CompressFormat): Promise<BufferResult>;
      hasPermission(type: string, options?: unknown): boolean;
      set chunkSize(value: number | string | undefined): void;
      get chunkSize(): number | undefined;
      get settings(): CompressSettings;
  }

  interface CompressConstructor extends ModuleConstructor {
      singleton(): ICompress;
      asBuffer(data: Buffer | Uint8Array): Buffer;
      readonly prototype: ICompress;
      new(module?: CompressModule): ICompress;
  }

Changelog
=========

.. versionadded:: 0.12.0

  - *ICompress* methods **intoGzipStream** | **intoBrotliStream** were created.
  - *CompressConstructor* method **asBuffer** was created.

.. versionchanged:: 0.12.0

  - *ICompress* methods **tryFile** | **tryImage** enforce read :alt:(file) and write :alt:(output) permissions.
  - ``BREAKING`` :alt:`type` function **PluginCompressor** argument :target:`mimeType` as :alt:`string` was replaced with :target:`metadata` as :alt:`PlainObject`.

.. versionchanged:: 0.10.0

  - *ICompress* property **chunkSize** was converted into a 1KB aligned accessor.

.. versionadded:: 0.9.0

  - *ICompress* methods **writeGzip** | **writeBrotli** were created.

.. versionremoved:: 0.9.0

  - *ICompress* methods **tryFile** | **tryImage** argument :target:`callback` as :alt:`function`.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_

  import type { BrotliOptions, ZlibOptions } from "zlib";
  import type { Options as ZopfliOptions } from "node-zopfli";

  interface CompressModule {
      gzip?: ZlibOptions;
      brotli?: BrotliOptions;
      zopfli?: ZopfliOptions;
      settings?: {
          broadcast_id?: string | string[];
          cache?: boolean;
          cache_expires?: number | string;
          gzip_level?: number;
          brotli_quality?: number;
          zopfli_iterations?: number;
          chunk_size?: number | string;
      };
  }

Changelog
---------

.. versionremoved:: 0.10.0

  - *Tinify* was converted into an optional plugin named **@pi-r/tinify**.

  ::

    interface CompressModule {
        tinify?: {
            api_key?: string;
            proxy?: string;
        };
    }

Example usage
-------------

.. code-block:: javascript

  const Compress = require("@e-mc/compress");

  const instance = new Compress({
    gzip: {
      memLevel: 1,
      windowBits: 16
    },
    tinify: {
      api_key: "**********"
    },
    settings: {
      gzip_level: 9, // Lowest priority
      brotli_quality: 11,
      chunk_size: "16kb" // All compression types
    }
  });
  instance.init();

  const stream = instance.createWriteStreamAsGzip("/tmp/archive.tar", "/path/output/archive.tar.gz", { level: 5, chunkSize: 4 * 1024 }); // Override settings
  stream
    .on("finish", () => console.log("finish"))
    .on("error", err => console.error(err));

  const options = {
    plugin: "@pi-r/tinify",
    format: "png", // Optional with extension
    timeout: 60 * 1000, // 1m
    options: {
      apiKey: "**********" // Override settings
    }
  };
  instance.tryImage("/tmp/image.png", "/path/output/compressed.png", options)
    .then(data => {
      console.log(Buffer.byteLength(data));
    })
    .catch(err => console.error(err));

References
==========

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/compress.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node
* https://www.npmjs.com/package/@types/node-zopfli