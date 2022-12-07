#Defining School Class
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

#This is the "PrimarySchool Class"

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    return super().__repr__() + " " + f"Also, the pickup policy is {self.pickupPolicy}"

#This is the 'HighSchool' Class:

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = []
    self.sportsTeams.append(sportsTeams)

  def get_sportsTeams(self):
    return sportsTeams

  def set_sportsTeams(self, sportsTeams):
    self.sportsTeams.append(sportsTeams)

  def __repr__(self):
    return super().__repr__() + " " + f"and the sports Teams are {self.sportsTeams}"

hs1 = HighSchool("Freedom High", 1000, "Fighters")

hs1.set_sportsTeams("Titans")

print(hs1)


penn_elementary = School("Penn Elementary", "Primary", 200)

print(penn_elementary)
print(penn_elementary.get_name())
print(penn_elementary.get_level())
print(penn_elementary.get_numberOfStudents())

penn_elementary.set_numberOfStudents(250)

print(penn_elementary.get_numberOfStudents())

ps1 = PrimarySchool("Unity Reed", 500, "School Bus")
