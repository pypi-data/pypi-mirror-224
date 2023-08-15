# knot_exporter

A Prometheus exporter for [Knot DNS](https://www.knot-dns.cz/)'s server and query statistics.

# Getting Started

The Knot instance also needs to be configured to collect statistics using
[Statistics module](https://www.knot-dns.cz/docs/latest/html/modules.html?highlight=mod%20stats#stats-query-statistics)

The exporter can be started via:

```bash
$ knot_exporter
```

To get a complete list of the available options, run:

```bash
$ knot_exporter --help
```
