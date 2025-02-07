class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair names and heights together
        people = list(zip(names, heights))

        # Sort by height in descending order
        people.sort(key=lambda x: x[1], reverse=True)

        # Extract the sorted names
        sorted_names = [person[0] for person in people]

        return(sorted_names)