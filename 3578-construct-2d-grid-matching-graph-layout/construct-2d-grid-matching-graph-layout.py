class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the degree counts for each node (0 to n-1) with 0
        counts = [0] * n
        
        # Adjacency list (a list of lists) to store neighbors of each node
        data = [[] for _ in range(n)]

        # Step 1: Fill the degree counts and adjacency list based on the given edges
        for a, b in edges:
            # Increase the degree of both nodes a and b as they are connected by an edge
            counts[a] += 1
            counts[b] += 1
            
            # Add each node to the other's adjacency list
            data[a].append(b)
            data[b].append(a)

        # Step 2: Frequency list to categorize nodes by their degree (1, 2, 3, 4)
        # We use a list of lists where index `i` represents the nodes with degree `i`
        freq = [[] for _ in range(max(counts) + 1)]  # max(counts) gives the maximum degree in the graph

        max_count = max(counts)  # Store the max degree, needed later for 4-degree node handling

        # Step 3: Populate the frequency list with nodes categorized by their degrees
        for num, count in enumerate(counts):
            # Append each node `num` to the list representing its degree
            freq[count].append(num)

        # A set to keep track of visited nodes
        visited = set()

        # Step 4: Case 1 - Handling when there are nodes with degree 1
        if freq[1]:
            result = [[]]  # Initialize the result grid (list of lists)
            one = freq[1][0]  # Pick the first node with degree 1
            result[0].append(one)  # Place this node in the first row
            visited.add(one)  # Mark this node as visited

        # Step 5: Case 2 - Handling when there are nodes with degree 4
        elif max_count == 4:
            result = [[]]  # Initialize the result grid
            
            # Pick the first node with degree 2 to start constructing the grid
            two = freq[2].pop()
            result[0].append(two)  # Place this node in the first row
            visited.add(two)  # Mark it as visited

            # Pick one of the neighbors of this 2-degree node to explore next
            curr = data[two][0]
            visited.add(curr)  # Mark it as visited

            # Step 5.1: Traverse through the grid until we find another 2-degree node
            while counts[curr] != 2:
                result.append([])  # Start a new row in the result grid
                result[-1].append(curr)  # Add the current node to this new row
                for num in data[curr]:
                    # Find the next node which is not already visited and is not a 4-degree node
                    if counts[num] != 4 and num not in visited:
                        visited.add(num)  # Mark this node as visited
                        curr = num  # Move to the next node
                        break

            # Add the last 2-degree node to the grid (fence node)
            result.append([])  # Start a new row for the last 2-degree node
            result[-1].append(curr)  # Add this node to the last row

        # Step 6: Case 3 - Handling when there are no degree 4 nodes (resulting in a 2-column grid)
        else:
            result = [[], []]  # Initialize the result grid as 2 columns (two empty lists)

            # Pick the first node with degree 2
            two = freq[2][0]
            result[0].append(two)  # Place this node in the first column of the first row
            visited.add(two)  # Mark it as visited

            # Find the adjacent node with degree 2 and place it in the second column
            for num in data[two]:
                if counts[num] == 2 and num not in visited:
                    visited.add(num)  # Mark this node as visited
                    result[1].append(num)  # Place it in the second column of the first row
                    break

        # Step 7: Fill the grid with the remaining nodes by visiting unvisited neighbors
        for _ in range(n // len(visited) - 1):  # Loop until we have visited all nodes
            for i, row in enumerate(result):
                last = row[-1]  # Get the last element of the current row
                for num in data[last]:
                    if num not in visited:  # If this neighbor is not visited
                        visited.add(num)  # Mark it as visited
                        row.append(num)  # Add it to the current row
                        break

        # Return the constructed grid layout
        return result