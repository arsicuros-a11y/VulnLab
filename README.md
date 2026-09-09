# VulnLab

Laboratorijska web aplikacija za demonstraciju IDS i IPS sistema.

## Opis

VulnLab je lokalna Flask web aplikacija razvijena za kontrolisano laboratorijsko okruženje u okviru seminarskog rada o detekciji i prevenciji mrežnih napada korišćenjem IDS i IPS sistema.

Aplikacija omogućava prikaz početne stranice, pregled korisnika, prijavu i kontrolnu tablu. Mrežni događaji u laboratoriji analiziraju se pomoću sistema Suricata.

## Struktura

```text
VulnLab/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── users.html
│   ├── login.html
│   ├── dashboard.html
│   └── about.html
└── static/
    └── style.css
```

## Pokretanje

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Aplikacija se pokreće na portu 5000 i namenjena je lokalnom laboratorijskom radu.

> Napomena: projekat je demonstracioni i nije namenjen produkcionoj upotrebi.
