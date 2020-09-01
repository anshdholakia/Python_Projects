# class Dad:
#     basketball=1
#
#
# class Son(Dad):
#     dance=1
#     def isdance(self):
#         return f"Yes I dance {self.dance} number of times"
#
# class Grandson(Son):
#
#
#     dance=6
#
#     def isdance(self):
#
#         return f"Dancer " \
#              f"Yes I dance ballet {self.dance} no of times"
#
#
#
# kane=Dad()
# debruyne=Son()
# Ansh=Grandson()
#
# print(Ansh.basketball)



class Electronic_Device:
    Quantity =100

class Pocket_gadgets(Electronic_Device):
    Carriable_Rating=8
    def Rating(self):
        return f"I am rated as {self.Carriable_Rating}/10 as the most carried device"


class phone(Pocket_gadgets):
    def Rating(self):
        return f"I am a phone and"\
            f"have the most {self.Carriable_Rating} rating as the most carried item"


nokia=Electronic_Device()
samsung=Pocket_gadgets()
HP=phone()

print(HP.Rating())