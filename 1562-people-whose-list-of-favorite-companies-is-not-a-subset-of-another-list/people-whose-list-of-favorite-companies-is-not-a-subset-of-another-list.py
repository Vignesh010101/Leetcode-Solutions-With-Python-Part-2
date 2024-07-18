class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        answer: list = []
        favoriteCompanies = [set(companies) for companies in favoriteCompanies]

        for index, companies in enumerate(favoriteCompanies):
            controller: bool = False
            for others in favoriteCompanies:
                if companies != others and others >= companies:
                    controller = True
                    break

            if not controller: answer.append(index)
            
        answer.sort()
        return answer