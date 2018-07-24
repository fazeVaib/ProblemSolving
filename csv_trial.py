import csv

with open('example.csv', 'r') as examplefile:
    exampleReader = csv.reader(examplefile)
    for row in exampleReader:
        print("Row #" + str(exampleReader.line_num) + " " + str("".join(row)))

examplefile.close()

with open('newfile.csv','w') as newfile:
    newWriter = csv.writer(newfile)
    newWriter.hea
    newWriter.writerow(["hello", 'my', 'name', 'is'])
    newWriter.writerow(["hello2", 'my2', 'name2', 'is2'])
    newWriter.writerow(["hello3", 'my3', 'name3', 'is3'])

newfile.close()

