#Author: Edward Inegbenosun
#Purpose: Creating Job File


exp_yes = ("yes","yeah","ya","y","yah","yeh","yep","ye")
exp_no = ("no","na","nah","n","nope")

#string variables ill need for text files
Id_str= "Id"
job_title_str = "JOB TITLE"
location_str = "LOCATION"
exp_str = "EXP"
rate_str = "RATE(€)"
hours_str = "HOURS"
earnings_str = "EARNINGS"
double_line = "="
single_line = "-"

#variables needed for summary
parttime= 0
fulltime= 0
highest_rate = -99999999999
lowest_rate= 99999999999
total_rate=0

#creating the text files and printing the heading
with open("parttime.txt","w") as newfile:
    print(f"{Id_str:3} {job_title_str:16} {location_str:12} {exp_str:5} {rate_str:8} {hours_str:7} {earnings_str:8}\n{double_line*66}", file= newfile)

with open("fulltime.txt","w") as newfile:
    print(f"{Id_str:3} {job_title_str:16} {location_str:12} {exp_str:5} {rate_str:8} {hours_str:7} {earnings_str:8}\n{double_line*66}", file= newfile)

#heading
print(f"Jobs Tracker\n{double_line*10}")

#creating loop for amount of jobs
while True:
    try:
        job_no = int(input("How many jobs would you like to add? "))
        if job_no > 0:
            break
    except:
        print("not valid, try again")

#inputs for user to enter
for i in range (job_no):

    print(f"Enter details of job {i+1}\n{single_line*30}")

    while True:
        try:
            job= str(input("What is the job title: "))
            if len(job) > 0:
                break

        except:
            print("not valid, try again")



    while True:
        try:
            company = str(input("What is the company name: "))
            if len(company) > 0:
                break
        except:
            print("not valid, try again")

    while True:
        try:
            employment_type = int(input("Please specify the employment type \n1. Full time \n2. Part time \n==>"))
            if employment_type == 1 or  employment_type == 2:
                break
        except:
            print("not valid, try again")



    while True:
        try:
            experience = str(input("Does the job require experience? (y/n)? ")).lower()
            if experience in exp_yes:
                experience = "yes"
                break
            elif experience in exp_no:
                experience = "no"
                break
        except:
            print("not valid, try again")


    if employment_type == 2:
        while True:
            try:
                hours = int(input("How many hours per week? "))
                if 40 > hours > 0:
                    break
            except:
                print("Please enter a valid number")
    if employment_type == 1:
        hours = 40


    while True:
        try:
            rate = float(input("Enter the rate paid per hour? €"))
            if rate > 0:
                break
        except:
            print("not valid, try again")

    earnings = rate * hours

    # getting total of rates
    total_rate = total_rate + rate

    #checking if rate is higher than previous rate
    if highest_rate < rate:
        highest_rate = rate
        high_company = company
        high_title = job

    if lowest_rate > rate:
        lowest_rate = rate

    #adding the information to text appropriate text files
    if employment_type == 1:
        fulltime = fulltime + 1
        with open("fulltime.txt", "a") as newfile:
            print(f"{i+1}   {job:17}{company:13}{experience:2}{rate:8.2f}{hours:7}{earnings:10}", file= newfile)

    if employment_type == 2:
        parttime = parttime + 1
        with open("parttime.txt", "a") as newfile:
            print(f"{i+1}   {job:17}{company:13}{experience:2}{rate:8.2f}{hours:7}{earnings:10}", file= newfile)



#creating summary
print(f"SUMMARY\n{double_line*8}")

if fulltime > 0:
    print(f"{fulltime} full time post(s) -  fulltime.txt has been updated")
if parttime > 0:
    print(f"{parttime} part time post(s) -  parttime.txt has been updated")

print(f"\nHourly pay rate  ranges from €{lowest_rate:.2f} to €{highest_rate:.2f}")

#getting average
average= total_rate/ job_no
print(f"\nAverage pay is {average:.2f}")


print(f"\nDetails of highest pay rate: {high_title} at {high_company}")
