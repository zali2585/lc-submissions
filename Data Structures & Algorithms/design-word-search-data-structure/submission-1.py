class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
            

    def search(self, word: str) -> bool:
        def dfs(index, node):
            # since index 0 is technically root, then last index of word is actually = len(word)
            if index == len(word):
                return node.isEnd
            # if not, then word still has letters left CONTINUE


            c = word[index]

            # if search is bxy, c = . but node is b bc on first iteration, index = 0 so c = b but node is root, so it checks if after root does b exist
            # in that same way, when c = ., node is b and it checks children of b which then automatically checks 
            # children of children of b to see if next letter (y) exists after some letter that is replaced by .
            if c == '.':
                # checks children of letter before . to see if there is substring of letter before ., any letter for ., and letter after .
                for child in node.children.values():
                    if dfs(index + 1, child):
                        # needs this return True, bc when end of word is found, returns begin propogating up and at end of word, returns true to finally say word was found
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(index + 1, node.children[c])
        return dfs(0, self.root)


        
