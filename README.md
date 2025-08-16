## ⚙️ Konfiguracja

W pliku `config.json` ustaw pod swoje preferencje bądź zachowaj domyślne ustawienia:

```json
{
  "channels": ["...", "..."],
  "wait_times": {
    "livestream_active": {
      "min": 0,
      "max": 0
    },
    "livestream_inactive": 0,
    "error_wait": 0
  },
  "authorization": "Bearer TWÓJ_TOKEN",
  "messages": [
    "...",
    "..."
  ]
}
```

### 🔑 Jak zdobyć token Bearer

1. Wejdź na dowolny stream na Kick.com
2. Otwórz narzędzia deweloperskie w przeglądarce (F12 lub Ctrl+Shift+I)
3. Przejdź do zakładki "Network" (Sieć)
4. Wyślij wiadomość na czacie streama
5. W narzędziach deweloperskich znajdź request do `https://kick.com/api/v2/messages/send/XXXXX`
6. Kliknij na ten request i w zakładce "Headers" (Nagłówki) znajdź pole "Authorization"
7. Skopiuj całą wartość (zaczynającą się od "Bearer") i wklej ją do pliku config.json

## 🚀 Jak Użyć

1. Pobierz Pythona: [Link tutaj](https://www.python.org/downloads/)
2. Zclonuj repozytorium `git clone` lub [pobierz stąd](https://github.com/blazejszhxk/kick-auto-points-collector/archive/refs/heads/main.zip)
3. Zainstaluj zależności w CMD (terminalu): `pip install cloudscraper`
4. Uruchom skrypt w CMD (terminalu) folderu: `python main.py`

## 📝 Jak to Działa

- Skrypt monitoruje podane kanały 
- Sprawdza czy stream jest aktywny
- Jeśli tak, wysyła losową emotkę z listy
- Czeka określony czas i powtarza proces
- W konsoli wyświetla informacje o statusie


*Uwaga: Używaj zgodnie z regulaminem Kick.com*


