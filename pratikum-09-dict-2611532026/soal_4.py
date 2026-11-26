class_list = input().split()
submitted_list = input("Submitted student number: ").split()

submitted_set = set(submitted_list)
not_submitted_set = set(class_list) - submitted_set

print(f"Submitted: {len(submitted_set)} student")
print(f"Not submitted: {len(not_submitted_set)} student")

for num in class_list:
    if num not in submitted_set:
        print(num)