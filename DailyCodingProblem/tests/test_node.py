import unittest

from DailyCodingProblem.dcp.serializebinarytree.Node import Node


class TestNode(unittest.TestCase):

    def test_serialize_empty_node(self):
        self.assertEqual(Node(None, None, None).serialize(), "")

    def test_serialize_node_without_leaves(self):
        self.assertEqual(Node('100', None, None).serialize(), "[][100][]")

    def test_serialize_node_with_one_simple_leave(self):
        self.assertEqual(Node('100', Node('50'), None).serialize(), "[[][50][]][100][]")

    def test_serialize_node_with_two_simple_leaves(self):
        self.assertEqual(Node('100', Node('50'), Node('150')).serialize(), "[[][50][]][100][[][150][]]")

    def test_serialize_node_with_two_complex_leaves(self):
        test_node = Node(
                            '100',
                            Node(
                                '50',
                                Node('25'),
                                Node('75')
                            ),
                            Node(
                                '150',
                                Node('125'),
                                Node('175')
                            )
                        )
        expected_result = "[[[][25][]][50][[][75][]]][100][[[][125][]][150][[][175][]]]"
        self.assertEqual(test_node.serialize(), expected_result)

    def test_deserialize_empty_string(self):
        self.assertIsNone(Node(0).deserialize(''))

    def test_deserialize_should_raize_value_error_if_first_symbol_is_not_open_square_bracket(self):
        self.assertRaises(ValueError, lambda: Node(0).deserialize('][][]['))

    def test_deserialize_should_return_node_with_empty_leaves(self):
        n = Node(0).deserialize("[][100][]")
        self.assertEqual(n, Node('100'))

    def test_deserialize_should_return_node_with_left_leave(self):
        n = Node(0).deserialize("[[][50][]][100][]")
        self.assertEqual(Node('100', Node('50'), None), n)

    def test_deserialize_should_return_node_with_two_leaves(self):
        n = Node(0).deserialize("[[][50][]][100][[][150][]]")
        self.assertEqual(Node('100', Node('50'), Node('150')), n)

    def test_deserialize_should_return_complex_node(self):
        expected_result = Node(
            '100',
            Node(
                '50',
                Node('25'),
                Node('75')
            ),
            Node(
                '150',
                Node('125'),
                Node('175')
            )
        )
        input_string = "[[[][25][]][50][[][75][]]][100][[[][125][]][150][[][175][]]]"
        actual_result = Node(0).deserialize(input_string)
        self.assertEqual(expected_result, actual_result)

    def test_serialize_deserialize_complex_node(self):
        n = Node(
            '100',
            Node(
                '50',
                Node('25'),
                Node('75')
            ),
            Node(
                '150',
                Node('125'),
                Node('175')
            )
        )
        serialized = n.serialize()
        deserialized = n.deserialize(serialized)
        self.assertEqual(n, deserialized)