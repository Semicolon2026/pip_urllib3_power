# pip_urllib3_power

A pip-based Python environment designed for **security validation, SBOM analysis, and cross-architecture vulnerability testing** using `urllib3` as the core dependency.

This project is primarily used for:

- CVE scanning validation workflows
- Software Bill of Materials (SBOM) generation & comparison
- POWER vs x86 architecture security analysis
- Vulnerability remediation testing pipelines
- Container-based dependency risk assessment

---

## 🎯 Purpose

Modern supply chain security requires validating dependencies across:

- Different architectures (x86_64 vs IBM POWER)
- Different OS baselines (slim images vs full images)
- Different dependency resolutions (pip builds)
- Different vulnerability scanners

This repo provides a controlled environment to test all of the above using `urllib3` as a representative dependency.

---

## 🧱 Key Components

- Python pip-based dependency installation
- `urllib3` as primary HTTP library dependency
- Containerized execution environment
- SBOM generation support
- CVE scan reproducibility testing
- Architecture-aware build workflows

---

## 📦 Base Stack

- Python 3.11
- pip (latest stable)
- urllib3
- certifi
- cryptography
- setuptools / wheel

---

## 🐳 Container Usage

### Build image

```bash
docker build -t pip-urllib3-power .
