# Object-Oriented Thinking — Notes to Future Me

> Lessons internalized while building MUD-WoW.
> Read this when the next concurrency problem feels overwhelming.

---

## Why this matters

Technologies change. Libraries get deprecated. Frameworks come and go.

But how you **think** about objects, state, references, and scope — that stays.
This is what separates someone who writes code from someone who builds systems.

---

## 1. Class vs Instance

`Player` is the blueprint. `player` is one specific being created from it.

```python
class Player:
    def __init__(self, name):
        self.name = name

player = Player("Thrall")   # one instance
player.name                  # "Thrall"
Player.name                  # WRONG — this references the class itself
```

**Rule**: when you want per-thing data, you work with the **instance** (`player.name`),
never the class (`Player.name`). The class is the mold; instances are the objects.

---

## 2. Reference vs Copy

When you assign an object to a variable, you get a **reference** — not a copy.
Two names can point to the same thing.

```python
player = Player("Thrall")
players[websocket] = player   # both names point to the SAME object

player.name = "Sylvanas"
players[websocket].name        # also "Sylvanas" — same object
```

**Rule**: mutating an attribute changes the underlying object.
Reassigning a variable just changes what the variable points to — the original object is untouched.

```python
players[websocket] = "Thrall"   # BUG: replaces the Player object with a string
player.name = "Thrall"          # CORRECT: mutates the existing object
```

---

## 3. Scope — Where Does This Live?

Variables exist within a context. Where you declare them decides who can see them.

```python
players = {}                    # module-level — every coroutine shares this

async def handler(websocket):
    player = Player(...)        # function-local — exists only for this connection
    players[websocket] = player # the module-level dict learns about it
```

**Rule**: shared state lives at module level. Per-thing state lives inside the function
that owns the thing.

If you accidentally write `players = ...` inside a function, you create a brand-new local
variable that shadows the module one. The shared dict is no longer being touched.

---

## 4. Data vs Behavior

A class holds both:
- **State** (data) — attributes like `name`, `room`, `hp`
- **Behavior** (methods) — actions like `take_damage()`, `move_to()`

```python
class Player:
    def __init__(self, name):
        self.name = name      # state
        self.hp = 100         # state

    def take_damage(self, amount):  # behavior
        self.hp -= amount
```

**Rule**: state describes what something **is**. Behavior describes what something **does**.
Keep them together in the class that owns them.

Anti-pattern: putting player logic inside the server handler, scattered across if/elif blocks.
Better: methods on the Player class. The server tells the player what to do; the player handles itself.

---

## 5. Strings as IDs vs Objects

In games and databases, you often store **identifiers** (strings) rather than full objects.

```python
player.room = "tavern"          # a STRING, the room's ID
rooms["tavern"]                  # the Room OBJECT
```

Why? IDs are simple, comparable, and serializable to a database.
Objects are rich but harder to store and copy.

**Rule**: store IDs in attributes; look up objects through a registry (`rooms[player.room]`)
when you need the full object.

---

## 6. Mutable Default Arguments — A Python Trap

```python
def __init__(self, exits={}):    # DANGEROUS
    self.exits = exits
```

The default `{}` is created **once** and shared by every instance that doesn't pass an argument.

```python
def __init__(self, exits=None):  # CORRECT
    self.exits = exits if exits is not None else {}
```

**Rule**: never use mutable defaults. Use `None` as the sentinel and create a fresh
mutable object inside the function.

---

## 7. The "What Is Shared?" Question

Whenever multiple agents (coroutines, threads, requests) touch state, ask:

- What is **shared** between them? (e.g. the `players` dict)
- Who **reads** it? (everyone iterating, broadcasting)
- Who **writes** to it? (the handler when a player joins/leaves)

Shared **read-only** state is safe.
Shared **mutable** state is where race conditions live.
Per-thing private state is always safe.

**Rule**: when you draw a system diagram, mark every piece of shared mutable state.
That's where you'll need locks, transactions, or careful ordering.

---

## 8. Cooperative Mindset (asyncio specifically)

The event loop cannot interrupt your code. You yield control voluntarily with `await`.

```python
async def task():
    do_some_work()
    await asyncio.sleep(1)      # yields control — loop runs others
    do_more_work()              # no yield here — loop is blocked until next await
```

**Rule**: in async code, every I/O operation must be awaited with an async-aware library.
A single blocking call freezes everything.

---

## What These Principles Have in Common

They all reduce to one bigger question:

> **"Where does this thing live, who owns it, and who is allowed to change it?"**

When you can answer that for every piece of data in your system,
you're thinking architecturally, not just programmatically.

---

## A Note on Pace

Most developers never internalize these clearly. They learn syntax, ship features, and rely on
intuition. That works until it doesn't — usually in concurrent systems or large codebases.

You're choosing the slow path: understanding before delivering.
This is slower in the short term and **dramatically** faster in the long term —
because every new framework or language becomes "the same thing in different syntax."

Stay with it.