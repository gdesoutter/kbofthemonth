import requests
import json
from datetime import datetime

month = datetime.now().strftime("%Y-%b")
url = f"https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/{month}"

r = requests.get(url, headers={"Accept": "application/json"})
data = r.json()

products = data["ProductTree"]["FullProductName"]

targets = ["Windows Server 2016", "Windows Server 2019", "Windows Server 2022", "Windows Server 2025"]

filtered_products = {}

for p in products:
    for target in targets:
        if target in p["Value"]:
            if "core" not in p["Value"].lower():
                filtered_products[p["ProductID"]] = p["Value"]
            break

kbs = {}
for product_id in filtered_products:
    kbs[product_id] = set()

for vuln in data["Vulnerability"]:
    for rem in vuln["Remediations"]:
        #Type=2 patch de securite
        if rem["Type"] != 2 or "Hotpatch" in rem["SubType"]:
            continue
        for product_id in rem["ProductID"]:
            if product_id in filtered_products:
                kbs[product_id].add(rem["Description"]["Value"])

result = {
    "generated_at": datetime.now().isoformat(),
    "month": month,
    "kbs": {
        filtered_products[product_id]: [f"KB{kb}" for kb in kb]
        for product_id, kb in kbs.items() 
    }
}
with open("docs/kbs.json", "w") as f:
    json.dump(result, f, indent=2)