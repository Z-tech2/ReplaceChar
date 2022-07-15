#Read README before this to learn how to use it
def ReplaceChar(var, pos, replacement):
  CharType = type(var);
  var = str(var)
  var = list(var);
  var[pos] = replacement;
  var = CharType(var);
  return var;
