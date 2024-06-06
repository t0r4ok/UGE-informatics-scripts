def f(stones, turn):
    if stones >= 435: return turn % 2 == 0
    if turn == 0: return 0

    actions = [
        f(stones + 5, turn - 1),
        f(stones * 3, turn - 1),
    ]

    return any(actions) if (turn - 1) % 2 == 0 else all(actions)


print('19)', [s for s in range(1, 435) if f(s, 2)])
print('20)', [s for s in range(1, 435) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 435) if not f(s, 2) and f(s, 4)])