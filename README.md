# 🔫 BUCKSHOT

A terminal-based multiplayer **Buckshot Roulette--style game** written
in Python.

The game supports **2--4 players**, randomized live/fake bullets, health
points, special abilities, multiple rounds, and elimination until one
player remains.

> **Note:** This README documents the current version of the code. Some
> abilities and game mechanics are still experimental/incomplete.

------------------------------------------------------------------------

## 🎮 Features

-   Supports **2, 3, or 4 players**
-   Each player starts with **5 hearts**
-   Randomly generated gun rounds
-   Live and fake bullets are shuffled randomly
-   Random starting player
-   Turn-based multiplayer gameplay
-   Players can shoot themselves or other players
-   Fake bullets can give the shooter another turn
-   Player elimination
-   Automatic winner detection
-   Special items/abilities
-   Multiple gun rounds
-   Terminal-based interface

------------------------------------------------------------------------

## 🧰 Requirements

You need:

-   Python **3.8+**
-   A terminal / command prompt

The project currently uses only Python standard-library modules:

``` text
random
time
os
```

No external packages are required.

------------------------------------------------------------------------

## 🚀 Installation

### 1. Clone the repository

``` bash
git clone https://github.com/Aquamankrish/Buckshot.git
cd Buckshot
```

### 2. Run the game

If your Python file is named `main.py`:

``` bash
python main.py
```

On some systems you may need:

``` bash
python3 main.py
```

------------------------------------------------------------------------

## 🕹️ How to Play

### 1. Choose the number of players

The game asks:

``` text
How many players are going to play ? (2/3/4)
```

Only **2--4 players** are accepted.

### 2. Enter player names

Each player enters their name.

Example:

``` text
Enter Player Name Arthur
Enter Player Name Alex
Enter Player Name John
```

After entering a name, the device can be passed to the next player.

### 3. Starting player

The game randomly chooses one player to start.

``` text
Player Alex Make a Move
```

### 4. Make a move

If the player has abilities available, they can choose:

``` text
1. Kill
2. Show Special Items
```

Otherwise:

``` text
1. Kill
```

------------------------------------------------------------------------

## 🔫 Shooting

When choosing to shoot, the game displays all remaining players and
their health.

Example:

``` text
Alex 0----- ❤︎ ❤︎ ❤︎ ❤︎ ❤︎
John 1----- ❤︎ ❤︎ ❤︎
Sam  2----- ❤︎ ❤︎ ❤︎ ❤︎
```

The current player selects the number corresponding to the player they
want to shoot.

### Live bullet

A live bullet reduces the target's hearts by the current shot power.

Normally:

``` text
Damage = 1 heart
```

Some abilities can increase the shot power.

### Fake bullet

A fake bullet causes no damage.

If a player fires a fake bullet at themselves, they receive another
chance.

------------------------------------------------------------------------

## ❤️ Health System

Every player starts with:

``` text
5 hearts
```

When a player's hearts reach `0`:

``` text
PLAYER IS DEAD !!
```

The player is removed from the game.

The game continues until only one player remains.

``` text
Only one man left...
Congratulations <PLAYER> You won the game
```

------------------------------------------------------------------------

## 🔄 Rounds

Whenever the gun becomes empty, a new round is generated.

Each round:

1.  Generates a new set of bullets
2.  Randomly determines the number of bullets
3.  Adds live and fake bullets
4.  Shuffles the bullets
5.  Gives players a new set of abilities
6.  Starts another round

The number of bullets depends on the number of players.

------------------------------------------------------------------------

## 🎲 Bullet System

The game represents bullets using:

``` python
bullet = [True, False]
```

Where:

  Value     Meaning
  --------- -------------
  `True`    Live bullet
  `False`   Fake bullet

The gun is randomized using:

``` python
random.shuffle(gun)
```

This means players cannot know the complete order of the bullets.

------------------------------------------------------------------------

## 🧩 Special Abilities

Players can receive random special items at the beginning of a round.

Currently defined abilities include:

  Ability               Description
  --------------------- ------------------------------------
  🔍 Magnifying Glass   Checks the next bullet
  🪚 Hand Saw           Increases shot power
  ⛓️ Handcuffs          Currently experimental
  🍺 Beer               Ejects the current bullet
  🚬 Cigarette Pack     Restores one heart
  📱 Hacker Phone       Reveals information about a bullet
  🔄 Inverter           Swaps live and fake bullets
  💊 Expired Medicine   Randomly gains or loses health
  💉 Adrenaline         Currently experimental

------------------------------------------------------------------------

## 🔍 Ability Details

### Magnifying Glass

The magnifying glass checks a bullet and reports whether it is live or
fake.

``` text
Using magnifying glass
Live bullet
```

### Hand Saw

The hand saw changes the shot power:

``` text
Power increased -=>|
```

The next live shot deals increased damage.

### Beer

Beer ejects a bullet from the gun.

``` text
Ejected Live bullet
```

or:

``` text
Ejected Fake bullet
```

### Cigarette Pack

The cigarette ability restores one heart to the current player.

### Hacker Phone

The hacker phone attempts to reveal whether a selected/random bullet is
live or fake.

### Inverter

The inverter reverses every bullet:

``` text
Live → Fake
Fake → Live
```

### Expired Medicine

The medicine randomly produces one of two outcomes:

-   Gain 2 hearts
-   Lose 1 heart

### Handcuffs

Currently prints a message indicating that a player was handcuffed. The
actual restriction mechanic is not implemented yet.

### Adrenaline

Currently only prints that adrenaline was used. Its gameplay effect is
not implemented yet.

------------------------------------------------------------------------

## 🧠 Main Classes and Functions

### `Player`

Represents an individual player.

Important attributes:

``` python
name
hearts
abilities
ability_left
```

Main methods:

``` python
shoot()
show_abilities()
```

------------------------------------------------------------------------

### `load_gun()`

Creates a new randomized gun round.

It determines:

-   Number of bullets
-   Live bullets
-   Fake bullets
-   Random bullet order

------------------------------------------------------------------------

### `check_death(player_shot)`

Checks whether a player's health has reached zero.

If the player dies, they are removed from:

``` python
players
```

------------------------------------------------------------------------

### `rotate_player()`

Controls turn rotation between surviving players.

A player can receive another turn when the relevant fake-bullet
condition is triggered.

------------------------------------------------------------------------

### `generate_ability()`

Randomly assigns special abilities to players at the beginning of a
round.

------------------------------------------------------------------------

### `update_ability()`

Re-indexes a player's remaining abilities after an ability is used.

------------------------------------------------------------------------

### `decide_starting_player()`

Randomly selects the player who begins the game.

------------------------------------------------------------------------

## ⚠️ Current Limitations

This version is a prototype and contains several areas that can be
improved.

### Input validation

Some inputs are converted directly using:

``` python
int(input(...))
```

Invalid non-numeric input can therefore cause an exception.

### Experimental abilities

`Handcuffs` and `Adrenaline` currently do not have complete gameplay
mechanics.

### Ability behavior

Some abilities use the end of the gun (`gun[-1]`) while shooting
consumes bullets from the beginning (`gun[0]`). This may need to be
standardized depending on the intended game rules.

### Hacker Phone

The current implementation contains round/bullet-state logic that may
need refinement to consistently reveal the intended bullet.

### Recursive input recovery

Invalid shooting input calls `current_player.shoot()` again. This could
eventually be replaced with a loop-based input system.

### User interface

The game currently runs entirely in the terminal. A graphical interface
could be added later.

------------------------------------------------------------------------

## 🔮 Future Improvements

Possible improvements include:

-   [ ] Better input validation
-   [ ] Cleaner terminal UI
-   [ ] Proper ability cooldown/usage rules
-   [ ] Fully implement Handcuffs
-   [ ] Fully implement Adrenaline
-   [ ] Improve Hacker Phone mechanics
-   [ ] Add game statistics
-   [ ] Add sound effects
-   [ ] Add animations
-   [ ] Add save/load functionality
-   [ ] Add a graphical interface
-   [ ] Add AI-controlled players
-   [ ] Add automated tests
-   [ ] Split the code into multiple modules
-   [ ] Add configurable game rules
-   [ ] Add difficulty/game modes

------------------------------------------------------------------------

## 🧪 Example Game Flow

``` text
---------------Welcome to BUCKSHOT---------------

How many players are going to play ? (2/3/4)
3

Enter Player Name Arthur
Enter Player Name Alex
Enter Player Name Sam

Round : 1
Loading Gun ..................
Gun Loaded !!

Live Bullets = 3
Fake Bullets = 4

Player Alex Make a Move

1.Kill
2.Show Special Items
```

The game continues until only one player survives.

------------------------------------------------------------------------

## 🛠️ Technologies

-   **Python**
-   `random` --- randomization of players, bullets and abilities
-   `os` --- terminal screen clearing
-   `time` --- timing-related functionality

------------------------------------------------------------------------

## 👨‍💻 Author

**Sahasrad Krish V S**
Student of st.joseph's college B.tech & IIT madras online BS

------------------------------------------------------------------------

## ⭐ Project Status

**Status:** Prototype / Development

This project is currently a terminal-based multiplayer game and is
suitable for further development into a more polished game.
