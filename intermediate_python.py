my_employees = [
  {
    'name': 'Taraneh',
    'age': 36,
    'salary': 50000,
    'title': 'Junior Accountant',
    'responsibilities': [
      'cashing checks',
      'transferring wires',
      'balancing account'
    ]
  },
  {
    'name': 'Juan',
    'age': 63,
    'salary': 100000,
    'title': 'Senior Accountant',
    'responsibilities': [
      'task1',
      'task2',
      'task3'
    ]
  },
  {
    'name': 'Randell',
    'age': 30,
    'salary': 75000,
    'title': 'Accountant I',
    'responsibilities': [
      'task1',
      'task2',
      'task3'
    ]
  }
]

print(my_employees[0]['responsibilities'][2])

new_employee = {
  'name': 'John',
  'age': 26,
  'salary': 40000,
  'title': 'Intern',
  'responsibilities': [
    'task1',
    'task2',
    'task3'
  ]
}

my_employees.append(new_employee)
print(my_employees)
