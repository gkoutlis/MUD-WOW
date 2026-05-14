Concurrency:
    Βοηθάει μόνο όταν υπάρχει αναμονή, asyncio της Python.

Race Conditions: Βασική Αρχή concurrent programming
    Εμφανίζονται όταν πολλαπλά "νήματα εκτέλεσης" τροποποιούν ταυτόχρονα τ ίδιο shared state.
    Το read only shared-state e;inai asfalew. Το  per-play private state είναι ασφάλες. Το shared 
    mutable state είναι το πρόβλημα.

Στο asyncio o cuncurrency συμβαίνει μόνο στο Await points. Αν δεν υπάρχει await δεν υπάρχει concurrency.
    O Event Loop δε μαντεύει πότε να αλλάξει task - η coroutine πρέπει εθελοντικά να του δώσει τον 
    έλεγχο.
