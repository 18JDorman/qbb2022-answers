# Feedback day2-lunch

This looks really good. There are a couple of small logic errors, but overall it's clear, well commented, and does all of the format checking needed.

- In the line where you check if fields[10] and fields[11] are of a lenth equal to fields[9], you do 2 equality checks that are identical. I think I understand why, but you only need one, since the two fields will each be checked when j=10 and j=11, respectively
- When you encounter an error, you count it and then use `continue`. Unfortunately, `continue` only skips to the next loop of its immediately enclosing for loop. In this case, that is the loop over each field for data type conversion. So, it would simply move on to the next field. This means that you could get multiple error entries for the same line, and if there wasn't a problem with type conversion it would still get appended to `bed`. Two alternatives would be to check these fields after the field conversion outside of that for loop, or you could replace both the append and continue with a `raise RunTimeError` or whatever you thought most appropriate. This would cause the code to exit the try statement and go to the except statement. Two birds, one stone.
- Just for your own knowledge, when you need a placeholder, using `None` is a handy one since it takes up no space and can't itself be changed, only replaced.

You seem to be in really good shape with respect to python. Great job and keep it up!