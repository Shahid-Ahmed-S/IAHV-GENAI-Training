def calc_total(m1, m2, m3):
    total = m1 + m2 + m3
    return total

def calc_avg(m1, m2, m3):
    avg = calc_total(m1, m2, m3) / 3
    return avg


rollno = int(input("Enter Roll No: "))
sname = input("Enter Student Name: ")

m1 = int(input("M1: "))
m2 = int(input("M2: "))
m3 = int(input("M3: "))

total = calc_total(m1, m2, m3)
avg = calc_avg(m1, m2, m3)

print(f"Roll No: {rollno} \nName: {sname} \nTotal Marks: {total} ")
print(f"Average Marks: {avg}")
