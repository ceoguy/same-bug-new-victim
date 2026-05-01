# Dataset

`incidents.csv` contains the 30 publicly-disclosed Web3 security incidents tracked for the April 2026 research report.

## Schema

| Column | Description |
|---|---|
| `date` | Incident date (YYYY-MM-DD) or YYYY-MM if specific day not disclosed |
| `protocol` | Protocol or entity name |
| `chain` | Primary chain affected |
| `usd_loss` | Reported USD loss at time of incident |
| `vulnerability_class` | Primary classification (see below) |
| `vector_layer` | Where in the stack the attack landed: `smart_contract`, `off_chain_human`, `off_chain_infrastructure` |
| `attribution` | Threat actor if publicly attributed; `unattributed` otherwise |
| `recovery_status` | Recovery state at time of writing |
| `attacker_address` | Primary attacker-controlled address if disclosed |
| `post_mortem_url` | Link to most authoritative public post-mortem |
| `notes` | Additional technical detail |

## Vulnerability classes

- `signer_social_engineering` — humans induced to sign valid-but-malicious transactions
- `off_chain_verifier_compromise` — bridge / oracle verifier infrastructure compromised
- `logic_error` — smart contract math or state-management bug
- `cross_chain_accounting` — bridge or wrapper-token accounting failure
- `bridge_exploit` — generic bridge exploit (subclass when specific)
- `centralized_exchange_theft` — CEX hot wallet or operational compromise
- `token_compromise` — token contract or supply compromise

## Caveats

- USD losses use values reported at incident time, not current market value
- Recovery status changes; check post-mortems for latest
- 22 sub-$2M incidents are aggregated into a single row; raw data lives in PeckShield daily logs and SlowMist HackedDB
- Attribution is preliminary in some cases; treat as "best public information as of late April 2026"

## License

CC BY 4.0. If you use this dataset, please cite:

> Rakhmanov, I. (2026). *Same Bug, New Victim: A Forensic Read on Web3's $600M April*. https://github.com/ceoguy/same-bug-new-victim
