import sys
INFINITY = sys.maxint


def find_slack_table(words, M, tot_chars):
    """
    Slack table calculation
    :param words:
    :param M:
    :param tot_chars:
    :return: cost, line_chars
    """
    pass
    cost = [[0 for i in range(tot_chars)] for j in range(tot_chars)]
    line_chars = [[0 for i in range(tot_chars)] for j in range(tot_chars)]
    for i in range(tot_chars):
        line_chars[i][i] = M - len(words[i])
        cost[i][i] = find_cost(line_chars[i][i], tot_chars, i)
        for j in range(i + 1, tot_chars):
            line_chars[i][j] = line_chars[i][j - 1] - len(words[j]) - 1
            cost[i][j] = find_cost(line_chars[i][j], tot_chars, j)
    return cost, line_chars


def slack_table(words, M):
    """

    :param words:
    :param M:
    :return: t_table, s_table
    """
    pass
    tot_chars = len(words)
    cost, line_chars = find_slack_table(words, M, tot_chars)
    s_table = [0 for i in range(tot_chars)]
    t_table = [0 for i in range(tot_chars)]
    for j in range(0, tot_chars):
        s_table[j] = INFINITY
        for i in range(0, j):
            if (s_table[i - 1] + cost[i][j]) < s_table[j]:
                s_table[j] = s_table[i - 1] + cost[i][j]
                t_table[j] = i
    return t_table, s_table[-1]


def find_cost(line_chars, tot_chars, i):
    """
    class for calculating cost
    :param line_chars:
    :param tot_chars:
    :param i:
    :return: cost
    """
    pass
    if line_chars < 0:
        cost = INFINITY
    elif i == tot_chars - 1 and line_chars >= 0:
        cost = 0
    else:
        cost = line_chars ** 3
    return cost


def print_neatly(words, M):
    """
    Print text neatly.
    Parameters
    ----------
    words: list of str
        Each string in the list is a word from the file.
    M: int
    The max number of characters per line including spaces

    Returns
    -------
    cost: number
        The optimal value as described in the textbook.
    text: str
        The entire text as one string with newline characters.
        It should not end with a blank line.
    >>> print print_neatly(words=['Magna', 'Carta', 'John,', 'by', 'the', 'grace', 'of', 'God,', 'king'], M=17)
    (8, 'Magna Carta John,\nby the grace of\nGod, king')
    Details
    -------
        Look at print_neatly_test for some code to test the solution.
    """
    # TODO: Solve the problem
    tot_chars = len(words)
    text = ''
    t_table, cost = slack_table(words, M)
    previous = tot_chars
    # loop until total characters are filled
    while previous > 0:
        current = t_table[previous - 1]
        line = words[current]
        for j in range(current + 1, previous):
            line = line + ' ' + words[j]
        if previous != tot_chars:
            text = line + '\n' + text
        else:
            text = line
        previous = current
    return cost, text


# return f

# print words
# cost = 0
# text = "abcd"
# return cost, text
# print print_neatly(words=['Magna', 'Carta', 'John,', 'by', 'the', 'grace', 'of', 'God,', 'king'], M=17)
