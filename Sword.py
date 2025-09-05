class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

# Implementation of a sword upgrade mechanic using index math thinking about future scalability
#     def __add__(self, other):
#       Check for non-Sword operands
#         if not isinstance(other, Sword):
#             return NotImplemented
#         if self.sword_type == other.sword_type and self.sword_type != "steel":
#             sword_types = ["bronze", "iron", "steel"]
#             upgraded_sword = sword_types.index(self.sword_type) + 1
#             return Sword(sword_types[upgraded_sword])
#         else:
#             raise Exception("cannot craft")

# Implementation using mapping for clearer scalability
    upgrades = {"bronze":"iron", "iron":"steel"}

    def __add__(self, other):
#       Check for non-Sword operands
        if not isinstance(other, Sword):
            return NotImplemented
        if self.sword_type == other.sword_type and self.sword_type in Sword.upgrades:
            return Sword(Sword.upgrades[self.sword_type])
        raise Exception("cannot craft")

