class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = ""
        cur_str = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                st.append([int(num), cur_str])
                num = ""
                cur_str = ""
            elif c.isalpha():
                cur_str += c
            elif c == ']':
                top_freq, prev_cur = st.pop()
                temp = cur_str * top_freq
                cur_str = prev_cur + temp
        return cur_str
            
