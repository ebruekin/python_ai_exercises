from __future__ import print_function
import random

test_outlook_generator = []
test_temp_generator = []
test_humidity_generator =[]
test_windy_generator = []
test_play_generator = []

outlo = ['sunny','overcast','rainy']
tempr = ['hot','mild','cool']
humid = ['high','normal']
wind = ['TRUE','FALSE']
ply = ['yes','no']

training_data = [[] *49]
training_data.pop(0)

siz = 0
while siz < 50:
    ou = random.randint(0, 2)
    tm = random.randint(0, 2)
    hu = random.randint(0, 1)
    wn = random.randint(0, 1)
    pa = random.randint(0, 1)
    training_data.append([outlo[ou],tempr[tm],humid[hu],wind[wn],ply[pa]])
   
    siz += 1
header = ["outlook", "temprature", "humidity", "windy" , "play"]
a=training_data
print ("The original tarining_data is : " + str(a))  
res = list(set(i for j in a for i in j)) 
print ("Unique values in training_data are : " + str(res)) 

def class_counts(rows):
	results={}
	for row  in rows:
		r=row[len(row)-1]
		if r not in results:
			results[r]=0
		results[r]+=1
	return results



class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
       
        val = example[self.column]
       
        return val == self.value

    def __repr__(self):
       
        condition = "=="
      
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))
         
    
 
def partition(rows, question):
    
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def entropy(rows):
	from math import log
	log2=lambda x:log(x)/log(2)
	results=class_counts(rows)
	
	ent=0.0
	for r in results.keys():
		p=float(results[r])/len(rows)
		ent=ent-p*log2(p)
	return ent

c_uncertainty = entropy(training_data)


def info_gain(left, right, c_uncertainty):
   
    p = float(len(left)) / (len(left) + len(right))
    return c_uncertainty - p * entropy(left) - (1 - p) * entropy(right)

def find_best_split(rows):
   
    best_gain = 0  
    best_question = None 
    c_uncertainty = entropy(rows)
    n_features = len(rows[0]) - 1 
    for col in range(n_features): 

        values = set([row[col] for row in rows])  

        for val in values:  
            question = Question(col, val)

           
            true_rows, false_rows = partition(rows, question)

          
          
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

           
            gain = info_gain(true_rows, false_rows, c_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question



class Leaf:
   
    def __init__(self, rows):
        self.predictions = class_counts(rows)
        
class Decision_Node:
  

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        
def build_tree(rows):
 
    gain, question = find_best_split(rows)

 
    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)

  
    true_branch = build_tree(true_rows)

  
    false_branch = build_tree(false_rows)

    return Decision_Node(question, true_branch, false_branch)



def print_tree(node, spacing=""):
  

    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

   
    print (spacing + str(node.question))

    
    print (spacing + '+ True:')
    print_tree(node.true_branch, spacing + "  ")

  
    print (spacing + '-False:')
    print_tree(node.false_branch, spacing + "  ")


my_tree = build_tree(training_data)

print_tree(my_tree)

def classify(row, node):

    if isinstance(node, Leaf):
        return node.predictions

  
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def print_leaf(counts):
    
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs


testing_data =[

['sunny','hot','high','FALSE','no'],
['sunny','hot','high','TRUE','no'],
['overcast','hot','high','FALSE','yes'],
['rainy','mild','high','FALSE','yes'],
['rainy','cool','normal','FALSE','yes'],
['rainy','cool','normal','TRUE','no'],
['overcast','cool','normal','TRUE','yes'],
['sunny','mild','high','FALSE','no'],
['sunny','cool','normal','FALSE','yes'],
['rainy','mild','normal','FALSE','yes'],
['sunny','mild','normal','TRUE','yes'],
['overcast','mild','high','TRUE','yes'],
['overcast','hot','normal','FALSE','yes'],
['rainy','mild','high','TRUE','no']

]
for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], print_leaf(classify(row, my_tree))))

