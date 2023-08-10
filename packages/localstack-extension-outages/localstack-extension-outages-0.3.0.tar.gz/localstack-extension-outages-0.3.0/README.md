# LocalStack Outages Extension

This LocalStack extension can simulate outages for any AWS region or service.

## Prerequisites

- LocalStack Pro
- Docker
- Python

## Installation

Before installing the extension, make sure you're logged into LocalStack. If not, log in using the following command:

```bash
localstack login
```

You can then install this extension using the following command:

```bash
localstack extensions install localstack-extension-outages
```

## Configuration

The extension can be configured using the following API endpoint.

Start an outage for specified AWS services or regions using the following PUT request.

```bash
curl --location --request PUT 'http://outages.localhost.localstack.cloud:4566/outages' \
  --header 'Content-Type: application/json' \
  --data '{
    "services": ["kms"],
    "regions": ["us-east-1"]
  }'
```

When activated, API calls to affected services and regions will return HTTP 503 Service Unavailable errors.

Outages may be stopped by using empty lists for `services` and/or `regions` parameters in the request.
The following request will clear the current configuration:

```bash
curl --location --request PUT 'http://outages.localhost.localstack.cloud:4566/outages' \
  --header 'Content-Type: application/json' \
  --data '{
    "services": [],
    "regions": []
  }'
```

To retrieve the current configuration, make the following GET call:

```bash
curl --location --request GET 'http://outages.localhost.localstack.cloud:4566/outages'
```

## License

(c) 2023 LocalStack
