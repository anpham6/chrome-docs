=============
@e-mc/request
=============

Interface
=========

.. highlight:: typescript

.. code-block::
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_
  :emphasize-lines: 36-37,46,62,64,67

  import type { IModule, ModuleConstructor } from "./index";
  import type { HttpAgentSettings, HttpProtocolVersion, HttpRequestClient, InternetProtocolVersion } from "./http";
  import type { ApplyOptions, Aria2Options, FormDataPart, HeadersOnCallback, HostConfig, OpenOptions, PostOptions, ProxySettings, PutOptions, ReadExpectType, RequestInit, StatusOnCallback } from "./request";
  import type { DnsLookupSettings, RequestModule, RequestSettings } from "./settings";

  import type { ClientRequest, OutgoingHttpHeaders } from "node:http";
  import type { LookupFunction } from "node:net";
  import type { Writable } from "node:stream";

  interface IRequest extends IModule {
      module: RequestModule;
      startTime: number;
      acceptEncoding: boolean;
      keepAlive: boolean | null;
      readTimeout: number;
      readExpect: ReadExpectType;
      proxy: ProxySettings | null;
      init(config?: RequestInit): this;
      apply(options: ApplyOptions): this;
      addDns(hostname: string, address: string, timeout: number): void;
      addDns(hostname: string, address: string, family?: string, timeout?: number): void;
      lookupDns(hostname: string): LookupFunction;
      proxyOf(uri: string, localhost?: boolean): ProxySettings | undefined;
      statusOn(name: number | number[], callback: StatusOnCallback): void;
      statusOn(name: number | number[], globUrl: string, callback: StatusOnCallback): void;
      headersOn(name: string | string[], callback: HeadersOnCallback): void;
      headersOn(name: string | string[], globUrl: string, callback: HeadersOnCallback): void;
      headersOf(uri: string): OutgoingHttpHeaders | undefined;
      aria2c(uri: string | URL, pathname: string): Promise<string[]>;
      aria2c(uri: string | URL, options?: Aria2Options): Promise<string[]>;
      json(uri: string | URL, options?: OpenOptions): Promise<object | null>;
      pipe(uri: string | URL, to: Writable, options?: OpenOptions): Promise<null>;
      opts(url: string | URL, options?: OpenOptions): HostConfig;
      open(uri: string | URL, options: OpenOptions): HttpRequestClient;
      head(uri: string | URL, options?: OpenOptions): ClientRequest;
      put(uri: string | URL, data: unknown, options: PutOptions): Promise<Buffer | string | null>;
      put(uri: string | URL, data: unknown, contentType?: string, options?: PutOptions): Promise<Buffer | string | null>;
      post(uri: string | URL, parts: FormDataPart[]): Promise<Buffer | string | null>;
      post(uri: string | URL, form: Record<string, unknown>, parts: FormDataPart[]): Promise<Buffer | string | null>;
      post(uri: string | URL, data: unknown, options: PostOptions): Promise<Buffer | string | null>;
      post(uri: string | URL, data: unknown, contentType?: string, options?: PostOptions): Promise<Buffer | string | null>;
      get(uri: string | URL, options?: OpenOptions): Promise<Buffer | object | string | null>;
      detach(singleton?: boolean): void;
      reset(): void;
      close(): void;
      set adapter(value: unknown);
      set agentTimeout(value);
      get agentTimeout(): number;
      set httpVersion(value);
      get httpVersion(): HttpProtocolVersion | null;
      set ipVersion(value);
      get ipVersion(): InternetProtocolVersion;
      get settings(): RequestSettings;
  }

  interface RequestConstructor extends ModuleConstructor {
      readCACert(value: string, cache?: boolean): string;
      readTLSKey(value: string, cache?: boolean): string;
      readTLSCert(value: string, cache?: boolean): string;
      isCert(value: string): boolean;
      /** @deprecated */
      fromURL(url: URL, value: string): string;
      /** @deprecated */
      fromStatusCode(value: number | string): string;
      defineHttpAgent(options: HttpAgentSettings): void;
      defineDnsLookup(options: DnsLookupSettings, clear?: boolean): void;
      defineHttpAdapter(module: unknown): void;
      getAria2Path(): string;
      readonly prototype: IRequest;
      new(module?: RequestModule): IRequest;
  }

Changelog
=========

.. versionadded:: 0.11.0

  - *IRequest* property setter **adapter** for the local HTTP request implementation as :alt:`IHttpAdapter` was created.
  - *RequestConstructor* static method **defineHttpAdapter** for the global HTTP request implementation as :alt:`IHttpAdapter` was created.

.. deprecated:: 0.11.0
  
  - *RequestConstructor* static methods **fromURL** | **fromStatusCode** were relocated into the utility package.

.. versionadded:: 0.10.3

  - *IRequest* method **put** for HTTP method :target:`PUT` was created.

.. versionchanged:: 0.9.0

  - *RequestInit* property **requestTimeout** was renamed :target:`readTimeout`.

.. versionadded:: 0.8.2

  - *IRequest* method **statusOn** was created.

.. versionadded:: 0.8.1

  - *IRequest* method **headersOn** was created.

Settings
========

.. code-block::
  :caption: `View JSON <https://www.unpkg.com/squared-express/dist/squared.json>`_
  :emphasize-lines: 39

  import type { PermittedDirectories } from "./core";
  import type { SecureConfig } from "./http";
  import type { PurgeComponent } from "./settings";

  import type { LookupAddress } from "dns";
  import type { OutgoingHttpHeaders } from "http";

  interface RequestModule {
      handler: "@e-mc/request";
      timeout?: number | string;
      read_timeout?: number | string;
      agent?: {
          keep_alive?: boolean;
          timeout?: number | string;
      };
      connect?: {
          timeout?: number | string;
          retry_wait?: number | string;
          retry_after?: number | string;
          retry_limit?: number;
          redirect_limit?: number;
      };
      dns?: {
          family?: number;
          expires?: number | string;
          resolve?: Record<string, Partial<LookupAddress>>;
      };
      use?: {
          http_version?: 1 | 2;
          accept_encoding?: boolean;
      };
      proxy?: {
          address?: string;
          port?: number;
          origin?: string;
          username?: string;
          password?: string;
          include?: string[];
          exclude?: string[];
          keep_alive?: boolean;
      };
      headers: Record<string, OutgoingHttpHeaders>;
      certs?: Record<string, SecureConfig<string | string[]>>;
      localhost?: string[];
      protocol?: {
          "http/1.1"?: string[];
          h2c?: string[];
          h2?: string[];
      };
      write_stream?: Record<string, number | string>;
      post_limit?: number | string;
      settings?: {
          broadcast_id?: string | string[];
          time_format?: "readable" | "relative" | "none";
          purge?: PurgeComponent;
      }
  }

  interface DownloadModule {
      expires?: number | string;
      aria2?: {
          bin?: string | false;
          exec?: {
              uid?: number;
              gid?: number;
          };
          update_status?: number | { interval?: number; broadcast_only?: boolean };
          max_concurrent_downloads?: number;
          max_connection_per_server?: number;
          check_integrity?: boolean;
          bt_stop_timeout?: number;
          bt_tracker_connect_timeout?: number;
          bt_tracker_timeout?: number;
          min_split_size?: string;
          disk_cache?: number | string;
          lowest_speed_limit?: number | string;
          always_resume?: boolean;
          file_allocation?: "none" | "prealloc" | "trunc" | "falloc";
          conf_path?: string;
      };
  }

Changelog
---------

.. versionchanged:: 0.11.0

  - *RequestModule* property **proxy.exclude** can be prefixed with "**!**" to negate a subset of glob addresses.

.. versionadded:: 0.10.1

  - *RequestModule* property **proxy.origin** is a combined alias for :target:`address` and :target:`port`.

.. versionadded:: 0.10.0

  - *DownloadModule* property **check_integrity** in :alt:`aria2` for hash validation was implemented.
  - *RequestModule* property **write_stream** for stream size :alt:`(kb)` configuration by host was created.

Example usage
-------------

.. code-block:: javascript

  const Request = require("@e-mc/request");

  const instance = new Request({
    read_timeout: 30,
    connect: {
      timeout: 20, // Seconds
      retry_wait: 1,
      retry_after: 30,
      retry_limit: 3, // Max attempts
      redirect_limit: 10
    },
    use: {
      http_version: 2,
      accept_encoding: true
    },
    dns: {
      family: 4 // ipVersion
    },
    agent: { keep_alive: true }
  });
  request.init({ ipVersion: 6 });

  const options = {
    format: "yaml",
    httpVersion: 1,
    silent: true,
    headers: { "x-goog-user-project": "project-1" }
  };
  instance.get("http://hostname/path/config.yml", options).then(data => {
    console.log(data.property);
  });

References
==========

- https://www.unpkg.com/@e-mc/types/lib/http.d.ts
- https://www.unpkg.com/@e-mc/types/lib/request.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts

* https://www.npmjs.com/package/@types/node