import matplotlib.pyplot as plt

expenditure_items=('food','clothing','transport','rent','Entertainment')
amounts_spent=[35,20,21,100,50]
h_pos=[1,2,3,4,5]

plt.bar(h_pos,amounts_spent)
plt.xticks(h_pos,expenditure_items)
plt.ylabel('Amount Spent')
plt.title('My Weekly Expenditure')
plt.show()