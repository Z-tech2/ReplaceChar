#Read README before this to learn how to use it
def ReplaceChar(var, pos, replacement):
  var = list(var);
  var[pos] = replacement;
  var = str(var);
  return var;
