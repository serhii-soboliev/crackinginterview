class Solution:

    def generate_sentences(self, synonyms, text: str):

        synonyms_dict = self.build_synonyms_dict(synonyms)
        new_dict = [text.split()]
        for k in synonyms_dict.keys():
            syns = synonyms_dict[k]
            new_sentences = self.generate_all_substitutions(k, new_dict, syns)
            new_dict += new_sentences
        new_dict = list(set(map(lambda x: " ".join(x), new_dict)))
        new_dict.sort()
        return new_dict

    def generate_all_substitutions(self, k, new_dict, syns):
        new_sentences = []
        for t in new_dict:
            for s in syns:
                self.generate_substitution(k, new_sentences, s, t)
        return new_sentences

    def generate_substitution(self, k, old_sentences, s, t):
        indexes_to_change = []
        for i in range(len(t)):
            if t[i] == k:
                indexes_to_change.append(i)

        changed_sentences = [t]
        for i in indexes_to_change:
            new_sentences = []
            for st in changed_sentences:
                sc = st.copy()
                sc[i] = s
                new_sentences.append(sc)
            changed_sentences += new_sentences
        old_sentences += changed_sentences

    def build_synonyms_dict(self, synonyms):
        res = {}
        for i in range(len(synonyms)):
            syn1, syn2 = synonyms[i]
            self.add_syn_for_another(res, syn1, syn2)
            self.add_syn_for_another(res, syn2, syn1)

        for k in res.keys():
            res.get(k).remove(k)

        return res

    def add_syn_for_another(self, res, syn1, syn2):
        synons = res.get(syn1, set())
        synons.add(syn2)
        synons |= res.get(syn2, set())
        res[syn1] = synons

        for sy in synons:
            s = res.get(sy, set())
            s.add(syn2)
            res[sy] = s
