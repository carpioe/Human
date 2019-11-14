class human():

    def __init__(self,name,age,gender,profession):
        self.name = name
        self.age = age
        self.gender = gender
        self.profession = profession

    def description(self):
        print(f"""My name is {self.name},my age is {self.age}I am a {self.gender}.
                and my profession is {self.profession}""")


