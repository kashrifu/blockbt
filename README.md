# BlockBT (BBT)

**The blockchain-optimized rewrite of dbt-core for trustless ELT**

> BlockBT rewrites dbt's SQL-first modularity for live chain ingestion, cross-chain transforms, ZK verifiability, and on-chain materialization. Built for Web3's $3B analytics market.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-MVP-orange.svg)](https://github.com/kashrifu/blockbt)

🌐 **[Visit the Website](https://kashrifu.github.io/blockbt/)** | 📖 **[Read the Technical Whitepaper](WHITEPAPER.md)** | 📚 **[Technical Documentation](TECHNICAL_DOCS.md)**

For full product vision, architecture, and roadmap.

---

## Abstract

BlockBT is the blockchain-optimized rewrite of dbt-core, enabling verifiable data pipelines that treat chains as native "warehouses." Users define dbt-like SQL models and YAML configs to ingest from RPCs/Subgraphs, transform with cross-chain DAGs, prove correctness via ZK, and materialize to JSON, tables, or contracts.

Addressing Web3 pains like data silos, latency, and trust gaps, BBT empowers **DeFi DAOs**, **CEXs**, **DEX builders**, **institutions**, and **AI agents**. The MVP launches as a Python CLI for Ethereum/Solana DeFi metrics, with V1 in Rust for scalability and a BBT token for decentralized proofs.

## Introduction

dbt-core transformed data engineering by abstracting SQL transformations into modular DAGs, allowing teams to build reliable pipelines in warehouses like Snowflake or Databricks. However, as blockchain adoption surges—generating **1B+ transactions daily** across 100+ networks—dbt's warehouse assumption breaks. Blockchain data is live, append-only, and distributed, requiring tools that handle reorgs, cross-chain aggregation, and cryptographic verifiability without centralized ETL.

BlockBT rewrites dbt-core's essence—SQL models, configs, and DAGs—into a chain-native tool. It enables users to **"transform chains like tables,"** delivering sub-second, proven insights for high-stakes Web3 use cases. From DAO governance to CEX compliance, BBT reduces costs by **50-90%** (no ETL mirrors) and eliminates trust risks with ZK proofs.

Built as **open-source (Apache 2.0)**, BBT's vision is a decentralized ELT layer for the **$469B blockchain economy by 2030**.

## Problem Statement

Web3 data analytics faces systemic challenges that dbt-core, designed for warehouses, can't address natively:

### Fragmentation and Latency
Data across EVM (Ethereum), SVM (Solana), and UTXO (Bitcoin) requires manual ETL (e.g., Airbyte to BigQuery), adding hours of delay and **$10k/mo costs** via services like Goldsky. dbt assumes pre-loaded data, ignoring live RPC velocity.

### Trust and Verifiability Gaps
Tools like Dune or Flipside offer queries but no proofs, risking manipulation (e.g., unproven TVL leads to bad DAO votes; FTX's reserves collapse). dbt's outputs are opaque, lacking cryptographic lineage.

### Centralization Risks
dbt relies on trusted warehouses for execution, vulnerable to outages or tampering. Blockchain's immutability demands decentralized compute, but dbt has no support for reorgs or on-chain outputs.

### Scalability Limitations
1B tx/day overwhelms batch tools; ZK maturity is underutilized for data integrity, leaving RWAs and AI with unverified inputs.

These issues cost billions in inefficient infrastructure. **BBT rewrites dbt to make pipelines as trustless as blockchains themselves.**

## Solution: BlockBT's Core Functionality

BlockBT is an open-source ELT engine that rewrites dbt-core's workflow:

- **Ingestion**: Live RPC/Subgraph fetches via adapters (e.g., web3.py for EVM)
- **Transformation**: dbt-like SQL models with `{{ ref() }}`/`{{ source() }}`; Cross-chain joins (e.g., ETH swaps + Sol liquidity)
- **Verification**: ZK proofs for aggregates/lineage (SP1 circuits)
- **Materialization**: JSON core, with pushes to tables (Dune/S&T), on-chain contracts, or IPFS

Users get dbt's modularity without warehouses—e.g., `bbt run --target eth_sol --select fees_model --prove --push dune` delivers a proven table in seconds.

## Technical Architecture

BBT's architecture rewrites dbt-core's warehouse abstraction for chains:

```
                    ┌─────────────────────────────┐
                    │   User: bbt run --select    │
                    └──────────────┬──────────────┘
                                   ↓
        ┌──────────────────────────────────────────┐
        │         CLI Layer (Click)                 │
        │  • bbt run/test/docs/compile            │
        │  • Argument parsing & validation         │
        │  • Error handling                        │
        └─────────────────┬────────────────────────┘
                          ↓
        ┌──────────────────────────────────────────┐
        │       Config Layer (PyYAML)               │
        │  • sources.yml (table definitions)       │
        │  • blockbt_project.yml (profiles)        │
        │  • Variable substitution                  │
        └─────────────────┬────────────────────────┘
                          ↓
        ┌──────────────────────────────────────────┐
        │     Ingestion Layer (Adapters)            │
        │  • Ethereum/EVM: web3.py                 │
        │  • Solana: solana-py                     │
        │  • Incremental: SQLite/LevelDB           │
        │  • Reorg handling                         │
        └─────────────────┬────────────────────────┘
                          ↓
        ┌──────────────────────────────────────────┐
        │   Transformation Layer (SQL Execution)     │
        │  • sqlparse (AST) → NetworkX (DAG)       │
        │  • Jinja templating (ref/source/var)     │
        │  • Polars/DuckDB execution               │
        │  • Cross-chain joins                     │
        └─────────────────┬────────────────────────┘
                          ↓
        ┌──────────────────────────────────────────┐
        │       Verification Layer (ZK)              │
        │  • SP1/RISC0 circuits                    │
        │  • Proof generation for aggregates       │
        │  • Lineage verification                   │
        └─────────────────┬────────────────────────┘
                          ↓
        ┌──────────────────────────────────────────┐
        │          Output Layer                     │
        │  • JSON + embedded proofs                │
        │  • Dune Analytics API                     │
        │  • Snowflake & Table                      │
        │  • On-chain (smart contracts)             │
        │  • IPFS (decentralized storage)           │
        └──────────────────────────────────────────┘
```

### Component Details

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **CLI** | Click (Python) | User interface and command routing |
| **Config** | PyYAML | Project and source configuration |
| **Ingestion** | web3.py, solana-py, SQLite | Fetch and decode blockchain data |
| **Transformation** | sqlparse, NetworkX, Polars, DuckDB | Parse SQL, resolve DAGs, execute queries |
| **Verification** | SP1, RISC0 | Generate ZK proofs for correctness |
| **Output** | JSON, APIs, Smart Contracts | Materialize results with proofs |

### Data Flow Example

```
User: bbt run --select fees_model --prove --target eth_sol
  ↓
1. CLI loads config, resolves dependencies
  ↓
2. DAG: fees_model depends on [eth_txns, sol_txns]
  ↓
3. Ingestion: Fetch from Ethereum RPC + Solana RPC
  ↓
4. Transformation: Execute SQL in DuckDB
   SELECT date, SUM(fee) FROM eth_txns UNION ALL 
   SELECT date, SUM(fee) FROM sol_txns GROUP BY date
  ↓
5. Verification: Generate ZK proof of aggregate sum
  ↓
6. Output: JSON with data + proof, optional push to Dune
```

**Note**: V1 transitions core engine to Rust for 10-100x performance gains.

## Installation

### From Source

```bash
git clone https://github.com/kashrifu/blockbt.git
cd blockbt
pip install -e .
```

### Dependencies

All dependencies are automatically installed:

- **Python 3.8+**
- **click>=8.0** - CLI framework
- **web3>=6.0** - Blockchain interaction (EVM)
- **polars>=0.20** - High-performance DataFrames
- **duckdb>=0.10** - Analytical database
- **sqlparse>=0.4** - SQL parsing
- **pyyaml>=6.0** - Configuration

## Quick Start

### 1. Install BlockBT

```bash
git clone https://github.com/kashrifu/blockbt.git
cd blockbt
pip install -e .
```

### 2. Set Environment Variables

```bash
# Windows CMD
set INFURA_KEY=your_infura_key
set SOLANA_RPC=https://api.mainnet-beta.solana.com

# Linux/Mac
export INFURA_KEY=your_infura_key
export SOLANA_RPC=https://api.mainnet-beta.solana.com
```

### 3. Run a Demo Model

```bash
# Cross-chain market share
bbt run --select cross_chain_market_share --target eth_sol

# Ethereum daily fees
bbt run --select eth_daily_fees --target eth

# Cross-chain 7-day trends
bbt run --select cross_chain_7d_trends --target eth_sol
```

### 4. Create Your Own Model

Create a SQL file in `models/`:

```sql
-- models/my_model.sql
SELECT 
    DATE_TRUNC('hour', block_time) as hour,
    SUM(gas_used * gas_price / 1e18 * eth_usd_price) as total_fees_usd
FROM {{ source('ethereum', 'swaps') }}
WHERE block_time >= NOW() - INTERVAL '24 hours'
GROUP BY 1
ORDER BY 1 DESC
```

Then run it:

```bash
bbt run --select my_model --target eth
```

See the [Technical Documentation](TECHNICAL_DOCS.md) for more details.

## CLI Commands

### `bbt run`
Run your models:

```bash
bbt run                          # Run all models
bbt run --select model1          # Run specific models
bbt run --full-refresh           # Force full refresh
bbt run --target eth_sol         # Cross-chain target
bbt run --prove                  # Generate ZK proofs
bbt run --push dune              # Push to Dune Analytics
```

### `bbt compile`
Compile SQL models to see the rendered SQL:

```bash
bbt compile                      # Compile all models
bbt compile --select model1
```

### `bbt test`
Run tests on your models:

```bash
bbt test                         # Run all tests
bbt test --select model1
```

### `bbt init`
Initialize a new BlockBT project:

```bash
bbt init                         # Initialize with default adapter
bbt init --adapter ethereum
bbt init --adapter solana
```

## Project Structure

```
blockbt/
├── bbt/                         # Main package
│   ├── adapters/                # Chain adapters (ethereum, solana, polymarket, prices)
│   ├── cli.py                   # Command-line interface
│   ├── executor.py              # SQL execution & DAG resolution
│   ├── fetcher.py               # Data ingestion
│   ├── prover.py                # ZK proof generation
│   └── state.py                 # Incremental state management
├── models/                      # Your SQL models (15+ demo models)
├── tests/                       # Test files
├── website/                     # Website files (HTML/CSS/JS)
├── setup.py                     # Package configuration
├── requirements.txt             # Python dependencies
├── TECHNICAL_DOCS.md            # Technical documentation
├── WHITEPAPER.md                # Product whitepaper
└── README.md                    # This file
```

## MVP Status (November 2025)

🚧 **Current Version: 0.1.0**

The MVP is a Python CLI validating DeFi use cases:

- ✅ ETH/Sol ingestion via adapters
- ✅ SQL models with dbt-like syntax (`{{ ref() }}`, `{{ source() }}`, `{{ config() }}`)
- ✅ Source definitions (YAML)
- ✅ Cross-chain joins (Ethereum + Solana)
- ✅ DAG resolution with NetworkX
- ✅ Incremental models with hash-based state tracking
- ✅ Real-time price fetching (ETH/USD, SOL/USD per block)
- ✅ Mock ZK proofs (infrastructure ready)
- ✅ JSON outputs with metadata
- ✅ Dune push stub
- ✅ Basic CLI commands (`run`, `compile`, `test`, `init`)
- ✅ Comprehensive demo models (15+ examples)

**Demo**: Cross-chain market share (`bbt run --select cross_chain_market_share --target eth_sol`)

**Website**: [https://kashrifu.github.io/blockbt/](https://kashrifu.github.io/blockbt/)

## Roadmap

### Beta (December 2025)
- [ ] Real ZK proofs (SP1 integration)
- [ ] 10+ chain adapters
- [ ] Full DAG resolution and execution
- [ ] Cloud SaaS ($49/mo)
- [ ] Documentation and tutorials

### V1 (Q1 2026)
- [ ] Rust rewrite for performance
- [ ] BBT token launch
- [ ] On-chain materialization
- [ ] zkAI integration
- [ ] Production-ready adapters

### Scale (2027)
- [ ] Fully Homomorphic Encryption (FHE)
- [ ] 100+ chain adapters
- [ ] DePIN marketplace
- [ ] Enterprise features

## Use Cases

- **DeFi DAOs**: Governance metrics, treasury analytics
- **CEXs**: Compliance reporting, reserve proofs
- **DEX Builders**: Volume analytics, LP optimization
- **Institutions**: On-chain asset tracking, risk analysis
- **AI Agents**: Verified on-chain data for training

## Contributing

Contributions are welcome! This project is in early stages, so feedback and contributions are especially valuable.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

**Areas we're looking for help:**
- Chain adapter implementations
- ZK proof circuits
- Documentation and examples
- Performance optimizations

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Inspired by [dbt](https://www.getdbt.com/)
- Built for the blockchain ecosystem and Web3 data community
- Special thanks to the open-source contributors

## Contact

- **Website**: [https://kashrifu.github.io/blockbt/](https://kashrifu.github.io/blockbt/)
- **GitHub**: [kashrifu/blockbt](https://github.com/kashrifu/blockbt)
- **Email**: hello@blockbt.com
- **Discord**: [Join our community](https://discord.gg/blockbt)

---

**Built with ❤️ for Web3. Transforming blockchain data, one SQL model at a time.**
