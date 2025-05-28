# Console solitaire

[English readme](./README.md)

_Console solitaire_ to wersja klasycznego pasjansa w TUI.

```blank
   S    |  A   B   C   D  | Moves: |
[ ] 5♣  | { } { } { } { } | 1      |
------------------------------------
0 K♦
1 [ ] A♣
2 [ ] [ ] J♦
3 [ ] [ ] [ ] A♥
4 [ ] [ ] [ ] [ ] 8♠
5 [ ] [ ] [ ] [ ] [ ] 7♦
6 [ ] [ ] [ ] [ ] [ ] [ ] 6♥
>
```

> [!NOTE]
> Kolumny są zorientowane poziomo.

## Akcje

- `h` - Wyświetl pomoc.
- `p p` - Przenieś karty pomiędzy stosami, gdzie `p` to nazwa stosu. Przykłady:
  - `1 a` przenieś z kolumny 1 do stosu końcowego A,
  - `5 4` przenieś z kolumny 5 do kolumny 4,
  - `s 6` przenieś ze stosu rezerwowego do kolumny 6.
- `s` - Dobierz kartę ze stosu rezerwowego.
- `ng` - Rozpocznij nową grę.
- `q` - Wyjdź z aplikacji.

## Informacje o projekcie

Projekt został wykonany w ramach durgiego etapu ogólnopolskiego konkursu programistycznego [_Gigathon_](https://www.gigathon.pl/) (2025).
