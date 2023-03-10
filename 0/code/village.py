a = []
for i in range(0,34):
    b=[]
    for j in range(0,140):
       b.append(" ")
    a.append(b)

for i in range(0,140):
    a[0][i]="X"
    a[33][i]="X"

for i in range(0,34):
    a[i][139]="X"
    a[i][0]="X"

for i in range(63,79):
    a[9][i]="o"
    a[20][i]="o"

for i in range(14,20):
    for j in range(67,74):
       a[i][j]="T"

for i in range(17,20):
    for j in range(64,67):
       a[i][j]="T"
       a[i][j+10]="T"


for i in range(9,21):
    a[i][63]="o"
    a[i][78]="o"


a[13][67]="^"
a[13][73]="^"
a[12][68]="^"
a[12][72]="^"
a[11][69]="^"
a[11][71]="^"
a[10][70]="^"


for i in range(0,34):
    for j in range(0,140):
       print(a[i][j],end="")
    print()


    

   
