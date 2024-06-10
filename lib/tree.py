class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if not self.root:
            return None
        return self._get_element_by_id_depth_first(self.root, id)

    def _get_element_by_id_depth_first(self, node, id):
         if node['id'] == id:
            return node
         for child in node['children']:
            result = self._get_element_by_id_depth_first(child, id)
            if result:
                return result  
         return None
