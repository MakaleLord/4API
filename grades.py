
<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');

body {
    text-align:center;
}

table{
  background-color: white;
  border-radius: 3px;
  font-family: 'Open Sans', sans-serif;
  font-size:18px;
  background-color:#34495e;
  table-layout: fixed;
  margin:30px auto;

}

td, th{
  padding:18px;
  border-radius: 3px;
  background-color: #2c3e50;
  color:white;
  box-shadow: 2px 2px 5px #34495e;
  text-align:center;
}

th{
  background-color: #2980b9;
}
</style>

<table><tbody>
<tr>
<th> Name </th>
<th> Marks </th>
<th> Grade </th>
</tr>
<tr>
<td> Jon </td>
<td> 65 </td>
<td> -- </td>
</tr>
<tr>
<td> Dave </td>
<td> 23 </td>
<td> -- </td>
</tr>
<tr>
<td> Thomas </td>
<td> 98 </td>
<td> -- </td>
</tr>
<tr>
<td> Max </td>
<td> 95 </td>
<td> -- </td>
</tr>
<tr>
<td> Tom </td>
<td> 58 </td>
<td> -- </td>
</tr>
<tr>
<td> Becky </td>
<td> 19 </td>
<td> -- </td>
</tr>
<tr>
<td> Penny </td>
<td> 91 </td>
<td> -- </td>
</tr>
<tr>
<td> Shreya </td>
<td> 30 </td>
<td> -- </td>
</tr>
<tr>
<td> Lisa </td>
<td> 60 </td>
<td> -- </td>
</tr>
<tr>
<td> George </td>
<td> 85 </td>
<td> -- </td>
</tr>
<tr>
<td> Rihana </td>
<td> 74 </td>
<td> -- </td>
</tr>
</tbody></table>
Here are Tom's grades:
<table><tbody>
<tr>
<th> Name </th>
<th> Marks </th>
</tr>
<tr>
<td> Tom </td>
<td> 58 </td>
</tr>
</tbody></table>
Students who are passing:
<table><tbody>
<tr>
<th> Name </th>
<th> Marks </th>
<th> Grade </th>
</tr>
<tr>
<td> Jon </td>
<td> 65 </td>
<td> -- </td>
</tr>
<tr>
<td> Thomas </td>
<td> 98 </td>
<td> A+ </td>
</tr>
<tr>
<td> Max </td>
<td> 95 </td>
<td> A </td>
</tr>
<tr>
<td> Penny </td>
<td> 91 </td>
<td> A- </td>
</tr>
<tr>
<td> Lisa </td>
<td> 60 </td>
<td> -- </td>
</tr>
<tr>
<td> George </td>
<td> 85 </td>
<td> -- </td>
</tr>
<tr>
<td> Rihana </td>
<td> 74 </td>
<td> -- </td>
</tr>
</tbody></table>
Students who are failing:
<table><tbody>
<tr>
<th> Name </th>
<th> Marks </th>
<th> Grade </th>
</tr>
<tr>
<td> Dave </td>
<td> 23 </td>
<td> Fail </td>
</tr>
<tr>
<td> Tom </td>
<td> 58 </td>
<td> Fail </td>
</tr>
<tr>
<td> Becky </td>
<td> 19 </td>
<td> Fail </td>
</tr>
<tr>
<td> Shreya </td>
<td> 30 </td>
<td> Fail </td>
</tr>
</tbody></table>
Student with highest grade:
<table><tbody>
<tr>
<th> Name </th>
<th> max(Marks) </th>
</tr>
<tr>
<td> Thomas </td>
<td> 98 </td>
</tr>
</tbody></table>
#!/usr/bin/python3

import cgitb
cgitb.enable()

print("Content-type:text/html")
print()

import sqlite3
connection = sqlite3.connect('database/school.db')
sql = connection.cursor()

from helper import show_data

sql.execute('''
Create table if not exists grading(
   Name Text,
   Marks Integer,
   Grade Text
)''')

sql.execute('''Insert into grading values
               ("Jon", 65, "--"),
               ("Dave", 23, "--"),
               ("Thomas", 98, "--"),
               ("Max", 95, "--"),
               ("Tom", 58, "--"),
               ("Becky", 19, "--"),
               ("Penny", 91, "--"),
               ("Shreya", 30, "--"),
               ("Lisa", 60, "--"),
               ("George", 85, "--"),
               ("Rihana", 74, "--")
''')

data = sql.execute("select * from grading")
show_data(data)

print("Here are Tom's grades:")
tom_data = sql.execute('''select Name, Marks from grading
            where Name = "Tom"''')
show_data(tom_data)

sql.execute('''update grading
                 set grade = "A"
                 where Marks >= 90''')

sql.execute('''update grading
                 set grade = "A+"
                 where Marks > 97 and Marks <= 100''')

sql.execute('''update grading
                 set grade = "A-"
                 where Marks >= 90 and Marks < 94''')



sql.execute('''update grading
                 set grade = "Fail"
                 where Marks < 60 ''')


print("Students who are passing:")
passed_data = sql.execute('''select * from grading
               where Marks >= 60''')
show_data(passed_data)

print("Students who are failing:")
passed_data = sql.execute('''select * from grading
               where Marks < 60''')
show_data(passed_data)

print("Student with highest grade:")
highest_grade = sql.execute('''select Name, max(Marks) from grading''')
show_data(highest_grade)
