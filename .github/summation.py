import os 
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
final = total * 1.18
print(f"Total: {total}")
print(f"Final amount: {final}")

   

github_output = os.environ.get("GITHUB_OUTPUT", "")
if github_output:
    with open(github_output, "a") as file:
        file.write(f"total={total}\n")
        file.write(f"final={final}\n")    