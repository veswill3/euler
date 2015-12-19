def run_sequence_step(num):
    if num % 2 == 0:
        return num / 2
    return 3 * num + 1

def get_sequence_len(num):
    next_num = run_sequence_step(num)
    cnt = 1
    while next_num != 1:
        next_num = run_sequence_step(next_num)
        cnt += 1
    return cnt

num_with_longest_chain = 0
longest_chain = 0

# check every number below 1 million
for start_num in xrange(1,999999):

    # print progress
    if start_num % 10000 == 0:
        pct = start_num/10000
        print("%i percent complete" % pct)

    chain_len = get_sequence_len(start_num)
    if chain_len > longest_chain:
        num_with_longest_chain = start_num
        longest_chain = chain_len

print("%i has the longest chain at %i" % (num_with_longest_chain, longest_chain))