class Solution:
    def line_reflection(self, coords):
        min_x = max_x = coords[0][0]
        coords_dict = dict()
        for coord in coords:
            if coord[0] < min_x:
                min_x = coord[0]
            if coord[0] > max_x:
                max_x = coord[0]
            if coords_dict.get(coord[0], None) is None:
                coords_dict[coord[0]] = set()
            coords_dict[coord[0]].add(coord[1])
        line_x = (min_x + max_x) / 2
        for x, y in coords:
            expected_x = 2 * line_x - x
            if expected_x != 0 and expected_x not in coords_dict.keys():
                return False
            if y not in coords_dict[expected_x]:
                return False
        return True


s = Solution()
print(s.line_reflection([[1, 1], [-1, 1]]))
print(s.line_reflection([[1, 1], [-1, -1]]))
print(s.line_reflection([[1, 1], [1, 2], [1, 3],
                         [-1, 1], [-1, 2], [-1, 3]]))
print(s.line_reflection([[1, 1], [1, 2], [1, 3],
                         [-1, 1], [-1, 2], [-1, 3], [0, 5]]))
