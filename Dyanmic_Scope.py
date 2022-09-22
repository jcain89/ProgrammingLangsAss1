from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):
    def init(self):
        self.env: Dict[str, Optional[Any]] = {}


dre = DynamicScope


def get_dynamic_re() -> DynamicScope:
    a = inspect.stack()
    print(a)
    dict = {}
    print("created dict :",dict)
    print("Type:", type(dict))
    for i in a:
        print("\n")
        print(i)
        print("LOCALS")
        print(i[0].f_locals.keys())
        print("VALUES")
        print(i[0].f_locals.values())
        print("TYPE")
        print(type(i[0].f_locals.keys()))
        listkeys = list(i[0].f_locals.keys())
        print("LIST")
        print(listkeys,"\n")
        print("Starting list print")
        for k in listkeys:
            print(k)
            print(type(k))
            #dict.update({k: (list(i[0].f_locals.values()))})
        print("FREEVARS")
        print(i[0].f_code.co_freevars)
        print("TYPE")
        print(i[0].f_code.co_freevars)
        print("\n")
        #dict.update({k: i[0].f_locals.values()})
        #dict.update(i[0].f_locals.keys())
        print("DICTIONARY")
        print(dict)

#Questions
#how to insert these values into the dictionary
#how to filter out the free variables
#

    # print("break")
    # for i in a:
    #    if(i==0):
    #        continue
    #    else:
    #        #if a.__contains__("abc"):
    #        #    print("THIS IS BAD")
    #        #else:
    #        print("keys of local vars")
    #        print(i[0].f_locals.keys())

    #        #b = list(i[0].f_code.co_freevars)
    #        #list(b)
    #        #enum = enumerate(b)
    #        #for i in enum:
    #        #    print("freevars")
    #        #    print(i[0].b.keys())
    #        #print(i[0].f_locals.keys())
    # print(a[0])

# get_dynamic_re()
