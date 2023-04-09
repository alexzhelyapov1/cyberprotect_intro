# Constants 
# ----------------------------------------------------------------------------------------------------------------------

combination_len = 3     # You can test it in len = 2

input_filename = "in_words.txt"
output_filename = "out_task.txt"

buffer_size = 1024000   # 1 MB

# ----------------------------------------------------------------------------------------------------------------------

def combination_weights(words):
    weights = {}
    for word in words:
        for i in range(len(word) - combination_len + 1):
            combination = word[i : combination_len + i]
            # print(combination, end=" ")
            if (combination not in weights.keys()):
                weights[combination] = 1
            else:
                weights[combination] += 1
        # print("")

    # for key in weights.keys():
    #     print(key, weights[key])
    
    return weights


def word_weights(words, combination_weights):
    word_weights = {}

    for word in words:
        if len(word) < combination_len:
            continue
        else:
            word_weights[word] = min([combination_weights[word[i : combination_len + i]] for i in range(len(word) - combination_len + 1)])
            # print(word, min([combination_weights[word[i : combination_len + i]] for i in range(len(word) - combination_len + 1)]))
    
    return word_weights
    
# ----------------------------------------------------------------------------------------------------------------------
# Main part
# ----------------------------------------------------------------------------------------------------------------------

# Read info from file
with open(input_filename, "r") as input_file:
    # We can safely read all data, because there is definitely enough memory (def file.read(int) -> max_int bytes > 1 MB)
    buffer = input_file.read(buffer_size)


words = buffer.split()
combination_weights = combination_weights(words)
word_weights = word_weights(words, combination_weights)


# Write down into the file
with open(output_filename, "w") as output_file:
    result = sorted(word_weights, reverse=True, key=lambda item: word_weights[item])
    print(result)
    for i in range(len(result)):
        output_file.write(result[i] + " ")
