"""
The test script for the course project.

Author: Emily Shader
Date: 01/13/2025
"""

import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')

    result = funcs.matching_parens('')
    introcs.assert_equals(False,result)

    result = funcs.matching_parens('()')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('em)ily')
    introcs.assert_equals(False,result)

    result = funcs.matching_parens('emily')
    introcs.assert_equals(False,result)

    result = funcs.matching_parens('e(m(il)y')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('(em(ily))')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('em(ily')
    introcs.assert_equals(False,result)


def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')

    result = funcs.first_in_parens('A(B)C')
    introcs.assert_equals('B',result)

    result = funcs.first_in_parens('A(B)(C)')
    introcs.assert_equals('B',result)

    result = funcs.first_in_parens('A(B (C))')
    introcs.assert_equals('B (C',result)

    result = funcs.first_in_parens('A (B))C')
    introcs.assert_equals('B',result)

    result = funcs.first_in_parens('(*)')
    introcs.assert_equals('*',result)


    
    
    
    

# Script Code
test_matching_parens()
test_first_in_parens()
print('Module funcs is working correctly')