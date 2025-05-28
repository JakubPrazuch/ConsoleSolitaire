# Console solitaire

[Polskie readme](./README.pl.md)

_Console solitaire_ is a TUI version of classic solitaire.

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
> Columns are oriented horizontally.

## Actions

- `h` - Display help.
- `p p` - Move cards between piles, where `p` is the name of a pile. Examples:
  - `1 a` move from column 1 to foundation pile A,
  - `5 4` move from column 5 to column 4,
  - `s 6` move from stockpile to column 6.
- `s` - Draw a card from the stockpile.
- `ng` - Start a new game.
- `q` - Quit the application.

## Project background

The project is for the second stage of a [_Gigathon_](https://www.gigathon.pl/) (2025) — a Polish programming competition.
