# Cross-Model Validation Guide

## Perché validare con un secondo modello

Il modello che genera un'ipotesi tende a confermarla. Per questo il
sistema è progettato per generare con Claude e validare con un modello
diverso. Questo riduce il confirmation bias.

## Come fare (passo passo)

### Opzione 1: Validazione con ChatGPT (raccomandata)

1. In Claude Code, dopo che `/discover` ha finito, digita:
   ```
   /export gpt
   ```
2. Apri il file `results/export-gpt.md`
3. Apri ChatGPT → seleziona **GPT-5.4 Thinking** (o Pro)
4. Attiva **Deep Research** se disponibile
5. Incolla TUTTO il contenuto del file
6. Aspetta il report (5-30 minuti)
7. Confronta: dove GPT-5.4 dà alta confidenza E Claude dà alta
   confidenza → candidata forte. Dove divergono → indaga perché.

### Opzione 2: Validazione con Gemini (per connessioni matematiche)

1. In Claude Code: `/export gemini`
2. Apri `results/export-gemini.md`
3. Apri Gemini AI Studio → seleziona **3.1 Pro** o **Deep Think**
4. Incolla il contenuto
5. Gemini è particolarmente utile se il bridge tra i campi è una
   struttura matematica formale

### Opzione 3: Entrambi

1. `/export both`
2. Segui i passi per entrambi
3. Se 2 modelli su 3 concordano su alta novità + confidenza →
   candidata prioritaria per expert review

## Come interpretare i risultati

| Claude dice | Altro modello dice | Significato |
|---|---|---|
| Alta confidenza | Alta confidenza | **Forte candidata** — cerca un esperto di dominio |
| Alta confidenza | Bassa confidenza | Possibile allucinazione di Claude — investiga |
| Bassa confidenza | Alta confidenza | Gemma nascosta — Claude era troppo cauto |
| Bassa confidenza | Bassa confidenza | Scarta |

## Dopo la validazione cross-model

Le ipotesi che sopravvivono dovrebbero essere presentate a esperti
di dominio. Il session-summary.md include per ogni ipotesi quale
tipo di esperto contattare (es. "immunologo con esperienza in
checkpoint PD-L1" o "fisico della materia condensata").
