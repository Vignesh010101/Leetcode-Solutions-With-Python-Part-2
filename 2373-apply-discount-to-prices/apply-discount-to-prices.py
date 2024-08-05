class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        return " ".join([f"${(float(x[1:])*(1-(discount/100))):.2f}" if x.startswith("$") and len(x) > 1 and x[1:].isnumeric() else x for x in sentence.split()])