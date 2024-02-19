=============
@e-mc/request
=============

- **npm** i *@e-mc/request*

Interface
=========

.. code-block:: typescript
  :caption: `View Source <https://www.unpkg.com/@e-mc/types/lib/index.d.ts>`_

  import type { IModule, ModuleConstructor } from "./index";
  import type { HttpAgentSettings, HttpProtocolVersion, HttpRequestClient, InternetProtocolVersion } from "./http";
  import type { ApplyOptions, Aria2Options, FormDataPart, HeadersOnCallback, HostConfig, OpenOptions, PostOptions, ProxySettings, ReadExpectType, RequestInit, StatusOnCallback } from "./request";
  import type { DnsLookupSettings, RequestModule, RequestSettings } from "./settings";

  import type { Writable } from "stream";
  import type { LookupFunction } from "net";
  import type { ClientRequest, OutgoingHttpHeaders } from "http";

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
      addDns(hostname: string, address: string, family?: string | number, timeout?: number): void;
      lookupDns(hostname: string): LookupFunction;
      proxyOf(uri: string, localhost?: boolean): ProxySettings | undefined;
      statusOn(name: number | number[], callback: StatusOnCallback): void;
      statusOn(name: number | number[], patternUrl: string, callback: StatusOnCallback): void;
      headersOn(name: string | string[], callback: HeadersOnCallback): void;
      headersOn(name: string | string[], patternUrl: string, callback: HeadersOnCallback): void;
      headersOf(uri: string): OutgoingHttpHeaders | undefined;
      aria2c(uri: string | URL, pathname: string): Promise<string[]>;
      aria2c(uri: string | URL, options?: Aria2Options): Promise<string[]>;
      json(uri: string | URL, options?: OpenOptions): Promise<object | null>;
      pipe(uri: string | URL, to: Writable, options?: OpenOptions): Promise<null>;
      opts(url: string | URL, options?: OpenOptions): HostConfig;
      open(uri: string | URL, options: OpenOptions): HttpRequestClient;
      head(uri: string | URL, options?: OpenOptions): ClientRequest;
      post(uri: string | URL, data: unknown, contentType: string): Promise<Buffer | string | null>;
      post(uri: string | URL, parts: FormDataPart[]): Promise<Buffer | string | null>;
      post(uri: string | URL, form: Record<string, unknown>, parts: FormDataPart[]): Promise<Buffer | string | null>;
      post(uri: string | URL, data: unknown, options: PostOptions): Promise<Buffer | string | null>;
      post(uri: string | URL, data: unknown, contentType?: string, options?: PostOptions): Promise<Buffer | string | null>;
      get(uri: string | URL, options?: OpenOptions): Promise<Buffer | object | string | null>;
      detach(singleton?: boolean): void;
      reset(): void;
      close(): void;
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
      fromURL(url: URL, value: string): string;
      fromStatusCode(value: number | string): string;
      defineHttpAgent(options: HttpAgentSettings): void;
      defineDnsLookup(options: DnsLookupSettings, clear?: boolean): void;
      getAria2Path(): string;
      readonly prototype: IRequest;
      new(module?: RequestModule): IRequest;
  }

.. versionadded:: 0.8.2

  *IRequest* method **statusOn** was created.

.. versionadded:: 0.8.1

  *IRequest* method **headersOn** was created.

References
==========

- https://www.unpkg.com/@e-mc/types/lib/http.d.ts
- https://www.unpkg.com/@e-mc/types/lib/request.d.ts
- https://www.unpkg.com/@e-mc/types/lib/settings.d.ts