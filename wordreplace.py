def replace_world():


    str = "Hi guys i am vision"
    world_to_replace = input("Enter the world to replace")
    world_replacemen =input('Enter the word to replce')
    abc = str.find(world_to_replace)
    str = str.replace(world_to_replace,world_replacemen)
    return str

print(replace_world())