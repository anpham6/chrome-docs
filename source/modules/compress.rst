==============
@e-mc/compress
==============

- **npm** i *@e-mc/compress*

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { CompressLevel } from "./squared";

  import type { IModule, ModuleConstructor } from "./index";
  import type { BufferResult, CompressFormat, TryFileCompressor, TryFileResult, TryImageResult } from "./compress";
  import type { CompressModule, CompressSettings } from "./settings";

  import type { WriteStream } from "fs";
  import type { Readable } from "stream";
  import type { BrotliCompress, Gzip } from "zlib";

  interface ICompress extends IModule {
      module: CompressModule;
      level: Record<string, number>;
      compressors: Record<string, TryFileCompressor>;
      chunkSize?: number;
      init(...args: unknown[]): this;
      register(format: string, callback: TryFileCompressor): void;
      getLevel(value: string, fallback?: number): number | undefined;
      getReadable(file: string | URL | Buffer): Readable;
      createGzip(file: string | Buffer, options?: CompressLevel): Gzip;
      createBrotliCompress(file: string | Buffer, options?: CompressLevel): BrotliCompress;
      createWriteStreamAsGzip(file: string | Buffer, output: string, options?: CompressLevel): WriteStream;
      createWriteStreamAsBrotli(file: string | Buffer, output: string, options?: CompressLevel): WriteStream;
      tryFile(file: string | Buffer, config: CompressFormat, callback?: TryFileResult): Promise<BufferResult>;
      tryFile(file: string | Buffer, output: string, config: CompressFormat, callback?: TryFileResult): Promise<BufferResult>;
      tryImage(file: string, config: CompressFormat, callback?: TryImageResult): Promise<BufferResult>;
      tryImage(file: string | Buffer, output: string, config: CompressFormat, callback?: TryImageResult): Promise<BufferResult>;
      get settings(): CompressSettings;
  }

  interface CompressConstructor extends ModuleConstructor {
      singleton(): ICompress;
      readonly prototype: ICompress;
      new(module?: CompressModule): ICompress;
  }

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
      tinify?: {
          api_key?: string;
          proxy?: string;
      };
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
    plugin: "tinify",
    format: "png", // Optional with extension
    timeout: 60 * 1000, // 1m
    options: {
      apiKey: "**********" // Override settings
    }
  };
  instance.tryImage("/tmp/image.png", "/path/output/compressed.png", options, (err, data) => {
    if (!err) {
      console.log(Buffer.byteLength(data));
    }
  });

References
==========

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/compress.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node
* https://www.npmjs.com/package/@types/node-zopfli