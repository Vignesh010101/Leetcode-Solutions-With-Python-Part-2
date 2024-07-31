class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        op = ''
        total_cols = int(   len(encodedText) / rows )
        row = 0
        col = 0
        while True:
            try:
                calc = (row*total_cols)+row+col
                char = encodedText[calc]
            except IndexError:
                break
            op += char
            row+=1
            if row == rows:
                row = 0
                col+=1
        return op.rstrip()