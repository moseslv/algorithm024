学习笔记


动态规划的重点：
	1. 判断是否存在最小可拆分重复子问题
	2. 思考状态转移函数如何构造



以三角形最小路径和为例：

分析：
若定义 f(i, j)f(i,j) 为 (i, j)(i,j) 点到底边的最小路径和，则易知递归求解式为:

f(i, j) = min(f(i + 1, j), f(i + 1, j + 1)) + triangle[i][j]f(i,j)=min(f(i+1,j),f(i+1,j+1))+triangle[i][j]

由此，我们将任一点到底边的最小路径和，转化成了与该点相邻两点到底边的最小路径和中的较小值，再加上该点本身的值。这样本题的 递归解法（解法一） 就完成了。



作者：sweetiee
链接：https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。