==============
@e-mc/compress
==============

- **npm** i *@e-mc/compress*

Interface
=========

.. code-block:: typescript

  import type { CompressLevel } from "./squared";

  import type { IModule, ModuleConstructor } from "./index";
  import type { BufferResult, CompressFormat, TryFileCompressor, TryFileResult, TryImageResult } from "./compress";   
  import type { CompressModule, CompressSettings } from "./settings";

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

References
==========

* https://www.unpkg.com/@e-mc/types/lib/index.d.ts

- https://www.unpkg.com/@e-mc/types/lib/squared.d.ts
- https://www.unpkg.com/@e-mc/types/lib/compress.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts