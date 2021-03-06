reservadas = {
    'smallint'  : 'SMALLINT',          'integer'  : 'INTEGER',   
    'bigint'    : 'BIGINT',            'numeric'  : 'NUMERIC',   
    'real'      : 'REAL',              'mode'     : 'MODE',
    'double'    : 'DOUBLE',            'precision': 'PRECISION', 
    'money'     : 'MONEY',             'character': 'CHARACTER', 
    'varying'   : 'VARYING',           'varchar'  : 'VARCHAR', 
    'char'      : 'CHAR',              'text'     : 'TEXT',
    'date'      : 'DATE',              'time'     : 'TIME', 
    'timestamp'      : 'TIMESTAMP',    'float'     : 'FLOAT',
    'int'      : 'INT',                'inherits'     : 'INHERITS',
    'boolean'   : 'BOOLEAN',           'create'   : 'CREATE', 
    'or'        : 'OR',                'replace'  : 'REPLACE', 
    'database'  : 'DATABASE',          'if'       : 'IF', 
    'not'       : 'NOT',               'exists'   : 'EXISTS', 
    'owner'     : 'OWNER',             'show'     : 'SHOW',         
    'like'      : 'LIKE',              'regex'    : 'REGEX',
    'alter'     : 'ALTER',             'rename'   : 'RENAME',
    'to'        : 'TO',                'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',    'drop'     : 'DROP',
    'table'     : 'TABLE',             'default'  : 'DEFAULT',
    'null'     : 'NULL',               'unique'   : 'UNIQUE',
    'and'       : 'AND',                'constraint': 'CONSTRAINT',        
    'check'     : 'CHECK',             'primary'  : 'PRIMARY',
    'key'       : 'KEY',               'references': 'REFERENCES',
    'foreign'   : 'FOREIGN',           'add'      : 'ADD',
    'column'    : 'COLUMN',            'insert'   : 'INSERT',
    'into'      : 'INTO',              'values'   : 'VALUES',
    'update'    : 'UPDATE',             'set'      : 'SET',
    'where'     : 'WHERE',             'delete'    : 'DELETE',
    'from'      : 'FROM',              'truncate'  : 'TRUNCATE',
    'cascade'   : 'CASCADE',           'year'      : 'YEAR',
    'month'     : 'MONTH',              'day'       : 'DAY',
    'minute'    : 'MINUTE',             'second'    : 'SECOND',
    'enum'      : 'ENUM',               'type'      : 'TYPE',
    'interval'  : 'INTERVAL',           'zone' : 'ZONE',
    'databases'  : 'DATABASES',         'without'  : 'WITHOUT',  
    'with'      : 'WITH',               'hour'     : 'HOUR',
    'select'    : 'SELECT',
    'as'        : 'AS',                'distinct'  : 'DISTINCT',
    'count'     : 'COUNT',             'sum'       : 'SUM',
    'avg'       : 'AVG',               'max'       : 'MAX',
    'min'       : 'MIN',               'in'        : 'IN',
    'group'     : 'GROUP',             'by'        : 'BY',
    'order'     : 'ORDER',             'having'    : 'HAVING',
    'asc'       : 'ASC',               'desc'      : 'DESC',
    'nulls'     : 'NULLS',             'first'     : 'FIRST',
    'last'      : 'LAST'
}

tokens  = [
    'DOSPUNTOS',   'COMA',      'PTCOMA',
    'LLAVIZQ',     'LLAVDER',   'PARIZQ',
    'PARDER',      'CORCHIZQ',  'CORCHDER',
    'IGUAL',       'MAS',       'MENOS',
    'ASTERISCO',   'DIVIDIDO',  'EXPONENTE',
    'MENQUE',      'MAYQUE',    
    'NIGUALQUE',   'DIFERENTE', 'MODULO',
    'DECIMAL',     'ENTERO',    'CADENADOBLE',
    'CADENASIMPLE','ID',        'MENIGUAL',
    'MAYIGUAL',    'PUNTO'
] + list(reservadas.values())

# Tokens
t_PUNTO     = r'\.'
t_DOSPUNTOS = r':'
t_COMA      = r','
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORCHIZQ  = r'\['
t_CORCHDER  = r'\]'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_ASTERISCO = r'\*'
t_DIVIDIDO  = r'/'
t_EXPONENTE = r'\^'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_MENIGUAL  = r'<='
t_MAYIGUAL  = r'>='
t_DIFERENTE = r'<>'
t_MODULO    = r'%'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')   
     return t

def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1] 
    return t 

def t_CADENASIMPLE(t):
    r'\'.*?\''
    t.value = t.value[1:-1] 
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // --
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Analizador léxico
import ply.lex as lex
lexer = lex.lex()
