failed_tokens_tests = {
    #   String to test as key: error position as value
    "\tdouble f=45e++ai": [1, 14],
    "\tchar *b = \"e42\n\n":  [1, 15],
    "int\t\t\tn\t= 0x1uLl;": [1, 19],
    "char\t\t\t*yo\t\t\t= \"": [1, 31],
    "{return 1;}\\\\\\n": [1, 12],
    "int a = a+++++a;\ndouble b = .0e4x;": [2, 12],
    "int a = 1;\nint b = 10ul;\nint c = 10lul;\n": [3, 9],
    "int number = 0x1uLl;": [1, 14],
    "int number = 0x1ULl;": [1, 14],
    "int number = 0x1lL;": [1, 14],
    "int number = 0x1Ll;": [1, 14],
    "int number = 0x1UlL;": [1, 14]
}
