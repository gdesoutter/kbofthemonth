# 🛡️ MSRC KB Tracker

> Suivi automatique des mises à jour de sécurité Microsoft pour Windows Server

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/gdesoutter/kbofthemonth/update_kbs.yml?label=Last%20update&style=flat-square)
![JSON](https://img.shields.io/badge/format-JSON-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## 📋 Description

Ce projet interroge automatiquement l'[API MSRC](https://api.msrc.microsoft.com) chaque semaine et publie les numéros de KB du Patch Tuesday pour les versions suivantes de Windows Server :

- Windows Server 2016
- Windows Server 2019
- Windows Server 2022
- Windows Server 2025

---

## 🔗 Endpoint

Les données sont disponibles publiquement à cette URL :

```
https://gdesoutter.github.io/kbofthemonth/kbs.json
```

### Exemple de réponse

```json
{
  "generated_at": "2026-02-21T00:45:25.383236",
  "month": "2026-Feb",
  "kbs": {
    "Windows Server 2016": ["KB5075999"],
    "Windows Server 2019": ["KB5075904"],
    "Windows Server 2022": ["KB5075906"],
    "Windows Server 2025": ["KB5075899"]
  }
}
```

---

## ⚙️ Fonctionnement

```
API MSRC (cvrf/v3.0)
    └── Extraction des ProductID Windows Server
    └── Filtrage des remediations (Type=2, hors Hotpatch)
    └── Génération du kbs.json
    └── Publication via GitHub Pages
```

Le workflow tourne automatiquement **chaque mercredi à midi** (le lendemain du Patch Tuesday) et peut aussi être déclenché manuellement depuis l'onglet **Actions** de ce repo.

---

## 🚀 Utilisation

### Depuis PowerShell

```powershell
Invoke-RestMethod -Uri "https://gdesoutter.github.io/kbofthemonth/kbs.json"
```

### Depuis Python

```python
import requests
data = requests.get("https://gdesoutter.github.io/kbofthemonth/kbs.json").json()
print(data["kbs"])
```

### Depuis curl

```bash
curl https://gdesoutter.github.io/kbofthemonth/kbs.json
```

---

## 🛠️ Stack

- **Python 3.12**
- **GitHub Actions** — automatisation
- **GitHub Pages** — exposition du JSON
- **API MSRC** — source des données

---

## 📅 Source des données

Les données proviennent de l'API officielle Microsoft Security Response Center :
[https://api.msrc.microsoft.com](https://api.msrc.microsoft.com)