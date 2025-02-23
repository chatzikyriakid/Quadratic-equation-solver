print('Quandratic equation solver')
print('---------------------------------------------')
print('Give the three unknowns')

a = float(input('Give a: '))
b = float(input('Give b: '))
c = float(input('Give c: '))

discriminant = (b**2-4*a*c)

if discriminant < 0:
    print('Discriminant is negative so there are no real solutions')   

elif discriminant == 0:
    x = - b / 2*a
    print('There is only one real solution x: {:.3f}'.format(x))

else:
    x1 = (- b + discriminant ** 0.5)/2*a
    x2 = (- b - discriminant ** 0.5)/2*a
    print('There are two real solutions x1\n: {:.3f} and x2: {:.3f}'.format(x1,x2))

print()
input('Press enter to exit')

