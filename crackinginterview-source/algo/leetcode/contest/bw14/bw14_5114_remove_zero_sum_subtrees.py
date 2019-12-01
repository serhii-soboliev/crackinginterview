class RemoveZeroSumSubtrees:

    def delete_tree_nodes(self, nodes, parent,  value) -> int:
        distinct_parents = sorted(list(set(parent)), reverse=True)
        distinct_parents.remove(-1)
        nodes_to_remove = []
        for i in range(nodes):
            if value[i] == 0 and i not in distinct_parents:
                nodes_to_remove.append(i)

        for dn in distinct_parents:
            cur_sum = value[dn]
            in_sum = []
            for i in range(nodes):
                if parent[i] == dn:
                    cur_sum += value[i]
                    in_sum.append(i)
            if cur_sum == 0:
                in_sum.append(dn)
                nodes_to_remove.extend(in_sum)
        else:
            return nodes - len(set(nodes_to_remove))


