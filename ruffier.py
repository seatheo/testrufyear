''' Модуль для розрахунку результатів проби Руa’є.
    S = 4* (P1 + P2 + P3)

Індекс Руф’є  
   IR = (S - 200) / 10
оцінюється за таблицею відповідно до віку:
           7-8             9-10             11-12          13-14                15+ 
                                                                      (тільки для підлітків!)
чуд.    6.4 і менше    4.9 і менше       3.4 і менше    1.9 і менше          0.4 і менше
доб.    6.5 - 11.9     5 - 10.4          3.5 - 8.9      2 - 7.4              0.5 - 5.9
задов.  12 - 16.9      10.5 - 15.4       9 - 13.9       7.5 - 12.4           6 - 10.9
слабкий 17 - 20.9      15.5 - 19.4       14 - 17.9      12.5 - 16.4          11 - 14.9
незад.  21 і більше    19.5 і більше     18 і більше    16.5 і більше        15 і більше
'''
txt_index = "Ваш індекс Руф’є:"
txt_workheart = "Працездатність серця:"
txt_nodata = ''' Немає даних для такого віку '''
txt_res = []
txt_res.append(''' Низька. Терміново зверніться до лікаря! ''')
txt_res.append(''' Задовільна. Зверніться до лікаря! ''')
txt_res.append(''' Середня. Можливо, варто додатково обстежитись у лікаря. ''')
txt_res.append(''' Вище середнього ''')
txt_res.append(''' Висока ''')


def ruffier_index(P1, P2, P3):
    return (4 * (P1+P2+P3) - 200) / 10


def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2 
    result = 21 - norm_age * 1.5
    return result
  
def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4 
    if r_index >= level:
        return 1
    level = level - 5 
    if r_index >= level:
        return 2
    level = level - 5.5 
    if r_index >= level:
        return 3
    return 4 


def test(P1, P2, P3, age):
   
   if age < 7:
       return (txt_index + "0", txt_nodata) 
   else:
       ruff_index = ruffier_index(P1, P2, P3) 
       result = txt_res[ruffier_result(ruff_index, neud_level(age))] 
       res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
       return res