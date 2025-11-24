# Grupo composto por:
# Leonardo Lemr Peres - Matriícula 23200521
#
# Arquivo da tabela de análise sintática preditiva

ParseTable = {
    
    ("MAIN", "def"): ["FLIST"],
    ("MAIN", "id"): ["STMT"],
    ("MAIN", "{"): ["STMT"],
    ("MAIN", "int"): ["STMT"],
    ("MAIN", "print"): ["STMT"],
    ("MAIN", "return"): ["STMT"],
    ("MAIN", "if"): ["STMT"],
    ("MAIN", "$"): ["ε"],
    
    ("FLIST", "def"): ["FDEF", "FLIST'"],
    
    ("FLIST'", "def"): ["FLIST"],
    ("FLIST'", "$"): ["ε"],
    
    ("FDEF", "def"): ["def", "id", "(", "PARLIST", ")", "{", "STMTLIST", "}"],
    
    ("PARLIST", ")"): ["ε"],
    ("PARLIST", "int"): ["int", "id", "PARLIST'"],
    
    ("PARLIST'", ","): [",", "PARLIST"],
    ("PARLIST'", ")"): ["ε"],
    
    ("VARLIST", "id"): ["id", "VARLIST'"],
    
    ("VARLIST'", ","): [",", "VARLIST"],
    ("VARLIST'", ";"): ["ε"],
    
    ("STMT", "id"): ["id", "STMT'"],
    ("STMT", "{"): ["{", "STMTLIST", "}"],
    ("STMT", "int"): ["int", "VARLIST", ";"],
    ("STMT", "print"): ["print", "EXPR", ";"],
    ("STMT", "return"): ["return", "RETURNST'", ";"],
    ("STMT", "if"): ["if", "(", "EXPR", ")", "{", "STMT", "}", "ELSESTMT"],
    ("STMT'", "="): ["=", "EXPR", ";"],
    ("STMT'", "("): ["(", "PARLISTCALL", ")", ";"],
    
    ("RETURNST'", "id"): ["id"],
    ("RETURNST'", ";"): ["ε"],
    
    ("ELSESTMT", "else"): ["else", "{", "STMT", "}"],
    ("ELSESTMT", "id"): ["ε"],
    ("ELSESTMT", "{"): ["ε"],
    ("ELSESTMT", "int"): ["ε"],
    ("ELSESTMT", "print"): ["ε"],
    ("ELSESTMT", "return"): ["ε"],
    ("ELSESTMT", "if"): ["ε"],
    ("ELSESTMT", "}"): ["ε"],
    
    ("STMTLIST", "id"): ["STMT", "STMTLIST"],
    ("STMTLIST", "{"): ["STMT", "STMTLIST"],
    ("STMTLIST", "int"): ["STMT", "STMTLIST"],
    ("STMTLIST", "print"): ["STMT", "STMTLIST"],
    ("STMTLIST", "return"): ["STMT", "STMTLIST"],
    ("STMTLIST", "if"): ["STMT", "STMTLIST"],
    ("STMTLIST", "}"): ["ε"],
    
    ("EXPR", "id"): ["NUMEXPR", "EXPR'"],
    ("EXPR", "("): ["NUMEXPR", "EXPR'"],
    ("EXPR", "num"): ["NUMEXPR", "EXPR'"],
    
    ("EXPR'", "<"): ["<", "NUMEXPR"],
    ("EXPR'", "<="): ["<=", "NUMEXPR"],
    ("EXPR'", ">"): [">", "NUMEXPR"],
    ("EXPR'", ">="): [">=", "NUMEXPR"],
    ("EXPR'", "=="): ["==", "NUMEXPR"],
    ("EXPR'", "!="): ["!=", "NUMEXPR"],
    ("EXPR'", ")"): ["ε"],
    ("EXPR'", ";"): ["ε"],
    
    ("NUMEXPR", "id"): ["TERM", "NUMEXPR'"],
    ("NUMEXPR", "("): ["TERM", "NUMEXPR'"],
    ("NUMEXPR", "num"): ["TERM", "NUMEXPR'"],
    
    ("NUMEXPR'", "+"): ["+", "TERM", "NUMEXPR'"],
    ("NUMEXPR'", "-"): ["-", "TERM", "NUMEXPR'"],
    ("NUMEXPR'", ")"): ["ε"],
    ("NUMEXPR'", ";"): ["ε"],
    ("NUMEXPR'", "<"): ["ε"],
    ("NUMEXPR'", "<="): ["ε"],
    ("NUMEXPR'", ">"): ["ε"],
    ("NUMEXPR'", ">="): ["ε"],
    ("NUMEXPR'", "=="): ["ε"],
    ("NUMEXPR'", "!="): ["ε"],
    
    ("TERM", "id"): ["FACTOR", "TERM'"],
    ("TERM", "("): ["FACTOR", "TERM'"],
    ("TERM", "num"): ["FACTOR", "TERM'"],
    
    ("TERM'", "*"): ["*", "FACTOR", "TERM'"],
    ("TERM'", "/"): ["/", "FACTOR", "TERM'"],
    ("TERM'", "+"): ["ε"],
    ("TERM'", "-"): ["ε"],
    ("TERM'", ")"): ["ε"],
    ("TERM'", ";"): ["ε"],
    ("TERM'", "<"): ["ε"],
    ("TERM'", "<="): ["ε"],
    ("TERM'", ">"): ["ε"],
    ("TERM'", ">="): ["ε"],
    ("TERM'", "=="): ["ε"],
    ("TERM'", "!="): ["ε"],
    
    ("FACTOR", "id"): ["id", "FACTOR'"],
    ("FACTOR", "("): ["(", "NUMEXPR", ")"],
    ("FACTOR", "num"): ["num"],
    
    ("FACTOR'", "("): ["(", "PARLISTCALL", ")"],
    ("FACTOR'", "+"): ["ε"],
    ("FACTOR'", "-"): ["ε"],
    ("FACTOR'", "*"): ["ε"],
    ("FACTOR'", "/"): ["ε"],
    ("FACTOR'", ")"): ["ε"],
    ("FACTOR'", ";"): ["ε"],
    ("FACTOR'", "<"): ["ε"],
    ("FACTOR'", "<="): ["ε"],
    ("FACTOR'", ">"): ["ε"],
    ("FACTOR'", ">="): ["ε"],
    ("FACTOR'", "=="): ["ε"],
    ("FACTOR'", "!="): ["ε"],
    
    ("PARLISTCALL", "id"): ["id", "PARLISTCALL'"],
    
    ("PARLISTCALL'", ","): [",", "PARLISTCALL"],
    ("PARLISTCALL'", ")"): ["ε"]
}