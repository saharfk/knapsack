# dar inja meghdare value ra be tabe midahim va key ra migirim
def findKey(val, dictionary):
    for key, value in dictionary.items():
        if value == val:
            return key


# meghdardehi hae avalie
budget = 24
w = [4, 5, 2, 8, 3, 1, 6, 7]
v = [11, 12, 5, 18, 8, 2, 14, 21]
taghsim = {}
taghsim_values = []

# marhale anjame taghsim ha ba do raghame aashar
for i in range(len(w)):
    taghsim[i] = float("%0.2f" % (v[i] / w[i]))
    taghsim_values.append(float("%0.2f" % (v[i] / w[i])))

# print javab taghsim ha
print('hasele sotune taghsim : ')
for j in range(len(taghsim_values)):
    print(taghsim_values[j])

sorted_v = []
sorted_w = []
print("\narraye sort shode : ")
taghsim_values = sorted(taghsim_values)
# j = akharin khune list = bozorgtrin value
j = len(taghsim_values) - 1
# sort array
for i in range(len(taghsim_values)):
    index = findKey(taghsim_values[j], taghsim)
    sorted_v.append(v[index])
    sorted_w.append(w[index])
    print(w[index], v[index])
    j -= 1
# mohasebe R
print('\nR : ')
new_w = []
new_v = []
i = 0
while True:
    try:
        if new_w[i - 1] + sorted_w[i] > budget:
            i -= 1
            break
    except:
        pass
    if i == 0:
        new_v.append(sorted_v[i])
        new_w.append(sorted_w[i])
        print(new_w[i], new_v[i])
        i += 1
    else:
        new_v.append(new_v[i - 1] + sorted_v[i])
        new_w.append(new_w[i - 1] + sorted_w[i])
        print(new_w[i], new_v[i])
        i += 1

first_lower_bound = new_v[i]
print("\nfirst lower bound :", first_lower_bound)
upper_bound = int(new_v[i - 1] + ((budget - new_w[i - 1]) * sorted_v[i]) / sorted_w[i])
print('\nupper bound :', upper_bound)

# mohasebe second lower bound
j = i
i += 1
second_lower_bound = 0
while True:
    if new_w[j] + sorted_w[i] < budget:
        second_lower_bound = new_v[j] + sorted_v[i]
        break
    else:
        i += 1
print('\nsecond lower bound :', second_lower_bound)
