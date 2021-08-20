Simple simulator based on "Snakes and Ladders" and similar games.
The players start at 1, and move along the numbers up to 100 by rolling a 6-sided die.

The twist is some fields on the board have a ladder, allowing a player landing on it to jump ahead to the field where the ladder ends,
or they may land on a field with a snake which takes them back to a previously passed field.

The aim of this game simulator was to brute force the shortest way to the top.
It is entirely possible for a player to be caught in a perpetual unlucky loop that will never end, so the maximum is infinite.
