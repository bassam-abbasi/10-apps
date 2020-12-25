import actors
import random

def print_header():
    print('----------------------------')
    print('    Game Wizard')
    print('----------------------------')


def game_loop():

    hero = actors.Wizard('Gandolf',5)
    print(hero)

    creatures = [actors.Creature('Toad',1), actors.Creature('Tiger', 12), actors.Creature('Bat', 3), actors.Creature('Dragon', 50), actors.Creature('Evil Wizard',1000)]
    
    

    while True:
        creature = random.choice(creatures)
        print('A {} with level {} has appeard from Dark and foggy forest'.format(creature.name, creature.level))
        cmd =  input("What do you want to do? [a]ttack, [r]un away, or [l]ook around: ")
        cmd = cmd.lower().strip()
        if cmd == 'a':
            hero.attack(creature)
        elif cmd== 'r':
            print("run away")
        elif cmd == 'l':
            print("look around")
        else:
            print("Exiting...")
            break
    print("existing the game loop")


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()