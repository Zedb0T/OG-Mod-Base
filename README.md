> [!NOTE]
> You can read the original README for the OpenGOAL project [here](https://github.com/open-goal/jak-project/blob/master/README.md).
> In particular you may want to check out the Development Environment setup [here](https://github.com/open-goal/jak-project/blob/master/README.md#setting-up-a-development-environment)


# A Complicated Mod


- **The premise is ~~simple~~ complicated.** You play through the game to defeat Gol and Maia.
  However, there is a countdown that is always running. If it reaches 0, you lose and the run restarts.
- Power cells, orbs, and scout flies **increase the timer.**
- There are also **complications and rules you need to follow.**
- **Play in speedrunner mode and start a new run** to start the game.
- Use the **Complicated Options** menu in Game Options to adjust the gameplay to your liking!

---

## Conditions: Rules vs. Complications

* **Rules:** Restrictions or tasks that require compliance or action. Each one comes with a punishment that takes effect if broken.
* **Complications:** Modifiers that add a twist or complicate gameplay.
* **Conditions:** General term for both rules and complications.

---

## Complicated Options (Menu Settings)
**Options -> Game Options -> Complicated Options**

| Setting | Description |
| :--- | :--- |
| **Countdown Start Time** | The global countdown's starting time, in seconds. |
| **Time Limit Multiplier** | A multiplier applied to rules that have time limits. For example, a value of 2.0 doubles the amount of time you have; 0.5 halves. |
| **Collectable Increments** | The amount of time, in seconds, that will be added to the timer for obtaining a Power Cell, Scout Fly, or Precursor Orb. |
| **Followed Rule Increment** | The amount of time, in seconds, that will be added to the timer for successfully following a rule. |
| **Condition Toggles** | Manually choose which conditions can or cannot be rolled. |
| **Punishment Toggles** | Manually choose which punishments can or cannot be rolled. |
| **Speedrun Timer** | Shows an in-game timer above the global countdown timer, to track your current run's duration. |
| **Klaww Assist** | Adds 30 seconds to the countdown timer after each Klaww phase. |
| **Fish Assist** | Adds 5 seconds to the countdown timer for each five-pound fish. |
| **Text Scale** | The size of the mod text. This includes condition names, descriptions, punishments, and timers. |
| **Pass Cost** | How many credits are required to gain a pass. A credit is rewarded on each rule followed. |

⚠️ **SPOILER WARNING: Below has names of conditions!**

### Difficulty Presets

| Preset | Start Time | Time Limit Multiplier | Cell | Orb | Fly | Pass Cost | Toggles Off
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Simple** | 30s | 1.5x | 40.0 | 2.0 | 15.0 | 8 | Spin to Win, Rotten Eggs, Heating Balloons, Hang Time, Quick Time Event, Get a Grip, Fast Reel, Quicksand, Crash Punishment |
| **Complicated** | 30s | 1.2x | 30.0 | 1.0 | 10.0 | 10 | Spin to Win, Hang Time
| **Esoteric** | 30s | 1.0x | 20.0 | 1.0 | 8.0 | 12 | None
| **Unfathomable** | 10s | 0.8x | 20.0 | 1.0 | 5.0 | 15 | None

## Condition Index

<details>
<summary><b>⚠️ Rules</b></summary>

| Name | Description | Explanation/Notes
| :--- | :--- | :--- |
| **GROUNDED** | DO NOT JUMP. | Anything that gains height is considered a jump. Yes, uppercuts and rolljumps count.
| **ANGER MANAGEMENT** | DO NOT PUNCH. | This only applies to punches. Ground pounds and yellow eco shots are allowed.
| **DIE** | KILL HIM. KILL HIM NOW. | Jak must be killed.
| **BLOODLUST** | KILL 6 LURKERS. |
| **HITLSIT** | KILL 3 UNIQUE LURKER TYPES. |
| **DOUBLE KILL** | KILL 2 LURKERS AT THE SAME TIME. |
| **SNIPER** | KILL A LURKER FROM AT LEAST 70 METERS AWAY. | Be at least 70 meters from a lurker when it dies, by any means.
| **BULL AND CHINA** | BREAK 5 CRATES. |
| **CASH GRAB** | COLLECT 20 ORBS. |
| **CELL PRESSURE** | COLLECT A POWER CELL. |
| **BUZZER BEATER** | COLLECT 2 SCOUT FLIES. |
| **FLOP THIS** | LURKERS MAY ONLY BE KILLED WITH GROUND POUNDS. | Jak's jump dive and Flut Flut's dive attack are the only means allowed.
| **KEEP IT LOW** | DO NOT JUMP KICK. | Do not kick/spin in the air. Doing it on the ground is allowed.
| **VENDETTA** | KILL A LURKER WITH RED ECO. |
| **HANDS ON** | CRATES MAY ONLY BE BROKEN BY DIRECT CONTACT FROM JAK. | Jak must make direct contact with the crate. Using eco, Flut Flut, explosions, or the zoomer breaks this rule.
| **STEP ONE** | STAY ALIVE. | Do not die.
| **SPIN TO WIN** | DO A ONE-FRAME. | A one-frame is performed by spinning exactly 15 frames after jumping on a jump pad. This is toggled off for Simple and Complicated difficulties.
| **SOCIAL DISTANCING** | DO NOT GET WITHIN 8 METERS OF A SCOUT FLY. |
| **RED LIGHT** | DO NOT MOVE. |
| **FOR BILLY** | PROTECT FARTHY'S SNACKS. DO NOT LEAVE BOGGY SWAMP. | You must complete the rats minigame, and also not leave Boggy Swamp.
| **COLD FEET** | KEEP OFF THE ICE. |
| **SPEED RACER** | REACH A SPEED OF 40 METERS PER SECOND. |
| **QUICK MATHS** | ANSWER A MATH QUESTION CORRECTLY. | Use the D-Pad to input your answer. Up/Down step with 1, Left/Right step with 5. You can use L3 to submit an answer early.
| **DON'T KNOW JAK** | ANSWER A TRIVIA QUESTION CORRECTLY. | Use the D-Pad to navigate choices. You can use L3 to submit an answer early.
| **GREEN-PILLED** | COLLECT 50 SMALL GREEN ECO PILLS. | Only the small ones count.
| **BUTTON PUSHER** | PUSH A BUTTON. | Not to be confused with Quick Time Event; Jak must press a button somewhere in the world.
| **LOYAL CUSTOMER** | BUY AN ORACLE CELL. |
| **COOKED** | BURN JAK. | The fire pits in Rock Village do *not* send a burn event.
| **SAGGING SAILS** | MISS 3 FIVE-POUND FISH. |
| **SIDE TO SIDE** | DO NOT TOUCH THE MIDDLE PLATFORM. | During the Klaww fight, do not touch the middle of the three small platforms you jump on.
| **LANDLUBBER** | STAY OUT OF THE WATER, MUD, AND TAR. | You can still drive over water on the zoomer.
| **TOUCH GRASS** | DO THAT. |
| **EXPRESS DELIVERY** | RETURN THE MUSE. OR SUFFER MY CURSE. |
| **QUICK TIME EVENT** | QUICKLY PRESS A SPECIFIC FACE BUTTON. | A random face button (X, Circle, Triangle or Square) is chosen. You must press it before time runs out.
| **HANG TIME** | STAY AIRBORNE FOR 3 CONSECUTIVE SECONDS. | Landing, grabbing a ledge, or entering goggles resets the progress.
| **DO NO HARM** | DO NOT KILL ANY LURKERS. |
| **SUPERCHARGED** | COLLECT BLUE ECO. |
| **KEEP ROLLING** | ROLL 30 TIMES. |

</details>
<details>
<summary><b>⚠️ Complications</b></summary>

| Name | Description | Explanation/Notes
| :--- | :--- | :--- |
| **BRITTLE BONES** | EVERY JUMP HAS A 10% CHANCE TO DAMAGE YOU. | Anything that gains height is considered a jump. Yes, uppercuts and rolljumps count.
| **ROTTEN EGGS** | ORBS KILL YOU. |
| **ECO ALLERGY** | ECO DAMAGES YOU. | Collecting eco deals damage.
| **SIZEABLE CONTRIBUTIONS** | ROLLJUMPS COST 2 ORBS. | Each rolljump subtracts 2 orbs from your current count. Jak cannot rolljump if you cannot afford one.
| **CUMBERSOME** | ORBS WEIGH JAK DOWN. | The more orbs you have, the slower Jak moves and the shorter rolljumps get.
| **HEATING BALLOONS** | COOLING BALLOONS MELT YOU. |
| **DROUGHT** | ALL WATER, LAVA, AND DARK ECO ARE GONE. |
| **OHKO** | JAK IS LIMITED TO ONE HEALTH. |
| **CRITICAL CONDITION** | CELLS CAN ONLY BE COLLECTED AT ONE HEALTH. | You will also be unable to talk to NPCs.
| **GLARE** | JAK FREEZES WHEN LURKERS SEE HIM. | When a lurker notices Jak, he freezes for exactly 3 seconds.
| **DISASSOCIATE** | KILLING A LURKER DISMOUNTS FLUT FLUT. |
| **BUS DRIVER** | ZOOMER EXPLODES IF TOO SLOW. | If you're on the zoomer and your speed goes below 20 meters per second, you explode.
| **FUEL SHORTAGE** | ALL POWER CELLS ARE GONE. | You will also be unable to talk to NPCs.
| **HIDDEN TREASURE** | ORBS ARE INVISIBLE. |
| **WINGS TIED** | YOU CANNOT COLLECT CELLS WHILE ON FLUT FLUT. |
| **JAK RABBIT** | JUMP HEIGHTS ARE DOUBLED. |
| **ECO RESERVE** | YELLOW ECO PAUSES TIMER. | The countdown timer is paused as long as you have yellow eco in your meter.
| **SEEING RED** | RED ECO PAUSES TIMER. | The countdown timer is paused as long as you have red eco in your meter.
| **RGYB** | BLUE AND YELLOW ECO ARE SWAPPED. | Clusters will respawn as the opposite type, and vents will grant the opposite powerup.
| **BUTTER FINGERS** | JAK CANNOT GRAB LEDGES. |
| **OVERCLOCK** | CITADEL DISCS ARE FASTER. | The large disc platforms in Citadel (pizzas) rotate faster.
| **BAD PING** | YOU HAVE 120MS INPUT DELAY. |
| **INVISIBLE MAN** | JAK IS INVISIBLE. |
| **JOYRIDE** | HEY! THERE'S THE FLUT-FLUT! | Jak immediately mounts the Flut Flut from wherever he is.
| **INFESTATION** | DOUBLE THE APHIDS. | The amount of bugs the Plant Boss spawns (aphids) is doubled.
| **THIS ONE SUCKS** | CONTROLS ARE INVERTED. |
| **LOOSE POCKETS** | BONKING OR TAKING DAMAGE LOSES 20 ORBS. |
| **TWISTED** | A LATER RULE MUST BE BROKEN. | A twisted rule is chosen at random. You must *break* this rule. Rules are colored orange. Using a pass on this will *not* mark the future rule as twisted.
| **VIBE CHECK** | I LIKE YA CUT, G. | Jak gets smacked into the air and takes damage.
| **INCOME TAX** | TIMER INCREMENTS ARE HALVED. | The additional time granted from cells, orbs, and flies is cut in half.
| **MIRRORED** | THE WORLD IS MIRRORED. |
| **ONE AND DONE** | JAK AND FLUT FLUT FORGOT HOW TO DOUBLE JUMP. |
| **UNBREAKABLE** | SCOUT FLY CRATES CAN ONLY BE BROKEN WITH ECO. | You will need to use either blue, yellow, or dark eco to break scout fly crates.
| **GET A GRIP** | FOR EVERY X SECONDS A LEDGE IS NOT GRABBED, YOU DIE. | A timer counts down from X seconds; if it reaches 0, you die. Grabbing a ledge resets it. The time limit scales with your Time Limit Multiplier.
| **FAST REEL** | YOUR REEL SPEED HAS INCREASED! | The fish during the fish minigame move faster.
| **PALATE CHANGE** | EELS ARE GOOD, YELLOWS ARE BAD. | Their effects are swapped: eels grant 5 pounds, and yellows fail the minigame.
| **JAK BE NIMBLE** | JAK BE QUICK. | Jak moves much faster.
| **SOUL BOND** | IF A LURKER DIES, YOU DIE TOO. |
| **SHIFTY** | JAK RANDOMLY TELEPORTS SHORT DISTANCES. | Jak will be slightly shifted in a random direction at random moments.
| **INTERFERENCE** | ECO PIXELATES THE SCREEN. | The game resolution is reduced by 90% while you have an eco power-up.
| **QUICKSAND** | TIMER DRAINS TWICE AS FAST WHILE ON SAND. |
| **LIGHTS OUT** | SORRY, WERE YOU USING THAT? | Makes the level very dark. Only rolls in Spider Cave.
| **LIMITED TIME OFFER** | POWER CELLS ARE 50% OFF! | Purchasing power cells from villagers and oracles costs half as much.

</details>

## Passes
- A pass lets you completely resolve any active condition. Any rule this is used on will not be considered broken or followed.
- Each pass will require an amount of credits. A credit is rewarded on each rule followed, and the amount needed can be changed in the options menu.
- Using a pass on TWISTED will *not* mark the future rule as twisted.
- To use a pass, press L2+R2.

## Seeds
- This mod supports seeds, which means each run has a sequence of numbers that determines all of its RNG. The seed is displayed on the bottom-left of the screen, and you can use that seed to roll the exact same RNG for another run! This is also nice for races.
- To input a custom seed, access the OpenGOAL toolbar by pressing Left Alt. Then select Tools -> Complicated Seed and input the seed into the box. The next run will use that seed! Leave this blank for a random seed.
- **Note:** The seed's RNG is prone to divergence or branching based on player action. Each condition roll takes into account many factors (your location, orb count, active punishments, etc.), meaning rolls can vary wildly based on where you are and what you do at certain moments. As long as you play the same, the RNG will be the same too!

## Final Score
- The final score is just something fun I added after OutrageousJosh gave me the idea. You can see it during the credits after a completed run.
- Here is everything that changes the score. The harder it makes the run, the more it increases the score:
  - Countdown Start Time
  - Time Limit Multiplier
  - Collectable Increments
  - Followed Rule Increment
  - Number of conditions toggled
  - Number of punishments toggled
  - Final time