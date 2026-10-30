# GitHub CI/CD és Branch Protection Lab

## Résztvevők
- Kover Marcell
- Melhem Mohamed
- Rasztovits Levente

## Program és helyi ellenőrzés

Python 3.12, külső függőség nélkül:

```bash
python hello-world.py
python -m unittest discover -v
```

Elvárt kimenet: `10+5 eredménye: 15`.

## CI

A `.github/workflows/python-app.yml` a main és feature/** ágak push eseményére,
valamint main célú pull requestre indul. A kötelező ellenőrzéshez használandó
jobnév: **build-and-test**. Lépései: szintaxisellenőrzés, unit tesztek és programfuttatás.
A tesztek pozitív, nulla, negatív és tört operandusokat, továbbá a konzolos kimenetet vizsgálják.

## Hibás → javított futás

A [#2 PR](https://github.com/etnevelpriv/ci-cd-pipeline-gyakorlas/pull/2)
a `feature/bug-test` ágból a `main` ágba készül.

- A kezdeti tesztek a meglévő hibákat mutatták ki: nulla operandusnál az összeg
  `None` volt, közvetlen futtatáskor pedig nem hívódott meg a main függvény.
- [Bizonyítottan hibás PR-futás](https://github.com/etnevelpriv/ci-cd-pipeline-gyakorlas/actions/runs/41024301327):
  a szintaxisellenőrzés sikeres, a Run tests lépés sikertelen.
- A javítás feltétel nélkül összead, és hozzáadja a szokásos Python belépési pontot.
- Ez meglévő hiba regressziós tesztelése; a feladatban kért szándékos új hiba bevezetését
  nem állítjuk megtörténtnek.

## Branch protection és emberi review

A teljes laborhoz a GitHub Settings → Rules → Rulesets oldalon aktív,
main ágra célzott branch ruleset szükséges:
- Bypass list: üres.
- Restrict updates: kikapcsolva.
- Require a pull request before merging: bekapcsolva.
- Required approvals: 1.
- Require status checks to pass: bekapcsolva, ellenőrzés: build-and-test.

A szabályok tényleges beállítása és a blokkolt merge bemutatása még ellenőrzendő.
A sikeres CI önmagában nem igazolja a branch protection működését.
A PR szerzőjétől különböző, megfelelő jogosultságú GitHub-felhasználónak kell
jóváhagynia a PR-t. Saját fiókból végzett AI-kódellenőrzés nem független jóváhagyás.
A védelem kikapcsolása nem helyettesíti ezt a lépést.

## Beadási bizonyítékok

1. Hibás Actions-futás és teszthiba.
2. Javított, sikeres Actions-futás ugyanabban a PR-ben.
3. Aktív main szabályok és a hibás/hiányzó jóváhagyás miatt blokkolt merge.
4. Független Approve review.
5. Sikeres merge és zöld main CI.

A 3–5. pont csak a tényleges végrehajtás után tekinthető késznek.
