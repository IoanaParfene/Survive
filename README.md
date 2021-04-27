# Survive
An implementation of the mobile game [Survive](https://play.google.com/store/apps/details?id=com.sandbaygames.survive).

## Type of Game:
  * Single Player
  * Perma-death
  * Android
  * Survival
  * Simulation
  * RPG
  * Crafting

## Core Gameplay - [Download for Android](https://drive.google.com/file/d/17hWR_fhJWUXVsCTYsNLl4vXYGPhCv32P/view?usp=sharing)
&nbsp;&nbsp;&nbsp;&nbsp;**Survive** a long, challanging, resource-scarce journey back to the main road, after getting lost
in the woods on a rainy night. **Forage** for wood, berries, water and vines. **Hunt**, **fish**, **rest**, **cook** and **craft** campfires, weapons, traps, bandages and clothing insulators. <br>
&nbsp;&nbsp;&nbsp;&nbsp;**Travel**, take different turns and make **strategic** choices in order to reach civilization before it is too late. Balance **hunger, temperature, thirst, health** and inventory to avoid **starvation,
hypothermia, dehydration*** and **illness**. <br>
&nbsp;&nbsp;&nbsp;&nbsp;Stay alive or **permanently lose** the game and start over!

<hr style="border:2px solid gray"> </hr>

## Progress - [Review Document](https://docs.google.com/document/d/18p3ZqKusjmE7E0jQpLz9sB5ZGjo3yPsahlz2MbFhpps/edit)

### Week 2
Started a **Python/PyGame** prototype. 

#### Researched - Excel files
   * **Actions** - Requirements, Outcome, Duration
   * **Inventory Items** - Categories, Weight, Actions+Outcomes

#### Implemented
  * **Inventory Class** + JSon item parsing
  * **Game Time** - day/night
  * **Status bars** - with decay over time
  * **Gameplay Menu Buttons** - Shelter, Fire, Inventory, etc <br>

### Week 3 - DONE
Continued to implement the prototype.

#### Researched
 * Location/Condition/Actions
 * Crafting
 * Traps/Hunting
 * Injury/Illness

#### Implemented
* Sleep 
* Location 
* Travel 
* Game Over/ Game Won
* Some items in inventory + Actions 
* Fire Starting 

### Week 4 - DONE
Continued to implement the prototype.

#### Implemented
* New Game
* Save/Load

### Week 5 - DONE
Started converting code to Kivy

#### Implemented
* Converted most code(Remaining Inventory and Fire)
* Added GUI Components

### Week 6 - DONE
* Created an Inventory Template, found a way to make an Android APK

#### Implemented
* Item Sloths
* Inventory Categories

### Week 7 - DONE
* Created exploration and a functional inventory with all items and their actions 

#### Implemented
* Throwing Items Away
* Eating
* Drinking
* Bandaging
* Cutting/Slicing to obtain new items
* Hunger based Travel
* Locations and their attributes, including resources
* Randomized resource lists for each new location
* Exploration of current location until the resource list is empty

### Week 8 - DONE
* Cleaned up the code, removed bugs, added features

#### Clean Up
* Created new .py files
* Separated screens
* Separated .kv files
* Added comments

#### Bugs Removed
* No more death on calorie deficit
* No crash on empty inventory slot press

#### New Features
* Remade all loading/waiting/action screens
* Added action result screens
* Added wood getting
* Cellphone has space=1
* Weight became space
* Fire screen item quantity labels added
* Wood can be scraped to tinder
* Status bars go below 0 without ruining value increase

### Week 9 - DONE
* Cleaned up the code, removed bugs, added features

#### New Features
* Heat decay based on: clothing, day/night, fire, rain, shelter
* Added rain
* Added a rain catcher
* Added water collecting

### Week 10 - DONE
* Cleaned up the code, removed bugs, added features

#### Bugs Removed
* Fixed raincatcher bug that allows bringing trash bag water to new location
* No crash on a specific heat code

#### New Features
* Implemented space adding items
* Boil Water
* Collect dirty water
* Area map destruction removes knowledge of remaining miles
* Dirty water removes condition
* Water bottles can be poured out
* Flashlight allows seeing direction, exploration and getting wood at night
* Nightime stops player from exploring and getting wood 8/10 times
* Exceeding inventory blocks player from travelling
* Building a rain catcher takes 15 minutes

