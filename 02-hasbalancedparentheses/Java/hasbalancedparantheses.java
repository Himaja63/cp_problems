// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

import java.io.*; 
import java.util.*;
import java.util.Stack;
 
class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){
		Stack<Character> st = new Stack<>();
		for(int i = 0; i < s.length(); i++){
			if(s.charAt(i) == '('){
				st.push(s.charAt(i));
			}
			else if(!st.empty() && s.charAt(i) == ')' && st.peek() == '('){
				st.pop();				
			}
			else{
				st.push(s.charAt(i));
			}
		}
		if (st.empty()) {
			return true;
		}
		else{
			return false;
		}			
	}
}
	