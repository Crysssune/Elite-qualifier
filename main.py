import time


# load dictionary words from file
def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time
  # log words loaded and elapsed time
  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words


def suggest(text, all_words):
  # YOUR CODE HERE. This currently doesn't suggest a correction, just checks if the input is already a word. You'll want to change that

  if text in all_words:
        print(text + ' is a word')
    else:
      similarities = [1-(textdistance.Jaccard(qval=2).distance(v,input_word)) for all_words in word_freq_dict.keys()]
      df = pd.safedict_simple(probs, orient='index').reset_index()
      df = df.rename(columns={'index':'Word', 0:'Prob'})
      df['Similarity'] = similarities
      output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
      return(output)

def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()

