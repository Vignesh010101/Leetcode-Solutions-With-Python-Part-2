class FrequencyTracker:
    def __init__(self):
        self.map = {} # Dictionary to store the count of each number
        self.frequency = [0] * (10**5 + 1) # List to store the frequency of each count

    def add(self, number):
        freq = self.map.get(number, 0) # Get the current count of the number
        if freq > 0 and self.frequency[freq] > 0: # If the current count is already present, decrement its frequency
            self.frequency[freq] -= 1
        self.map[number] = freq + 1 # Increment the count of the number in the map
        self.frequency[self.map[number]] += 1 # Increment the frequency of the new count in the frequency list

    def deleteOne(self, n):
        count = self.map.get(n, 0) # Get the current count of the number
        if count > 0:
            self.frequency[count] -= 1 # Decrement the frequency of the current count in the frequency list
            if count == 1:
                del self.map[n] # If the count is 1, remove the number from the map
            else:
                self.map[n] = count - 1 # Decrement the count of the number in the map
                self.frequency[self.map[n]] += 1 # Increment the frequency of the new count in the frequency list

    def hasFrequency(self, number):
        return number < len(self.frequency) and self.frequency[number] > 0 # Check if the frequency of the given number is greater than 0