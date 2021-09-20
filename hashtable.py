'''
HashMaps are a type of data sctructure in Computer Science, that store a value with its key.
This type o data structure is useful for searching in big databases since its time complexity
is O(1), being a fast way to find the specific data the user needs.
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_hash_table()

    def create_hash_table(self):
        return [[] for i in range(self.size)]
    
    def insert_value(self, key, value):
        # Use Python's hash function to create a value for the key
        hash_key = hash(key) % self.size
        # Insert hash key in position
        pos = self.hash_table[hash_key]

        # Checking if key exists before inserting
        found_key = False
        for index, element in enumerate(pos):
            i_key, i_val = element
            if i_key == key:
                found_key = True
                break # If it's found, break and stop the loop
        if found_key:
            pos[index] = (key, value)
        else:
            pos.append((key, value))

    def get_value(self, key):
        hash_key = hash(key) % self.size
        pos = self.hash_table[hash_key]

        found_key = False
        for index, element in enumerate(pos):
            i_key, i_val = element
            if i_key == key:
                found_key = True
                break # If it's found, break and stop the loop
        if found_key:
            print('Item at position', i_key, ':', i_val)
            return i_val
        else:
            return "No value found for key."
    
    def delete_val(self, key):
        hash_key = hash(key) % self.size
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

# Testing the implementation

hashTable = HashTable(10)
hashTable.insert_value(1, 'Renata')
hashTable.insert_value(5, 'Joao')
print('Inserted values: ', hashTable)

hashTable.get_value(5)

hashTable.delete_val(1)
print('Deleted values: ', hashTable)

'''
Output: 
Inserted values:  [][(1, 'Renata')][][][][(5, 'Joao')][][][][]
Item at position 5 : Joao
Deleted values:  [][][][][][(5, 'Joao')][][][][]
'''
