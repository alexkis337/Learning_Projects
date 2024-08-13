class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
    # add more parameters here

  def est_cost(self):
    self.insurance_cost = 250 * self.age + 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    return self.insurance_cost

  def upd_age(self, new_age):
    self.age = new_age
    self.est_cost()
    return print(f'{self.name} is now {self.age} years\nUpdate insurance cost is: {self.est_cost()}')

  def upd_children(self, new_num_of_children):
    self.num_of_children = new_num_of_children
    children_form = 'children' if self.num_of_children != 1 else 'child'
    return print(f'{self.name} has now {self.num_of_children} {children_form}\nUpdate insurance cost is: {self.est_cost()}')

  def patient_profile(self):
    patient_information = {"Name": self.name,
                           "Age": self.age,
                           "Sex": 'Male' if self.sex == 1 else 'Female',
                           "BMI": self.bmi,
                           "Number of Children": self.num_of_children,
                           "Smoker": 'No' if self.smoker == 0 else 'Yes'}
    return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 1, 0)
print(patient1.name, patient1.age)
print('Insurance cost is ', patient1.est_cost())
patient1.upd_age(27)
patient1.upd_children(1)

print(patient1.patient_profile())