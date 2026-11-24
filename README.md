# Delete System32 — the worst AI advice, in one line

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/intan151/makefun-worst-ai-advice-01/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/intan151/makefun-worst-ai-advice-01/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun](https://make.fun) competition
[Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/c/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

`main.py` writes one line of deliberately terrible AI advice (103 characters)
to `/output/entry.txt`: a confident, tidy assistant telling you to delete
System32 to speed up a slow laptop — concrete, followable, and instantly
regrettable.

## How to run

```sh
python3 main.py
```

It writes `/output/entry.txt` (creating `/output` if needed). Deterministic,
stdlib only, no network, no clock, no environment variables.

## How to verify

```sh
python3 main.py
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), 'characters'); print(repr(t))"
```

The text must be UTF-8, 1–140 Unicode characters, and not only whitespace.
Running the program twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
