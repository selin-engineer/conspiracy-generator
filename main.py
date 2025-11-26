from scripts import aliens

def main():
    print("🛸 Welcome to the Conspiracy Generator!")
    theory = aliens.generate()
    print("Theory of the day:", theory)

if _name_ == "_main_":
    main()
