'''
HashMaps are a type of data sctructure in Computer Science, that store a value with its key.
This type o data structure is useful for searching in big databases since its time complexity
is O(1), being a fast way to find the specific data the user needs.
'''
import math
from random import random
from random import seed
from random import randint
from random import randint, randrange
import tracemalloc

class Empregado:    
    def insere_empregado(self, codigo, salario, setor):
        empregado = {
            'codigo': codigo,
            'salario': salario,
            'setor': setor
        }
        return empregado
    
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_hash_table()
        self.colisao = 0

    def create_hash_table(self):
        return [[] for i in range(self.size)]

    def insert_value_modular(self, dictionary):
        key = dictionary['codigo']
        # Use Python's hash function to create a dictionary for the key
        hash_key = key % self.size
        # Insert hash key in position
        pos = self.hash_table[hash_key]
        # Checking if key exists before inserting
        found_key = False
        for index, element in enumerate(pos): 
            i_key, i_val = element
            if i_key == key:
                found_key = True
                self.colisao += 1
                break # If it's found, break and stop the loop
        if found_key:
            pos[index] = (key, dictionary)
        else:
            pos.append((key, dictionary))
        
    def stringify(self, valor):
        string_items = []
        while len(valor) > 0:
            for item in valor:
                chars = [int(c) for c in str(item)]
            valor.remove(item)
            string_items.append(chars)
        return string_items

    def hash_dobra(self, valor):
        hashes = []
        while len(valor) > 0:
            hash_val = 0
            for item in valor:
                while len(item) > 1:
                    str_1 = str(item[0])
                    str_2 = str(item[1])
                    str_concat = str_1 + str_2
                    bifold = int(str_concat)
                    hash_val += bifold
                    item.pop(0)
                    item.pop(0)
                else:
                    if len(item) > 0:
                        hash_val += item[0]
                    else:
                        pass
                hashes.append(hash_val)
            return hashes

    def insert_value_dobra(self, dictionary):
        key = dictionary['codigo']
        stringKey = self.stringify([key])
        hash_key = self.hash_dobra(stringKey)
        # Insert hash key in position
        pos = self.hash_table[hash_key[0]]
        # Checking if key exists before inserting
        found_key = False
        for index, element in enumerate(pos): 
            i_key, i_val = element
            if i_key == key:
                found_key = True
                self.colisao += 1
                break # If it's found, break and stop the loop
        if found_key:
            pos[index] = (key, dictionary)
        else:
            pos.append((key, dictionary))
    
    def hash_multiplicacao(self, valor, tamanho):
        hash_key = math.floor(tamanho*(valor*random() % 1))
        return hash_key

    def insert_value_multiplicacao(self, dictionary):
        key = dictionary['codigo']
        hash_key = self.hash_multiplicacao(key, self.size-1)
        # Insert hash key in position
        pos = self.hash_table[hash_key]
        # Checking if key exists before inserting
        found_key = False
        for index, element in enumerate(pos): 
            i_key, i_val = element
            if i_key == key:
                found_key = True
                self.colisao += 1
                break # If it's found, break and stop the loop
        if found_key:
            pos[index] = (key, dictionary)
        else:
            pos.append((key, dictionary))

    def get_value(self, dictionary):
        key = dictionary['codigo']
        hash_key = key % self.size
        
        key = dictionary['codigo']
        hash_key = self.hash_multiplicacao(key, self.size-1)

        pos = self.hash_table[hash_key]

        found_key = False
        for index, element in enumerate(pos):
            i_key, i_val = element
            if i_key == key:
                found_key = True
                break # If it's found, break and stop the loop
        if found_key:
            print('Empregado com código', hash_key, ':', i_val, '\n')
            return i_val
        else:
            return "Não há registro de empregados com esse código. \n"
    
    def delete_value(self, dictionary):
        key = dictionary['codigo']
        hash_key = key % self.size
        pos = self.hash_table[hash_key]

        found_key = False
        for index, element in enumerate(pos):
            i_key, i_val = element
            if i_key == key:
                found_key = True
                break # If it's found, break and stop the loop
        if found_key:
            pos.pop(index)
        return

    # Just to print the hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

    def get_collision(self):
        return self.colisao    

def codigo(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def populate_table(size, empregados, hashTable, hashFunction):
    if hashFunction == 'modular':
        tracemalloc.start()
        for _ in range(0, size):
            empregado = empregados.insere_empregado(codigo(9), randrange(1000, 100000), randrange(1, 10))
            hashTable.insert_value_modular(empregado)
            # for _ in range(0, 10):
            #     hashTable.get_value(empregado)
        current, peak = tracemalloc.get_traced_memory()
        print('Uso de memória atual:  %.2f MB ' % ((current/1024)/1024), 'Maior uso foi: %.2f MB ' % ((peak/1024)/1024))
        tracemalloc.reset_peak()
        tracemalloc.stop()
        print('Modular -> número de colisões para:', size, ':', hashTable.get_collision())
    elif hashFunction == 'dobra':
        tracemalloc.start()
        for _ in range(0, size):
            empregado = empregados.insere_empregado(codigo(9), randrange(1000, 100000), randrange(1, 10))
            hashTable.insert_value_dobra(empregado)
        print('Dobra -> número de colisões para:', size, ':', hashTable.get_collision())
        current, peak = tracemalloc.get_traced_memory()
        print('Uso de memória atual:  %.2f MB ' % ((current/1024)/1024), 'Maior uso foi: %.2f MB ' % ((peak/1024)/1024))
        tracemalloc.reset_peak()
        tracemalloc.stop()
    else:
        tracemalloc.start()
        for _ in range(0, size):
            empregado = empregados.insere_empregado(codigo(9), randrange(1000, 100000), randrange(1, 10))
            hashTable.insert_value_multiplicacao(empregado)
        print('Multiplicação -> número de colisões para:', size, ':', hashTable.get_collision())
        current, peak = tracemalloc.get_traced_memory()
        print('Uso de memória atual:  %.2f MB ' % ((current/1024)/1024), 'Maior uso foi: %.2f MB ' % ((peak/1024)/1024))
        tracemalloc.reset_peak()
        tracemalloc.stop()

# Testing the implementation
# empregados = Empregado()
# hashTable = HashTable(5000)
# populate_table(5000, empregados, hashTable, 'modular')

# empregados = Empregado()
# hashTable = HashTable(20000)
# populate_table(20000, empregados, hashTable, 'modular')

# empregados = Empregado()
# hashTable = HashTable(100000)
# populate_table(100000, empregados, hashTable, 'modular')

empregados = Empregado()
hashTable = HashTable(5000)
populate_table(5000, empregados, hashTable, 'dobra')

empregados = Empregado()
hashTable = HashTable(20000)
populate_table(20000, empregados, hashTable, 'dobra')

empregados = Empregado()
hashTable = HashTable(100000)
populate_table(100000, empregados, hashTable, 'dobra')

# empregados = Empregado()
# hashTable = HashTable(5000)
# populate_table(5000, empregados, hashTable, 'multiplicacao')

# empregados = Empregado()
# hashTable = HashTable(20000)
# populate_table(20000, empregados, hashTable, 'multiplicacao')

# empregados = Empregado()
# hashTable = HashTable(100000)
# populate_table(100000, empregados, hashTable, 'multiplicacao')
