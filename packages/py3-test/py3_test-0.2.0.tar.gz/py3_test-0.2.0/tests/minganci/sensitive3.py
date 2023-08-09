aset = {
    ".",
    "-",
    ",",
    "'",
    '"',
    ":",
    "。",
    "\\",
    "&",
    "`",
    "~",
    "!",
    "@",
    "#",
    "%",
    "*",
    "(",
    ")",
    "=",
    "+",
    "_",
    "|",
    "?",
    "@",
    "",
    " ",
    " ",
    "\r",
    "\n",
    "-",
    "、",
    "—",
}


class Node:
    def __init__(self):
        self.children = None
        # 标记匹配到了关键词
        self.flag = False


# The encode of word is UTF-8
def add_word(root, word):
    if len(word) <= 0:
        return
    node = root
    for i in range(len(word)):
        if node.children is None:
            node.children = {}
            node.children[word[i]] = Node()

        elif word[i] not in node.children:
            node.children[word[i]] = Node()
        node = node.children[word[i]]
    node.flag = True


def init(word_list):
    root = Node()
    for line in word_list:
        add_word(root, line)
    return root


def key_contain(message, root):
    res = []
    for i in range(len(message)):
        p = root
        j = i
        while (
            j < len(message)
            and p.children is not None
            and (message[j] in p.children or message[j] in aset)
        ):
            if message[j] in aset:
                j = j + 1
                continue
            if p.flag is True:
                res.append(message[i:j])
            p = p.children[message[j]]
            j = j + 1

        if p.children is None or p.flag is True:
            res.append(message[i:j])
            # print '---word---',message[i:j]
    return res


def dfa():
    print("----------------dfa-----------")
    word_list = ["hello", "民警", "朋友", "女儿", "派出所", "派出所民警"]
    with open("sensitive_word.txt") as f:
        for line in f.readlines():
            keyword = line.strip().decode()
            word_list.append(keyword)
    root = init(word_list)

    message = "洪传四处乱咬乱吠，习**近平，习**近平，十字弓弩吓得家中11岁的女*儿躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征得主人同意后，民警和村民合力将这只发疯的狗打死"
    message = "习**近-平aaa十字弓，藏独，藏独"
    x = key_contain(message, root)
    for item in x:
        print(item)
    #     message = message.replace(item,"*"*len(item))
    # print message


if __name__ == "__main__":
    dfa()
