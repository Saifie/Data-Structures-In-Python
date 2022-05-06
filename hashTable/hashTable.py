from array import array


class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size

    def __hash(self,key):
        my_hash = 0
        for letter in key :
            my_hash=(my_hash+ord(letter)*23) % len(self.data_map)
        return my_hash    

    def printing(self):
        for i,val in enumerate(self.data_map):
            print(i,val)    

    def set_item(self,key,value):
        index=self.__hash(key)
        if(self.data_map[index]==None):
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index=self.__hash(key)
        if(self.data_map[index] is not None):
            for j in range(len(self.data_map[index])):
                if(self.data_map[index][j][0]==key):
                    return self.data_map[index][j][1]
        return None            
    def keys(self):
        array=[]
        for i in range(len(self.data_map)):
            if(self.data_map[i] is not None):
                for j in range(len(self.data_map[i])):
                    array.append(self.data_map[i][j][0])
        return array            





hashe=HashTable()
hashe.set_item("heythere",600)
hashe.set_item("by",500)
hashe.set_item("heythere",600)
# print(hashe.get_item("heythere"))
print(hashe.keys())

# hashe.printing()