# Basal metabolic rate calculator

from curses.ascii import isdigit
from enum import Enum

# The biological sex of an individual from birth.
class Sex(Enum):
    MALE = 1
    FEMALE = 1

# Calculates someone's BMR using the Harris-Benedict formula (1990 rev.).
class HarrisBenedictBMR:
    sex: Sex
    age: int
    height_cm: float
    weight_kg: float

    def __init__(self, sex, age, height_cm, weight_kg):
        self.sex = sex
        self.age = age
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    # Returns the BMR for an individual.
    def calculate(self) -> float:
        if self.sex == Sex.MALE:
            return 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age + 5
        else:
            return 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age - 161

def interp(start, end, value):
    return (end - start) * value + start

sex_str = input('Biological sex (M/F): ')
match sex_str.lower():
    case 'm':
        sex = Sex.MALE
    case 'f':
        sex = Sex.FEMALE
    case _:
        print('You did not enter a valid sex.')
        exit(1)

try:
    age = int(input('Age in years: '))
    height_cm = float(input('Height in cm: '))
    weight_kg = float(input('Weight in kg: '))
except:
    print('Bad input!')
    exit(1)

hb_bmr = HarrisBenedictBMR(sex, age, height_cm, weight_kg)
bmr = hb_bmr.calculate()

print()
print(f'Your BMR is: {bmr} kcal.')
print(f'This means that your body consumes {bmr} calories every day to stay alive.')
print()

try:
    print('Physical activity level examples: ')
    print(' * Sedentary or light: 2-3')
    print(' * Active or moderately active: 4-5')
    print(' * Vigorously active: 8-9')
    pal_simple = int(input('How physically active are you (1-10): '))
except:
    print('Bad input!')
    exit(1)

pal = interp(1.2, 2.5, pal_simple / 10.0)
maintenance_cal = int(bmr * pal)

print()
print(f'Your maintenance calories is: {maintenance_cal} kcal.')
print(f'This means that if you want to maintain your current weight, you need to eat around {maintenance_cal} calories for your current lifestyle.')
print()

print(f'To gain lean muscle mass, increase to {int(maintenance_cal * 1.10)} calories.')
print(f'To lose body fat, reduce to {int(maintenance_cal * 0.90)} calories.')
print('Re-evaluate once a week.')
