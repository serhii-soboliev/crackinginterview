class SearchSuggestionSystem:
    def suggested_products(self, products, searchWord: str):
        products_dictionary = self.build_dictionary(products)
        search_lexemes = self.build_lexems(searchWord)
        search_result = []
        for lexeme in search_lexemes:
            search_result.append(self.build_suggestion(products_dictionary, lexeme))
        return search_result

    def build_suggestion(self, products_dictionary, lexeme):
        l_fl = lexeme[0]
        p_l = products_dictionary.get(l_fl, [])
        if not p_l:
            return []
        result = []
        res_cnt = 0
        for p in p_l:
            if p.startswith(lexeme):
                result.append(p)
                res_cnt += 1
            if res_cnt > 2:
                break
        return result

    def build_lexems(self, searchWord):
        import copy
        lexemes = [searchWord[0]]
        for i in range(1, len(searchWord)):
            new_lexeme = copy.deepcopy(lexemes[-1]) + searchWord[i]
            lexemes.append(new_lexeme)
        return lexemes

    def build_dictionary(self, products):
        s_prods = sorted(products)
        product_dictionary = {}
        for product in s_prods:
            fl = product[0]
            fl_list = product_dictionary.get(fl, [])
            fl_list.append(product)
            product_dictionary[fl] = fl_list
        return product_dictionary

    def find_lex_index(self, p_l, lexeme):
        index_to_start = 0
        sub_lexems = reversed(self.build_lexems(lexeme))
        for sub_lexeme in sub_lexems:
            for i in range(len(p_l)):
                if p_l[i].startswith(sub_lexeme):
                    return i
        return index_to_start
