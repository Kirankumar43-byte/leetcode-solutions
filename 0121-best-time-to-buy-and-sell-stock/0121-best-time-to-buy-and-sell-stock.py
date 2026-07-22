class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_a=float('inf')
        m_profit=0
        for current in prices:
            min_a=min(current,min_a)
            m_profit=max(m_profit,current-min_a)
        return m_profit