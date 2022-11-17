import numpy as np
from matplotlib import pyplot as plt
import skfuzzy as fl
from skfuzzy import control as ctrl

34
try:
    temp = input('Введите температуру: ')
    temp = float(temp)
    print(temp)
    activity = input('Введите уровень солнечной активности : ')
    activity = int(activity)
    print(activity)
except ValueError:
    print('Пожалуйста, введите корректные значения!')
else:

    temp_arr = np.arange(0, 40, 0.1)
    temp_fuzzy = ctrl.Antecedent(temp_arr, 'temperature')
    activity_arr = np.arange(0, 100, 1)
    activity_fuzzy = ctrl.Antecedent(np.arange(0, 100, 1), 'activity')

temp_fuzzy['cold'] = fl.trapmf(temp_fuzzy.universe, [0.0, 0.0, 15.0, 20.0])
temp_fuzzy['normal'] = fl.trapmf(temp_fuzzy.universe, [15.0, 20.0, 25.0, 30.0])
temp_fuzzy['hot'] = fl.trapmf(temp_fuzzy.universe, [25.0, 30.0, 40.0, 40.0])
plt.plot(temp_arr, temp_fuzzy['cold'].mf, temp_arr, temp_fuzzy['normal'].mf, temp_arr, temp_fuzzy['hot'].mf)
plt.vlines(temp, 0.0, 1.0, 'r')
plt.show()
activity_fuzzy['low'] = fl.trapmf(activity_fuzzy.universe, [0.0, 0.0, 15.0, 20.0])
activity_fuzzy['normal'] = fl.trapmf(activity_fuzzy.universe, [15.0, 25.0, 50.0, 60.0])
activity_fuzzy['high'] = fl.trapmf(activity_fuzzy.universe, [50.0, 65.0, 100.0, 100.0])
plt.plot(activity_arr, activity_fuzzy['low'].mf, activity_arr, activity_fuzzy['normal'].mf, activity_arr, activity_fuzzy['high'].mf)
plt.vlines(activity, 0.0, 1.0, 'r')
plt.show()


blow_arr = np.arange(0.0, 100.0, 0.1)
blow = ctrl.Consequent(blow_arr, 'blow')
blow['low'] = fl.trimf(blow.universe, [0.0, 0.0, 50.0])
blow['medium'] = fl.trimf(blow.universe, [0.0, 50.0, 100.0])
blow['high'] = fl.trimf(blow.universe, [50.0, 100.0, 100.0])


rule1 = ctrl.Rule(temp_fuzzy['cold'] & activity_fuzzy['low'], blow['low'])
rule2 = ctrl.Rule(temp_fuzzy['normal'] & activity_fuzzy['normal'], blow['low'])
rule3 = ctrl.Rule(temp_fuzzy['normal'] & activity_fuzzy['high'], blow['medium'])
rule4 = ctrl.Rule(temp_fuzzy['hot'], blow['high'])

blow_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

climate = ctrl.ControlSystemSimulation(blow_ctrl)
climate.input['temperature'] = temp
climate.input['activity'] = activity
climate.compute()
print('Значение обдува: {}'.format(climate.output['blow']))


plt.plot(blow_arr, blow['low'].mf, blow_arr, blow['medium'].mf, blow_arr, blow['high'].mf)
plt.vlines(climate.output['blow'], 0.0, 1.0, 'r')
plt.show()
