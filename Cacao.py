class Cacao:
    def __init__(self, type="", clasification="", humedity=0.0, price=0.0):
        self.type = type
        self.clasification = clasification
        self.humedity = humedity
        self.price = price

    def get_cacao_type(self):
        while True:
            print("Insert cacao type:")
            print("1. National")
            print("2. Criollo")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.type = "National"
                break
            elif choice == "2":
                self.type = "Criollo"
                break
            else:
                print("Invalid option, try again.")

    def get_cacao_clasification(self):
        while True:
            print("Insert cacao clasification:")
            print("1. Seco")
            print("2. Mojado")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.clasification = "Seco"
                break
            elif choice == "2":
                self.clasification = "Mojado"
                break
            else:
                print("Invalid option, try again.")



    def get_cacao_properties(self):
        # Call the other method on self
        self.get_cacao_type()
        self.get_cacao_clasification()
        self.humedity = float(input("Insert cacao humedity: "))
        self.price = float(input("Insert price per libra: "))


    def show_cacao_properties(self):
        print(f"Cacao type: {self.type}")
        print(f"Clasification: {self.clasification}")
        print(f"Humidity: {self.humedity}")
        print(f"Price per libra: {self.price}")


# Create a Cacao object and run
cacao = Cacao()
cacao.get_cacao_properties()
cacao.show_cacao_properties()



