# Colored Graph Grouping
This is a demo project to show a problem:
- You are given a directed acyclic graph, $G = (V,E)$
- Each vertex in $V$ contains a "coloring/protocol" (think of this as a machine to be computed on).
- $f : V \to C$, where $C$ is the set of colors

We want to find a sorting of the nodes such that:
- For all $e = (v_1, v_2) \in E$, $v_1$ is ordered before $v_2$
- Minimize the number of "color/protocol" changes. That is, for each consecutive $v_i, v_j$ in the sort, there is a change if $f(v_i) \neq f(v_j)$

**Example**
![image](https://github.com/willwng/colored-tree-grouping/assets/8275672/e054caf5-f0d0-4e10-860a-10c11f228855)
![image](https://github.com/willwng/colored-tree-grouping/assets/8275672/019989a2-7a84-4793-9d58-e458f9814bae)

The following ordering is not optimal since we sort by all the red, then green, then blue
