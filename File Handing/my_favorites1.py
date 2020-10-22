import csv

title = input('title : ').strip().upper()
 
# titles = {}
with open('src7/favorites/Favorite TV Shows - Form Responses 1.csv','r') as file:
    reader = csv.DictReader(file)
    
    counter = 0
    for row in reader:
    #     title = row['title'].strip().upper()

    #     if title in titles:
    #         titles[title] += 1
    #     else:
    #         titles[title] = 1

        
        if (row['title'].strip().upper() == title):
            counter += 1

    print(counter)

# for title in sorted(titles, key= lambda title : titles[title], reverse=True):
#     print(title, titles[title])