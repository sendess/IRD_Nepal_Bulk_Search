import spacy
import csv
import time

def calculate_text_accuracy(text1, text2):
    nlp = spacy.load("en_core_web_sm")

    # Create Doc objects for the two text passages
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    # Calculate the cosine similarity between the two Doc objects
    cosine_similarity = doc1.similarity(doc2)

    # Calculate the accuracy percentage
    accuracy_percentage = cosine_similarity * 100

    return accuracy_percentage


with open(r".\final list\compare_list.txt","r")as f:
    data_txt = f.readlines()
data_txt = [d.strip().split(',') for d in data_txt]


start = time.time()
count = 0
with open(r".\final list\match_result.csv",'w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    for original,found in data_txt:
        accuracy = calculate_text_accuracy(original.lower(),found.lower())
        if accuracy == 100:
            flag = f"Exactly match"
            tail = f"{accuracy:.2f}"
        elif accuracy >=90:
            flag = f"{accuracy:.2f} % matching name"
            tail = f"{accuracy:.2f}"
        else:
            print(f"{count}){original}\t\t{found}\t\t\t{accuracy:.2f}")
            flag = f"{original} and {found} quiet not same"
            tail = f"{accuracy:.2f}"
        count += 1
        name = [original,found,flag,tail]
        writer.writerow(name)
    
end = time.time()

elapsed = end-start
print(f"elapsed time = {elapsed}")
# # Example usage
# text1 = "White Hat Engineering And Construction Pvt Ltd"
# text2 = "White Hat Engineering And Construction"

# accuracy_percentage = calculate_text_accuracy(text1, text2)
# print(f"The texts are {accuracy_percentage:.2f}% accurate to each other.")