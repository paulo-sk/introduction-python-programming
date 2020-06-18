def world_war():
    alliance_world_war_win = input("What alliance win the wolrd war 2? ")
    end_world_war = input("When did world war 2 end? ")
    # o retorno e uma tupla
    return alliance_world_war_win, end_world_war

def main():
    world_war_info = world_war()
    print(f"The war was won by {world_war_info[0]} and the war ended in {world_war_info[1]}")
    print(type(world_war_info))

if __name__ == "__main__":
    main()