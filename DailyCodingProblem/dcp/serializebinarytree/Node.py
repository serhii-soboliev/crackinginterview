import logging as log

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.empty_string = ""
        self.open_square_bracket = '['
        self.close_square_bracket = ']'
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
        log.basicConfig(format=FORMAT, level=log.DEBUG)

    def serialize(self):
        if self.val is None:
            log.debug("The Node is empty, returning empty string")
            res = self.empty_string
        else:
            left_serialize = self.left.serialize() if self.left is not None else self.empty_string
            right_serialize = self.right.serialize() if self.right is not None else self.empty_string
            res = '[{0}][{1}][{2}]'.format(left_serialize, self.val, right_serialize)
            log.debug(f'Serialization result = {res}')
        return res

    def deserialize(self, s):
        log.debug(f'Starting deserialization string {s}')
        if s == self.empty_string or s == []:
            return None
        if self.string_is_content(s):
            return Node(s)
        else:
            left_section = self.get_first_section_from_string(s)
            left_section_content = left_section[1:-1]
            log.debug(f'Left section content from string {s} is {left_section_content}')
            left_node = self.deserialize(left_section_content)
            root_residual = s[len(left_section):]
            root_section = self.get_first_section_from_string(root_residual)
            root_value = root_section[1:-1]
            log.debug(f'Deserialized root value from {s} is {root_value}')
            right_section = root_residual[len(root_section):]
            right_section_content = right_section[1:-1]
            log.debug(f'Right section content from string {s} is {right_section_content}')
            right_node = self.deserialize(right_section_content)
            return Node(root_value, left_node, right_node)

    def get_first_section_from_string(self, s):
        first_char = s[0]
        if first_char != self.open_square_bracket:
            raise ValueError(f'First symbol of deserialized string {s} must be open square bracket, but actual symbol is {first_char}')
        closing_sb_position = self.find_closing_square_bracket_position(s[1:])
        log.debug(f'Closing square bracket position for string {s} found: {closing_sb_position}')
        first_section = s[:closing_sb_position + 1]
        log.debug(f'First section = {first_section}')
        return first_section

    def find_closing_square_bracket_position(self, input_string):
        open_square_bracket_num = 1
        current_position = 1
        for s in input_string:
            if s == self.open_square_bracket:
                open_square_bracket_num += 1
            if s == self.close_square_bracket:
                open_square_bracket_num -= 1
                if open_square_bracket_num == 0:
                    return current_position
            current_position += 1
        raise ValueError(f'No closing square bracket in string {str}')

    def string_is_content(self, first_section_content):
        return self.open_square_bracket not in first_section_content

    def __eq__(self, o: object) -> bool:
        return (
           self.__class__ == o.__class__ and
           self.val == o.val and
           self.left == o.left and
           self.right == o.right
        )

