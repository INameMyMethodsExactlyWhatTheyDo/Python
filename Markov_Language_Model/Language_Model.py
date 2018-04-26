import datetime
import random

class lang_model:
    
    def __init__(self, filename, degree):
        self.degree = degree
        self.model = {}
        self.cache = {} 
        random.seed(datetime.datetime.second)
        if filename != "":
            input = open(filename, 'r')
            self.data = input.read().split(" ")
            self.print_train(filename)
            self.train_from_text()
        
    def add_to_model(self, prefix, predict, add = 1):
        copy = tuple(prefix)
        if copy in self.model:
            if predict in self.model[copy]:
                self.model[copy][predict] += 1
            else:
                self.model[copy][predict] = 1
        else:
            self.model[copy] = {predict : add} 

    def train_from_text(self):
        prefix = []
        predict = self.data[self.degree]
        for x in range (self.degree):
            prefix.append(self.data[x])

        self.add_to_model(prefix, predict)
        for x in range(self.degree + 1, len(self.data)):
            del prefix[0]
            prefix.insert(len(prefix), predict)
            predict = self.data[x]
            self.add_to_model(prefix, predict)
    
    def flatten_list(self, prefix):
        copy = tuple(prefix)
        flattened_list = []
        if copy not in self.cache:   
            for x in self.model[copy].keys():
                for y in range (0, self.model[copy][x]):
                    flattened_list.insert(len(flattened_list), x)
            self.cache[copy] = tuple(flattened_list)
        return self.cache[copy]

    def write(self, num):
        self.print_write(num)
        prefix = list(random.choice(list(self.model.keys())))
        predict = random.choice(self.flatten_list(prefix))
        a = ""
        for x in prefix:
            a = a + x + " "
        a = a + predict + " "
        for x in range (0, num):
            del prefix[0]
            prefix.insert(len(prefix), predict)
            try:
                predict = random.choice(self.flatten_list(prefix))
            except KeyError as e:
                prefix = list(random.choice(list(self.model.keys())))
                predict = random.choice(self.flatten_list(prefix))
            a = a + predict + " "
        print(a)

    def __add__ (self, other):
        if self.degree != other.degree:
            print("Cannot combine models that have different degrees")
            return
        ret = lang_model("", self.degree)
        for x in self.model.keys():
            for y in self.model[x].keys():
                ret.add_to_model(x, y, self.model[x][y])
        for x in other.model.keys():
            for y in other.model[x].keys():
                ret.add_to_model(x, y, other.model[x][y])
        return ret

    #for debugging pruposes
    def print_train(self, filename):
        print("---------------------------------------------------")
        print("Training model off of: " + filename)
        print("---------------------------------------------------\n")
    def print_write(self, num):
        print("---------------------------------------------------")
        print("Generating " + str(num) + " word text from model")
        print("---------------------------------------------------")
    def print_text(self):
        for x in self.data:
            print(x)
    def print_model(self):
        for x in self.model.keys():
            print(x)
            print()
            for y in self.model[x].keys():
                print("\t" + str(y) + ":" + str(self.model[x][y]))
    def print_ran(self):
        print(random.randint(0, 10))
                
