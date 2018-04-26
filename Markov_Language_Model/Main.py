from Language_Model import *

# Kyle Zhou
# This program will train a language model based on a text input
# The degree determines how close the generated text will be to the original (min 2)
# adding mutiple word models will combine the trained models, 
# although when adding there is a bias towards the model trained with a larger text 
# the .write(n) method will generate a text of n words based on the language model

degree = 3
ham = lang_model("GreenEggsAndHam.txt", degree)
ody = lang_model("Odyssey.txt", degree)
tur = lang_model("Turing.txt", degree)
wal = lang_model("Walden.txt", degree)
combined  = ody + wal + tur + ham
combined.write(1000)
