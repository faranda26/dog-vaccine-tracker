from storage import load, save

data = load()

def add_dog(dog):
    already_exists = any(
        d["name"] == dog["name"] and d["owner_id"] == dog["owner_id"]
        for d in data["dogs"]
    )
    if already_exists:
        print(f"You already have a dog named '{dog['name']}'.")
        return
    data["dogs"].append(dog)
    save(data)

def add_vaccine(vaccine):
    dog_exists = any(d["id"] == vaccine["dog_id"] for d in data["dogs"])
    if not dog_exists:
        print(f"No dog found with id '{vaccine['dog_id']}'.")
        return
    data["vaccines"].append(vaccine)
    save(data)

def list_dogs():
    if len(data["dogs"]) == 0:
        print("No dogs to list")
    else:
        for dog in data["dogs"]:
            print(f"{dog}\n")

def main():

    while True:
        print("Choose an option:\n")
        print("1. Add Dog\n")
        print("2. List Dogs\n")
        print("3. Add vaccine\n")
        print("4. Quit")
        
        choise = input("\nChoose: ")
        if choise == 1:
            continue
            # add_dog()
        elif choise == 2:
            list_dogs()
            break
        elif choise == 3:
            continue
            # add_vaccine()
        else:
            break



if __name__ == "__main__":
    main()

